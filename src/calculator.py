from PyQt5.QtWidgets import *
from clcLib.calculatorUI import Ui_MainWindow
import clcLib.mathlib as m
import sys

showOnDisplay = ""
leftSide = ""
rightSide = ""
leftSideValue = ""
rightSideValue = ""
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
        #self.ui.plusMinusButton.clicked.connect(lambda x:self.numberClick("."))

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
        global showOnDisplay
        global operatorFlag
        global leftSide
        global rightSide
        global errorFlag
        global leftSideValue
        #global rightSideValue

        if operatorFlag == False:
            if (number == "+" or number == "-" or number == "*" or number == "/" or number == "^" or number == '\u221A' or number == "mod" or number == "!"):
                leftSideValue = eval(leftSide)
                operatorFlag = True
            else:
                leftSide = leftSide + str(number)

            showOnDisplay = showOnDisplay + str(number)
            self.ui.Display.setText(showOnDisplay)
        else:
            if (number == "+" or number == "-" or number == "*" or number == "/" or number == "^" or number == '\u221A' or number == "mod" or number == "!"):
                pass
            else:
                if "!" in showOnDisplay:
                    pass
                else:
                    rightSide = rightSide + str(number)
                    showOnDisplay = showOnDisplay + str(number)
                    self.ui.Display.setText(showOnDisplay)

        self.ui.resultDisplay.setText("")

    def backClick(self):
        global showOnDisplay
        global leftSide
        global rightSide
        global operatorFlag

        if showOnDisplay:
            if showOnDisplay[-1] == "+" or showOnDisplay[-1] == "-" or showOnDisplay[-1] == "*" or showOnDisplay[-1] == "/" or showOnDisplay[-1] == "^" or showOnDisplay[-1] == '\u221A' or showOnDisplay[-1] == "mod" or showOnDisplay[-1] == "!":
                operatorFlag = False
            else:
                if not rightSide:
                    leftSide = leftSide[:-1]
                else:
                    rightSide = rightSide[:-1]

            showOnDisplay = showOnDisplay[:-1]
            self.ui.Display.setText(showOnDisplay)
        
    def cClick(self):

        clearEverything()

        self.ui.Display.setText("0")
        self.ui.resultDisplay.setText("")
        
    def equalClick(self):
        global showOnDisplay
        global operatorFlag
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
            if not leftSide or not rightSide:
                result = "Invalid input"
            elif '+' in showOnDisplay:
                result = m.add(leftSideValue,rightSideValue)

            elif '-' in showOnDisplay:
                result = m.subtraction(leftSideValue,rightSideValue)

            elif '*' in showOnDisplay:
                result = m.multiplication(leftSideValue,rightSideValue)

            elif '/' in showOnDisplay:
                result = m.divide(leftSideValue,rightSideValue)

            elif '^' in showOnDisplay:
                result = m.multiplication(leftSideValue,rightSideValue)

            elif '\u221A' in showOnDisplay: #odmocnina
                result = m.nthRoot(leftSideValue,rightSideValue)

            elif 'mod' in showOnDisplay:
                result = m.modulo(leftSideValue,rightSideValue)

            if '!' in showOnDisplay and not rightSide:
                result = m.factorial(leftSideValue)
            else:
                result = "Invalid input"

        self.ui.resultDisplay.setText(str(result))
        clearEverything()

        
def clearEverything():
    global showOnDisplay
    global operatorFlag
    global leftSide
    global rightSide
    global errorFlag
    global leftSideValue
    global rightSideValue

    showOnDisplay = ""
    leftSide = ""
    rightSide = ""
    leftSideValue = ""
    rightSideValue = ""
    operatorFlag = False
    errorFlag = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    logic = Logic()
    logic.show()
    sys.exit(app.exec_())