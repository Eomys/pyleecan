# -*- coding: utf-8 -*-

# File generated according to WVent.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WVent(object):
    def setupUi(self, WVent):
        WVent.setObjectName("WVent")
        WVent.resize(630, 470)
        WVent.setMinimumSize(QtCore.QSize(630, 470))
        self.main_layout = QtWidgets.QVBoxLayout(WVent)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_vent_type = QtWidgets.QLabel(WVent)
        self.in_vent_type.setObjectName("in_vent_type")
        self.horizontalLayout.addWidget(self.in_vent_type)
        self.c_vent_type = QtWidgets.QComboBox(WVent)
        self.c_vent_type.setObjectName("c_vent_type")
        self.c_vent_type.addItem("")
        self.c_vent_type.addItem("")
        self.c_vent_type.addItem("")
        self.horizontalLayout.addWidget(self.c_vent_type)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.main_layout.addLayout(self.horizontalLayout)
        self.w_vent = QtWidgets.QWidget(WVent)
        self.w_vent.setMinimumSize(QtCore.QSize(640, 480))
        self.w_vent.setObjectName("w_vent")
        self.main_layout.addWidget(self.w_vent)

        self.retranslateUi(WVent)
        QtCore.QMetaObject.connectSlotsByName(WVent)

    def retranslateUi(self, WVent):
        _translate = QtCore.QCoreApplication.translate
        WVent.setWindowTitle(_translate("WVent", "Form"))
        self.in_vent_type.setText(_translate("WVent", "Ventilation Shape:"))
        self.c_vent_type.setItemText(0, _translate("WVent", "Circular"))
        self.c_vent_type.setItemText(1, _translate("WVent", "Polar"))
        self.c_vent_type.setItemText(2, _translate("WVent", "Trapeze"))
