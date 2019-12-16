# -*- coding: utf-8 -*-

# File generated according to WMatSelect.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WMatSelect(object):
    def setupUi(self, WMatSelect):
        WMatSelect.setObjectName("WMatSelect")
        WMatSelect.resize(283, 50)
        WMatSelect.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout = QtWidgets.QHBoxLayout(WMatSelect)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_mat_type = QtWidgets.QLabel(WMatSelect)
        self.in_mat_type.setObjectName("in_mat_type")
        self.horizontalLayout.addWidget(self.in_mat_type)
        self.c_mat_type = QtWidgets.QComboBox(WMatSelect)
        self.c_mat_type.setObjectName("c_mat_type")
        self.c_mat_type.addItem("")
        self.c_mat_type.addItem("")
        self.c_mat_type.addItem("")
        self.horizontalLayout.addWidget(self.c_mat_type)
        self.b_matlib = QtWidgets.QPushButton(WMatSelect)
        self.b_matlib.setObjectName("b_matlib")
        self.horizontalLayout.addWidget(self.b_matlib)

        self.retranslateUi(WMatSelect)
        QtCore.QMetaObject.connectSlotsByName(WMatSelect)
        WMatSelect.setTabOrder(self.c_mat_type, self.b_matlib)

    def retranslateUi(self, WMatSelect):
        _translate = QtCore.QCoreApplication.translate
        WMatSelect.setWindowTitle(_translate("WMatSelect", "Form"))
        self.in_mat_type.setText(_translate("WMatSelect", "mat_type :"))
        self.c_mat_type.setItemText(0, _translate("WMatSelect", "M400-50A"))
        self.c_mat_type.setItemText(1, _translate("WMatSelect", "M350-50A"))
        self.c_mat_type.setItemText(2, _translate("WMatSelect", "M330-35A"))
        self.b_matlib.setText(_translate("WMatSelect", "Edit Materials"))


from pyleecan.GUI.Resources import pyleecan_rc
