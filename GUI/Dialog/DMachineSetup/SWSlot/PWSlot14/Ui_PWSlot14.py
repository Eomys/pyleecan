# -*- coding: utf-8 -*-

# File generated according to PWSlot14.ui
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PWSlot14(object):
    def setupUi(self, PWSlot14):
        PWSlot14.setObjectName("PWSlot14")
        PWSlot14.resize(630, 470)
        PWSlot14.setMinimumSize(QtCore.QSize(630, 470))
        PWSlot14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(PWSlot14)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_slot = QtWidgets.QLabel(PWSlot14)
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
            QtGui.QPixmap(":/images/images/MachineSetup/WSlot/Slot 14.PNG")
        )
        self.img_slot.setScaledContents(True)
        self.img_slot.setObjectName("img_slot")
        self.verticalLayout_2.addWidget(self.img_slot)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_W0 = QtWidgets.QLabel(PWSlot14)
        self.in_W0.setObjectName("in_W0")
        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)
        self.lf_W0 = FloatEdit(PWSlot14)
        self.lf_W0.setObjectName("lf_W0")
        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)
        self.unit_W0 = QtWidgets.QLabel(PWSlot14)
        self.unit_W0.setObjectName("unit_W0")
        self.gridLayout.addWidget(self.unit_W0, 0, 2, 1, 1)
        self.in_W3 = QtWidgets.QLabel(PWSlot14)
        self.in_W3.setObjectName("in_W3")
        self.gridLayout.addWidget(self.in_W3, 1, 0, 1, 1)
        self.lf_W3 = FloatEdit(PWSlot14)
        self.lf_W3.setObjectName("lf_W3")
        self.gridLayout.addWidget(self.lf_W3, 1, 1, 1, 1)
        self.unit_W3 = QtWidgets.QLabel(PWSlot14)
        self.unit_W3.setObjectName("unit_W3")
        self.gridLayout.addWidget(self.unit_W3, 1, 2, 1, 1)
        self.in_H0 = QtWidgets.QLabel(PWSlot14)
        self.in_H0.setObjectName("in_H0")
        self.gridLayout.addWidget(self.in_H0, 2, 0, 1, 1)
        self.lf_H0 = FloatEdit(PWSlot14)
        self.lf_H0.setObjectName("lf_H0")
        self.gridLayout.addWidget(self.lf_H0, 2, 1, 1, 1)
        self.unit_H0 = QtWidgets.QLabel(PWSlot14)
        self.unit_H0.setObjectName("unit_H0")
        self.gridLayout.addWidget(self.unit_H0, 2, 2, 1, 1)
        self.in_H1 = QtWidgets.QLabel(PWSlot14)
        self.in_H1.setObjectName("in_H1")
        self.gridLayout.addWidget(self.in_H1, 3, 0, 1, 1)
        self.lf_H1 = FloatEdit(PWSlot14)
        self.lf_H1.setObjectName("lf_H1")
        self.gridLayout.addWidget(self.lf_H1, 3, 1, 1, 1)
        self.unit_H1 = QtWidgets.QLabel(PWSlot14)
        self.unit_H1.setObjectName("unit_H1")
        self.gridLayout.addWidget(self.unit_H1, 3, 2, 1, 1)
        self.in_H3 = QtWidgets.QLabel(PWSlot14)
        self.in_H3.setObjectName("in_H3")
        self.gridLayout.addWidget(self.in_H3, 4, 0, 1, 1)
        self.lf_H3 = FloatEdit(PWSlot14)
        self.lf_H3.setObjectName("lf_H3")
        self.gridLayout.addWidget(self.lf_H3, 4, 1, 1, 1)
        self.unit_H3 = QtWidgets.QLabel(PWSlot14)
        self.unit_H3.setObjectName("unit_H3")
        self.gridLayout.addWidget(self.unit_H3, 4, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.w_out = WWSlotOut(PWSlot14)
        self.w_out.setObjectName("w_out")
        self.verticalLayout.addWidget(self.w_out)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(PWSlot14)
        QtCore.QMetaObject.connectSlotsByName(PWSlot14)
        PWSlot14.setTabOrder(self.lf_W0, self.lf_W3)
        PWSlot14.setTabOrder(self.lf_W3, self.lf_H0)
        PWSlot14.setTabOrder(self.lf_H0, self.lf_H1)
        PWSlot14.setTabOrder(self.lf_H1, self.lf_H3)

    def retranslateUi(self, PWSlot14):
        _translate = QtCore.QCoreApplication.translate
        PWSlot14.setWindowTitle(_translate("PWSlot14", "Form"))
        self.in_W0.setText(_translate("PWSlot14", "W0 :"))
        self.unit_W0.setText(_translate("PWSlot14", "m"))
        self.in_W3.setText(_translate("PWSlot14", "W3 :"))
        self.unit_W3.setText(_translate("PWSlot14", "m"))
        self.in_H0.setText(_translate("PWSlot14", "H0 :"))
        self.unit_H0.setText(_translate("PWSlot14", "m"))
        self.in_H1.setText(_translate("PWSlot14", "H1 :"))
        self.unit_H1.setText(_translate("PWSlot14", "m"))
        self.in_H3.setText(_translate("PWSlot14", "H3 :"))
        self.unit_H3.setText(_translate("PWSlot14", "m"))


from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut
from ......GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
