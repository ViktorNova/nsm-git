# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stagepatch.ui'
#
# Created: Thu Feb 26 06:04:28 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Stagepatch(object):
    def setupUi(self, Stagepatch):
        Stagepatch.setObjectName(_fromUtf8("Stagepatch"))
        Stagepatch.setWindowModality(QtCore.Qt.WindowModal)
        Stagepatch.resize(400, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Stagepatch)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtGui.QLabel(Stagepatch)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.overwritePatchbay = QtGui.QPushButton(Stagepatch)
        self.overwritePatchbay.setObjectName(_fromUtf8("overwritePatchbay"))
        self.verticalLayout.addWidget(self.overwritePatchbay)
        self.reloadPatchbay = QtGui.QPushButton(Stagepatch)
        self.reloadPatchbay.setObjectName(_fromUtf8("reloadPatchbay"))
        self.verticalLayout.addWidget(self.reloadPatchbay)
        self.disconnectAll = QtGui.QPushButton(Stagepatch)
        self.disconnectAll.setObjectName(_fromUtf8("disconnectAll"))
        self.verticalLayout.addWidget(self.disconnectAll)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.textBrowser = QtGui.QTextBrowser(Stagepatch)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_2.addWidget(self.textBrowser)
        spacerItem2 = QtGui.QSpacerItem(20, 51, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)

        self.retranslateUi(Stagepatch)
        QtCore.QMetaObject.connectSlotsByName(Stagepatch)

    def retranslateUi(self, Stagepatch):
        Stagepatch.setWindowTitle(_translate("Stagepatch", "Dialog", None))
        self.label.setText(_translate("Stagepatch", "Overwrite saved patchbay with the current state of all MIDI and JACK connections", None))
        self.overwritePatchbay.setText(_translate("Stagepatch", "Overwrite Patchbay", None))
        self.reloadPatchbay.setToolTip(_translate("Stagepatch", "Disconnect everything and reload from previously saved patchbay", None))
        self.reloadPatchbay.setText(_translate("Stagepatch", "PushButton", None))
        self.disconnectAll.setText(_translate("Stagepatch", "Disconnect All", None))

