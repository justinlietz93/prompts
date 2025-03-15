# Form implementation generated from reading ui file 'C:\git\Prometheus_AI_Companion\prometheus_prompt_generator\ui\designer\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.leftWidget = QtWidgets.QWidget(parent=self.splitter)
        self.leftWidget.setObjectName("leftWidget")
        self.leftLayout = QtWidgets.QVBoxLayout(self.leftWidget)
        self.leftLayout.setContentsMargins(0, 0, 0, 0)
        self.leftLayout.setObjectName("leftLayout")
        self.promptTypesHeader = QtWidgets.QLabel(parent=self.leftWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.promptTypesHeader.setFont(font)
        self.promptTypesHeader.setObjectName("promptTypesHeader")
        self.leftLayout.addWidget(self.promptTypesHeader)
        self.searchLayout = QtWidgets.QHBoxLayout()
        self.searchLayout.setObjectName("searchLayout")
        self.searchInput = QtWidgets.QLineEdit(parent=self.leftWidget)
        self.searchInput.setObjectName("searchInput")
        self.searchLayout.addWidget(self.searchInput)
        self.leftLayout.addLayout(self.searchLayout)
        self.selectButtonsLayout = QtWidgets.QHBoxLayout()
        self.selectButtonsLayout.setObjectName("selectButtonsLayout")
        self.selectAllButton = QtWidgets.QPushButton(parent=self.leftWidget)
        self.selectAllButton.setObjectName("selectAllButton")
        self.selectButtonsLayout.addWidget(self.selectAllButton)
        self.selectNoneButton = QtWidgets.QPushButton(parent=self.leftWidget)
        self.selectNoneButton.setObjectName("selectNoneButton")
        self.selectButtonsLayout.addWidget(self.selectNoneButton)
        self.leftLayout.addLayout(self.selectButtonsLayout)
        self.promptList = QtWidgets.QListWidget(parent=self.leftWidget)
        self.promptList.setAlternatingRowColors(True)
        self.promptList.setObjectName("promptList")
        self.leftLayout.addWidget(self.promptList)
        self.addPromptButton = QtWidgets.QPushButton(parent=self.leftWidget)
        self.addPromptButton.setObjectName("addPromptButton")
        self.leftLayout.addWidget(self.addPromptButton)
        self.rightWidget = QtWidgets.QWidget(parent=self.splitter)
        self.rightWidget.setObjectName("rightWidget")
        self.rightLayout = QtWidgets.QVBoxLayout(self.rightWidget)
        self.rightLayout.setContentsMargins(0, 0, 0, 0)
        self.rightLayout.setObjectName("rightLayout")
        self.urgencyHeader = QtWidgets.QLabel(parent=self.rightWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.urgencyHeader.setFont(font)
        self.urgencyHeader.setObjectName("urgencyHeader")
        self.rightLayout.addWidget(self.urgencyHeader)
        self.urgencyDisplay = QtWidgets.QLabel(parent=self.rightWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.urgencyDisplay.setFont(font)
        self.urgencyDisplay.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.urgencyDisplay.setObjectName("urgencyDisplay")
        self.rightLayout.addWidget(self.urgencyDisplay)
        self.urgencySlider = QtWidgets.QSlider(parent=self.rightWidget)
        self.urgencySlider.setMinimum(1)
        self.urgencySlider.setMaximum(10)
        self.urgencySlider.setProperty("value", 5)
        self.urgencySlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.urgencySlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.urgencySlider.setObjectName("urgencySlider")
        self.rightLayout.addWidget(self.urgencySlider)
        self.generatedPromptHeader = QtWidgets.QLabel(parent=self.rightWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.generatedPromptHeader.setFont(font)
        self.generatedPromptHeader.setObjectName("generatedPromptHeader")
        self.rightLayout.addWidget(self.generatedPromptHeader)
        self.outputText = QtWidgets.QTextEdit(parent=self.rightWidget)
        self.outputText.setObjectName("outputText")
        self.rightLayout.addWidget(self.outputText)
        self.buttonRow = QtWidgets.QHBoxLayout()
        self.buttonRow.setObjectName("buttonRow")
        self.generatePromptsButton = QtWidgets.QPushButton(parent=self.rightWidget)
        self.generatePromptsButton.setMinimumHeight(40)
        self.generatePromptsButton.setObjectName("generatePromptsButton")
        self.buttonRow.addWidget(self.generatePromptsButton)
        self.copyToClipboardButton = QtWidgets.QPushButton(parent=self.rightWidget)
        self.copyToClipboardButton.setMinimumHeight(40)
        self.copyToClipboardButton.setObjectName("copyToClipboardButton")
        self.buttonRow.addWidget(self.copyToClipboardButton)
        self.rightLayout.addLayout(self.buttonRow)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTheme = QtWidgets.QMenu(parent=self.menuView)
        self.menuTheme.setObjectName("menuTheme")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtGui.QAction(parent=MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtGui.QAction(parent=MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionChangeFont = QtGui.QAction(parent=MainWindow)
        self.actionChangeFont.setObjectName("actionChangeFont")
        self.actionResetFont = QtGui.QAction(parent=MainWindow)
        self.actionResetFont.setObjectName("actionResetFont")
        self.actionLightTheme = QtGui.QAction(parent=MainWindow)
        self.actionLightTheme.setObjectName("actionLightTheme")
        self.actionDarkTheme = QtGui.QAction(parent=MainWindow)
        self.actionDarkTheme.setObjectName("actionDarkTheme")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionChangeFont)
        self.menuEdit.addAction(self.actionResetFont)
        self.menuTheme.addAction(self.actionLightTheme)
        self.menuTheme.addAction(self.actionDarkTheme)
        self.menuView.addAction(self.menuTheme.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prometheus AI Prompt Generator"))
        self.promptTypesHeader.setText(_translate("MainWindow", "Prompt Types"))
        self.searchInput.setPlaceholderText(_translate("MainWindow", "Search prompts..."))
        self.selectAllButton.setText(_translate("MainWindow", "Select All"))
        self.selectNoneButton.setText(_translate("MainWindow", "Select None"))
        self.addPromptButton.setText(_translate("MainWindow", "Add Custom Prompt"))
        self.urgencyHeader.setText(_translate("MainWindow", "Urgency Level"))
        self.urgencyDisplay.setText(_translate("MainWindow", "Normal (5/10)"))
        self.generatedPromptHeader.setText(_translate("MainWindow", "Generated Prompt"))
        self.outputText.setPlaceholderText(_translate("MainWindow", "Generated prompt will appear here. You can edit it as needed."))
        self.generatePromptsButton.setText(_translate("MainWindow", "Generate Prompts"))
        self.copyToClipboardButton.setText(_translate("MainWindow", "Copy to Clipboard"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionImport.setText(_translate("MainWindow", "Import Prompts..."))
        self.actionExport.setText(_translate("MainWindow", "Export Prompts..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionChangeFont.setText(_translate("MainWindow", "Change Font..."))
        self.actionResetFont.setText(_translate("MainWindow", "Reset Font"))
        self.actionLightTheme.setText(_translate("MainWindow", "Light"))
        self.actionDarkTheme.setText(_translate("MainWindow", "Dark"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
