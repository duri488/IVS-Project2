from PyQt5.QtWidgets import *
from clcLib.calculatorUI import Ui_MainWindow
import clcLib.mathlib as m
import sys

leftSide = ""
rightSide = ""
leftSideValue = ""
rightSideValue = ""
operator = ""
operatorFlag = False
errorFlag = False

class Logic(QMainWindow):
    def __init__(self):
        super(Logic, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.oneButton.clicked.connect(lambda x:self.numberClick("1"))
        self.ui.twoButton.clicked.connect(lambda x:self.numberClick("2"))
        self.ui.threeButton.clicked.connect(lambda x:self.numberClick("3"))
        self.ui.fourButton.clicked.connect(lambda x:self.numberClick("4"))
        self.ui.fiveButton.clicked.connect(lambda x:self.numberClick("5"))
        self.ui.sixButton.clicked.connect(lambda x:self.numberClick("6"))
        self.ui.sevenButton.clicked.connect(lambda x:self.numberClick("7"))
        self.ui.eightButton.clicked.connect(lambda x:self.numberClick("8"))
        self.ui.nineButton.clicked.connect(lambda x:self.numberClick("9"))
        self.ui.zeroButton.clicked.connect(lambda x:self.numberClick("0"))
        self.ui.pointButton.clicked.connect(lambda x:self.numberClick("."))
        self.ui.plusMinusButton.clicked.connect(self.changeSign)

        self.ui.plusButton.clicked.connect(lambda x:self.numberClick("+"))
        self.ui.minusButton.clicked.connect(lambda x:self.numberClick("-"))
        self.ui.multiplyButton.clicked.connect(lambda x:self.numberClick("*"))
        self.ui.divButton.clicked.connect(lambda x:self.numberClick("/"))
        self.ui.powerButton.clicked.connect(lambda x:self.numberClick("^"))

        self.ui.sqrtButton.clicked.connect(lambda x:self.numberClick('\u221A')) #odmocnina
        self.ui.modButton.clicked.connect(lambda x:self.numberClick("mod"))
        self.ui.unknownButton.clicked.connect(lambda x:self.numberClick("!"))
        self.ui.piButton.clicked.connect(lambda x:self.numberClick('\u03C0')) #pi

        self.ui.backButton.clicked.connect(self.backClick)
        self.ui.cButton.clicked.connect(self.cClick)

        self.ui.equalButton.clicked.connect(self.equalClick)

    def numberClick(self,number):
        global operatorFlag
        global leftSide
        global rightSide
        global errorFlag
        global leftSideValue
        global operator
        #global rightSideValue

        if operatorFlag == False:
            if (number == "+" or number == "-" or number == "*" or number == "/" or number == "^" or number == '\u221A' or number == "mod" or number == "!"):
                leftSideValue = eval(leftSide)
                operator = str(number)
                operatorFlag = True
            else:
                leftSide = leftSide + str(number)

            self.ui.Display.setText(leftSide+operator+rightSide)
        else:
            if (number == "+" or number == "-" or number == "*" or number == "/" or number == "^" or number == '\u221A' or number == "mod" or number == "!"):
                pass
            else:
                if "!" in operator:
                    pass
                else:
                    rightSide = rightSide + str(number)
                    self.ui.Display.setText(leftSide+operator+rightSide)

        self.ui.resultDisplay.setText("")

    def backClick(self):
        #global showOnDisplay
        #global leftSide
        #global rightSide
        #global operatorFlag

        #if showOnDisplay:
        #    if showOnDisplay[-1] == "+" or showOnDisplay[-1] == "-" or showOnDisplay[-1] == "*" or showOnDisplay[-1] == "/" or showOnDisplay[-1] == "^" or showOnDisplay[-1] == '\u221A' or showOnDisplay[-1] == "mod" or showOnDisplay[-1] == "!":
        #        operatorFlag = False
        #    else:
        #        if not rightSide:
        #            leftSide = leftSide[:-1]
        #        else:
        #            rightSide = rightSide[:-1]

        #    showOnDisplay = showOnDisplay[:-1]
        #    self.ui.Display.setText(showOnDisplay)
        pass
        
    def cClick(self):

        clearEverything()

        self.ui.Display.setText("0")
        self.ui.resultDisplay.setText("")

    def changeSign(self):
        global operator
        global leftSide
        global rightSide

        if leftSide:
            if not operator:
                if leftSide[0] != "-":
                    leftSide = "-"+leftSide
                else:
                    leftSide = leftSide[1:]
            else:
                if rightSide:
                    if rightSide[0] != "-":
                        rightSide = "-"+rightSide
                    else:
                        leftSide = rightSide[1:]
            self.ui.Display.setText(leftSide+operator+rightSide)
        else:
            pass

        
        
    def equalClick(self):
        global operatorFlag
        global operator
        global leftSide
        global rightSide
        global errorFlag
        global leftSideValue
        global rightSideValue

        if rightSide:
            rightSideValue = eval(rightSide)
        result=""

        if errorFlag:
            result = "Invalid input"
        else:
            if not leftSide:
                result = "Invalid input"

            elif '!' in operator:
                result = m.factorial(leftSideValue)

            elif not rightSide:
                result = "Invalid input"

            elif '+' in operator:
                result = m.add(leftSideValue,rightSideValue)

            elif '-' in operator:
                result = m.subtraction(leftSideValue,rightSideValue)

            elif '*' in operator:
                result = m.multiplication(leftSideValue,rightSideValue)

            elif '/' in operator:
                result = m.divide(leftSideValue,rightSideValue)

            elif '^' in operator:
                result = m.multiplication(leftSideValue,rightSideValue)

            elif '\u221A' in operator: #odmocnina
                result = m.nthRoot(leftSideValue,rightSideValue)

            elif 'mod' in operator:
                result = m.modulo(leftSideValue,rightSideValue)

        self.ui.resultDisplay.setText(str(result))
        clearEverything()

        
def clearEverything():
    global operatorFlag
    global leftSide
    global rightSide
    global errorFlag
    global leftSideValue
    global rightSideValue
    global operator

    leftSide = ""
    rightSide = ""
    leftSideValue = ""
    rightSideValue = ""
    operator = ""
    operatorFlag = False
    errorFlag = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    logic = Logic()
    logic.show()
    sys.exit(app.exec_())