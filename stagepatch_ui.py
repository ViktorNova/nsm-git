# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stagepatch.ui'
#
# Created: Fri Apr 10 04:56:37 2015
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
        Stagepatch.resize(442, 377)
        Stagepatch.setMinimumSize(QtCore.QSize(0, 30))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Stagepatch)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(Stagepatch)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label = QtGui.QLabel(Stagepatch)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.overwritePatchbay = QtGui.QPushButton(Stagepatch)
        self.overwritePatchbay.setObjectName(_fromUtf8("overwritePatchbay"))
        self.verticalLayout_2.addWidget(self.overwritePatchbay)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_2 = QtGui.QLabel(Stagepatch)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.reloadPatchbay = QtGui.QPushButton(Stagepatch)
        self.reloadPatchbay.setObjectName(_fromUtf8("reloadPatchbay"))
        self.verticalLayout_2.addWidget(self.reloadPatchbay)
        self.stackedwidget = QtGui.QStackedWidget(Stagepatch)
        self.stackedwidget.setObjectName(_fromUtf8("stackedwidget"))
        self.Page1 = QtGui.QWidget()
        self.Page1.setObjectName(_fromUtf8("Page1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.Page1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_4 = QtGui.QLabel(self.Page1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.disconnectAll = QtGui.QPushButton(self.Page1)
        self.disconnectAll.setObjectName(_fromUtf8("disconnectAll"))
        self.verticalLayout.addWidget(self.disconnectAll)
        self.stackedwidget.addWidget(self.Page1)
        self.verticalLayout_2.addWidget(self.stackedwidget)

        self.retranslateUi(Stagepatch)
        QtCore.QMetaObject.connectSlotsByName(Stagepatch)

    def retranslateUi(self, Stagepatch):
        Stagepatch.setWindowTitle(_translate("Stagepatch", "Dialog", None))
        self.label_3.setText(_translate("Stagepatch", "STAGEPATCH", None))
        self.label.setText(_translate("Stagepatch", "Overwrite saved patchbay with the current state of all MIDI and JACK connections", None))
        self.overwritePatchbay.setText(_translate("Stagepatch", "Overwrite Patchbay", None))
        self.label_2.setText(_translate("Stagepatch", "Reload the patchbay from save file", None))
        self.reloadPatchbay.setToolTip(_translate("Stagepatch", "Disconnect everything and reload from previously saved patchbay", None))
        self.reloadPatchbay.setText(_translate("Stagepatch", "Reload", None))
        self.label_4.setText(_translate("Stagepatch", "Remove all MIDI and JACK connections", None))
        self.disconnectAll.setText(_translate("Stagepatch", "Disconnect All", None))

