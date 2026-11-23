"""Use letter_grade() from grades.py. Importing grades.py does not run its tests.

Run from this folder:   python use_grades.py
"""
from grades import letter_grade      # <---- runs grades.py, where __name__ is now "grades"

for score in [95, 83, 71, 40]:
    print(score, "->", letter_grade(score))
