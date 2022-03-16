# -*- coding: utf-8 -*-

# File generated according to SWindCond.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .....GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SWindCond(object):
    def setupUi(self, SWindCond):
        if not SWindCond.objectName():
            SWindCond.setObjectName(u"SWindCond")
        SWindCond.resize(650, 550)
        SWindCond.setMinimumSize(QSize(650, 550))
        self.main_layout = QVBoxLayout(SWindCond)
        self.main_layout.setObjectName(u"main_layout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.in_cond_type = QLabel(SWindCond)
        self.in_cond_type.setObjectName(u"in_cond_type")

        self.horizontalLayout.addWidget(self.in_cond_type)

        self.c_cond_type = QComboBox(SWindCond)
        self.c_cond_type.addItem("")
        self.c_cond_type.addItem("")
        self.c_cond_type.setObjectName(u"c_cond_type")
        self.c_cond_type.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.c_cond_type)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.w_mat_0 = WMatSelect(SWindCond)
        self.w_mat_0.setObjectName(u"w_mat_0")
        self.w_mat_0.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.w_mat_0)

        self.w_mat_1 = WMatSelect(SWindCond)
        self.w_mat_1.setObjectName(u"w_mat_1")
        self.w_mat_1.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.w_mat_1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.main_layout.addLayout(self.horizontalLayout)

        self.w_cond = QWidget(SWindCond)
        self.w_cond.setObjectName(u"w_cond")

        self.main_layout.addWidget(self.w_cond)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.b_previous = QPushButton(SWindCond)
        self.b_previous.setObjectName(u"b_previous")

        self.horizontalLayout_2.addWidget(self.b_previous)

        self.b_next = QPushButton(SWindCond)
        self.b_next.setObjectName(u"b_next")

        self.horizontalLayout_2.addWidget(self.b_next)

        self.main_layout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SWindCond)

        QMetaObject.connectSlotsByName(SWindCond)

    # setupUi

    def retranslateUi(self, SWindCond):
        SWindCond.setWindowTitle(QCoreApplication.translate("SWindCond", u"Form", None))
        self.in_cond_type.setText(
            QCoreApplication.translate("SWindCond", u"Conductor type :", None)
        )
        self.c_cond_type.setItemText(
            0, QCoreApplication.translate("SWindCond", u"Preformed Rectangular", None)
        )
        self.c_cond_type.setItemText(
            1, QCoreApplication.translate("SWindCond", u"Random Round Wire", None)
        )

        self.b_previous.setText(
            QCoreApplication.translate("SWindCond", u"Previous", None)
        )
        self.b_next.setText(QCoreApplication.translate("SWindCond", u"Next", None))

    # retranslateUi
