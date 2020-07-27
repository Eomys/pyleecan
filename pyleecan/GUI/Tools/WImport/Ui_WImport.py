# -*- coding: utf-8 -*-

# File generated according to WImport.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WImport(object):
    def setupUi(self, WImport):
        WImport.setObjectName("WImport")
        WImport.resize(678, 491)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WImport.sizePolicy().hasHeightForWidth())
        WImport.setSizePolicy(sizePolicy)
        WImport.setMinimumSize(QtCore.QSize(0, 0))
        self.main_layout = QtWidgets.QVBoxLayout(WImport)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_param = QtWidgets.QLabel(WImport)
        self.in_param.setObjectName("in_param")
        self.horizontalLayout.addWidget(self.in_param)
        self.c_type_import = QtWidgets.QComboBox(WImport)
        self.c_type_import.setObjectName("c_type_import")
        self.horizontalLayout.addWidget(self.c_type_import)
        self.main_layout.addLayout(self.horizontalLayout)
        self.w_import = QtWidgets.QWidget(WImport)
        self.w_import.setObjectName("w_import")
        self.main_layout.addWidget(self.w_import)

        self.retranslateUi(WImport)
        QtCore.QMetaObject.connectSlotsByName(WImport)

    def retranslateUi(self, WImport):
        _translate = QtCore.QCoreApplication.translate
        WImport.setWindowTitle(_translate("WImport", "Form"))
        self.in_param.setText(_translate("WImport", "Param_name: "))


from pyleecan.GUI.Resources import pyleecan_rc
