# -*- coding: utf-8 -*-

# File generated according to GuiOption.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GUIOption(object):
    def setupUi(self, GUIOption):
        GUIOption.setObjectName("GUIOption")
        GUIOption.resize(480, 138)
        GUIOption.setMinimumSize(QtCore.QSize(0, 0))
        GUIOption.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(GUIOption)
        self.verticalLayout.setObjectName("verticalLayout")
        self.w_matlib_path = WPathSelector(GUIOption)
        self.w_matlib_path.setObjectName("w_matlib_path")
        self.verticalLayout.addWidget(self.w_matlib_path)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_unit_m = QtWidgets.QLabel(GUIOption)
        self.in_unit_m.setObjectName("in_unit_m")
        self.horizontalLayout.addWidget(self.in_unit_m)
        self.c_unit_m = QtWidgets.QComboBox(GUIOption)
        self.c_unit_m.setObjectName("c_unit_m")
        self.c_unit_m.addItem("")
        self.c_unit_m.addItem("")
        self.horizontalLayout.addWidget(self.c_unit_m)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.in_unit_m2 = QtWidgets.QLabel(GUIOption)
        self.in_unit_m2.setObjectName("in_unit_m2")
        self.horizontalLayout_2.addWidget(self.in_unit_m2)
        self.c_unit_m2 = QtWidgets.QComboBox(GUIOption)
        self.c_unit_m2.setObjectName("c_unit_m2")
        self.c_unit_m2.addItem("")
        self.c_unit_m2.addItem("")
        self.horizontalLayout_2.addWidget(self.c_unit_m2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(GUIOption)
        QtCore.QMetaObject.connectSlotsByName(GUIOption)

    def retranslateUi(self, GUIOption):
        _translate = QtCore.QCoreApplication.translate
        GUIOption.setWindowTitle(_translate("GUIOption", "Form"))
        self.in_unit_m.setText(_translate("GUIOption", "Meter unit"))
        self.c_unit_m.setItemText(0, _translate("GUIOption", "m"))
        self.c_unit_m.setItemText(1, _translate("GUIOption", "mm"))
        self.in_unit_m2.setText(_translate("GUIOption", "Surface unit"))
        self.c_unit_m2.setItemText(0, _translate("GUIOption", "m²"))
        self.c_unit_m2.setItemText(1, _translate("GUIOption", "mm²"))


from ....GUI.Tools.WPathSelector.WPathSelector import WPathSelector
from pyleecan.GUI.Resources import pyleecan_rc
