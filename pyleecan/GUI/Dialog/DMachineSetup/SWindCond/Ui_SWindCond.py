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
            SWindCond.setObjectName("SWindCond")
        SWindCond.resize(650, 550)
        SWindCond.setMinimumSize(QSize(650, 550))
        self.main_layout = QVBoxLayout(SWindCond)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_cond_type = QLabel(SWindCond)
        self.in_cond_type.setObjectName("in_cond_type")

        self.horizontalLayout.addWidget(self.in_cond_type)

        self.c_cond_type = QComboBox(SWindCond)
        self.c_cond_type.addItem("")
        self.c_cond_type.addItem("")
        self.c_cond_type.setObjectName("c_cond_type")
        self.c_cond_type.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.c_cond_type)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.w_mat_0 = WMatSelect(SWindCond)
        self.w_mat_0.setObjectName("w_mat_0")
        self.w_mat_0.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.w_mat_0)

        self.w_mat_1 = WMatSelect(SWindCond)
        self.w_mat_1.setObjectName("w_mat_1")
        self.w_mat_1.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.w_mat_1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.main_layout.addLayout(self.horizontalLayout)

        self.w_cond = QWidget(SWindCond)
        self.w_cond.setObjectName("w_cond")

        self.main_layout.addWidget(self.w_cond)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.b_previous = QPushButton(SWindCond)
        self.b_previous.setObjectName("b_previous")

        self.horizontalLayout_2.addWidget(self.b_previous)

        self.b_next = QPushButton(SWindCond)
        self.b_next.setObjectName("b_next")

        self.horizontalLayout_2.addWidget(self.b_next)

        self.main_layout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SWindCond)

        QMetaObject.connectSlotsByName(SWindCond)

    # setupUi

    def retranslateUi(self, SWindCond):
        SWindCond.setWindowTitle(QCoreApplication.translate("SWindCond", "Form", None))
        self.in_cond_type.setText(
            QCoreApplication.translate("SWindCond", "Conductor type :", None)
        )
        self.c_cond_type.setItemText(
            0, QCoreApplication.translate("SWindCond", "Preformed Rectangular", None)
        )
        self.c_cond_type.setItemText(
            1, QCoreApplication.translate("SWindCond", "Random Round Wire", None)
        )

        self.b_previous.setText(
            QCoreApplication.translate("SWindCond", "Previous", None)
        )
        self.b_next.setText(QCoreApplication.translate("SWindCond", "Next", None))

    # retranslateUi
