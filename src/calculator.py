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
    """
    Trieda ktorá dedí z triedy Ui_MainWindow a rozširuje ju o logickú funkcionalitu kalkulačky.
    """
    def __init__(self):
        """
        Inicializácia kalkulačky a priradenie funkcionality tlačidlám
        """
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

        """
        Funkcia na zaznamenávanie vstupu od uživateľa.
        :param number: symbol tlačítka ktoré použil uživateľ
        """

        global operatorFlag
        global leftSide
        global rightSide
        global errorFlag
        global leftSideValue
        global operator

        if operatorFlag == False:
            if (number == "+" or number == "-" or number == "*" or number == "/" or number == "^" or number == '\u221A' or number == "mod" or number == "!"):
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

        """
        Funkcia na odstránenie posledného pridaného znaku.
        """

        global operatorFlag
        global leftSide
        global rightSide
        global errorFlag
        global leftSideValue
        global operator

        if rightSide:
            rightSide = rightSide[:-1]
            self.ui.Display.setText(leftSide+operator+rightSide)
        elif operator:
            operatorFlag = False
            operator = ""
            self.ui.Display.setText(leftSide+operator+rightSide)
        elif leftSide:
            leftSide = leftSide[:-1]
            self.ui.Display.setText(leftSide+operator+rightSide)
        else:
            pass
        
    def cClick(self):
        """
        Funkcia zobrazí displej po vyčistení pamäte kalkulačky
        """

        clearEverything()

        self.ui.Display.setText("0")
        self.ui.resultDisplay.setText("")

    def changeSign(self):

        """
        Funkcia na zmenu znamienka zadávaného čísla do kalkulačky.
        """
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
        """
        Funkcia na vyhodnotenie zadaného príkladu v kalkulačke. Volá funkcie z matematickej knižnice mathlib.py
        """
        global operatorFlag
        global operator
        global leftSide
        global rightSide
        global errorFlag
        global leftSideValue
        global rightSideValue

        if rightSide:
            if "\u03C0" in rightSide:
                if rightSide[0] == "-":
                    rightSideValue =(-m.PI)
                else:
                    rightSideValue =(m.PI)
            else:
                rightSideValue = eval(rightSide)

        if leftSide:
            if "\u03C0" in leftSide:
                if leftSide[0] == "-":
                    leftSideValue =(-m.PI)
                else:
                    leftSideValue =(m.PI)
            else:
                leftSideValue = eval(leftSide)

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
                result = m.power(leftSideValue,rightSideValue)

            elif '\u221A' in operator: #odmocnina
                result = m.nthRoot(leftSideValue,rightSideValue)

            elif 'mod' in operator:
                result = m.modulo(leftSideValue,rightSideValue)

            if not operator and leftSide and not rightSide:
                result = leftSideValue

        self.ui.resultDisplay.setText(str(result))
        clearEverything()



        
def clearEverything():

    """
    Táto funkcia vyčistí pamäť kalkulačky a všetky použité premenné
    """

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