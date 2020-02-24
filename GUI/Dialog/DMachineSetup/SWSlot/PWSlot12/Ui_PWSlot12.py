# -*- coding: utf-8 -*-

# File generated according to PWSlot12.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PWSlot12(object):
    def setupUi(self, PWSlot12):
        PWSlot12.setObjectName("PWSlot12")
        PWSlot12.resize(630, 470)
        PWSlot12.setMinimumSize(QtCore.QSize(630, 470))
        PWSlot12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(PWSlot12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_slot = QtWidgets.QLabel(PWSlot12)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.img_slot.setText("")
        self.img_slot.setPixmap(
            QtGui.QPixmap(":/images/images/MachineSetup/WSlot/Slot 12.PNG")
        )
        self.img_slot.setScaledContents(True)
        self.img_slot.setObjectName("img_slot")
        self.verticalLayout_2.addWidget(self.img_slot)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_R1 = QtWidgets.QLabel(PWSlot12)
        self.in_R1.setObjectName("in_R1")
        self.gridLayout.addWidget(self.in_R1, 0, 0, 1, 1)
        self.lf_R1 = FloatEdit(PWSlot12)
        self.lf_R1.setObjectName("lf_R1")
        self.gridLayout.addWidget(self.lf_R1, 0, 1, 1, 1)
        self.unit_R1 = QtWidgets.QLabel(PWSlot12)
        self.unit_R1.setObjectName("unit_R1")
        self.gridLayout.addWidget(self.unit_R1, 0, 2, 1, 1)
        self.in_R2 = QtWidgets.QLabel(PWSlot12)
        self.in_R2.setObjectName("in_R2")
        self.gridLayout.addWidget(self.in_R2, 1, 0, 1, 1)
        self.lf_R2 = FloatEdit(PWSlot12)
        self.lf_R2.setObjectName("lf_R2")
        self.gridLayout.addWidget(self.lf_R2, 1, 1, 1, 1)
        self.unit_R2 = QtWidgets.QLabel(PWSlot12)
        self.unit_R2.setObjectName("unit_R2")
        self.gridLayout.addWidget(self.unit_R2, 1, 2, 1, 1)
        self.in_H0 = QtWidgets.QLabel(PWSlot12)
        self.in_H0.setObjectName("in_H0")
        self.gridLayout.addWidget(self.in_H0, 2, 0, 1, 1)
        self.lf_H0 = FloatEdit(PWSlot12)
        self.lf_H0.setObjectName("lf_H0")
        self.gridLayout.addWidget(self.lf_H0, 2, 1, 1, 1)
        self.unit_H0 = QtWidgets.QLabel(PWSlot12)
        self.unit_H0.setObjectName("unit_H0")
        self.gridLayout.addWidget(self.unit_H0, 2, 2, 1, 1)
        self.in_H1 = QtWidgets.QLabel(PWSlot12)
        self.in_H1.setObjectName("in_H1")
        self.gridLayout.addWidget(self.in_H1, 3, 0, 1, 1)
        self.lf_H1 = FloatEdit(PWSlot12)
        self.lf_H1.setObjectName("lf_H1")
        self.gridLayout.addWidget(self.lf_H1, 3, 1, 1, 1)
        self.unit_H1 = QtWidgets.QLabel(PWSlot12)
        self.unit_H1.setObjectName("unit_H1")
        self.gridLayout.addWidget(self.unit_H1, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.w_out = WWSlotOut(PWSlot12)
        self.w_out.setObjectName("w_out")
        self.verticalLayout.addWidget(self.w_out)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(PWSlot12)
        QtCore.QMetaObject.connectSlotsByName(PWSlot12)
        PWSlot12.setTabOrder(self.lf_R1, self.lf_R2)
        PWSlot12.setTabOrder(self.lf_R2, self.lf_H0)
        PWSlot12.setTabOrder(self.lf_H0, self.lf_H1)

    def retranslateUi(self, PWSlot12):
        _translate = QtCore.QCoreApplication.translate
        PWSlot12.setWindowTitle(_translate("PWSlot12", "Form"))
        self.in_R1.setText(_translate("PWSlot12", "R1 :"))
        self.unit_R1.setText(_translate("PWSlot12", "m"))
        self.in_R2.setText(_translate("PWSlot12", "R2 :"))
        self.unit_R2.setText(_translate("PWSlot12", "m"))
        self.in_H0.setText(_translate("PWSlot12", "H0 :"))
        self.unit_H0.setText(_translate("PWSlot12", "m"))
        self.in_H1.setText(_translate("PWSlot12", "H1 :"))
        self.unit_H1.setText(_translate("PWSlot12", "m"))


from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut
from pyleecan.GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
