from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    """
    Automaticky vygenerovaná trieda pomocou QT Designeru ktorá definuje GUI
    """

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(540, 610)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setWindowIcon(QtGui.QIcon('./images/ms-icon-70x70.png'))
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.modButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modButton.sizePolicy().hasHeightForWidth())
        self.modButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.modButton.setFont(font)
        self.modButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.modButton.setObjectName("modButton")
        self.gridLayout.addWidget(self.modButton, 4, 0, 1, 1)
        self.pointButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pointButton.sizePolicy().hasHeightForWidth())
        self.pointButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pointButton.setFont(font)
        self.pointButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(94, 94, 94);")
        self.pointButton.setObjectName("pointButton")
        self.gridLayout.addWidget(self.pointButton, 8, 2, 1, 1)
        self.plusButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusButton.sizePolicy().hasHeightForWidth())
        self.plusButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plusButton.setFont(font)
        self.plusButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.plusButton.setObjectName("plusButton")
        self.gridLayout.addWidget(self.plusButton, 7, 3, 1, 1)
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sevenButton.sizePolicy().hasHeightForWidth())
        self.sevenButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sevenButton.setFont(font)
        self.sevenButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(94, 94, 94);")
        self.sevenButton.setObjectName("sevenButton")
        self.gridLayout.addWidget(self.sevenButton, 5, 0, 1, 1)
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oneButton.sizePolicy().hasHeightForWidth())
        self.oneButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.oneButton.setFont(font)
        self.oneButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(94, 94, 94);")
        self.oneButton.setObjectName("oneButton")
        self.gridLayout.addWidget(self.oneButton, 7, 0, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 3, 3, 1, 1)
        self.sixButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sixButton.sizePolicy().hasHeightForWidth())
        self.sixButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sixButton.setFont(font)
        self.sixButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(94, 94, 94);")
        self.sixButton.setObjectName("sixButton")
        self.gridLayout.addWidget(self.sixButton, 6, 2, 1, 1)
        self.cButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cButton.sizePolicy().hasHeightForWidth())
        self.cButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cButton.setFont(font)
        self.cButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.cButton.setObjectName("cButton")
        self.gridLayout.addWidget(self.cButton, 3, 2, 1, 1)
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zeroButton.sizePolicy().hasHeightForWidth())
        self.zeroButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.zeroButton.setFont(font)
        self.zeroButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(94, 94, 94);")
        self.zeroButton.setObjectName("zeroButton")
        self.gridLayout.addWidget(self.zeroButton, 8, 1, 1, 1)
        self.piButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.piButton.sizePolicy().hasHeightForWidth())
        self.piButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.piButton.setFont(font)
        self.piButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.piButton.setObjectName("piButton")
        self.gridLayout.addWidget(self.piButton, 3, 1, 1, 1)
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiplyButton.sizePolicy().hasHeightForWidth())
        self.multiplyButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.multiplyButton.setObjectName("multiplyButton")
        self.gridLayout.addWidget(self.multiplyButton, 5, 3, 1, 1)
        self.equalButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equalButton.sizePolicy().hasHeightForWidth())
        self.equalButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.equalButton.setFont(font)
        self.equalButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.equalButton.setObjectName("equalButton")
        self.gridLayout.addWidget(self.equalButton, 8, 3, 1, 1)
        self.threeButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threeButton.sizePolicy().hasHeightForWidth())
        self.threeButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.threeButton.setFont(font)
        self.threeButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(94, 94, 94);")
        self.threeButton.setObjectName("threeButton")
        self.gridLayout.addWidget(self.threeButton, 7, 2, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 100))
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 520, 100))
        self.scrollAreaWidgetContents_6.setMinimumSize(QtCore.QSize(0, 75))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_4.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.resultDisplay = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultDisplay.sizePolicy().hasHeightForWidth())
        self.resultDisplay.setSizePolicy(sizePolicy)
        self.resultDisplay.setMinimumSize(QtCore.QSize(0, 0))
        self.resultDisplay.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.resultDisplay.setFont(font)
        self.resultDisplay.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.resultDisplay.setStyleSheet("color: rgb(255, 255, 255);")
        self.resultDisplay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.resultDisplay.setObjectName("resultDisplay")
        self.gridLayout_4.addWidget(self.resultDisplay, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout.addWidget(self.scrollArea_2, 1, 0, 1, 4)
        self.minusButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minusButton.sizePolicy().hasHeightForWidth())
        self.minusButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minusButton.setFont(font)
        self.minusButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.minusButton.setObjectName("minusButton")
        self.gridLayout.addWidget(self.minusButton, 6, 3, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(520, 100))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 125))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 520, 109))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Display = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Display.setFont(font)
        self.Display.setStyleSheet("color: rgb(255, 255, 255);")
        self.Display.setObjectName("Display")
        self.gridLayout_3.addWidget(self.Display, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 4)
        self.powerButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerButton.sizePolicy().hasHeightForWidth())
        self.powerButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.powerButton.setFont(font)
        self.powerButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.powerButton.setObjectName("powerButton")
        self.gridLayout.addWidget(self.powerButton, 4, 2, 1, 1)
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fiveButton.sizePolicy().hasHeightForWidth())
        self.fiveButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fiveButton.setFont(font)
        self.fiveButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(94, 94, 94);")
        self.fiveButton.setObjectName("fiveButton")
        self.gridLayout.addWidget(self.fiveButton, 6, 1, 1, 1)
        self.sqrtButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sqrtButton.sizePolicy().hasHeightForWidth())
        self.sqrtButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sqrtButton.setFont(font)
        self.sqrtButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.sqrtButton.setObjectName("sqrtButton")
        self.gridLayout.addWidget(self.sqrtButton, 4, 1, 1, 1)
        self.fourButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fourButton.sizePolicy().hasHeightForWidth())
        self.fourButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fourButton.setFont(font)
        self.fourButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(94, 94, 94);")
        self.fourButton.setObjectName("fourButton")
        self.gridLayout.addWidget(self.fourButton, 6, 0, 1, 1)
        self.twoButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twoButton.sizePolicy().hasHeightForWidth())
        self.twoButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.twoButton.setFont(font)
        self.twoButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(94, 94, 94);")
        self.twoButton.setObjectName("twoButton")
        self.gridLayout.addWidget(self.twoButton, 7, 1, 1, 1)
        self.unknownButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unknownButton.sizePolicy().hasHeightForWidth())
        self.unknownButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.unknownButton.setFont(font)
        self.unknownButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.unknownButton.setObjectName("unknownButton")
        self.gridLayout.addWidget(self.unknownButton, 3, 0, 1, 1)
        self.plusMinusButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusMinusButton.sizePolicy().hasHeightForWidth())
        self.plusMinusButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plusMinusButton.setFont(font)
        self.plusMinusButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(94, 94, 94);")
        self.plusMinusButton.setObjectName("plusMinusButton")
        self.gridLayout.addWidget(self.plusMinusButton, 8, 0, 1, 1)
        self.eightButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eightButton.sizePolicy().hasHeightForWidth())
        self.eightButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.eightButton.setFont(font)
        self.eightButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(94, 94, 94);")
        self.eightButton.setObjectName("eightButton")
        self.gridLayout.addWidget(self.eightButton, 5, 1, 1, 1)
        self.divButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divButton.sizePolicy().hasHeightForWidth())
        self.divButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.divButton.setFont(font)
        self.divButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.divButton.setObjectName("divButton")
        self.gridLayout.addWidget(self.divButton, 4, 3, 1, 1)
        self.nineButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nineButton.sizePolicy().hasHeightForWidth())
        self.nineButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nineButton.setFont(font)
        self.nineButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(94, 94, 94);")
        self.nineButton.setObjectName("nineButton")
        self.gridLayout.addWidget(self.nineButton, 5, 2, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStandard = QtWidgets.QAction(MainWindow)
        self.actionStandard.setObjectName("actionStandard")
        self.actionScientific = QtWidgets.QAction(MainWindow)
        self.actionScientific.setObjectName("actionScientific")
        self.actionProgrammer = QtWidgets.QAction(MainWindow)
        self.actionProgrammer.setObjectName("actionProgrammer")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.menuMenu.addAction(self.actionStandard)
        self.menuMenu.addAction(self.actionScientific)
        self.menuMenu.addAction(self.actionProgrammer)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionAbout_2)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
   
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.modButton.setText(_translate("MainWindow", "mod"))
        self.modButton.setShortcut(_translate("MainWindow", "M"))
        self.pointButton.setText(_translate("MainWindow", ","))
        self.pointButton.setShortcut(_translate("MainWindow", "."))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.plusButton.setShortcut(_translate("MainWindow", "+"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.sevenButton.setShortcut(_translate("MainWindow", "7"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.oneButton.setShortcut(_translate("MainWindow", "1"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.backButton.setShortcut(_translate("MainWindow", "Backspace"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.sixButton.setShortcut(_translate("MainWindow", "6"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.cButton.setShortcut(_translate("MainWindow", "C"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.zeroButton.setShortcut(_translate("MainWindow", "0"))
        self.piButton.setText(_translate("MainWindow", '\u03C0'))
        self.piButton.setShortcut(_translate("MainWindow", "P"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.multiplyButton.setShortcut(_translate("MainWindow", "*"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.equalButton.setShortcut(_translate("MainWindow", "Enter"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.threeButton.setShortcut(_translate("MainWindow", "3"))
        self.resultDisplay.setText(_translate("MainWindow", ""))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.minusButton.setShortcut(_translate("MainWindow", "-"))
        self.Display.setText(_translate("MainWindow", "0"))
        self.powerButton.setText(_translate("MainWindow", "x^y"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.fiveButton.setShortcut(_translate("MainWindow", "5"))
        self.sqrtButton.setText(_translate("MainWindow", '\u221A'))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fourButton.setShortcut(_translate("MainWindow", "4"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.twoButton.setShortcut(_translate("MainWindow", "2"))
        self.unknownButton.setText(_translate("MainWindow", "n!"))
        self.plusMinusButton.setText(_translate("MainWindow", "+/-"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.eightButton.setShortcut(_translate("MainWindow", "8"))
        self.divButton.setText(_translate("MainWindow", "/"))
        self.divButton.setShortcut(_translate("MainWindow", "/"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.nineButton.setShortcut(_translate("MainWindow", "9"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionStandard.setText(_translate("MainWindow", "Standard"))
        self.actionScientific.setText(_translate("MainWindow", "Scientific"))
        self.actionProgrammer.setText(_translate("MainWindow", "Programmer"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))
