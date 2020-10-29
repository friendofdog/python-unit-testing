Unit testing in Python
======================

*Instructional project for Tokyo Python Society: https://www.meetup.com/TokyoPythonSocietyClub*

This is a very, very brief illustration of unit testing in Python. It uses the `unittest`, a testing module from the standard Python library.

This is a simple application that takes a given cost and discount, applies the discount, and prints the original & discounted prices to the console.

`tests/` contains the tests which run against the "implementation" (which is the actual code which makes up the application). The idea is that all code in implementation is covered by a test, ensuring that all smaller parts of the application are functional.

Running tests
-------------

To run tests, run `python -m unittest` in your console. You will see whether or not the tests passed, and if not, a brief explanation.

A note about the import statement at the top of the `tests_` files. Because `discount/` contains an `__init__.py` file, the directory is considered to be a package by the Python intepreter. Thus, `discount` is the package name and `app` is the module. This is why the statement `from discount.app import [...]` works.

As is, the tests will pass. If you want to see what a failing test looks like, try to intentionally break the function which is being tested. You should see specifics printed to the console.

Running implementation
----------------------

The entrypoint to this app is found in `discount/app.py`. It can be evoked in the command line by running `python -m discount.app`.

Recommended reading
-------------------

- https://www.datacamp.com/community/tutorials/unit-testing-python
- https://www.toptal.com/qa/how-to-write-testable-code-and-why-it-matters
- https://realpython.com/python-testing/
- https://docs.python.org/3/library/unittest.html
- https://spin.atomicobject.com/2012/12/06/writing-tests-is-not-tdd/
