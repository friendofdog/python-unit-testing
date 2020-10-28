Unit testing in Python
======================

This is a very, very brief illustration of unit testing in Python. It uses the `unittest`, a testing module from the standard Python library.

`discount.py` is a simple application that takes a static list of costs, applies a discount, and prints the original & discounted prices to the console. `test_discount.py` contains the tests to run against the "implementation" (which is the actual code which makes up the application).

Running tests
-------------

To run tests, run `python -m unittest` in your console. You will see whether or not the tests passed, and if not, a brief explanation.

As is, the tests will pass. If you want to see what a failing test looks like, try to intentionally break the function which is being tested. You should see specifics printed to the console.

Recommended reading
-------------------

- https://www.datacamp.com/community/tutorials/unit-testing-python
- https://www.toptal.com/qa/how-to-write-testable-code-and-why-it-matters
- https://realpython.com/python-testing/
- https://docs.python.org/3/library/unittest.html
- https://spin.atomicobject.com/2012/12/06/writing-tests-is-not-tdd/
