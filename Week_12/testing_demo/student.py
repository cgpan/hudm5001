"""The Student class from section 2.3 of the Session 12 notebook.

This file holds only the code. Its tests live in two other files:
test_student.py (for unittest) and test_student_pytest.py (for pytest).
"""


class Student:
    """A student with a name and a list of scores, each a number from 0 to 100."""

    passing_score = 60

    def __init__(self, name, scores=None):
        self.name = name
        self.scores = []
        if scores is not None:
            for score in scores:
                self.add_score(score)       # starting scores go through the same checks

    def average(self):
        """Return the mean of this student's scores, or None if there are none yet."""
        if len(self.scores) == 0:
            return None
        return sum(self.scores) / len(self.scores)

    def add_score(self, score):
        """Add one score, a number from 0 to 100, to this student's list. Returns nothing."""
        if not isinstance(score, (int, float)):
            raise TypeError(f"score must be a number, got {repr(score)}")
        if score < 0 or score > 100:
            raise ValueError(f"score must be between 0 and 100, got {score}")
        self.scores.append(score)

    def passed(self):
        """Return True if the average reaches the passing score, and False with no scores yet."""
        if self.average() is None:
            return False
        return self.average() >= self.passing_score

    def __repr__(self):
        """Return a short description, written like the code that creates the student."""
        return f"Student(name='{self.name}', scores={self.scores})"
