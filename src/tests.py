import pytest
import mathlib as m

# run with: "pytest -q tests.py" or "pytest tests.py"
# class name have to start with "Test" otherwise it will be skipped
# test name have to start with "test_" otherwise it will be skipped

class TestAdd:
    def test_addEqual(self):
        #positive number & positive number
        assert m.add(2, 3) == 5
        assert m.add(5, 5) == 10
        assert m.add(4, 8) == 12
        assert m.add(0, 9) == 9
        assert m.add(99, 0) == 99
        assert m.add(56, 20) == 76
        assert m.add(150, 70) == 220
        assert m.add(10000, 2536) == 12536
        assert m.add(1653, 752) == 2405

        #positive number & negative number
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

        #negative number & negative number
        assert m.add(-2, -3) == -5
        assert m.add(-5, -18) == -23
        assert m.add(-1, -7) == -8
        assert m.add(-4, -111) == -115
        assert m.add(-4025, -46555) == -50580
        assert m.add(-1484910, -6515612) == -8000522

    def test_addNotEqual(self):
        #positive number & positive number
        assert m.add(2, 4) != 2
        assert m.add(70, 3) != -5
        assert m.add(210, 18) != 17
        assert m.add(10, 107) != -8.8
        assert m.add(4, 111) != 100000
        assert m.add(4025, 46555) != 0
        assert m.add(1484910, 6515612) != 654589214

        #positive number & negative number
        assert m.add(-2, 311) != 111
        assert m.add(-5, 80) != 40.45
        assert m.add(10, -7) != 12
        assert m.add(-12, 110) != -34.78
        assert m.add(45, -5) != -13
        assert m.add(-14, 51) != -9.65
        assert m.add(-25, 125) != 0
        assert m.add(100, -103564) != 0

        #negative number & negative number
        assert m.add(-2, -3) != -2
        assert m.add(-5, -1) != -27
        assert m.add(-13, -7) != 87.7
        assert m.add(-40, -11) != 0
        assert m.add(-4025, -46555) != -44524
        assert m.add(-1484910, -6515612) != 1001


class TestSubtraction:
    def test_subEqual(self):
        #positive number & positive number
        assert m.subtraction(10, 3) == 7
        assert m.subtraction(4, 3) == 1
        assert m.subtraction(8, 4) == 4
        assert m.subtraction(15, 6) == 9
        assert m.subtraction(53, 25) == 28
        assert m.subtraction(70, 42) == 28
        assert m.subtraction(130, 65) == 65
        assert m.subtraction(1111, 111) == 1000
        assert m.subtraction(25485, 10254) == 15231

        #positive number & negative number
        assert m.subtraction(5, -3) == 8
        assert m.subtraction(10, -5) == 15
        assert m.subtraction(2, -8) == 10
        assert m.subtraction(2, -1) == 3
        assert m.subtraction(-8, 9) == -17
        assert m.subtraction(2, -6) == 8
        assert m.subtraction(-15, 15) == -30
        assert m.subtraction(-253, 100) == -353
        assert m.subtraction(35, -77) == 112
        assert m.subtraction(2566, -1120) == 3686
        assert m.subtraction(-9999, 1111) == -11110

        #negative number & negative number
        assert m.subtraction(-5, -8) == 3
        assert m.subtraction(-30, -18) == -12
        assert m.subtraction(-3, -7) == 4
        assert m.subtraction(-301, -121) == -180
        assert m.subtraction(-1025, -2555) == 1530
        assert m.subtraction(-19796, -20123) == 327
        
    def test_subNotEqual(self):
        #positive number & positive number
        assert m.subtraction(2, 4) != 0
        assert m.subtraction(70, 30) != 15
        assert m.subtraction(2100, 181) != 171
        assert m.subtraction(100, 107) != 7
        assert m.subtraction(40, 111) != -1044524
        assert m.subtraction(4025, 46555) != 0.5
        assert m.subtraction(1484910, 6515612) != -1

        #positive number & negative number
        assert m.subtraction(-22, 311) != -111
        assert m.subtraction(-564, 80) != 40
        assert m.subtraction(10, -7) != 45
        assert m.subtraction(-12, 110) != 100
        assert m.subtraction(45, -5) != -12
        assert m.subtraction(-74, 51) != -9
        assert m.subtraction(-25, 25) != 0
        assert m.subtraction(100, -103564) != 0

        #negative number & negative number
        assert m.subtraction(-2, -3) != 0
        assert m.subtraction(-5, -1) != -27.5
        assert m.subtraction(-13, -7) != -46
        assert m.subtraction(-40, -11) != 10
        assert m.subtraction(-4025, -46555) != 3.33
        assert m.subtraction(-1480.45, -6515612) != -12314
        
class TestDivide:
    def test_divEqual(self):
        assert m.divide(10, 5) == 2
        assert m.divide(2, 0) == "Invalid input"
    
    def test_divNotEqual(self):
        assert m.divide(12, 2) != 8
