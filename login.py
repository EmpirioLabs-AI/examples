#!/usr/bin/env python3
"""Sign in with EmpirioLabs AI in your browser and use the connection in this shell.

    eval "$(python login.py)"                  # bash and zsh
    python login.py --powershell | iex         # PowerShell

Opens the EmpirioLabs AI consent page, waits for your approval on a local port, and prints the
command that sets EMPIRIOLABS_API_KEY for this shell, so every example in this repository runs
without copying a key. The connection appears in Settings > Connected applications, where
Disconnect revokes it; `python login.py --revoke` revokes the one in EMPIRIOLABS_API_KEY.

An API key works the same way: create one at https://platform.empiriolabs.ai/dashboard/api-keys
and run export EMPIRIOLABS_API_KEY="sk-empiriolabs-...".

Follows https://docs.empiriolabs.ai/oauth: OAuth 2.1 authorization code with PKCE (S256), a
loopback redirect on a free port, and this repository's client metadata document as client_id.
Messages go to standard error; only the command goes to standard output.
Python 3.9+, standard library only.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import http.server
import json
import os
import secrets
import sys
import threading
import urllib.error
import urllib.parse
import urllib.request
import webbrowser

ISSUER = "https://platform.empiriolabs.ai"
API = "https://api.empiriolabs.ai"
CLIENT_ID = "https://raw.githubusercontent.com/EmpirioLabs-AI/examples/main/oauth/client.json"
USER_AGENT = "EmpirioLabs-AI-examples-login/1.0 (+https://github.com/EmpirioLabs-AI/examples)"
WAIT_SECONDS = 600


class LoginError(Exception):
    pass


def say(message):
    print(message, file=sys.stderr, flush=True)


def request(url, form=None):
    data = urllib.parse.urlencode(form).encode() if form is not None else None
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if data is not None:
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=headers), timeout=60) as response:
            return response.status, json.loads(response.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as error:
        try:
            return error.code, json.loads(error.read().decode("utf-8") or "{}")
        except ValueError:
            return error.code, {}


def metadata():
    status, meta = request(ISSUER + "/.well-known/oauth-authorization-server")
    needed = ("authorization_endpoint", "token_endpoint", "revocation_endpoint")
    if status != 200 or not all(str(meta.get(key, "")).startswith("https://") for key in needed):
        raise LoginError("could not read the authorization server's metadata (HTTP %s)" % status)
    return meta


def pkce():
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode("ascii")).digest()).rstrip(b"=").decode("ascii")
    return verifier, challenge


def authorize_url(endpoint, redirect_uri, challenge, state):
    return endpoint + "?" + urllib.parse.urlencode({
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": redirect_uri,
        "scope": "api",
        "resource": API,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
        "state": state,
    })


PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>EmpirioLabs AI</title>
<meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="font-family:system-ui,sans-serif;background:#0b1020;color:#e8ecf6;display:grid;place-items:center;min-height:100vh;margin:0">
<main style="text-align:center;max-width:32rem;padding:2rem"><h1 style="font-size:1.4rem">{title}</h1><p>{body}</p></main></body></html>"""


def wait_for_code(state):
    """(redirect_uri, server, result): a one-shot loopback listener on a free port."""
    result = {}
    done = threading.Event()

    class Callback(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urllib.parse.urlparse(self.path)
            query = {key: values[0] for key, values in urllib.parse.parse_qs(parsed.query).items()}
            if parsed.path != "/callback" or done.is_set() or query.get("state") != state:
                self.send_response(404)
                self.end_headers()
                return
            result.update(query)
            ok = "code" in query
            title = "Signed in to EmpirioLabs AI" if ok else "Sign-in was not completed"
            body = ("You can close this tab and return to your terminal." if ok
                    else html.escape(query.get("error_description") or query.get("error") or "No code was returned."))
            page = PAGE.format(title=title, body=body).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(page)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(page)
            done.set()

        def log_message(self, *args):
            pass

    server = http.server.HTTPServer(("127.0.0.1", 0), Callback)
    redirect_uri = "http://127.0.0.1:%d/callback" % server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return redirect_uri, server, result, done


def exchange(meta, code, redirect_uri, verifier):
    status, body = request(meta["token_endpoint"], form={
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "client_id": CLIENT_ID,
        "code_verifier": verifier,
        "resource": API,
    })
    token = body.get("access_token")
    if status != 200 or not isinstance(token, str) or not token:
        raise LoginError("the token exchange failed: %s" % (body.get("error_description") or body.get("error") or status))
    return token


def shell_line(token, powershell):
    if powershell:
        return "$env:EMPIRIOLABS_API_KEY = '" + token.replace("'", "''") + "'"
    return "export EMPIRIOLABS_API_KEY='" + token.replace("'", "'\\''") + "'"


def login(open_browser=True, powershell=False):
    meta = metadata()
    verifier, challenge = pkce()
    state = secrets.token_urlsafe(24)
    redirect_uri, server, result, done = wait_for_code(state)
    try:
        url = authorize_url(meta["authorization_endpoint"], redirect_uri, challenge, state)
        say("Approve the connection in your browser. If it did not open, visit:\n" + url)
        if open_browser:
            webbrowser.open(url)
        if not done.wait(WAIT_SECONDS):
            raise LoginError("no approval within %d minutes" % (WAIT_SECONDS // 60))
    finally:
        server.shutdown()
    if "code" not in result:
        raise LoginError(result.get("error_description") or result.get("error") or "no code was returned")
    token = exchange(meta, result["code"], redirect_uri, verifier)
    say("Signed in. EMPIRIOLABS_API_KEY is set for this shell; disconnect anytime in Settings > Connected applications.")
    return shell_line(token, powershell)


def revoke():
    token = os.environ.get("EMPIRIOLABS_API_KEY", "")
    if not token:
        raise LoginError("EMPIRIOLABS_API_KEY is not set")
    status, body = request(metadata()["revocation_endpoint"], form={"token": token, "client_id": CLIENT_ID})
    if status != 200:
        raise LoginError("revocation failed: %s (only a connection made by login.py can be revoked here)"
                         % (body.get("error_description") or body.get("error") or status))
    say("Revoked. Run unset EMPIRIOLABS_API_KEY (PowerShell: Remove-Item Env:EMPIRIOLABS_API_KEY).")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--powershell", action="store_true", help="print the PowerShell command instead of the bash one")
    parser.add_argument("--no-browser", action="store_true", help="print the address instead of opening a browser")
    parser.add_argument("--revoke", action="store_true", help="revoke the connection in EMPIRIOLABS_API_KEY")
    args = parser.parse_args(argv)
    try:
        if args.revoke:
            revoke()
            return 0
        print(login(open_browser=not args.no_browser, powershell=args.powershell))
        return 0
    except LoginError as error:
        say("login.py: " + str(error))
        return 1
    except OSError as error:
        say("login.py: " + str(error))
        return 2


if __name__ == "__main__":
    sys.exit(main())
