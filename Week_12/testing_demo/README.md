# Tests outside a notebook

This folder goes with the tip "Tests outside a notebook" at the end of section 2.7 in the Session 12 notebook. In a notebook, `run_tests()` runs your tests. Once your code lives in `.py` files, as it does in most projects, the tests move into files too. The folder shows the three setups the tip mentions, each with a few short files you can run:

1. tests in a file of their own, run with `python -m unittest`
2. tests at the bottom of the file they test, under `if __name__ == "__main__":`
3. the same tests written for pytest, with plain `assert` lines

## The files

| File | What it holds | Used in |
|---|---|---|
| `student.py` | the `Student` class from section 2.3, the code being tested | 1 and 3 |
| `test_student.py` | six unit tests for `Student`, written with `unittest` | 1 and 3 |
| `grades.py` | `letter_grade()` from Exercise 5, with its tests at the bottom of the same file | 2 |
| `use_grades.py` | a short script that imports `letter_grade` and uses it | 2 |
| `test_student_pytest.py` | the six tests from `test_student.py`, rewritten for pytest | 3 |

## Before you start

Open a terminal (Session 09) and move into this folder, for example with `cd Week_12/testing_demo` from the top of the course repo. Run every command below from inside this folder, since that is where Python looks for `student.py` and `grades.py`. To work in Colab instead, see the last section.

The outputs below come from Python 3.11. Other recent versions print the same lines.

## 1. Tests in a file of their own

`student.py` holds only the class, with no tests in it. The tests live next to it in `test_student.py`, which starts by importing the class:

```python
import unittest

from student import Student
```

The rest of the file is a `TestStudent` class like the one in section 2.6, with six test methods. To run them, type:

```bash
python -m unittest -v
```

```
test_average_of_two_scores (test_student.TestStudent.test_average_of_two_scores) ... ok
test_average_to_two_decimals (test_student.TestStudent.test_average_to_two_decimals) ... ok
test_average_with_no_scores_is_none (test_student.TestStudent.test_average_with_no_scores_is_none) ... ok
test_exactly_60_passes (test_student.TestStudent.test_exactly_60_passes) ... ok
test_new_students_do_not_share_scores (test_student.TestStudent.test_new_students_do_not_share_scores) ... ok
test_score_above_100_raises (test_student.TestStudent.test_score_above_100_raises) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

`python -m unittest` searches the folder for files whose names start with `test`, imports each one, and runs every `TestCase` class it finds. It does the job of the notebook's `run_tests()`, for all the test files at once. The `-v` (for verbose) prints one line per test. Without it, you get one dot per passing test:

```
......
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

Two details are worth noticing.

- `test_student_pytest.py` also starts with `test`, so `unittest` imports it too. Its tests are plain functions instead of methods of a `TestCase` class, and `unittest` skips plain functions. That is why it ran 6 tests and not 12.
- `python test_student.py` prints nothing at all. The file only defines a class, and nothing in it runs the tests. `python -m unittest` is the part that finds and runs them.

## 2. Tests at the bottom of the file they test

`grades.py` holds `letter_grade()` and, under it, a `TestLetterGrade` class with the tests from Exercise 5. The file ends with these two lines:

```python
if __name__ == "__main__":
    unittest.main(verbosity=2)
```

Python gives every file a variable named `__name__`. When you run a file directly, its `__name__` is `"__main__"`. When another file imports it, its `__name__` is the file's own name without `.py`, here `"grades"`. The first thing `grades.py` does is print its `__name__`, so you can watch this happen.

Run the file directly:

```bash
python grades.py
```

```
grades.py is loading. Its __name__ is __main__
test_boundaries (__main__.TestLetterGrade.test_boundaries) ... ok
test_out_of_range_raises (__main__.TestLetterGrade.test_out_of_range_raises) ... ok
test_typical_scores (__main__.TestLetterGrade.test_typical_scores) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

`__name__` was `"__main__"`, so the `if` block called `unittest.main()`, which ran the three tests. Now run a script that only imports the function:

```bash
python use_grades.py
```

```
grades.py is loading. Its __name__ is grades
95 -> A
83 -> B
71 -> C
40 -> F
```

The import ran `grades.py` from top to bottom, which is why its first line printed. This time `__name__` was `"grades"`, so Python skipped the `if` block, and the tests did not run. That is what the guard is for: the same file works as a tool that other files import and as a script that checks itself. (The `print` at the top of `grades.py` is only there for this demo. A real module should not print anything when it is imported.)

## 3. The same tests with pytest

pytest is a testing library that many Python projects use in place of `unittest`. Colab has it already. On your own computer, install it once:

```bash
pip install pytest
```

Open `test_student_pytest.py` next to `test_student.py`. Each test is now a plain function whose name starts with `test_`, and each check is a plain `assert` line, as in section 2.5:

```python
def test_average_of_two_scores():
    ann = Student("Ann", [90, 80])
    assert ann.average() == 85
```

There is no class, no `self`, and no `self.assertEqual`. Run pytest from this folder:

```bash
pytest -v
```

```
collected 12 items

test_student.py::TestStudent::test_average_of_two_scores PASSED          [  8%]
test_student.py::TestStudent::test_average_to_two_decimals PASSED        [ 16%]
test_student.py::TestStudent::test_average_with_no_scores_is_none PASSED [ 25%]
test_student.py::TestStudent::test_exactly_60_passes PASSED              [ 33%]
test_student.py::TestStudent::test_new_students_do_not_share_scores PASSED [ 41%]
test_student.py::TestStudent::test_score_above_100_raises PASSED         [ 50%]
test_student_pytest.py::test_average_of_two_scores PASSED                [ 58%]
test_student_pytest.py::test_average_with_no_scores_is_none PASSED       [ 66%]
test_student_pytest.py::test_average_to_two_decimals PASSED              [ 75%]
test_student_pytest.py::test_exactly_60_passes PASSED                    [ 83%]
test_student_pytest.py::test_score_above_100_raises PASSED               [ 91%]
test_student_pytest.py::test_new_students_do_not_share_scores PASSED     [100%]

============================== 12 passed in 0.01s ==============================
```

(The first lines of the report, which name your versions of Python and pytest, are left out here.)

pytest searches the folder for files whose names start with `test_` and runs both kinds of test it finds: the six plain functions, and the six `unittest` tests in `test_student.py`, which pytest runs as they are. That is why it reports 12.

One test in `test_student_pytest.py` looks different from the others. To check that `add_score(950)` raises a `ValueError`, it uses `try` and `except` from section 2.4. Most pytest projects write that test with `pytest.raises` instead:

```python
import pytest

def test_score_above_100_raises():
    with pytest.raises(ValueError):
        Student("Eve").add_score(950)
```

I left `import pytest` out of this folder on purpose. `python -m unittest` imports every file whose name starts with `test`, so on a computer without pytest, that one line would make step 1 fail.

## Try it: plant a bug

Open `student.py` and, in `passed()`, change `>=` to `>`. A student whose average is exactly 60 now fails, which is wrong. Save the file and run both tools again.

`python -m unittest` points at the boundary test:

```
...F..
======================================================================
FAIL: test_exactly_60_passes (test_student.TestStudent.test_exactly_60_passes)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".../testing_demo/test_student.py", line 27, in test_exactly_60_passes
    self.assertTrue(dan.passed())
AssertionError: False is not true

----------------------------------------------------------------------
Ran 6 tests in 0.000s

FAILED (failures=1)
```

pytest finds the same bug twice, once in each test file, and ends with `2 failed, 10 passed`. For the plain `assert`, it also shows where the `False` came from, down to the student it was checking:

```
>       assert dan.passed()
E       AssertionError: assert False
E        +  where False = passed()
E        +    where passed = Student(name='Dan', scores=[55, 65]).passed
```

Change `>` back to `>=` when you are done.

## In Colab

The free version of Colab has no terminal, but a line that starts with `!` runs a terminal command, and `%cd` moves into a folder. Put these lines in a Colab cell and run it:

```python
!git clone https://github.com/cgpan/hudm5001.git
%cd hudm5001/Week_12/testing_demo
!python -m unittest -v
!python grades.py
!python use_grades.py
!pytest -v
```

The first line copies the whole course repo into your Colab session. To plant the bug, open `student.py` from the Files panel on the left (double-click it to edit), make the change, and run the test commands again.
