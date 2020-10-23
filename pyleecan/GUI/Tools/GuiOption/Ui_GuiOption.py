# -*- coding: utf-8 -*-

# File generated according to GuiOption.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ....GUI.Tools.WPathSelector.WPathSelector import WPathSelector

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_GUIOption(object):
    def setupUi(self, GUIOption):
        if not GUIOption.objectName():
            GUIOption.setObjectName(u"GUIOption")
        GUIOption.resize(480, 138)
        GUIOption.setMinimumSize(QSize(0, 0))
        GUIOption.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(GUIOption)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.w_matlib_path = WPathSelector(GUIOption)
        self.w_matlib_path.setObjectName(u"w_matlib_path")

        self.verticalLayout.addWidget(self.w_matlib_path)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.in_unit_m = QLabel(GUIOption)
        self.in_unit_m.setObjectName(u"in_unit_m")

        self.horizontalLayout.addWidget(self.in_unit_m)

        self.c_unit_m = QComboBox(GUIOption)
        self.c_unit_m.addItem("")
        self.c_unit_m.addItem("")
        self.c_unit_m.setObjectName(u"c_unit_m")

        self.horizontalLayout.addWidget(self.c_unit_m)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.in_unit_m2 = QLabel(GUIOption)
        self.in_unit_m2.setObjectName(u"in_unit_m2")

        self.horizontalLayout_2.addWidget(self.in_unit_m2)

        self.c_unit_m2 = QComboBox(GUIOption)
        self.c_unit_m2.addItem("")
        self.c_unit_m2.addItem("")
        self.c_unit_m2.setObjectName(u"c_unit_m2")

        self.horizontalLayout_2.addWidget(self.c_unit_m2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.retranslateUi(GUIOption)

        QMetaObject.connectSlotsByName(GUIOption)

    # setupUi

    def retranslateUi(self, GUIOption):
        GUIOption.setWindowTitle(QCoreApplication.translate("GUIOption", u"Form", None))
        self.in_unit_m.setText(
            QCoreApplication.translate("GUIOption", u"Meter unit", None)
        )
        self.c_unit_m.setItemText(
            0, QCoreApplication.translate("GUIOption", u"m", None)
        )
        self.c_unit_m.setItemText(
            1, QCoreApplication.translate("GUIOption", u"mm", None)
        )

        self.in_unit_m2.setText(
            QCoreApplication.translate("GUIOption", u"Surface unit", None)
        )
        self.c_unit_m2.setItemText(
            0, QCoreApplication.translate("GUIOption", u"m\u00b2", None)
        )
        self.c_unit_m2.setItemText(
            1, QCoreApplication.translate("GUIOption", u"mm\u00b2", None)
        )

    # retranslateUi
