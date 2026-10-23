import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import xml.etree.ElementTree as ET

from pr_ci import check_vampire, parse_kif


class VampireResultsTest(unittest.TestCase):
    def test_contradictions_fail_even_with_timeout(self):
        for result in ("Unsatisfiable", "Theorem", "ContradictoryAxioms"):
            with self.subTest(result=result), self.assertRaises(ValueError):
                check_vampire(f"% SZS status {result}\nTime limit reached", 1)
        with self.assertRaises(ValueError):
            check_vampire("Refutation found", 0)

    def test_expected_results(self):
        self.assertIn("satisfiable", check_vampire("% SZS status Satisfiable", 0))
        for log in ("% SZS status Timeout", "% Time limit reached!"):
            self.assertIn("no contradiction", check_vampire(log, 1))

    def test_execution_failures_are_not_consistent(self):
        for log, code in (("", 0), ("parse error", 1), ("% SZS status Error", 1),
                          ("% SZS status Timeout", 139), ("Satisfiable", 127)):
            with self.subTest(log=log, code=code), self.assertRaises(ValueError):
                check_vampire(log, code)


class ParseReportTest(unittest.TestCase):
    def test_recursive_parse_and_junit_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "ontology"
            (root / "nested").mkdir(parents=True)
            for name in ("good.kif", "nested/bad.kif", "Useful-terms_2023.kif"):
                (root / name).write_text("(p a)")
            output = Path(tmp) / "results"
            results = [subprocess.CompletedProcess([], 0, "valid"),
                       subprocess.CompletedProcess([], 1, "bad <syntax>\x1b")]
            with patch("pr_ci.subprocess.run", side_effect=results) as run:
                failed = parse_kif(Path("sumo"), root, Path("config.xml"), output)
            self.assertTrue(failed)
            self.assertEqual(run.call_count, 2)
            self.assertEqual(run.call_args.args[0][-2:], ["validate", "--parse"])
            suite = ET.parse(output / "TEST-sigma-parse.xml").getroot()
            self.assertEqual(suite.get("tests"), "2")
            self.assertEqual(suite.get("failures"), "1")
            self.assertEqual(suite.find("testcase/failure").text, "bad <syntax>")

    def test_timeout_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a.kif").write_text("(p a)")
            with patch("pr_ci.subprocess.run", side_effect=subprocess.TimeoutExpired("sumo", 120)):
                self.assertTrue(parse_kif(Path("sumo"), root, Path("config.xml"), root))
            self.assertEqual(ET.parse(root / "TEST-sigma-parse.xml").getroot().get("failures"), "1")

    def test_ingest_error_fails_even_with_zero_exit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "bad.kif").write_text("(p a")
            for log in ("[2026-10-23 ERROR] ingest: unbalanced parentheses",
                        "error[parse/unbalanced-parens]: unbalanced parentheses\n"
                        "  --> bad.kif:1"):
                with self.subTest(log=log):
                    result = subprocess.CompletedProcess([], 0, log)
                    with patch("pr_ci.subprocess.run", return_value=result):
                        self.assertTrue(parse_kif(Path("sumo"), root, Path("config.xml"), root))

    def test_empty_suite_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                parse_kif(Path("sumo"), Path(tmp), Path("config.xml"), Path(tmp))


if __name__ == "__main__":
    unittest.main()
