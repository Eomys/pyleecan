# -*- coding: utf-8 -*-

# File generated according to DTableData.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DTableData(object):
    def setupUi(self, DTableData):
        DTableData.setObjectName("DTableData")
        DTableData.resize(746, 536)
        self.verticalLayout = QtWidgets.QVBoxLayout(DTableData)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_row = QtWidgets.QLabel(DTableData)
        self.in_row.setObjectName("in_row")
        self.horizontalLayout.addWidget(self.in_row)
        self.si_row = QtWidgets.QSpinBox(DTableData)
        self.si_row.setMinimum(1)
        self.si_row.setMaximum(999999999)
        self.si_row.setObjectName("si_row")
        self.horizontalLayout.addWidget(self.si_row)
        self.in_col = QtWidgets.QLabel(DTableData)
        self.in_col.setObjectName("in_col")
        self.horizontalLayout.addWidget(self.in_col)
        self.si_col = QtWidgets.QSpinBox(DTableData)
        self.si_col.setMinimum(1)
        self.si_col.setMaximum(999999999)
        self.si_col.setObjectName("si_col")
        self.horizontalLayout.addWidget(self.si_col)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.w_tab = QtWidgets.QTableWidget(DTableData)
        self.w_tab.setObjectName("w_tab")
        self.w_tab.setColumnCount(0)
        self.w_tab.setRowCount(0)
        self.verticalLayout.addWidget(self.w_tab)
        self.b_close = QtWidgets.QDialogButtonBox(DTableData)
        self.b_close.setOrientation(QtCore.Qt.Horizontal)
        self.b_close.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.b_close.setObjectName("b_close")
        self.verticalLayout.addWidget(self.b_close)

        self.retranslateUi(DTableData)
        self.b_close.accepted.connect(DTableData.accept)
        self.b_close.rejected.connect(DTableData.reject)
        QtCore.QMetaObject.connectSlotsByName(DTableData)

    def retranslateUi(self, DTableData):
        _translate = QtCore.QCoreApplication.translate
        DTableData.setWindowTitle(_translate("DTableData", "Material Library"))
        self.in_row.setText(_translate("DTableData", "N_row: "))
        self.in_col.setText(_translate("DTableData", "N_column:"))


from pyleecan.GUI.Resources import pyleecan_rc
