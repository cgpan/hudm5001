"""letter_grade() from Exercise 5 of the Session 12 notebook, with its tests at the bottom of the same file.

Run the tests:            python grades.py
Use the function only:    python use_grades.py    (it imports this file, and the tests do not run)
"""
import unittest

print("grades.py is loading. Its __name__ is", __name__, flush=True)    # only here to show __name__; flush=True prints it at once


def letter_grade(score):
    """Return the letter grade for a score from 0 to 100."""
    if score < 0 or score > 100:
        raise ValueError(f"score must be between 0 and 100, got {score}")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


class TestLetterGrade(unittest.TestCase):
    """Tests for letter_grade. They run only when this file itself is run."""

    def test_typical_scores(self):
        self.assertEqual(letter_grade(95), "A")
        self.assertEqual(letter_grade(85), "B")
        self.assertEqual(letter_grade(72), "C")
        self.assertEqual(letter_grade(40), "F")

    def test_boundaries(self):
        self.assertEqual(letter_grade(90), "A")
        self.assertEqual(letter_grade(89.5), "B")
        self.assertEqual(letter_grade(70), "C")
        self.assertEqual(letter_grade(0), "F")

    def test_out_of_range_raises(self):
        with self.assertRaises(ValueError):
            letter_grade(101)
        with self.assertRaises(ValueError):
            letter_grade(-1)


if __name__ == "__main__":             # <---- True only when you run python grades.py
    unittest.main(verbosity=2)         # <---- run the tests above and print one line per test
