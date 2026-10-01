"""Checkpoint and deadline regression tests (no prover required)."""

import argparse
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

spec = importlib.util.spec_from_file_location("audit", Path(__file__).with_name("nightly_audit.py"))
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.state = {"version": 1, "fingerprint": "abc", "engine_fingerprint": "engine",
                      "seed": 0, "next_step": 0}

    def test_resume_and_changed_input_reset(self):
        path = self.root / "checkpoint.json"
        self.state.update(seed=3, next_step=200)
        audit.atomic_json(path, self.state)
        self.assertEqual(audit.checkpoint(path, "abc", "engine"), self.state)
        reset = audit.checkpoint(path, "changed", "engine")
        self.assertEqual((reset["seed"], reset["next_step"]), (0, 0))

    def test_changed_engine_and_legacy_checkpoints_restart_the_sweep(self):
        path = self.root / "checkpoint.json"
        self.state.update(seed=3, next_step=200)
        audit.atomic_json(path, self.state)
        reset = audit.checkpoint(path, "abc", "new-engine")
        self.assertEqual((reset["seed"], reset["next_step"]), (0, 0))
        self.assertEqual(reset["engine_fingerprint"], "new-engine")
        del self.state["engine_fingerprint"]
        audit.atomic_json(path, self.state)
        self.assertEqual(audit.checkpoint(path, "abc", "new-engine"), reset)

    def test_frontend_only_engine_commit_change_preserves_progress(self):
        path = self.root / "checkpoint.json"
        self.state.update(seed=3, next_step=200)
        audit.atomic_json(path, self.state)
        self.assertEqual(audit.checkpoint(path, "abc", "engine"), self.state)

    def test_manifest_membership_and_content_are_hashed(self):
        manifest = self.root / "manifest"
        manifest.write_text("a.kif\n")
        (self.root / "a.kif").write_text("(instance A B)")
        (self.root / "excluded.kif").write_text("old")
        _, first = audit.constituents(self.root, manifest)
        (self.root / "excluded.kif").write_text("changed")
        self.assertEqual(audit.constituents(self.root, manifest)[1], first)
        (self.root / "a.kif").write_text("(instance A C)")
        second = audit.constituents(self.root, manifest)[1]
        self.assertNotEqual(first, second)
        manifest.write_text("a.kif\nexcluded.kif\n")
        self.assertNotEqual(second, audit.constituents(self.root, manifest)[1])
        manifest.write_text("missing.kif\n")
        with self.assertRaises(FileNotFoundError):
            audit.constituents(self.root, manifest)

    def test_advance_and_finish_sweep(self):
        result = {"seed": 0, "step": 0, "next_step": 10, "total": 20}
        next_state = audit.advance(self.state, result, 10)
        self.assertEqual((next_state["seed"], next_state["next_step"]), (0, 10))
        result.update(step=10, next_step=20)
        next_state = audit.advance(next_state, result, 10)
        self.assertEqual((next_state["seed"], next_state["next_step"]), (1, 0))

    def test_bad_results_do_not_skip_formulas(self):
        for result in (
            {"seed": 1, "step": 0, "next_step": 10, "total": 20},
            {"seed": 0, "step": 0, "next_step": 0, "total": 20},
            {"seed": 0, "step": 0, "next_step": 11, "total": 20},
            {"seed": 0, "step": 0, "next_step": 10, "total": 5},
        ):
            with self.subTest(result=result), self.assertRaises(ValueError):
                audit.advance(self.state, result, 10)

    def test_corrupt_checkpoint_fails_closed(self):
        path = self.root / "checkpoint.json"
        self.state["next_step"] = -1
        audit.atomic_json(path, self.state)
        with self.assertRaises(ValueError):
            audit.checkpoint(path, "abc", "engine")

    def test_contradiction_report_has_reproduction_coordinates_and_kif(self):
        report = audit.contradiction_report([{
            "seed": 7,
            "step": 42,
            "proof_steps": 3,
            "axioms": [{"file": "Merge.kif", "line": 10,
                        "kif": "(instance A B)"}],
        }])
        self.assertIn("Seed: `7`", report)
        self.assertIn("Start step: `42`", report)
        self.assertIn("Merge.kif:10", report)
        self.assertIn("```lisp\n(instance A B)\n```", report)

    def test_deadline_terminates_process(self):
        with (self.root / "log").open("w") as log:
            started = time.monotonic()
            code = audit.execute([sys.executable, "-c", "import time; time.sleep(30)"],
                                 log, subprocess.STDOUT, 0.1, self.root)
        self.assertIsNone(code)
        self.assertLess(time.monotonic() - started, 5)

    def test_findings_and_interrupted_chunk_preserve_completed_progress(self):
        output = self.root / "out"
        calls = []

        def execute(command, stdout, stderr, seconds, cwd):
            calls.append(command)
            if "load" in command:
                config_path = command[command.index("--config") + 1]
                self.assertIn('<kb name="SUMO">', Path(config_path).read_text())
                config = ET.parse(config_path)
                directory = next(p.attrib["value"] for p in config.getroot()
                                 if p.attrib.get("name") == "editDir")
                (Path(directory) / "SUMO.lmdb").mkdir()
                return 0
            if len(calls) == 2:
                json.dump({"seed": 0, "step": 0, "next_step": 1, "total": 20,
                           "inconsistent": True, "contradictions": [{"axioms": []}]}, stdout)
                stdout.flush()
                return 1
            return None

        args = argparse.Namespace(output=str(output), sumo="/fake/sumo",
                                  seconds=10, chunk_size=1, timeout=1)
        with patch.object(audit, "constituents", return_value=(["a.kif"], "abc")), (
            patch.object(audit, "execute", side_effect=execute)
        ), (
            patch.object(audit, "replay_metadata", return_value={"complete": False, "engine": {"fingerprint": "engine"}})
        ):
            self.assertEqual(audit.run(args), 1)
        saved = json.loads((output / "checkpoint.json").read_text())
        self.assertEqual((saved["seed"], saved["next_step"]), (0, 1))
        result = json.loads((output / "results.jsonl").read_text())
        self.assertEqual(result["contradictions"][0]["audit_seed"], 0)
        self.assertEqual(result["contradictions"][0]["audit_step"], 0)
        self.assertIn("Seed: `0`", (output / "contradictions.md").read_text())
        self.assertIn("Deadline interrupted a chunk: True", (output / "summary.md").read_text())
        report = (output / "contradictions.md").read_text()
        replay = json.loads(report.split("```sigma-audit-replay\n")[1].split("\n```")[0])
        self.assertTrue(replay["complete"])
        self.assertEqual(replay["findings"][0]["step"], 0)

    def test_multi_step_chunks_are_rejected_before_loading(self):
        with self.assertRaisesRegex(ValueError, "chunk-size 1"):
            audit.run(argparse.Namespace(chunk_size=2))

    def test_replay_metadata_pins_bytes_run_and_cli_settings(self):
        (self.root / "a.kif").write_bytes(b"(instance A B)\r\n")
        with patch.object(audit.subprocess, "check_output", return_value=b"a" * 40 + b"\n"), (
            patch.object(audit, "engine_identity", return_value={"commit": "b" * 40, "fingerprint": "c" * 64})
        ), patch.dict(audit.os.environ, {"GITHUB_RUN_ID": "12", "GITHUB_RUN_ATTEMPT": "2"}):
            replay = audit.replay_metadata(self.root, ["a.kif"], "fingerprint", 10)
        self.assertEqual(replay["sumo_commit"], "a" * 40)
        self.assertEqual((replay["run_id"], replay["run_attempt"]), ("12", 2))
        self.assertEqual(replay["constituents"][0]["sha256"], audit.hashlib.sha256(b"(instance A B)\r\n").hexdigest())
        self.assertEqual(replay["config"]["maxSteps"], 500000)
        self.assertEqual(replay["config"]["maxLits"], 12)
        self.assertEqual(replay["request"], {"count": 1, "batch": 1, "limit": 64})
        self.assertFalse(replay["complete"])

    def test_failed_load_report_cannot_be_replayed(self):
        args = argparse.Namespace(output=str(self.root / "out"), sumo="/fake/sumo",
                                  seconds=10, chunk_size=1, timeout=1)
        with patch.object(audit, "constituents", return_value=(["a.kif"], "abc")), (
            patch.object(audit, "replay_metadata", return_value={"complete": False, "engine": {"fingerprint": "engine"}})
        ), patch.object(audit, "execute", return_value=2):
            with self.assertRaises(RuntimeError):
                audit.run(args)
        report = (self.root / "out" / "contradictions.md").read_text()
        self.assertIn('"complete": false', report)


if __name__ == "__main__":
    unittest.main()
