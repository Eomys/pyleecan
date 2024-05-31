# -*- coding: utf-8 -*-

# File generated according to WNotch.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit


class Ui_WNotch(object):
    def setupUi(self, WNotch):
        if not WNotch.objectName():
            WNotch.setObjectName("WNotch")
        WNotch.resize(760, 490)
        WNotch.setMinimumSize(QSize(760, 490))
        self.main_layout = QVBoxLayout(WNotch)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.c_notch_type = QComboBox(WNotch)
        self.c_notch_type.addItem("")
        self.c_notch_type.addItem("")
        self.c_notch_type.addItem("")
        self.c_notch_type.addItem("")
        self.c_notch_type.addItem("")
        self.c_notch_type.addItem("")
        self.c_notch_type.addItem("")
        self.c_notch_type.setObjectName("c_notch_type")

        self.horizontalLayout.addWidget(self.c_notch_type)

        self.in_Zn = QLabel(WNotch)
        self.in_Zn.setObjectName("in_Zn")

        self.horizontalLayout.addWidget(self.in_Zn)

        self.si_Zn = QSpinBox(WNotch)
        self.si_Zn.setObjectName("si_Zn")

        self.horizontalLayout.addWidget(self.si_Zn)

        self.in_alpha = QLabel(WNotch)
        self.in_alpha.setObjectName("in_alpha")

        self.horizontalLayout.addWidget(self.in_alpha)

        self.lf_alpha = FloatEdit(WNotch)
        self.lf_alpha.setObjectName("lf_alpha")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lf_alpha.sizePolicy().hasHeightForWidth())
        self.lf_alpha.setSizePolicy(sizePolicy)
        self.lf_alpha.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.lf_alpha)

        self.c_alpha_unit = QComboBox(WNotch)
        self.c_alpha_unit.addItem("")
        self.c_alpha_unit.addItem("")
        self.c_alpha_unit.setObjectName("c_alpha_unit")

        self.horizontalLayout.addWidget(self.c_alpha_unit)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.b_plot = QPushButton(WNotch)
        self.b_plot.setObjectName("b_plot")

        self.horizontalLayout.addWidget(self.b_plot)

        self.main_layout.addLayout(self.horizontalLayout)

        self.w_notch = QWidget(WNotch)
        self.w_notch.setObjectName("w_notch")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.w_notch.sizePolicy().hasHeightForWidth())
        self.w_notch.setSizePolicy(sizePolicy1)
        self.w_notch.setMinimumSize(QSize(750, 450))

        self.main_layout.addWidget(self.w_notch)

        self.retranslateUi(WNotch)

        QMetaObject.connectSlotsByName(WNotch)

    # setupUi

    def retranslateUi(self, WNotch):
        WNotch.setWindowTitle(QCoreApplication.translate("WNotch", "Notch setup", None))
        self.c_notch_type.setItemText(
            0, QCoreApplication.translate("WNotch", "Slot Type 50", None)
        )
        self.c_notch_type.setItemText(
            1, QCoreApplication.translate("WNotch", "Slot Type 51", None)
        )
        self.c_notch_type.setItemText(
            2, QCoreApplication.translate("WNotch", "Slot Type 52", None)
        )
        self.c_notch_type.setItemText(
            3, QCoreApplication.translate("WNotch", "Slot Type 53", None)
        )
        self.c_notch_type.setItemText(
            4, QCoreApplication.translate("WNotch", "Slot Type 54", None)
        )
        self.c_notch_type.setItemText(
            5, QCoreApplication.translate("WNotch", "Slot Type 55", None)
        )
        self.c_notch_type.setItemText(
            6, QCoreApplication.translate("WNotch", "Slot Type 56", None)
        )

        self.in_Zn.setText(QCoreApplication.translate("WNotch", "Zn:", None))
        self.in_alpha.setText(QCoreApplication.translate("WNotch", "Alpha:", None))
        self.c_alpha_unit.setItemText(
            0, QCoreApplication.translate("WNotch", "[rad]", None)
        )
        self.c_alpha_unit.setItemText(
            1, QCoreApplication.translate("WNotch", "[deg]", None)
        )

        self.b_plot.setText(QCoreApplication.translate("WNotch", "Preview Notch", None))

    # retranslateUi
