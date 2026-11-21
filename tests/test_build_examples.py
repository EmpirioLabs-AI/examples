"""Offline tests for scripts/build_examples.py and scripts/check_generated_paths.py.

The fixture is four models from the live feed: a chat model (cURL and the OpenAI SDK), an image model (submit, poll
and Python), a realtime model (websockets) and an embedding model. Nothing here touches the network.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import os
import shutil
import subprocess
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(ROOT, "tests", "fixtures", "feed.json")


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, "scripts", name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


builder = load("build_examples")
checker = load("check_generated_paths")


def feed():
    with open(FIXTURE, encoding="utf-8") as handle:
        return json.load(handle)


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.models = builder.validate(feed())
        self.files = builder.build(self.models)

    def test_each_model_gets_its_files_and_the_index_lists_it(self):
        expected = {
            "kimi-k3": {"README.md", "request.sh", "example.py"},
            "seedream-5-5": {"README.md", "submit.sh", "poll.sh", "example.py"},
            "qwen3-8-omni-flash-realtime": {"README.md", "realtime.py"},
            "skylark-embedding-vision": {"README.md", "request.sh", "example.py"},
        }
        for slug, names in expected.items():
            self.assertEqual({p.split("/")[-1] for p in self.files if p.startswith("models/" + slug + "/")}, names, slug)
        self.assertEqual(len(self.files), 1 + sum(len(n) for n in expected.values()))
        index = self.files["README.md"]
        self.assertIn("4 models in", index)
        for slug in expected:
            self.assertIn("[models/" + slug + "](models/" + slug + ")", index)
            self.assertIn("(https://empiriolabs.ai/models/" + slug + ")", index)
        self.assertEqual(builder.build(builder.validate(feed())), self.files, "the build is deterministic")

    def test_python_files_compile_and_read_the_key_from_the_environment(self):
        for path, content in self.files.items():
            if not path.endswith(".py"):
                continue
            compile(content, path, "exec")
            self.assertNotIn("YOUR_EMPIRIOLABS_API_KEY", content, path)
            self.assertRegex(content, r"os\.environ\[[\"']EMPIRIOLABS_API_KEY[\"']\]", path)
            self.assertRegex(content, r"(?m)^import os$|^import [\w, ]*\bos\b", path)
        self.assertIn('api_key=os.environ["EMPIRIOLABS_API_KEY"]', self.files["models/kimi-k3/example.py"])
        self.assertIn("Requires: pip install openai", self.files["models/kimi-k3/example.py"])
        self.assertIn("Requires: pip install websockets", self.files["models/qwen3-8-omni-flash-realtime/realtime.py"])

    def test_shell_files_stop_without_the_key_and_poll_asks_for_the_job(self):
        for path, content in self.files.items():
            if path.endswith(".sh"):
                self.assertTrue(content.startswith("#!/usr/bin/env bash\n"), path)
                self.assertIn("set -euo pipefail", content)
                self.assertIn(': "${EMPIRIOLABS_API_KEY:?', content)
                self.assertIn('-H "Authorization: Bearer $EMPIRIOLABS_API_KEY"', content)
        poll = self.files["models/seedream-5-5/poll.sh"]
        self.assertIn("/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned}", poll)
        self.assertNotIn("JOB_ID \\", poll.replace("${JOB_ID", ""))
        bash = shutil.which("bash")
        if bash:
            for path, content in self.files.items():
                if path.endswith(".sh"):
                    result = subprocess.run([bash, "-n"], input=content.encode(), capture_output=True)
                    self.assertEqual(result.returncode, 0, path + ": " + result.stderr.decode())

    def test_a_python_and_an_openai_block_get_two_files(self):
        data = feed()
        model = next(m for m in data["models"] if m["slug"] == "kimi-k3")
        model["blocks"].append({"kind": "python", "title": "Python", "language": "python",
                                "code": 'import requests\nprint(requests.get("https://api.empiriolabs.ai/v1/models").status_code)'})
        files = builder.build(builder.validate(data))
        self.assertIn("models/kimi-k3/example_openai.py", files)
        self.assertIn("models/kimi-k3/example.py", files)
        self.assertIn("from openai import OpenAI", files["models/kimi-k3/example_openai.py"])

    def test_readmes_are_professional_and_link_the_model(self):
        readme = self.files["models/seedream-5-5/README.md"]
        self.assertTrue(readme.startswith("# Seedream 5.5 API examples\n"))
        self.assertIn("| Endpoint | `POST /v1/images/generations` |", readme)
        self.assertIn("[`submit.sh`](submit.sh)", readme)
        self.assertIn("JOB_ID=<the job_id submit.sh returned> bash poll.sh", readme)
        self.assertIn("- [Seedream 5.5 pricing and specs](https://empiriolabs.ai/models/seedream-5-5)", readme)
        self.assertIn("- [Try Seedream 5.5 in the Playground]", readme)
        self.assertNotIn("Playground", self.files["models/qwen3-8-omni-flash-realtime/README.md"])
        for path, content in self.files.items():
            self.assertNotIn("\u2014", content, path)
            self.assertNotIn("<script", content.lower(), path)


class RefusalTests(unittest.TestCase):
    def refused(self, mutate):
        data = feed()
        mutate(data)
        with self.assertRaises(builder.FeedError):
            builder.build(builder.validate(data))

    def first(self, data, slug="seedream-5-5"):
        return next(m for m in data["models"] if m["slug"] == slug)

    def test_refuses_what_a_feed_must_not_carry(self):
        self.refused(lambda d: d.update(object="something.else"))
        self.refused(lambda d: d.update(models=[]))
        self.refused(lambda d: self.first(d).update(slug="../escape"))
        self.refused(lambda d: self.first(d).update(slug="kimi-k3"))
        self.refused(lambda d: self.first(d)["blocks"][0].update(kind="javascript"))
        self.refused(lambda d: self.first(d)["blocks"][0].update(language="python"))
        self.refused(lambda d: self.first(d)["blocks"][0].update(code="curl https://evil.example.net/v1"))
        self.refused(lambda d: self.first(d)["links"].update(page="https://elsewhere.example/models/x"))
        self.refused(lambda d: self.first(d)["links"].update(playground="https://platform.empiriolabs.ai/x"))
        self.refused(lambda d: self.first(d).update(description="Fast \u2014 and good"))
        self.refused(lambda d: self.first(d)["endpoint"].update(path="/v2/../x"))
        self.refused(lambda d: self.first(d, "kimi-k3")["blocks"][1].update(code='key = "YOUR_EMPIRIOLABS_API_KEY_2"'))


class WriteTests(unittest.TestCase):
    def test_write_then_check_and_stale_folders_go(self):
        files = builder.build(builder.validate(feed()))
        with tempfile.TemporaryDirectory() as out:
            builder.write(out, files)
            self.assertEqual(builder.check(out, files), [])
            stale = os.path.join(out, "models", "retired-model")
            os.makedirs(stale)
            with open(os.path.join(stale, "README.md"), "w") as handle:
                handle.write("old")
            self.assertEqual(builder.check(out, files), ["models/retired-model/README.md (not in the build)"])
            builder.write(out, files)
            self.assertFalse(os.path.exists(stale))
            self.assertEqual(builder.main(["--feed", FIXTURE, "--out", out, "--check"]), 0)


class GeneratedPathTests(unittest.TestCase):
    @staticmethod
    def raw(*entries):
        out = b""
        for old_mode, new_mode, path in entries:
            out += f":{old_mode} {new_mode} 0000000 0000000 M".encode() + b"\0" + path.encode() + b"\0"
        return out

    def test_accepts_generated_files_only(self):
        self.assertEqual(checker.problems(self.raw(("100644", "100644", "README.md"),
                                                   ("000000", "100644", "models/new-model/request.sh"),
                                                   ("100644", "000000", "models/retired/example.py"))), [])
        for path in ("scripts/build_examples.py", ".github/workflows/refresh.yml", "LICENSE", "tests/x.py",
                     "models/x/evil.js", "models/../scripts/x.py", "models/x/y/README.md"):
            self.assertTrue(checker.problems(self.raw(("100644", "100644", path))), path)
        self.assertTrue(checker.problems(self.raw(("100644", "100755", "models/x/request.sh"))))
        self.assertTrue(checker.problems(self.raw(("000000", "120000", "models/x/README.md"))))


if __name__ == "__main__":
    unittest.main()
