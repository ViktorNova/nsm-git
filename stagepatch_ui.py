# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stagepatch.ui'
#
# Created: Wed Feb 25 05:03:38 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import argparse

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(811, 424)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.overwritePatchbay = QtGui.QPushButton(self.centralwidget)
        self.overwritePatchbay.setObjectName(_fromUtf8("overwritePatchbay"))
        self.verticalLayout.addWidget(self.overwritePatchbay)
        self.disconnectAll = QtGui.QPushButton(self.centralwidget)
        self.disconnectAll.setObjectName(_fromUtf8("disconnectAll"))
        self.verticalLayout.addWidget(self.disconnectAll)
        self.reloadPatchbay = QtGui.QPushButton(self.centralwidget)
        self.reloadPatchbay.setObjectName(_fromUtf8("reloadPatchbay"))
        self.verticalLayout.addWidget(self.reloadPatchbay)
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setEnabled(True)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.verticalLayout.addWidget(self.commandLinkButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_2.addWidget(self.textBrowser)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Stagepatch", None))
        self.label.setText(_translate("MainWindow", "Overwrite saved patchbay with the current state of all MIDI and JACK connections", None))
        self.overwritePatchbay.setText(_translate("MainWindow", "Overwrite Patchbay", None))
        self.disconnectAll.setText(_translate("MainWindow", "Disconnect All", None))
        self.reloadPatchbay.setToolTip(_translate("MainWindow", "Disconnect everything and reload from previously saved patchbay", None))
        self.reloadPatchbay.setText(_translate("MainWindow", "PushButton", None))
        self.commandLinkButton.setText(_translate("MainWindow", "CommandLinkButton..?", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

