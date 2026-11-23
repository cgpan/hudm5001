"""Unit tests for student.py, kept in a file of their own.

Run them from this folder with:   python -m unittest -v
"""
import unittest

from student import Student          # <---- the code under test comes from student.py


class TestStudent(unittest.TestCase):
    """Unit tests for the Student class."""

    def test_average_of_two_scores(self):
        ann = Student("Ann", [90, 80])
        self.assertEqual(ann.average(), 85)

    def test_average_with_no_scores_is_none(self):
        bob = Student("Bob")
        self.assertIsNone(bob.average())

    def test_average_to_two_decimals(self):
        cara = Student("Cara", [78, 82, 91])
        self.assertAlmostEqual(cara.average(), 83.67, places=2)

    def test_exactly_60_passes(self):                 # a boundary: an average of exactly 60
        dan = Student("Dan", [55, 65])
        self.assertTrue(dan.passed())

    def test_score_above_100_raises(self):
        eve = Student("Eve")
        with self.assertRaises(ValueError):
            eve.add_score(950)

    def test_new_students_do_not_share_scores(self):  # a regression test for the scores=[] trap
        finn = Student("Finn")
        gina = Student("Gina")
        finn.add_score(77)
        self.assertEqual(gina.scores, [])
