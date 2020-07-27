# -*- coding: utf-8 -*-

# File generated according to WImportMatrixTable.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WImportMatrixTable(object):
    def setupUi(self, WImportMatrixTable):
        WImportMatrixTable.setObjectName("WImportMatrixTable")
        WImportMatrixTable.resize(546, 511)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            WImportMatrixTable.sizePolicy().hasHeightForWidth()
        )
        WImportMatrixTable.setSizePolicy(sizePolicy)
        WImportMatrixTable.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout = QtWidgets.QHBoxLayout(WImportMatrixTable)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_matrix = QtWidgets.QLabel(WImportMatrixTable)
        self.in_matrix.setObjectName("in_matrix")
        self.horizontalLayout.addWidget(self.in_matrix)
        self.b_convert = QtWidgets.QPushButton(WImportMatrixTable)
        self.b_convert.setObjectName("b_convert")
        self.horizontalLayout.addWidget(self.b_convert)
        self.b_tab = QtWidgets.QPushButton(WImportMatrixTable)
        self.b_tab.setObjectName("b_tab")
        self.horizontalLayout.addWidget(self.b_tab)
        self.b_plot = QtWidgets.QPushButton(WImportMatrixTable)
        self.b_plot.setObjectName("b_plot")
        self.horizontalLayout.addWidget(self.b_plot)

        self.retranslateUi(WImportMatrixTable)
        QtCore.QMetaObject.connectSlotsByName(WImportMatrixTable)

    def retranslateUi(self, WImportMatrixTable):
        _translate = QtCore.QCoreApplication.translate
        WImportMatrixTable.setWindowTitle(_translate("WImportMatrixTable", "Form"))
        self.in_matrix.setText(_translate("WImportMatrixTable", "Matrix size (100,2)"))
        self.b_convert.setText(_translate("WImportMatrixTable", "Convert to Excel"))
        self.b_tab.setText(_translate("WImportMatrixTable", "Preview Table"))
        self.b_plot.setText(_translate("WImportMatrixTable", "Preview Plot"))


from pyleecan.GUI.Resources import pyleecan_rc
