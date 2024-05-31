# -*- coding: utf-8 -*-

# File generated according to PVentCirc.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.DAVDuct.WVentOut.WVentOut import WVentOut
from ......GUI.Tools.SpinBox import SpinBox

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PVentCirc(object):
    def setupUi(self, PVentCirc):
        if not PVentCirc.objectName():
            PVentCirc.setObjectName("PVentCirc")
        PVentCirc.resize(700, 470)
        PVentCirc.setMinimumSize(QSize(700, 470))
        PVentCirc.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PVentCirc)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_vent = QLabel(PVentCirc)
        self.img_vent.setObjectName("img_vent")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_vent.sizePolicy().hasHeightForWidth())
        self.img_vent.setSizePolicy(sizePolicy)
        self.img_vent.setMinimumSize(QSize(410, 300))
        self.img_vent.setMaximumSize(QSize(16777215, 16777215))
        self.img_vent.setPixmap(
            QPixmap(
                ":/images/images/MachineSetup/LamParam/VentilationCirc_empty_int_rotor.png"
            )
        )
        self.img_vent.setScaledContents(False)
        self.img_vent.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.img_vent)

        self.scrollArea = QScrollArea(PVentCirc)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(300, 0))
        self.scrollArea.setMaximumSize(QSize(300, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 298, 446))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_D0 = QLabel(self.scrollAreaWidgetContents)
        self.in_D0.setObjectName("in_D0")

        self.gridLayout.addWidget(self.in_D0, 2, 0, 1, 1)

        self.in_H0 = QLabel(self.scrollAreaWidgetContents)
        self.in_H0.setObjectName("in_H0")

        self.gridLayout.addWidget(self.in_H0, 1, 0, 1, 1)

        self.unit_D0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_D0.setObjectName("unit_D0")

        self.gridLayout.addWidget(self.unit_D0, 2, 2, 1, 1)

        self.si_Zh = SpinBox(self.scrollAreaWidgetContents)
        self.si_Zh.setObjectName("si_Zh")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.si_Zh.sizePolicy().hasHeightForWidth())
        self.si_Zh.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.si_Zh, 0, 1, 1, 1)

        self.lf_H0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H0.setObjectName("lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 1, 1, 1, 1)

        self.lf_D0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_D0.setObjectName("lf_D0")

        self.gridLayout.addWidget(self.lf_D0, 2, 1, 1, 1)

        self.unit_H0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H0.setObjectName("unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 1, 2, 1, 1)

        self.in_Zh = QLabel(self.scrollAreaWidgetContents)
        self.in_Zh.setObjectName("in_Zh")

        self.gridLayout.addWidget(self.in_Zh, 0, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 286, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.w_out = WVentOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName("w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_H0, self.lf_D0)

        self.retranslateUi(PVentCirc)

        QMetaObject.connectSlotsByName(PVentCirc)

    # setupUi

    def retranslateUi(self, PVentCirc):
        PVentCirc.setWindowTitle(QCoreApplication.translate("PVentCirc", "Form", None))
        self.img_vent.setText("")
        self.in_D0.setText(QCoreApplication.translate("PVentCirc", "D0 :", None))
        self.in_H0.setText(QCoreApplication.translate("PVentCirc", "H0 :", None))
        self.unit_D0.setText(QCoreApplication.translate("PVentCirc", "m", None))
        self.unit_H0.setText(QCoreApplication.translate("PVentCirc", "m", None))
        self.in_Zh.setText(QCoreApplication.translate("PVentCirc", "Zh :", None))

    # retranslateUi
