from PyQt5.QtWidgets import *
from clcLib.calculatorUI import Ui_MainWindow
import sys

showOnDisplay = ""

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

        showOnDisplay = showOnDisplay + str(number)
        self.ui.Display.setText(showOnDisplay)

    def backClick(self):
        global showOnDisplay

        showOnDisplay = showOnDisplay[:-1]
        self.ui.Display.setText(showOnDisplay)
        
    def cClick(self):
        global showOnDisplay

        showOnDisplay = ""
        self.ui.Display.setText("0")
        self.ui.resultDisplay.setText("")
        
    def equalClick(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    logic = Logic()
    logic.show()
    sys.exit(app.exec_())