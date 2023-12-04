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
from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelectV import WMatSelectV

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PWSlot14(object):
    def setupUi(self, PWSlot14):
        if not PWSlot14.objectName():
            PWSlot14.setObjectName(u"PWSlot14")
        PWSlot14.resize(889, 479)
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
            QPixmap(u":/images/images/MachineSetup/WSlot/SlotW14_wind_ext_stator.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(PWSlot14)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 459))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_H1 = QLabel(self.scrollAreaWidgetContents)
        self.in_H1.setObjectName(u"in_H1")

        self.gridLayout.addWidget(self.in_H1, 3, 0, 1, 1)

        self.lf_H3 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H3.setObjectName(u"lf_H3")

        self.gridLayout.addWidget(self.lf_H3, 4, 1, 1, 1)

        self.in_H0 = QLabel(self.scrollAreaWidgetContents)
        self.in_H0.setObjectName(u"in_H0")

        self.gridLayout.addWidget(self.in_H0, 2, 0, 1, 1)

        self.unit_W3 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W3.setObjectName(u"unit_W3")

        self.gridLayout.addWidget(self.unit_W3, 1, 3, 1, 1)

        self.unit_H3 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H3.setObjectName(u"unit_H3")

        self.gridLayout.addWidget(self.unit_H3, 4, 3, 1, 1)

        self.lf_H0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H0.setObjectName(u"lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 2, 1, 1, 1)

        self.unit_W0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W0.setObjectName(u"unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 0, 3, 1, 1)

        self.in_H3 = QLabel(self.scrollAreaWidgetContents)
        self.in_H3.setObjectName(u"in_H3")

        self.gridLayout.addWidget(self.in_H3, 4, 0, 1, 1)

        self.unit_H0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H0.setObjectName(u"unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 2, 3, 1, 1)

        self.in_W3 = QLabel(self.scrollAreaWidgetContents)
        self.in_W3.setObjectName(u"in_W3")

        self.gridLayout.addWidget(self.in_W3, 1, 0, 1, 1)

        self.in_W0 = QLabel(self.scrollAreaWidgetContents)
        self.in_W0.setObjectName(u"in_W0")

        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)

        self.lf_W0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W0.setObjectName(u"lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)

        self.lf_H1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H1.setObjectName(u"lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 3, 1, 1, 1)

        self.lf_W3 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W3.setObjectName(u"lf_W3")

        self.gridLayout.addWidget(self.lf_W3, 1, 1, 1, 1)

        self.c_H1_unit = QComboBox(self.scrollAreaWidgetContents)
        self.c_H1_unit.setObjectName(u"c_H1_unit")

        self.gridLayout.addWidget(self.c_H1_unit, 3, 3, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.g_wedge = QGroupBox(self.scrollAreaWidgetContents)
        self.g_wedge.setObjectName(u"g_wedge")
        self.g_wedge.setCheckable(True)
        self.g_wedge.setChecked(False)
        self.gridLayout_2 = QGridLayout(self.g_wedge)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.in_type = QLabel(self.g_wedge)
        self.in_type.setObjectName(u"in_type")
        self.in_type.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.in_type, 0, 0, 1, 1)

        self.w_wedge_mat = WMatSelectV(self.g_wedge)
        self.w_wedge_mat.setObjectName(u"w_wedge_mat")
        self.w_wedge_mat.setMinimumSize(QSize(100, 100))

        self.gridLayout_2.addWidget(self.w_wedge_mat, 2, 0, 1, 2)

        self.c_wedge_type = QComboBox(self.g_wedge)
        self.c_wedge_type.addItem("")
        self.c_wedge_type.setObjectName(u"c_wedge_type")
        self.c_wedge_type.setMaximumSize(QSize(200, 16777215))
        self.c_wedge_type.setEditable(False)

        self.gridLayout_2.addWidget(self.c_wedge_type, 0, 1, 1, 1)

        self.verticalLayout_3.addWidget(self.g_wedge)

        self.verticalSpacer = QSpacerItem(
            17, 37, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.w_out = WWSlotOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout_3.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_W0, self.lf_W3)
        QWidget.setTabOrder(self.lf_W3, self.lf_H0)
        QWidget.setTabOrder(self.lf_H0, self.lf_H1)
        QWidget.setTabOrder(self.lf_H1, self.lf_H3)
        QWidget.setTabOrder(self.lf_H3, self.g_wedge)
        QWidget.setTabOrder(self.g_wedge, self.c_wedge_type)
        QWidget.setTabOrder(self.c_wedge_type, self.scrollArea)

        self.retranslateUi(PWSlot14)

        QMetaObject.connectSlotsByName(PWSlot14)

    # setupUi

    def retranslateUi(self, PWSlot14):
        PWSlot14.setWindowTitle(QCoreApplication.translate("PWSlot14", u"Form", None))
        self.img_slot.setText("")
        self.in_H1.setText(QCoreApplication.translate("PWSlot14", u"H1", None))
        self.in_H0.setText(QCoreApplication.translate("PWSlot14", u"H0", None))
        self.unit_W3.setText(QCoreApplication.translate("PWSlot14", u"m", None))
        self.unit_H3.setText(QCoreApplication.translate("PWSlot14", u"m", None))
        self.unit_W0.setText(QCoreApplication.translate("PWSlot14", u"m", None))
        self.in_H3.setText(QCoreApplication.translate("PWSlot14", u"H3", None))
        self.unit_H0.setText(QCoreApplication.translate("PWSlot14", u"m", None))
        self.in_W3.setText(QCoreApplication.translate("PWSlot14", u"W3", None))
        self.in_W0.setText(QCoreApplication.translate("PWSlot14", u"W0", None))
        self.g_wedge.setTitle(QCoreApplication.translate("PWSlot14", u"Wedge", None))
        self.in_type.setText(QCoreApplication.translate("PWSlot14", u"Type", None))
        self.c_wedge_type.setItemText(
            0, QCoreApplication.translate("PWSlot14", u"Standard", None)
        )

        self.c_wedge_type.setCurrentText(
            QCoreApplication.translate("PWSlot14", u"Standard", None)
        )

    # retranslateUi
