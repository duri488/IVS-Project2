import pytest
import mathlib as m

# run with: "pytest -q tests.py" or "pytest tests.py"
# class name have to start with "Test" otherwise it will be skipped
# test name have to start with "test_" otherwise it will be skipped

class TestClass:
    def test_addEqual(self):
        assert m.add(2,3) == 5
        assert m.add(-2,3) == 1

    def test_addNotEqual(self):
        assert m.add(-2,-4) != 2


        