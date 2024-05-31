# -*- coding: utf-8 -*-

# File generated according to WVent.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Tools.HelpButton import HelpButton
from ......GUI.Tools.FloatEdit import FloatEdit


class Ui_WVent(object):
    def setupUi(self, WVent):
        if not WVent.objectName():
            WVent.setObjectName("WVent")
        WVent.resize(630, 470)
        WVent.setMinimumSize(QSize(630, 470))
        self.main_layout = QVBoxLayout(WVent)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_vent_type = QLabel(WVent)
        self.in_vent_type.setObjectName("in_vent_type")

        self.horizontalLayout.addWidget(self.in_vent_type)

        self.c_vent_type = QComboBox(WVent)
        self.c_vent_type.setObjectName("c_vent_type")

        self.horizontalLayout.addWidget(self.c_vent_type)

        self.in_Alpha0 = QLabel(WVent)
        self.in_Alpha0.setObjectName("in_Alpha0")

        self.horizontalLayout.addWidget(self.in_Alpha0)

        self.lf_Alpha0 = FloatEdit(WVent)
        self.lf_Alpha0.setObjectName("lf_Alpha0")
        self.lf_Alpha0.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.lf_Alpha0)

        self.c_Alpha0_unit = QComboBox(WVent)
        self.c_Alpha0_unit.addItem("")
        self.c_Alpha0_unit.addItem("")
        self.c_Alpha0_unit.setObjectName("c_Alpha0_unit")

        self.horizontalLayout.addWidget(self.c_Alpha0_unit)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.main_layout.addLayout(self.horizontalLayout)

        self.w_vent = QWidget(WVent)
        self.w_vent.setObjectName("w_vent")
        self.w_vent.setMinimumSize(QSize(640, 480))

        self.main_layout.addWidget(self.w_vent)

        self.retranslateUi(WVent)

        QMetaObject.connectSlotsByName(WVent)

    # setupUi

    def retranslateUi(self, WVent):
        WVent.setWindowTitle(QCoreApplication.translate("WVent", "Form", None))
        self.in_vent_type.setText(
            QCoreApplication.translate("WVent", "Cooling Duct Shape:", None)
        )
        self.in_Alpha0.setText(QCoreApplication.translate("WVent", "Alpha0 :", None))
        self.c_Alpha0_unit.setItemText(
            0, QCoreApplication.translate("WVent", "[rad]", None)
        )
        self.c_Alpha0_unit.setItemText(
            1, QCoreApplication.translate("WVent", "[\u00b0]", None)
        )

    # retranslateUi
