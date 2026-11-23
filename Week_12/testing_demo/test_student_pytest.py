"""The tests from test_student.py, written for pytest.

Each test is a plain function whose name starts with test_, and each check is a
plain assert line. There is no class and no self.assertEqual.

Install pytest once with   pip install pytest   (Colab already has it),
then run from this folder:   pytest -v
"""
from student import Student


def test_average_of_two_scores():
    ann = Student("Ann", [90, 80])
    assert ann.average() == 85


def test_average_with_no_scores_is_none():
    bob = Student("Bob")
    assert bob.average() is None


def test_average_to_two_decimals():
    cara = Student("Cara", [78, 82, 91])
    assert round(cara.average(), 2) == 83.67


def test_exactly_60_passes():                         # a boundary: an average of exactly 60
    dan = Student("Dan", [55, 65])
    assert dan.passed()


def test_score_above_100_raises():
    eve = Student("Eve")
    try:
        eve.add_score(950)
    except ValueError:
        return                                        # the error we expected, so the test passes
    assert False, "add_score(950) should raise a ValueError"


def test_new_students_do_not_share_scores():          # a regression test for the scores=[] trap
    finn = Student("Finn")
    gina = Student("Gina")
    finn.add_score(77)
    assert gina.scores == []
