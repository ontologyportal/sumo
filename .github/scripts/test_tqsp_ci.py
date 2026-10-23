import unittest

from tqsp_ci import grade


class TqspResultTests(unittest.TestCase):
    def test_conjecture_proof(self):
        log = "Refutation found\n% SZS status Theorem for SP01S\nfof(x,negated_conjecture,p(a))."
        self.assertIn("Theorem proved", grade(log, 0))

    def test_budget_exhaustion(self):
        self.assertIn("No proof", grade("% SZS status Timeout", 1))
        self.assertIn("No proof", grade("% SZS status GaveUp", 0))

    def test_inconsistent_background_or_failed_process(self):
        for log, code in (
            ("Refutation found\n% SZS status Unsatisfiable", 0),
            ("Refutation found\n% SZS status Theorem", 0),
            ("% SZS status Timeout", 139),
            ("parse error", 4),
            ("", 0),
        ):
            with self.subTest(log=log, code=code), self.assertRaises(ValueError):
                grade(log, code)


if __name__ == "__main__":
    unittest.main()
