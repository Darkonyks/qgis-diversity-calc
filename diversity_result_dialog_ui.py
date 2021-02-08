# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diversity_results_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgResult(object):
    def setupUi(self, dlgResult):
        dlgResult.setObjectName("dlgResult")
        dlgResult.resize(640, 480)
        self.verticalLayoutWidget = QtWidgets.QWidget(dlgResult)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lytMain = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lytMain.setContentsMargins(0, 0, 0, 0)
        self.lytMain.setObjectName("lytMain")
        self.trwResults = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.trwResults.setAlternatingRowColors(True)
        self.trwResults.setObjectName("trwResults")
        self.lytMain.addWidget(self.trwResults)

        self.retranslateUi(dlgResult)
        QtCore.QMetaObject.connectSlotsByName(dlgResult)

    def retranslateUi(self, dlgResult):
        _translate = QtCore.QCoreApplication.translate
        dlgResult.setWindowTitle(_translate("dlgResult", "Diversity Results"))
        self.trwResults.headerItem().setText(0, _translate("dlgResult", "Name"))
        self.trwResults.headerItem().setText(1, _translate("dlgResult", "Count"))
        self.trwResults.headerItem().setText(2, _translate("dlgResult", "Richness"))
        self.trwResults.headerItem().setText(3, _translate("dlgResult", "Evenness"))
        self.trwResults.headerItem().setText(4, _translate("dlgResult", "Shannons"))
        self.trwResults.headerItem().setText(5, _translate("dlgResult", "Simpsons"))
