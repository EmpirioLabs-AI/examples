"""Offline tests for login.py: the whole sign-in against a fake authorization server on the loopback.

The fake server checks what the real one checks (the PKCE verifier against the S256 challenge, the
client_id, scope and resource, the redirect URI) and answers a token; a test plays the browser that
returns to the redirect URI after approval. Nothing here touches the network.
"""

from __future__ import annotations

import base64
import hashlib
import http.server
import importlib.util
import json
import os
import threading
import time
import unittest
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("login", os.path.join(ROOT, "login.py"))
login = importlib.util.module_from_spec(spec)
spec.loader.exec_module(login)


class FakeServer:
    """The token and revocation endpoints; it remembers the challenge the authorize address carried."""

    def __init__(self):
        self.challenge = None
        self.redirect_uri = None
        self.revoked = []
        outer = self

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_POST(self):
                form = {k: v[0] for k, v in urllib.parse.parse_qs(self.rfile.read(int(self.headers["Content-Length"])).decode()).items()}
                if self.path == "/token":
                    good = (form.get("grant_type") == "authorization_code" and form.get("code") == "the-code"
                            and form.get("client_id") == login.CLIENT_ID and form.get("resource") == login.API
                            and form.get("redirect_uri") == outer.redirect_uri
                            and base64.urlsafe_b64encode(hashlib.sha256(form.get("code_verifier", "").encode()).digest()).rstrip(b"=").decode() == outer.challenge)
                    body = {"access_token": "tok'en-123", "token_type": "Bearer", "scope": "api"} if good else {"error": "invalid_grant"}
                    self.reply(200 if good else 400, body)
                elif self.path == "/revoke":
                    outer.revoked.append((form.get("token"), form.get("client_id")))
                    self.reply(200, {})

            def reply(self, status, body):
                data = json.dumps(body).encode()
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            def log_message(self, *args):
                pass

        self.server = http.server.HTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        base = "http://127.0.0.1:%d" % self.server.server_address[1]
        self.meta = {"authorization_endpoint": base + "/authorize", "token_endpoint": base + "/token",
                     "revocation_endpoint": base + "/revoke"}


class LoginTests(unittest.TestCase):
    def setUp(self):
        self.fake = FakeServer()
        self.addCleanup(self.fake.server.shutdown)
        self.messages = []
        self._saved = (login.metadata, login.say)
        login.metadata = lambda: self.fake.meta
        login.say = self.messages.append
        self.addCleanup(self.restore)

    def restore(self):
        login.metadata, login.say = self._saved

    def run_login(self, browser, powershell=False):
        """Run login() in a thread; `browser(authorize_query)` plays the user's browser."""
        out = {}
        thread = threading.Thread(target=lambda: out.update(line=self.capture(powershell)), daemon=True)
        thread.start()
        deadline = time.time() + 10
        while not self.messages and time.time() < deadline:
            time.sleep(0.02)
        url = self.messages[0].split("\n", 1)[1]
        query = {k: v[0] for k, v in urllib.parse.parse_qs(urllib.parse.urlparse(url).query).items()}
        self.fake.challenge, self.fake.redirect_uri = query["code_challenge"], query["redirect_uri"]
        browser(query)
        thread.join(10)
        return out, query

    def capture(self, powershell):
        try:
            return login.login(open_browser=False, powershell=powershell)
        except login.LoginError as error:
            return "ERROR: " + str(error)

    @staticmethod
    def visit(url):
        try:
            with urllib.request.urlopen(url, timeout=10) as response:
                return response.status, response.read().decode()
        except urllib.error.HTTPError as error:
            return error.code, ""

    def test_the_authorize_address_asks_for_the_api_with_pkce(self):
        def browser(query):
            self.assertEqual(query["client_id"], login.CLIENT_ID)
            self.assertEqual((query["scope"], query["resource"]), ("api", "https://api.empiriolabs.ai"))
            self.assertEqual((query["response_type"], query["code_challenge_method"]), ("code", "S256"))
            self.assertRegex(query["redirect_uri"], r"^http://127\.0\.0\.1:\d+/callback$")
            self.assertGreaterEqual(len(query["state"]), 24)
            status, page = self.visit(query["redirect_uri"] + "?" + urllib.parse.urlencode({"code": "the-code", "state": query["state"]}))
            self.assertEqual(status, 200)
            self.assertIn("Signed in to EmpirioLabs AI", page)
        out, _query = self.run_login(browser)
        self.assertEqual(out["line"], "export EMPIRIOLABS_API_KEY='tok'\\''en-123'")
        self.assertIn("Connected applications", self.messages[-1])

    def test_powershell_line(self):
        def browser(query):
            self.visit(query["redirect_uri"] + "?" + urllib.parse.urlencode({"code": "the-code", "state": query["state"]}))
        out, _query = self.run_login(browser, powershell=True)
        self.assertEqual(out["line"], "$env:EMPIRIOLABS_API_KEY = 'tok''en-123'")

    def test_a_wrong_state_is_ignored_and_a_decline_is_reported(self):
        def browser(query):
            status, _page = self.visit(query["redirect_uri"] + "?" + urllib.parse.urlencode({"code": "the-code", "state": "forged"}))
            self.assertEqual(status, 404)
            status, page = self.visit(query["redirect_uri"] + "?" + urllib.parse.urlencode(
                {"error": "access_denied", "error_description": "The user declined <the request>", "state": query["state"]}))
            self.assertEqual(status, 200)
            self.assertIn("The user declined &lt;the request&gt;", page)
        out, _query = self.run_login(browser)
        self.assertEqual(out["line"], "ERROR: The user declined <the request>")

    def test_revoke_sends_the_token_with_this_client(self):
        os.environ["EMPIRIOLABS_API_KEY"] = "tok-to-revoke"
        self.addCleanup(os.environ.pop, "EMPIRIOLABS_API_KEY", None)
        self.assertEqual(login.main(["--revoke"]), 0)
        self.assertEqual(self.fake.revoked, [("tok-to-revoke", login.CLIENT_ID)])


class ClientDocumentTests(unittest.TestCase):
    def test_the_client_document_names_its_own_address_and_loopback_redirects(self):
        with open(os.path.join(ROOT, "oauth", "client.json"), encoding="utf-8") as handle:
            document = json.load(handle)
        self.assertEqual(document["client_id"], login.CLIENT_ID)
        self.assertEqual(login.CLIENT_ID, "https://raw.githubusercontent.com/EmpirioLabs-AI/examples/main/oauth/client.json")
        self.assertEqual(document["token_endpoint_auth_method"], "none")
        self.assertIn("http://127.0.0.1/callback", document["redirect_uris"])
        self.assertEqual(document["client_name"], "EmpirioLabs AI examples")


if __name__ == "__main__":
    unittest.main()
