import pytest
import mathLib.mathlib as m

# run with: "pytest -q tests.py" or "pytest tests.py"
# class name have to start with "Test" otherwise it will be skipped
# test name have to start with "test_" otherwise it will be skipped

class TestAdd:
    def test_addEqualPositivePositive(self):
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

    def test_addEqualPositiveNegative(self):
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

    def test_addEqualNegativeNegative(self):
        #negative number & negative number
        assert m.add(-2, -3) == -5
        assert m.add(-5, -18) == -23
        assert m.add(-1, -7) == -8
        assert m.add(-4, -111) == -115
        assert m.add(-4025, -46555) == -50580
        assert m.add(-1484910, -6515612) == -8000522

    def test_addNotEqualPositivePositive(self):
        #positive number & positive number
        assert m.add(2, 4) != 2
        assert m.add(70, 3) != -5
        assert m.add(210, 18) != 17
        assert m.add(10, 107) != -8.8
        assert m.add(4, 111) != 100000
        assert m.add(4025, 46555) != 0
        assert m.add(1484910, 6515612) != 654589214

    def test_addNotEqualPositiveNegative(self):
        #positive number & negative number
        assert m.add(-2, 311) != 111
        assert m.add(-5, 80) != 40.45
        assert m.add(10, -7) != 12
        assert m.add(-12, 110) != -34.78
        assert m.add(45, -5) != -13
        assert m.add(-14, 51) != -9.65
        assert m.add(-25, 125) != 0
        assert m.add(100, -103564) != 0

    def test_addNotEqualNegativeNegative(self):
        #negative number & negative number
        assert m.add(-2, -3) != -2
        assert m.add(-5, -1) != -27
        assert m.add(-13, -7) != 87.7
        assert m.add(-40, -11) != 0
        assert m.add(-4025, -46555) != -44524
        assert m.add(-1484910, -6515612) != 1001

class TestSubtraction:
    def test_subEqualPositivePositive(self):
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

    def test_subEqualPositiveNegative(self):
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

    def test_subEqualNegativeNegative(self):
        #negative number & negative number
        assert m.subtraction(-5, -8) == 3
        assert m.subtraction(-30, -18) == -12
        assert m.subtraction(-3, -7) == 4
        assert m.subtraction(-301, -121) == -180
        assert m.subtraction(-1025, -2555) == 1530
        assert m.subtraction(-19796, -20123) == 327
        
    def test_subNotEqualPositivePositive(self):
        #positive number & positive number
        assert m.subtraction(2, 4) != 0
        assert m.subtraction(70, 30) != 15
        assert m.subtraction(2100, 181) != 171
        assert m.subtraction(100, 107) != 7
        assert m.subtraction(40, 111) != -1044524
        assert m.subtraction(4025, 46555) != 0.5
        assert m.subtraction(1484910, 6515612) != -1

    def test_subNotEqualPositiveNegative(self):
        #positive number & negative number
        assert m.subtraction(-22, 311) != -111
        assert m.subtraction(-564, 80) != 40
        assert m.subtraction(10, -7) != 45
        assert m.subtraction(-12, 110) != 100
        assert m.subtraction(45, -5) != -12
        assert m.subtraction(-74, 51) != -9
        assert m.subtraction(-25, 25) != 0
        assert m.subtraction(100, -103564) != 0

    def test_subNotEqualNegativeNegative(self):
        #negative number & negative number
        assert m.subtraction(-2, -3) != 0
        assert m.subtraction(-5, -1) != -27.5
        assert m.subtraction(-13, -7) != -46
        assert m.subtraction(-40, -11) != 10
        assert m.subtraction(-4025, -46555) != 3.33
        assert m.subtraction(-1480.45, -6515612) != -12314

class TestMultiplication:
    def test_mulEqualPositivePositive(self):
        #positive number & positive number
        assert m.multiplication(0, 0) == 0
        assert m.multiplication(0, 67) == 0
        assert m.multiplication(9855, 0) == 0
        assert m.multiplication(3, 4) == 12
        assert m.multiplication(13, 6) == 78
        assert m.multiplication(55, 23) == 1265
        assert m.multiplication(647, 87) == 56289
        assert m.multiplication(7472, 954) == 7128288

    def test_mulEqualPositiveNegative(self):
        #positive number & negative number
        assert m.multiplication(-5, 0) == 0
        assert m.multiplication(0, -45) == 0
        assert m.multiplication(-5, 12) == -60
        assert m.multiplication(7, -43) == -301
        assert m.multiplication(-76, 97) == -7372
        assert m.multiplication(-56, 38) == -2128
        assert m.multiplication(92, -111) == -10212
        assert m.multiplication(-6574, 3759) == -24711666

    def test_mulEqualNegativeNegative(self):
        #negative number & negative number
        assert m.multiplication(-5, -1) == 5
        assert m.multiplication(-3, -7) == 21
        assert m.multiplication(-43, -5) == 215
        assert m.multiplication(-3, -98) == 294
        assert m.multiplication(-75, -28) == 2100
        assert m.multiplication(-69, -55) == 3795
        assert m.multiplication(-423, -30) == 12690
        assert m.multiplication(-6, -666) == 3996
        assert m.multiplication(-485, -608) == 294880
        assert m.multiplication(-5034, -7837) == 39451458

    def test_mulNotEqualPositivePositive(self):
        #positive number & positive number
        assert m.multiplication(0, 0) != 8
        assert m.multiplication(53, 0) != 53
        assert m.multiplication(0, 679) != 3
        assert m.multiplication(4, 3) != 231
        assert m.multiplication(76, 9) != 83
        assert m.multiplication(45, 20) != 50
        assert m.multiplication(653, 788) != 89043
        assert m.multiplication(502, 3) != 10001
        assert m.multiplication(3904, 2200) != 7849027

    def test_mulNotEqualPositiveNegative(self):
        #positive number & negative number
        assert m.multiplication(0, -5) != 8
        assert m.multiplication(-22, 0) != 42
        assert m.multiplication(4, -8) != -31
        assert m.multiplication(25, -3) != 75
        assert m.multiplication(80, -80) != -1616
        assert m.multiplication(-71, 993) != 73922
        assert m.multiplication(441, -2) != -655
        assert m.multiplication(232, -391) != -74583
        assert m.multiplication(-9563, -3068) != 392702

    def test_mulNotEqualNegativeNegative(self):
        #negative number & negative number
        assert m.multiplication(-3, -9) != 0
        assert m.multiplication(-1, -5) != -5
        assert m.multiplication(-4, -8) != 98
        assert m.multiplication(-18, -7) != -40
        assert m.multiplication(-36, -89) != 3689
        assert m.multiplication(-328, -2) != -403
        assert m.multiplication(-532, -439) != 903320
        assert m.multiplication(-4345, -6821) != -28333745
        assert m.multiplication(-73923, -4) != -38392

class TestDivide:
    def test_divEqualPositivePositive(self):
        #positive number & positive number
        assert m.divide(10, 5) == 2
        assert m.divide(15, 3) == 5
        assert m.divide(21, 7) == 3
        assert m.divide(32, 4) == 8
        assert m.divide(99, 3) == 33
        assert m.divide(1152, 18) == 64
        assert m.divide(0, 14568) == 0
        assert m.divide(119658, 231) == 518
        assert m.divide(2, 0) == "Invalid input"

    def test_divEqualPositiveNegative(self):
        #positive number & negative number
        assert m.divide(6, -3) == -2
        assert m.divide(28, -7) == -4
        assert m.divide(12, -2) == -6
        assert m.divide(-18, 6) == -3
        assert m.divide(-64, 8) == -8
        assert m.divide(-110, 5) == -22
        assert m.divide(294, -14) == -21
        assert m.divide(3509, -121) == -29
        assert m.divide(-37730, 154) == -245

    def test_divEqualNegativeNegative(self):
        #negative number & negative number
        assert m.divide(-5, -5) == 1
        assert m.divide(-14, -7) == 2
        assert m.divide(-35, -7) == 5
        assert m.divide(-81, -3) == 27
        assert m.divide(-144, -6) == 24
        assert m.divide(-256, -4) == 64
        assert m.divide(-17848, -92) == 194
        assert m.divide(-177152, -512) == 346
        assert m.divide(-297416, -452) == 658
    
    def test_divNotEqualPositivePositive(self):
        #postive number & positive number
        assert m.divide(12, 2) != 8
        assert m.divide(90, 3) != 15
        assert m.divide(15, 5) != 4
        assert m.divide(6, 3) != 1
        assert m.divide(225, 15) != 14
        assert m.divide(333, 3) != 100
        assert m.divide(1024, 256) != 5
        assert m.divide(1568, 4) != 393
        assert m.divide(177152, 346) != 500 

    def test_divNotEqualPositiveNegative(self):
        #positive number & negative number
        assert m.divide(-12, 4) != 3
        assert m.divide(18, -6) != 3
        assert m.divide(25, -25) != 0
        assert m.divide(56, -7) != 8
        assert m.divide(234, -2) != -116
        assert m.divide(-81, 9) != 9
        assert m.divide(169, -13) != 13
        assert m.divide(-1200, 4) != 300
        assert m.divide(392702, -3068) != 9563
        
    def test_divNotEqualNegativeNegative(self):        
        #negative number & negative number
        assert m.divide(-25, -5) != -5
        assert m.divide(-32, -8) != 155
        assert m.divide(-72, -6) != 13
        assert m.divide(-121, -11) != -11
        assert m.divide(-13952, -4) != 45668
        assert m.divide(-156468, -5612) != 468412
        assert m.divide(-4532, -1133) != -4
        assert m.divide(-332688, -348) != -956
        assert m.divide(-5943456, -4586) != 1300

class TestModulo:
    def test_modEqualPositivePositive(self):
        #positive number & positive number
        assert m.modulo(5, 2) == 1
        assert m.modulo(10, 4) == 2
        assert m.modulo(21, 6) == 3
        assert m.modulo(32, 3) == 2
        assert m.modulo(153, 12) == 9
        assert m.modulo(185, 13) == 3
        assert m.modulo(2546, 25) == 21
        assert m.modulo(33458, 16500) == 458
        assert m.modulo(125485, 24555) == 2710

    def test_modEqualPositiveNegative(self):
        #positive number & negative number
        assert m.modulo(12, -5) == -3
        assert m.modulo(27, -4) == -1
        assert m.modulo(-36, 5) == 4
        assert m.modulo(47, -7) == -2
        assert m.modulo(-80, 23) == 12
        assert m.modulo(123, -14) == -3
        assert m.modulo(-256, 15) == 14
        assert m.modulo(-48252, 1269) == 1239
        assert m.modulo(7026500, -9683) == -3358

    def test_modEqualNegativeNegative(self):
        #negative number & negative number
        assert m.modulo(-6, -4) == -2
        assert m.modulo(-13, -5) == -3
        assert m.modulo(-19, -4) == -3
        assert m.modulo(-28, -12) == -4
        assert m.modulo(-43, -19) == -5
        assert m.modulo(-89, -23) == -20
        assert m.modulo(-168, -13) == -12
        assert m.modulo(-2496, -1342) == -1154
        assert m.modulo(-15896, -2652) == -2636

    def test_modNotEqualPositivePositive(self):
        #positive number & positive number
        assert m.modulo(4, 2) != 2
        assert m.modulo(8, 3) != 1
        assert m.modulo(12, 9) != 4
        assert m.modulo(5, 2) != 0
        assert m.modulo(45, 4) != 5
        assert m.modulo(49, 7) != 7
        assert m.modulo(149, 25) != 23
        assert m.modulo(638, 125) != 40
        assert m.modulo(2049, 459) != 3548
        assert m.modulo(145986, 2462) != 0

    def test_modNotEqualPositiveNegative(self):
        #positive number & negative number
        assert m.modulo(5, -2) != 1
        assert m.modulo(9, -5) != -4
        assert m.modulo(16, -6) != -4
        assert m.modulo(-82, 40) != 2
        assert m.modulo(125, -24) != -5
        assert m.modulo(-195, 128) != -15
        assert m.modulo(-5489, 5489) != 1
        assert m.modulo(18237, -6000) != -237
        assert m.modulo(259453, -42149) != 0

    def test_modNotEqualNegativeNegative(self):
        #negative number & negative number
        assert m.modulo(-15, -4) != 3
        assert m.modulo(-6, -4) != 2
        assert m.modulo(-93, -21) != 9
        assert m.modulo(-45, -13) != 6
        assert m.modulo(-7, -5) != 2
        assert m.modulo(-69, -42) != -28
        assert m.modulo(-153, -122) != 122
        assert m.modulo(-6548, -2555) != -1689
        assert m.modulo(-48294, -48294) != 1 

class TestPower:
    def test_powEqualPositivePositive(self):
        #positive number & positive number
        assert m.power(0, 0) == 1 
        assert m.power(5, 0) == 1
        assert m.power(7, 2) == 49
        assert m.power(3, 5) == 243
        assert m.power(0, 27) == 0 
        assert m.power(35, 4) == 1500625
        assert m.power(123, 1) == 123
        assert m.power(609, 3) == 225866529

    def test_powEqualPositiveNegative(self):
        #positive number & negative number
        assert m.power(0, -3) == "Invalid input" 
        assert m.power(2, -2) == 0.25
        assert m.power(20, -1) == 0.05
        assert m.power(5, -4) == 0.0016 
        assert m.power(1, -5) == 1 
        assert m.power(4, -6) == 0.000244140625
        assert m.power(2, -3) == 0.125
        assert m.power(8, -2) == 0.015625 

    def test_powEqualNegativePositive(self):
        #negative number & positive number
        assert m.power(-2, 0) == 1
        assert m.power(-3, 2) == 9
        assert m.power(-7, 4) == 2401
        assert m.power(-5, 1) == -5
        assert m.power(-14, 2) == 196
        assert m.power(-22, 3) == -10648
        assert m.power(-5, 4) == 625
        assert m.power(-15, 3) == -3375
        
    def test_powEqualNegativeNegative(self):
        #negative number & negative number
        assert m.power(-1, -1) == -1
        assert m.power(-1, -89) == -1
        assert m.power(-2, -3) == -0.125
        assert m.power(-20, -2) == 0.0025
        assert m.power(-4, -2) == 0.0625
        assert m.power(-8, -1) == -0.125
        assert m.power(-5, -2) == 0.04
        assert m.power(-5, -1) == -0.2

    def test_powNotEqualPositivePositive(self):
        #positive number & positive number
        assert m.power(0, 0) != 3
        assert m.power(0, 2) != 1
        assert m.power(21, 0) != 21
        assert m.power(50, 5) != 55
        assert m.power(23, 2) != 675
        assert m.power(652, 1) != 1000
        assert m.power(17, 8) != 34533346
        assert m.power(84, 5) != 689239

    def test_powNotEqualPositiveNegative(self):
        #positive number & negative number
        assert m.power(3, -1) != 0.5332
        assert m.power(6, -6) != -0.4321
        assert m.power(23, -1) != 0.64893
        assert m.power(5, -4) != 2.445
        assert m.power(32, -3) != -4583
        assert m.power(66, -2) != -0.6892
        assert m.power(4, -3) != 0.1124
        assert m.power(86, -7) != 933

    def test_powNotEqualNegativePositive(self):
        #negative number & positive number
        assert m.power(-4, 5) != -20
        assert m.power(-7, 2) != 50
        assert m.power(-34, 0) != -1
        assert m.power(-4, 2) != -16
        assert m.power(-84, 4) != -5432123
        assert m.power(-643, 0) != -643
        assert m.power(-45, 3) != 632
        assert m.power(-6325, 1) != 6325

    def test_powNotEqualNegativeNegative(self):
        #negative number & negative number
        assert m.power(-1, -1) != -2
        assert m.power(-3, -3) != -9
        assert m.power(-23, -1) != -0.5333
        assert m.power(-6, -3) != -0.000005
        assert m.power(-2, -13) != -0.0353638
        assert m.power(-43, -5) != -0.6373223
        assert m.power(-5, -2) != 10
        assert m.power(-74, -2) != -321321

class TestNthRoot:
    def test_nthEqualPositivePositive(self):
        #positive number & negative number
        assert m.nthRoot(2, 4) == 2 
        assert m.nthRoot(2, 25) == 5
        assert m.nthRoot(2, 144) == 12
        assert m.nthRoot(3, 27) == 3
        assert m.nthRoot(3, 64) == 4
        assert m.nthRoot(3, 729) == 9
        assert m.nthRoot(4, 625) == 5
        assert m.nthRoot(5, 7776) == 6
        assert m.nthRoot(10, 1073741824) == 8 

    def test_nthEqualPositiveNegative(self):
        #positive number & negative number
        assert m.nthRoot(2, -3) == "Invalid input"
        assert m.nthRoot(2, -144) == "Invalid input"
        assert m.nthRoot(3, -27) == -3
        assert m.nthRoot(3, -64) == -4
        assert m.nthRoot(3, -13824) == -24
        assert m.nthRoot(3, -1331) == -11
        assert m.nthRoot(7, -279936) == -6
        assert m.nthRoot(5, -371293) == -13
        assert m.nthRoot(9, -134217728) == -8

    def test_nthEqualNegativePositive(self):
        #negative number & positive number
        assert m.nthRoot(-2, 3) == 0.57735026918963
        assert m.nthRoot(-2, 5) == 0.44721359549996
        assert m.nthRoot(-2, 8) == 0.35355339059327
        assert m.nthRoot(-2, 256) == 0.0625
        assert m.nthRoot(-4, 345) == 0.2320305803247
        assert m.nthRoot(-4, 425) == 0.22024333135708
        assert m.nthRoot(-5, 152) == 0.36612659984709
        assert m.nthRoot(-10, 512) == 0.53588673126815
        assert m.nthRoot(-20, 388) == 0.74226402743811

    def test_nthEqualNegativeNegative(self):
        #negative number & negative number
        assert m.nthRoot(-2, -13) == "Invalid input"
        assert m.nthRoot(-2, -66) == "Invalid input"
        assert m.nthRoot(-2, -112) == "Invalid input"
        assert m.nthRoot(-4, -98) == "Invalid input"
        assert m.nthRoot(-4, -69) == "Invalid input"
        assert m.nthRoot(-4, -6) == "Invalid input"
        assert m.nthRoot(-5, -10) == -0.63095734448019
        assert m.nthRoot(-10, -46) == "Invalid input"
        assert m.nthRoot(-20, 623) == 0.72489582367171

    def test_nthNotEqualPositivePositive(self):
        #positive number & positive number
        assert m.nthRoot(2, 9) != 4
        assert m.nthRoot(2, 0) != 1
        assert m.nthRoot(2, 25) != 6
        assert m.nthRoot(3, 64) != 5
        assert m.nthRoot(3, 125) != 10
        assert m.nthRoot(3, 216) != 7
        assert m.nthRoot(4, 81) != 4
        assert m.nthRoot(5, 3125) != -5
        assert m.nthRoot(8, 43046721) != 10
        
    def test_nthNotEqualPositiveNegative(self):
        #positive number & negative number
        assert m.nthRoot(2, -25) != -5
        assert m.nthRoot(2, -36) != -6
        assert m.nthRoot(2, -49) != -7 
        assert m.nthRoot(4, -81) != -3
        assert m.nthRoot(6, -46656) != -6
        assert m.nthRoot(9, -262144) != -5
        assert m.nthRoot(6, -2985984) != -12
        assert m.nthRoot(15, -32768) != 2
        assert m.nthRoot(17, -129140163) != 3

    def test_nthNotEqualNegativePositive(self):
        #negative number & positive number
        assert m.nthRoot(-2, 25) != 0.3 
        assert m.nthRoot(-2, 36) != 0.15
        assert m.nthRoot(-2, 49) != 0.13
        assert m.nthRoot(-3, 125) != 5
        assert m.nthRoot(-3, 1000) != 10
        assert m.nthRoot(-4, 23) != 0.5
        assert m.nthRoot(-6, 48) != 1
        assert m.nthRoot(-9, 456) != 45
        assert m.nthRoot(-10, 1000000) != 25

    def test_nthNotEqualNegativeNegative(self):
        #negative number & negative number
        assert m.nthRoot(-2, -49) != -7
        assert m.nthRoot(-2, -458) != -13
        assert m.nthRoot(-2, -596) != 1
        assert m.nthRoot(-4, -156) != -4.5
        assert m.nthRoot(-6, -789) != 12
        assert m.nthRoot(-8, -165546) != -128
        assert m.nthRoot(-9, -369) != 2
        assert m.nthRoot(-12, -45698) != 0.5
        assert m.nthRoot(-20, -1354648) != 0.1

class TestFactorial:
    def test_facEqualPositive(self):
        #positive number
        assert m.factorial(1) == 1
        assert m.factorial(2) == 2
        assert m.factorial(0) == 1
        assert m.factorial(5) == 120
        assert m.factorial(7) == 5040
        assert m.factorial(10) == 3628800
        assert m.factorial(12) == 479001600
        assert m.factorial(13) == 6227020800

    def test_facEqualNegative(self):
        #negative number
        assert m.factorial(-3) == "Invalid input"
        assert m.factorial(-2) == "Invalid input"
        assert m.factorial(-4) == "Invalid input"
        assert m.factorial(-1) == "Invalid input"
        assert m.factorial(-7) == "Invalid input"
        assert m.factorial(-5) == "Invalid input"

    def test_facNotEqualPositive(self):
        #positive number
        assert m.factorial(1) != 0
        assert m.factorial(3) != 9
        assert m.factorial(4) != 12
        assert m.factorial(6) != -720
        assert m.factorial(0) != 0
        assert m.factorial(9) != 36288
        assert m.factorial(11) != 7598364
        assert m.factorial(14) != 6535333
        assert m.factorial(5) != 25

    def test_facNotEqualNegative(self):
        #negative number
        assert m.factorial(-2) != 4
        assert m.factorial(-4) != 16
        assert m.factorial(-6) != 45
        assert m.factorial(-1) != 1
        assert m.factorial(-5) != 625
        assert m.factorial(-11) != 72528034
