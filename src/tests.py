import pytest
import mathlib as m

# run with: "pytest -q tests.py" or "pytest tests.py"
# class name have to start with "Test" otherwise it will be skipped
# test name have to start with "test_" otherwise it will be skipped

class TestAdd:
    def test_addEqual(self):
        #kladne + kladne
        assert m.add(2, 3) == 5
        assert m.add(5, 5) == 10
        assert m.add(4, 8) == 12
        assert m.add(0, 9) == 9
        assert m.add(99, 0) == 99
        assert m.add(56, 20) == 76
        assert m.add(150, 70) == 220
        assert m.add(10000, 2536) == 12536
        assert m.add(1653, 752) == 2405

        #kladne + zaporne
        assert m.add(-2, 3) == 1
        assert m.add(-5, 8) == 3
        assert m.add(10, -7) == 3
        assert m.add(-4, 1) == -3
        assert m.add(4, -5) == -1
        assert m.add(-14, 5) == -9
        assert m.add(-25, 25) == 0
        assert m.add(100, -100) == 0
        assert m.add(-23, 77) == 54
        assert m.add(120, -1700) == -1580
        assert m.add(12302, -12123) == 179

        #zaporne + zaporne
        assert m.add(-2, -3) == -5
        assert m.add(-5, -18) == -23
        assert m.add(-1, -7) == -8
        assert m.add(-4, -111) == -115
        assert m.add(-4025, -46555) == -50580
        assert m.add(-1484910, -6515612) == -8000522

    def test_addNotEqual(self):
        assert m.add(-2, -4) != 2
        
        
class TestDivide:
    def test_divEqual(self):
        assert m.divide(10, 5) == 2
        assert m.divide(2, 0) == "Invalid input"
    
    def test_divNotEqual(self):
        assert m.divide(12, 2) != 8
