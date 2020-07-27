# -*- coding: utf-8 -*-

# File generated according to WImportExcel.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WImportExcel(object):
    def setupUi(self, WImportExcel):
        WImportExcel.setObjectName("WImportExcel")
        WImportExcel.resize(546, 511)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WImportExcel.sizePolicy().hasHeightForWidth())
        WImportExcel.setSizePolicy(sizePolicy)
        WImportExcel.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(WImportExcel)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.w_file_path = WPathSelector(WImportExcel)
        self.w_file_path.setObjectName("w_file_path")
        self.verticalLayout_3.addWidget(self.w_file_path)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.in_sheet = QtWidgets.QLabel(WImportExcel)
        self.in_sheet.setObjectName("in_sheet")
        self.horizontalLayout_2.addWidget(self.in_sheet)
        self.c_sheet = QtWidgets.QComboBox(WImportExcel)
        self.c_sheet.setObjectName("c_sheet")
        self.horizontalLayout_2.addWidget(self.c_sheet)
        self.in_range = QtWidgets.QLabel(WImportExcel)
        self.in_range.setObjectName("in_range")
        self.horizontalLayout_2.addWidget(self.in_range)
        self.le_range = QtWidgets.QLineEdit(WImportExcel)
        self.le_range.setObjectName("le_range")
        self.horizontalLayout_2.addWidget(self.le_range)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.g_axe1 = QtWidgets.QGroupBox(WImportExcel)
        self.g_axe1.setObjectName("g_axe1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.g_axe1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.c_axe1_name = QtWidgets.QComboBox(self.g_axe1)
        self.c_axe1_name.setObjectName("c_axe1_name")
        self.horizontalLayout_3.addWidget(self.c_axe1_name)
        self.c_axe1_type = QtWidgets.QComboBox(self.g_axe1)
        self.c_axe1_type.setObjectName("c_axe1_type")
        self.horizontalLayout_3.addWidget(self.c_axe1_type)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.w_axe1 = QtWidgets.QWidget(self.g_axe1)
        self.w_axe1.setObjectName("w_axe1")
        self.verticalLayout.addWidget(self.w_axe1)
        self.verticalLayout_3.addWidget(self.g_axe1)
        self.g_axe2 = QtWidgets.QGroupBox(WImportExcel)
        self.g_axe2.setObjectName("g_axe2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.g_axe2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.c_axe2_name = QtWidgets.QComboBox(self.g_axe2)
        self.c_axe2_name.setObjectName("c_axe2_name")
        self.horizontalLayout_4.addWidget(self.c_axe2_name)
        self.c_axe2_type = QtWidgets.QComboBox(self.g_axe2)
        self.c_axe2_type.setObjectName("c_axe2_type")
        self.horizontalLayout_4.addWidget(self.c_axe2_type)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.w_axe2 = QtWidgets.QWidget(self.g_axe2)
        self.w_axe2.setObjectName("w_axe2")
        self.verticalLayout_2.addWidget(self.w_axe2)
        self.verticalLayout_3.addWidget(self.g_axe2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.b_convert = QtWidgets.QPushButton(WImportExcel)
        self.b_convert.setObjectName("b_convert")
        self.horizontalLayout.addWidget(self.b_convert)
        self.b_tab = QtWidgets.QPushButton(WImportExcel)
        self.b_tab.setObjectName("b_tab")
        self.horizontalLayout.addWidget(self.b_tab)
        self.b_plot = QtWidgets.QPushButton(WImportExcel)
        self.b_plot.setObjectName("b_plot")
        self.horizontalLayout.addWidget(self.b_plot)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(WImportExcel)
        QtCore.QMetaObject.connectSlotsByName(WImportExcel)

    def retranslateUi(self, WImportExcel):
        _translate = QtCore.QCoreApplication.translate
        WImportExcel.setWindowTitle(_translate("WImportExcel", "Form"))
        self.in_sheet.setText(_translate("WImportExcel", "Sheet: "))
        self.in_range.setText(_translate("WImportExcel", "Range: "))
        self.g_axe1.setTitle(_translate("WImportExcel", "First axe"))
        self.g_axe2.setTitle(_translate("WImportExcel", "Second axe"))
        self.b_convert.setText(_translate("WImportExcel", "Convert to Matrix"))
        self.b_tab.setText(_translate("WImportExcel", "Preview Table"))
        self.b_plot.setText(_translate("WImportExcel", "Preview Plot"))


from .....GUI.Tools.WPathSelector.WPathSelector import WPathSelector
from pyleecan.GUI.Resources import pyleecan_rc
