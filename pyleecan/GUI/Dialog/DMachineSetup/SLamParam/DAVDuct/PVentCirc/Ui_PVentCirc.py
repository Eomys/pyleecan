# -*- coding: utf-8 -*-

# File generated according to PVentCirc.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .......GUI.Tools.FloatEdit import FloatEdit
from .......GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.WVentOut.WVentOut import WVentOut

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PVentCirc(object):
    def setupUi(self, PVentCirc):
        if not PVentCirc.objectName():
            PVentCirc.setObjectName(u"PVentCirc")
        PVentCirc.resize(630, 470)
        PVentCirc.setMinimumSize(QSize(630, 470))
        PVentCirc.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PVentCirc)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_vent = QLabel(PVentCirc)
        self.img_vent.setObjectName(u"img_vent")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_vent.sizePolicy().hasHeightForWidth())
        self.img_vent.setSizePolicy(sizePolicy)
        self.img_vent.setMaximumSize(QSize(16777215, 16777215))
        self.img_vent.setPixmap(
            QPixmap(u":/images/images/MachineSetup/LamParam/CircVentDuct.png")
        )
        self.img_vent.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.img_vent)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lf_D0 = FloatEdit(PVentCirc)
        self.lf_D0.setObjectName(u"lf_D0")

        self.gridLayout.addWidget(self.lf_D0, 2, 1, 1, 1)

        self.lf_Alpha0 = FloatEdit(PVentCirc)
        self.lf_Alpha0.setObjectName(u"lf_Alpha0")

        self.gridLayout.addWidget(self.lf_Alpha0, 3, 1, 1, 1)

        self.unit_D0 = QLabel(PVentCirc)
        self.unit_D0.setObjectName(u"unit_D0")

        self.gridLayout.addWidget(self.unit_D0, 2, 2, 1, 1)

        self.in_Alpha0 = QLabel(PVentCirc)
        self.in_Alpha0.setObjectName(u"in_Alpha0")

        self.gridLayout.addWidget(self.in_Alpha0, 3, 0, 1, 1)

        self.unit_Alpha0 = QLabel(PVentCirc)
        self.unit_Alpha0.setObjectName(u"unit_Alpha0")

        self.gridLayout.addWidget(self.unit_Alpha0, 3, 2, 1, 1)

        self.unit_H0 = QLabel(PVentCirc)
        self.unit_H0.setObjectName(u"unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 1, 2, 1, 1)

        self.lf_H0 = FloatEdit(PVentCirc)
        self.lf_H0.setObjectName(u"lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 1, 1, 1, 1)

        self.in_H0 = QLabel(PVentCirc)
        self.in_H0.setObjectName(u"in_H0")

        self.gridLayout.addWidget(self.in_H0, 1, 0, 1, 1)

        self.in_D0 = QLabel(PVentCirc)
        self.in_D0.setObjectName(u"in_D0")

        self.gridLayout.addWidget(self.in_D0, 2, 0, 1, 1)

        self.in_Zh = QLabel(PVentCirc)
        self.in_Zh.setObjectName(u"in_Zh")

        self.gridLayout.addWidget(self.in_Zh, 0, 0, 1, 1)

        self.si_Zh = QSpinBox(PVentCirc)
        self.si_Zh.setObjectName(u"si_Zh")

        self.gridLayout.addWidget(self.si_Zh, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.w_out = WVentOut(PVentCirc)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.horizontalLayout.addLayout(self.verticalLayout)

        QWidget.setTabOrder(self.lf_H0, self.lf_D0)
        QWidget.setTabOrder(self.lf_D0, self.lf_Alpha0)

        self.retranslateUi(PVentCirc)

        QMetaObject.connectSlotsByName(PVentCirc)

    # setupUi

    def retranslateUi(self, PVentCirc):
        PVentCirc.setWindowTitle(QCoreApplication.translate("PVentCirc", u"Form", None))
        self.img_vent.setText("")
        self.unit_D0.setText(QCoreApplication.translate("PVentCirc", u"m", None))
        self.in_Alpha0.setText(
            QCoreApplication.translate("PVentCirc", u"Alpha0 :", None)
        )
        self.unit_Alpha0.setText(QCoreApplication.translate("PVentCirc", u"rad", None))
        self.unit_H0.setText(QCoreApplication.translate("PVentCirc", u"m", None))
        self.in_H0.setText(QCoreApplication.translate("PVentCirc", u"H0 :", None))
        self.in_D0.setText(QCoreApplication.translate("PVentCirc", u"D0 :", None))
        self.in_Zh.setText(QCoreApplication.translate("PVentCirc", u"Zh :", None))

    # retranslateUi
