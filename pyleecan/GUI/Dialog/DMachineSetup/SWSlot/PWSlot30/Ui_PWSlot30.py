# -*- coding: utf-8 -*-

# File generated according to PWSlot30.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut
from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelectV import WMatSelectV

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PWSlot30(object):
    def setupUi(self, PWSlot30):
        if not PWSlot30.objectName():
            PWSlot30.setObjectName("PWSlot30")
        PWSlot30.resize(899, 470)
        PWSlot30.setMinimumSize(QSize(630, 470))
        PWSlot30.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PWSlot30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_slot = QLabel(PWSlot30)
        self.img_slot.setObjectName("img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(":/images/images/MachineSetup/WSlot/SlotW30_wind_ext_stator.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(PWSlot30)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 450))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_W3 = QLabel(self.scrollAreaWidgetContents)
        self.in_W3.setObjectName("in_W3")

        self.gridLayout.addWidget(self.in_W3, 1, 0, 1, 1)

        self.in_H1 = QLabel(self.scrollAreaWidgetContents)
        self.in_H1.setObjectName("in_H1")

        self.gridLayout.addWidget(self.in_H1, 4, 0, 1, 1)

        self.in_W0 = QLabel(self.scrollAreaWidgetContents)
        self.in_W0.setObjectName("in_W0")

        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)

        self.in_R2 = QLabel(self.scrollAreaWidgetContents)
        self.in_R2.setObjectName("in_R2")

        self.gridLayout.addWidget(self.in_R2, 6, 0, 1, 1)

        self.lf_W3 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W3.setObjectName("lf_W3")

        self.gridLayout.addWidget(self.lf_W3, 1, 1, 1, 1)

        self.unit_H0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H0.setObjectName("unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 3, 2, 1, 1)

        self.unit_W3 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W3.setObjectName("unit_W3")

        self.gridLayout.addWidget(self.unit_W3, 1, 2, 1, 1)

        self.unit_H1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H1.setObjectName("unit_H1")

        self.gridLayout.addWidget(self.unit_H1, 4, 2, 1, 1)

        self.lf_H0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H0.setObjectName("lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 3, 1, 1, 1)

        self.lf_H1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H1.setObjectName("lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 4, 1, 1, 1)

        self.lf_W0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W0.setObjectName("lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)

        self.in_H0 = QLabel(self.scrollAreaWidgetContents)
        self.in_H0.setObjectName("in_H0")

        self.gridLayout.addWidget(self.in_H0, 3, 0, 1, 1)

        self.unit_R2 = QLabel(self.scrollAreaWidgetContents)
        self.unit_R2.setObjectName("unit_R2")

        self.gridLayout.addWidget(self.unit_R2, 6, 2, 1, 1)

        self.unit_W0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W0.setObjectName("unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 0, 2, 1, 1)

        self.lf_R2 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_R2.setObjectName("lf_R2")

        self.gridLayout.addWidget(self.lf_R2, 6, 1, 1, 1)

        self.in_R1 = QLabel(self.scrollAreaWidgetContents)
        self.in_R1.setObjectName("in_R1")

        self.gridLayout.addWidget(self.in_R1, 5, 0, 1, 1)

        self.lf_R1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_R1.setObjectName("lf_R1")

        self.gridLayout.addWidget(self.lf_R1, 5, 1, 1, 1)

        self.unit_R1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_R1.setObjectName("unit_R1")

        self.gridLayout.addWidget(self.unit_R1, 5, 2, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.g_wedge = QGroupBox(self.scrollAreaWidgetContents)
        self.g_wedge.setObjectName("g_wedge")
        self.g_wedge.setCheckable(True)
        self.g_wedge.setChecked(False)
        self.gridLayout_2 = QGridLayout(self.g_wedge)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.w_wedge_mat = WMatSelectV(self.g_wedge)
        self.w_wedge_mat.setObjectName("w_wedge_mat")
        self.w_wedge_mat.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.w_wedge_mat, 0, 0, 1, 2)

        self.verticalLayout_3.addWidget(self.g_wedge)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.w_out = WWSlotOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName("w_out")

        self.verticalLayout_3.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_W0, self.lf_W3)
        QWidget.setTabOrder(self.lf_W3, self.lf_H0)
        QWidget.setTabOrder(self.lf_H0, self.lf_H1)
        QWidget.setTabOrder(self.lf_H1, self.lf_R2)
        QWidget.setTabOrder(self.lf_R2, self.g_wedge)
        QWidget.setTabOrder(self.g_wedge, self.scrollArea)

        self.retranslateUi(PWSlot30)

        QMetaObject.connectSlotsByName(PWSlot30)

    # setupUi

    def retranslateUi(self, PWSlot30):
        PWSlot30.setWindowTitle(QCoreApplication.translate("PWSlot30", "Form", None))
        self.img_slot.setText("")
        self.in_W3.setText(QCoreApplication.translate("PWSlot30", "W3", None))
        self.in_H1.setText(QCoreApplication.translate("PWSlot30", "H1", None))
        self.in_W0.setText(QCoreApplication.translate("PWSlot30", "W0", None))
        self.in_R2.setText(QCoreApplication.translate("PWSlot30", "R2", None))
        self.unit_H0.setText(QCoreApplication.translate("PWSlot30", "m", None))
        self.unit_W3.setText(QCoreApplication.translate("PWSlot30", "m", None))
        self.unit_H1.setText(QCoreApplication.translate("PWSlot30", "m", None))
        self.in_H0.setText(QCoreApplication.translate("PWSlot30", "H0", None))
        self.unit_R2.setText(QCoreApplication.translate("PWSlot30", "m", None))
        self.unit_W0.setText(QCoreApplication.translate("PWSlot30", "m", None))
        self.in_R1.setText(QCoreApplication.translate("PWSlot30", "R1", None))
        self.unit_R1.setText(QCoreApplication.translate("PWSlot30", "m", None))
        self.g_wedge.setTitle(QCoreApplication.translate("PWSlot30", "Wedge", None))

    # retranslateUi
