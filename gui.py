# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sun Jun 23 23:44:06 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(394, 171)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.upButton = QtGui.QPushButton(self.centralwidget)
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.gridLayout.addWidget(self.upButton, 0, 1, 1, 1)
        self.leftButton = QtGui.QPushButton(self.centralwidget)
        self.leftButton.setObjectName(_fromUtf8("leftButton"))
        self.gridLayout.addWidget(self.leftButton, 1, 0, 1, 1)
        self.fireButton = QtGui.QPushButton(self.centralwidget)
        self.fireButton.setObjectName(_fromUtf8("fireButton"))
        self.gridLayout.addWidget(self.fireButton, 1, 1, 1, 1)
        self.rightButton = QtGui.QPushButton(self.centralwidget)
        self.rightButton.setObjectName(_fromUtf8("rightButton"))
        self.gridLayout.addWidget(self.rightButton, 1, 2, 1, 1)
        self.downButton = QtGui.QPushButton(self.centralwidget)
        self.downButton.setObjectName(_fromUtf8("downButton"))
        self.gridLayout.addWidget(self.downButton, 2, 1, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Armageddon", None))
        self.upButton.setText(_translate("mainWindow", "Up", None))
        self.upButton.setShortcut(_translate("mainWindow", "Up", None))
        self.leftButton.setText(_translate("mainWindow", "Left", None))
        self.leftButton.setShortcut(_translate("mainWindow", "Left", None))
        self.fireButton.setText(_translate("mainWindow", "Fire", None))
        self.fireButton.setShortcut(_translate("mainWindow", "Return", None))
        self.rightButton.setText(_translate("mainWindow", "Right", None))
        self.rightButton.setShortcut(_translate("mainWindow", "Right", None))
        self.downButton.setText(_translate("mainWindow", "Down", None))
        self.downButton.setShortcut(_translate("mainWindow", "Down", None))

