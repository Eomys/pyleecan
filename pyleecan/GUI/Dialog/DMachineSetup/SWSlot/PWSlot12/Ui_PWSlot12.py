# -*- coding: utf-8 -*-

# File generated according to PWSlot12.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PWSlot12(object):
    def setupUi(self, PWSlot12):
        if not PWSlot12.objectName():
            PWSlot12.setObjectName(u"PWSlot12")
        PWSlot12.resize(630, 470)
        PWSlot12.setMinimumSize(QSize(630, 470))
        PWSlot12.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PWSlot12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_slot = QLabel(PWSlot12)
        self.img_slot.setObjectName(u"img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(u":/images/images/MachineSetup/WSlot/Slot 12.PNG")
        )
        self.img_slot.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_R1 = QLabel(PWSlot12)
        self.in_R1.setObjectName(u"in_R1")

        self.gridLayout.addWidget(self.in_R1, 0, 0, 1, 1)

        self.lf_R1 = FloatEdit(PWSlot12)
        self.lf_R1.setObjectName(u"lf_R1")

        self.gridLayout.addWidget(self.lf_R1, 0, 1, 1, 1)

        self.unit_R1 = QLabel(PWSlot12)
        self.unit_R1.setObjectName(u"unit_R1")

        self.gridLayout.addWidget(self.unit_R1, 0, 2, 1, 1)

        self.in_R2 = QLabel(PWSlot12)
        self.in_R2.setObjectName(u"in_R2")

        self.gridLayout.addWidget(self.in_R2, 1, 0, 1, 1)

        self.lf_R2 = FloatEdit(PWSlot12)
        self.lf_R2.setObjectName(u"lf_R2")

        self.gridLayout.addWidget(self.lf_R2, 1, 1, 1, 1)

        self.unit_R2 = QLabel(PWSlot12)
        self.unit_R2.setObjectName(u"unit_R2")

        self.gridLayout.addWidget(self.unit_R2, 1, 2, 1, 1)

        self.in_H0 = QLabel(PWSlot12)
        self.in_H0.setObjectName(u"in_H0")

        self.gridLayout.addWidget(self.in_H0, 2, 0, 1, 1)

        self.lf_H0 = FloatEdit(PWSlot12)
        self.lf_H0.setObjectName(u"lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 2, 1, 1, 1)

        self.unit_H0 = QLabel(PWSlot12)
        self.unit_H0.setObjectName(u"unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 2, 2, 1, 1)

        self.in_H1 = QLabel(PWSlot12)
        self.in_H1.setObjectName(u"in_H1")

        self.gridLayout.addWidget(self.in_H1, 3, 0, 1, 1)

        self.lf_H1 = FloatEdit(PWSlot12)
        self.lf_H1.setObjectName(u"lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 3, 1, 1, 1)

        self.unit_H1 = QLabel(PWSlot12)
        self.unit_H1.setObjectName(u"unit_H1")

        self.gridLayout.addWidget(self.unit_H1, 3, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.w_out = WWSlotOut(PWSlot12)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.horizontalLayout.addLayout(self.verticalLayout)

        QWidget.setTabOrder(self.lf_R1, self.lf_R2)
        QWidget.setTabOrder(self.lf_R2, self.lf_H0)
        QWidget.setTabOrder(self.lf_H0, self.lf_H1)

        self.retranslateUi(PWSlot12)

        QMetaObject.connectSlotsByName(PWSlot12)

    # setupUi

    def retranslateUi(self, PWSlot12):
        PWSlot12.setWindowTitle(QCoreApplication.translate("PWSlot12", u"Form", None))
        self.img_slot.setText("")
        self.in_R1.setText(QCoreApplication.translate("PWSlot12", u"R1 :", None))
        self.unit_R1.setText(QCoreApplication.translate("PWSlot12", u"m", None))
        self.in_R2.setText(QCoreApplication.translate("PWSlot12", u"R2 :", None))
        self.unit_R2.setText(QCoreApplication.translate("PWSlot12", u"m", None))
        self.in_H0.setText(QCoreApplication.translate("PWSlot12", u"H0 :", None))
        self.unit_H0.setText(QCoreApplication.translate("PWSlot12", u"m", None))
        self.in_H1.setText(QCoreApplication.translate("PWSlot12", u"H1 :", None))
        self.unit_H1.setText(QCoreApplication.translate("PWSlot12", u"m", None))

    # retranslateUi
