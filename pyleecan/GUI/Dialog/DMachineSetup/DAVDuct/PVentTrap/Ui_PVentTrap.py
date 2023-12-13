# -*- coding: utf-8 -*-

# File generated according to PVentTrap.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.DAVDuct.WVentOut.WVentOut import WVentOut
from ......GUI.Tools.SpinBox import SpinBox

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PVentTrap(object):
    def setupUi(self, PVentTrap):
        if not PVentTrap.objectName():
            PVentTrap.setObjectName(u"PVentTrap")
        PVentTrap.resize(700, 470)
        PVentTrap.setMinimumSize(QSize(700, 470))
        PVentTrap.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PVentTrap)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.img_vent = QLabel(PVentTrap)
        self.img_vent.setObjectName(u"img_vent")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_vent.sizePolicy().hasHeightForWidth())
        self.img_vent.setSizePolicy(sizePolicy)
        self.img_vent.setMinimumSize(QSize(410, 300))
        self.img_vent.setMaximumSize(QSize(16777215, 16777215))
        self.img_vent.setPixmap(
            QPixmap(
                u":/images/images/MachineSetup/LamParam/VentilationTrap_empty_int_rotor.png"
            )
        )
        self.img_vent.setScaledContents(False)
        self.img_vent.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.img_vent)

        self.scrollArea = QScrollArea(PVentTrap)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(300, 0))
        self.scrollArea.setMaximumSize(QSize(300, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 298, 446))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lf_H0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H0.setObjectName(u"lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 1, 1, 1, 1)

        self.unit_H0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H0.setObjectName(u"unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 1, 2, 1, 1)

        self.lf_W1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W1.setObjectName(u"lf_W1")

        self.gridLayout.addWidget(self.lf_W1, 3, 1, 1, 1)

        self.in_D0 = QLabel(self.scrollAreaWidgetContents)
        self.in_D0.setObjectName(u"in_D0")

        self.gridLayout.addWidget(self.in_D0, 2, 0, 1, 1)

        self.unit_W2 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W2.setObjectName(u"unit_W2")

        self.gridLayout.addWidget(self.unit_W2, 4, 2, 1, 1)

        self.in_H0 = QLabel(self.scrollAreaWidgetContents)
        self.in_H0.setObjectName(u"in_H0")

        self.gridLayout.addWidget(self.in_H0, 1, 0, 1, 1)

        self.lf_D0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_D0.setObjectName(u"lf_D0")

        self.gridLayout.addWidget(self.lf_D0, 2, 1, 1, 1)

        self.in_W1 = QLabel(self.scrollAreaWidgetContents)
        self.in_W1.setObjectName(u"in_W1")

        self.gridLayout.addWidget(self.in_W1, 3, 0, 1, 1)

        self.si_Zh = SpinBox(self.scrollAreaWidgetContents)
        self.si_Zh.setObjectName(u"si_Zh")

        self.gridLayout.addWidget(self.si_Zh, 0, 1, 1, 1)

        self.lf_W2 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W2.setObjectName(u"lf_W2")

        self.gridLayout.addWidget(self.lf_W2, 4, 1, 1, 1)

        self.in_Zh = QLabel(self.scrollAreaWidgetContents)
        self.in_Zh.setObjectName(u"in_Zh")

        self.gridLayout.addWidget(self.in_Zh, 0, 0, 1, 1)

        self.in_W2 = QLabel(self.scrollAreaWidgetContents)
        self.in_W2.setObjectName(u"in_W2")

        self.gridLayout.addWidget(self.in_W2, 4, 0, 1, 1)

        self.unit_D0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_D0.setObjectName(u"unit_D0")

        self.gridLayout.addWidget(self.unit_D0, 2, 2, 1, 1)

        self.unit_W1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W1.setObjectName(u"unit_W1")

        self.gridLayout.addWidget(self.unit_W1, 3, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 228, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.w_out = WVentOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_H0, self.lf_D0)

        self.retranslateUi(PVentTrap)

        QMetaObject.connectSlotsByName(PVentTrap)

    # setupUi

    def retranslateUi(self, PVentTrap):
        PVentTrap.setWindowTitle(QCoreApplication.translate("PVentTrap", u"Form", None))
        self.img_vent.setText("")
        self.unit_H0.setText(QCoreApplication.translate("PVentTrap", u"m", None))
        self.in_D0.setText(QCoreApplication.translate("PVentTrap", u"D0 :", None))
        self.unit_W2.setText(QCoreApplication.translate("PVentTrap", u"m", None))
        self.in_H0.setText(QCoreApplication.translate("PVentTrap", u"H0 :", None))
        self.in_W1.setText(QCoreApplication.translate("PVentTrap", u"W1 :", None))
        self.in_Zh.setText(QCoreApplication.translate("PVentTrap", u"Zh :", None))
        self.in_W2.setText(QCoreApplication.translate("PVentTrap", u"W2 :", None))
        self.unit_D0.setText(QCoreApplication.translate("PVentTrap", u"m", None))
        self.unit_W1.setText(QCoreApplication.translate("PVentTrap", u"m", None))

    # retranslateUi
