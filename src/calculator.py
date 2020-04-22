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

        #connecting buttons to functions
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

        self.ui.sqrtButton.clicked.connect(lambda x:self.numberClick('\u221A')) #root symbol
        self.ui.modButton.clicked.connect(lambda x:self.numberClick("%"))
        self.ui.unknownButton.clicked.connect(lambda x:self.numberClick("!"))
        self.ui.piButton.clicked.connect(lambda x:self.numberClick('\u03C0')) #pi

        self.ui.backButton.clicked.connect(self.backClick)
        self.ui.cButton.clicked.connect(self.cClick)

        self.ui.equalButton.clicked.connect(self.equalClick)

        self.ui.actionAbout_2.triggered.connect(self.popup)

    def popup(self):
        """
        Funkcia ktorá vytvára okno nápovedy a jej obsah
        """

        msg = QMessageBox()
        msg.setWindowTitle("Nápoveda!")
        msg.setText(
"""
Nápoveda!\n
"+" - sčíta dve čísla (5+5)
"-" - odčíta dve čísla (5-5)
"*" - násobí dve čísla (5*5)
"/" - delí dve čísla (5/5)
"x^y" - umocňuje x na y (5^5)
"\u221A" - n-tá odmocnina (2 \u221A 4)
"%" - modulo dvoch čísel (5 mod 3)
"n!" - faktoriál čísla n (5!)
"\u03C0" - hodnota čísla PÍ(presnosť na 14 desatin. miest)
"C" - vyčistí pamäť kalkulačky
"\u232B" - vymaže posledný symbol výrazu
"+/-" - zmení znamienko posledného čísla
"." - desatinná čiarka
"=" - vyhodnotí zadaný výraz

Ak sa symbol nachádza na klávesnici,tak sa dá použiť\nako klávesová skratka.
"""
)
        msg.setIcon(QMessageBox.Question)

        x = msg.exec_()

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


        if operatorFlag == False:   #if there is no operator in expression - working with left side of expression
            if (number == "+" or number == "-" or number == "*" or number == "/" or number == "^" or number == '\u221A' or number == "%" or number == "!"): #catching an operator
                operator = str(number)
                operatorFlag = True
            else:   #if its not operator its still left side of expression 
                leftSide = leftSide + str(number)

            self.ui.Display.setText(leftSide+operator+rightSide)
        else:   #operator was inserted so we are working with right side of expression
            if (number == "+" or number == "-" or number == "*" or number == "/" or number == "^" or number == '\u221A' or number == "%" or number == "!"):
                pass    #we ignor adding second operator
            else:
                if "!" in operator:     #special case for factorial(it has only left part of expression)
                    pass    #ignoring everything after factorial symbol
                else:   #adding next symbol to right side of expression
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

        #looking for side of expression user is currently inserting
        if rightSide:
            rightSide = rightSide[:-1]  #removing last symbol 
            self.ui.Display.setText(leftSide+operator+rightSide)
        elif operator:
            operatorFlag = False    #clearing operator value
            operator = ""
            self.ui.Display.setText(leftSide+operator+rightSide)
        elif leftSide:
            leftSide = leftSide[:-1]    #removing last symbol
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
            if not operator:    #if we have only left side we are changing sign there
                if leftSide[0] != "-":  #checking first symbol and adding or removing "-" sign
                    leftSide = "-"+leftSide
                else:
                    leftSide = leftSide[1:]
            else:   
                if rightSide: #we have also right side so we are changing sign there
                    if rightSide[0] != "-": #checking first symbol and adding or removing "-" sign
                        rightSide = "-"+rightSide
                    else:
                        rightSide = rightSide[1:]
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

        rightSideValue = SideValue(rightSide)

        leftSideValue = SideValue(leftSide)

        result=""

        if errorFlag:
            result = "Invalid input"
        else:
            if not leftSide:
                result = "Invalid input"

            #calling functions from mathlib based on operator value
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

            elif '\u221A' in operator: #root symbol
                result = m.nthRoot(leftSideValue,rightSideValue)

            elif '%' in operator:
                result = m.modulo(leftSideValue,rightSideValue)

            if not operator and leftSide and not rightSide: # if user inserted only one number without operator
                result = leftSideValue

        self.ui.resultDisplay.setText(str(result))
        clearEverything()

def SideValue(side):

    """
    Funkcia transformuje zadaný vstup od uživateľa na jeho hodnotu
    
    :param side: vstup danej strany zadaný uživateľom
    :return: hodnota výrazu danej strany 
    """

    if side:
        if "\u03C0" in side: #kontrola pre výskyt symbolu "pí" vo výraze
            if side[0] == "-":
                return (-m.PI)
            else:
                return (m.PI)
        else:
            return eval(side)

        
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


    #clearing all variables
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