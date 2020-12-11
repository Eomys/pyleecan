# -*- coding: utf-8 -*-

# File generated according to PWSlot14.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PWSlot14(object):
    def setupUi(self, PWSlot14):
        if not PWSlot14.objectName():
            PWSlot14.setObjectName(u"PWSlot14")
        PWSlot14.resize(630, 470)
        PWSlot14.setMinimumSize(QSize(630, 470))
        PWSlot14.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PWSlot14)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_slot = QLabel(PWSlot14)
        self.img_slot.setObjectName(u"img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(u":/images/images/MachineSetup/WSlot/Slot 14.PNG")
        )
        self.img_slot.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_W0 = QLabel(PWSlot14)
        self.in_W0.setObjectName(u"in_W0")

        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)

        self.lf_W0 = FloatEdit(PWSlot14)
        self.lf_W0.setObjectName(u"lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)

        self.unit_W0 = QLabel(PWSlot14)
        self.unit_W0.setObjectName(u"unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 0, 2, 1, 1)

        self.in_W3 = QLabel(PWSlot14)
        self.in_W3.setObjectName(u"in_W3")

        self.gridLayout.addWidget(self.in_W3, 1, 0, 1, 1)

        self.lf_W3 = FloatEdit(PWSlot14)
        self.lf_W3.setObjectName(u"lf_W3")

        self.gridLayout.addWidget(self.lf_W3, 1, 1, 1, 1)

        self.unit_W3 = QLabel(PWSlot14)
        self.unit_W3.setObjectName(u"unit_W3")

        self.gridLayout.addWidget(self.unit_W3, 1, 2, 1, 1)

        self.in_H0 = QLabel(PWSlot14)
        self.in_H0.setObjectName(u"in_H0")

        self.gridLayout.addWidget(self.in_H0, 2, 0, 1, 1)

        self.lf_H0 = FloatEdit(PWSlot14)
        self.lf_H0.setObjectName(u"lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 2, 1, 1, 1)

        self.unit_H0 = QLabel(PWSlot14)
        self.unit_H0.setObjectName(u"unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 2, 2, 1, 1)

        self.in_H1 = QLabel(PWSlot14)
        self.in_H1.setObjectName(u"in_H1")

        self.gridLayout.addWidget(self.in_H1, 3, 0, 1, 1)

        self.lf_H1 = FloatEdit(PWSlot14)
        self.lf_H1.setObjectName(u"lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 3, 1, 1, 1)

        self.unit_H1 = QLabel(PWSlot14)
        self.unit_H1.setObjectName(u"unit_H1")

        self.gridLayout.addWidget(self.unit_H1, 3, 2, 1, 1)

        self.in_H3 = QLabel(PWSlot14)
        self.in_H3.setObjectName(u"in_H3")

        self.gridLayout.addWidget(self.in_H3, 4, 0, 1, 1)

        self.lf_H3 = FloatEdit(PWSlot14)
        self.lf_H3.setObjectName(u"lf_H3")

        self.gridLayout.addWidget(self.lf_H3, 4, 1, 1, 1)

        self.unit_H3 = QLabel(PWSlot14)
        self.unit_H3.setObjectName(u"unit_H3")

        self.gridLayout.addWidget(self.unit_H3, 4, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.w_out = WWSlotOut(PWSlot14)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.horizontalLayout.addLayout(self.verticalLayout)

        QWidget.setTabOrder(self.lf_W0, self.lf_W3)
        QWidget.setTabOrder(self.lf_W3, self.lf_H0)
        QWidget.setTabOrder(self.lf_H0, self.lf_H1)
        QWidget.setTabOrder(self.lf_H1, self.lf_H3)

        self.retranslateUi(PWSlot14)

        QMetaObject.connectSlotsByName(PWSlot14)

    # setupUi

    def retranslateUi(self, PWSlot14):
        PWSlot14.setWindowTitle(QCoreApplication.translate("PWSlot14", u"Form", None))
        self.img_slot.setText("")
        self.in_W0.setText(QCoreApplication.translate("PWSlot14", u"W0 :", None))
        self.unit_W0.setText(QCoreApplication.translate("PWSlot14", u"m", None))
        self.in_W3.setText(QCoreApplication.translate("PWSlot14", u"W3 :", None))
        self.unit_W3.setText(QCoreApplication.translate("PWSlot14", u"m", None))
        self.in_H0.setText(QCoreApplication.translate("PWSlot14", u"H0 :", None))
        self.unit_H0.setText(QCoreApplication.translate("PWSlot14", u"m", None))
        self.in_H1.setText(QCoreApplication.translate("PWSlot14", u"H1 :", None))
        self.unit_H1.setText(QCoreApplication.translate("PWSlot14", u"m", None))
        self.in_H3.setText(QCoreApplication.translate("PWSlot14", u"H3 :", None))
        self.unit_H3.setText(QCoreApplication.translate("PWSlot14", u"m", None))

    # retranslateUi
