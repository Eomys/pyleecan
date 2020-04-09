# -*- coding: utf-8 -*-

# File generated according to PCondType12.ui
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PCondType12(object):
    def setupUi(self, PCondType12):
        PCondType12.setObjectName("PCondType12")
        PCondType12.resize(965, 672)
        self.horizontalLayout = QtWidgets.QHBoxLayout(PCondType12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_cond = QtWidgets.QLabel(PCondType12)
        self.img_cond.setMinimumSize(QtCore.QSize(0, 0))
        self.img_cond.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.img_cond.setText("")
        self.img_cond.setPixmap(
            QtGui.QPixmap(":/images/images/MachineSetup/WindParam/Cond_1_2.PNG")
        )
        self.img_cond.setScaledContents(True)
        self.img_cond.setObjectName("img_cond")
        self.horizontalLayout.addWidget(self.img_cond)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_Nwpc1 = QtWidgets.QLabel(PCondType12)
        self.in_Nwpc1.setMinimumSize(QtCore.QSize(60, 0))
        self.in_Nwpc1.setObjectName("in_Nwpc1")
        self.gridLayout.addWidget(self.in_Nwpc1, 0, 0, 1, 1)
        self.si_Nwpc1 = QtWidgets.QSpinBox(PCondType12)
        self.si_Nwpc1.setMinimumSize(QtCore.QSize(70, 0))
        self.si_Nwpc1.setProperty("value", 99)
        self.si_Nwpc1.setObjectName("si_Nwpc1")
        self.gridLayout.addWidget(self.si_Nwpc1, 0, 1, 1, 1)
        self.in_Wwire = QtWidgets.QLabel(PCondType12)
        self.in_Wwire.setMinimumSize(QtCore.QSize(40, 0))
        self.in_Wwire.setObjectName("in_Wwire")
        self.gridLayout.addWidget(self.in_Wwire, 1, 0, 1, 1)
        self.lf_Wwire = FloatEdit(PCondType12)
        self.lf_Wwire.setMinimumSize(QtCore.QSize(50, 0))
        self.lf_Wwire.setMaximumSize(QtCore.QSize(100, 20))
        self.lf_Wwire.setObjectName("lf_Wwire")
        self.gridLayout.addWidget(self.lf_Wwire, 1, 1, 1, 1)
        self.unit_Wwire = QtWidgets.QLabel(PCondType12)
        self.unit_Wwire.setMinimumSize(QtCore.QSize(0, 0))
        self.unit_Wwire.setObjectName("unit_Wwire")
        self.gridLayout.addWidget(self.unit_Wwire, 1, 2, 1, 1)
        self.in_Wins_wire = QtWidgets.QLabel(PCondType12)
        self.in_Wins_wire.setMinimumSize(QtCore.QSize(40, 0))
        self.in_Wins_wire.setObjectName("in_Wins_wire")
        self.gridLayout.addWidget(self.in_Wins_wire, 2, 0, 1, 1)
        self.lf_Wins_wire = FloatEdit(PCondType12)
        self.lf_Wins_wire.setMinimumSize(QtCore.QSize(50, 0))
        self.lf_Wins_wire.setMaximumSize(QtCore.QSize(100, 20))
        self.lf_Wins_wire.setObjectName("lf_Wins_wire")
        self.gridLayout.addWidget(self.lf_Wins_wire, 2, 1, 1, 1)
        self.unit_Wins_wire = QtWidgets.QLabel(PCondType12)
        self.unit_Wins_wire.setMinimumSize(QtCore.QSize(0, 0))
        self.unit_Wins_wire.setObjectName("unit_Wins_wire")
        self.gridLayout.addWidget(self.unit_Wins_wire, 2, 2, 1, 1)
        self.in_Wins_cond = QtWidgets.QLabel(PCondType12)
        self.in_Wins_cond.setObjectName("in_Wins_cond")
        self.gridLayout.addWidget(self.in_Wins_cond, 3, 0, 1, 1)
        self.lf_Wins_cond = FloatEdit(PCondType12)
        self.lf_Wins_cond.setMinimumSize(QtCore.QSize(50, 0))
        self.lf_Wins_cond.setMaximumSize(QtCore.QSize(100, 20))
        self.lf_Wins_cond.setObjectName("lf_Wins_cond")
        self.gridLayout.addWidget(self.lf_Wins_cond, 3, 1, 1, 1)
        self.unit_Wins_cond = QtWidgets.QLabel(PCondType12)
        self.unit_Wins_cond.setObjectName("unit_Wins_cond")
        self.gridLayout.addWidget(self.unit_Wins_cond, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.w_out = WCondOut(PCondType12)
        self.w_out.setObjectName("w_out")
        self.verticalLayout_2.addWidget(self.w_out)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(PCondType12)
        QtCore.QMetaObject.connectSlotsByName(PCondType12)
        PCondType12.setTabOrder(self.si_Nwpc1, self.lf_Wwire)
        PCondType12.setTabOrder(self.lf_Wwire, self.lf_Wins_wire)

    def retranslateUi(self, PCondType12):
        _translate = QtCore.QCoreApplication.translate
        PCondType12.setWindowTitle(_translate("PCondType12", "Form"))
        self.in_Nwpc1.setText(_translate("PCondType12", "Nwpc1 :"))
        self.in_Wwire.setText(_translate("PCondType12", "Wwire :"))
        self.unit_Wwire.setText(_translate("PCondType12", "m"))
        self.in_Wins_wire.setText(_translate("PCondType12", "Wins_wire :"))
        self.unit_Wins_wire.setText(_translate("PCondType12", "m"))
        self.in_Wins_cond.setText(_translate("PCondType12", "Wins_cond :"))
        self.unit_Wins_cond.setText(_translate("PCondType12", "m"))


from ......GUI.Dialog.DMachineSetup.SWindCond.WCondOut.WCondOut import WCondOut
from ......GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
