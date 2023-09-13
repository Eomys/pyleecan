# -*- coding: utf-8 -*-

# File generated according to PHoleM57.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PHoleM57(object):
    def setupUi(self, PHoleM57):
        if not PHoleM57.objectName():
            PHoleM57.setObjectName(u"PHoleM57")
        PHoleM57.resize(1164, 491)
        PHoleM57.setMinimumSize(QSize(0, 0))
        PHoleM57.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PHoleM57)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.img_slot = QLabel(PHoleM57)
        self.img_slot.setObjectName(u"img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMinimumSize(QSize(0, 0))
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(u":/images/images/MachineSetup/SMHoleMag/HoleM57.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.img_slot)

        self.scrollArea = QScrollArea(PHoleM57)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 467))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lf_W3 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W3.setObjectName(u"lf_W3")

        self.gridLayout.addWidget(self.lf_W3, 5, 1, 1, 1)

        self.lf_W0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W0.setObjectName(u"lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 2, 1, 1, 1)

        self.in_W1 = QLabel(self.scrollAreaWidgetContents)
        self.in_W1.setObjectName(u"in_W1")

        self.gridLayout.addWidget(self.in_W1, 3, 0, 1, 1)

        self.lf_H2 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H2.setObjectName(u"lf_H2")

        self.gridLayout.addWidget(self.lf_H2, 1, 1, 1, 1)

        self.unit_W1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W1.setObjectName(u"unit_W1")

        self.gridLayout.addWidget(self.unit_W1, 3, 2, 1, 1)

        self.lf_H1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H1.setObjectName(u"lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 0, 1, 1, 1)

        self.unit_W2 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W2.setObjectName(u"unit_W2")

        self.gridLayout.addWidget(self.unit_W2, 4, 2, 1, 1)

        self.in_W3 = QLabel(self.scrollAreaWidgetContents)
        self.in_W3.setObjectName(u"in_W3")

        self.gridLayout.addWidget(self.in_W3, 5, 0, 1, 1)

        self.unit_W4 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W4.setObjectName(u"unit_W4")

        self.gridLayout.addWidget(self.unit_W4, 6, 2, 1, 1)

        self.lf_W4 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W4.setObjectName(u"lf_W4")

        self.gridLayout.addWidget(self.lf_W4, 6, 1, 1, 1)

        self.unit_W0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W0.setObjectName(u"unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 2, 2, 1, 1)

        self.in_W2 = QLabel(self.scrollAreaWidgetContents)
        self.in_W2.setObjectName(u"in_W2")

        self.gridLayout.addWidget(self.in_W2, 4, 0, 1, 1)

        self.in_W0 = QLabel(self.scrollAreaWidgetContents)
        self.in_W0.setObjectName(u"in_W0")

        self.gridLayout.addWidget(self.in_W0, 2, 0, 1, 1)

        self.in_W4 = QLabel(self.scrollAreaWidgetContents)
        self.in_W4.setObjectName(u"in_W4")

        self.gridLayout.addWidget(self.in_W4, 6, 0, 1, 1)

        self.unit_H1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H1.setObjectName(u"unit_H1")

        self.gridLayout.addWidget(self.unit_H1, 0, 2, 1, 1)

        self.in_H2 = QLabel(self.scrollAreaWidgetContents)
        self.in_H2.setObjectName(u"in_H2")

        self.gridLayout.addWidget(self.in_H2, 1, 0, 1, 1)

        self.lf_W2 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W2.setObjectName(u"lf_W2")

        self.gridLayout.addWidget(self.lf_W2, 4, 1, 1, 1)

        self.in_H1 = QLabel(self.scrollAreaWidgetContents)
        self.in_H1.setObjectName(u"in_H1")

        self.gridLayout.addWidget(self.in_H1, 0, 0, 1, 1)

        self.unit_W3 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W3.setObjectName(u"unit_W3")

        self.gridLayout.addWidget(self.unit_W3, 5, 2, 1, 1)

        self.lf_W1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W1.setObjectName(u"lf_W1")

        self.gridLayout.addWidget(self.lf_W1, 3, 1, 1, 1)

        self.unit_H2 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H2.setObjectName(u"unit_H2")

        self.gridLayout.addWidget(self.unit_H2, 1, 2, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.w_mat_0 = WMatSelect(self.scrollAreaWidgetContents)
        self.w_mat_0.setObjectName(u"w_mat_0")
        self.w_mat_0.setMinimumSize(QSize(100, 0))

        self.verticalLayout_3.addWidget(self.w_mat_0)

        self.w_mat_1 = WMatSelect(self.scrollAreaWidgetContents)
        self.w_mat_1.setObjectName(u"w_mat_1")
        self.w_mat_1.setMinimumSize(QSize(100, 0))

        self.verticalLayout_3.addWidget(self.w_mat_1)

        self.w_mat_2 = WMatSelect(self.scrollAreaWidgetContents)
        self.w_mat_2.setObjectName(u"w_mat_2")
        self.w_mat_2.setMinimumSize(QSize(100, 0))

        self.verticalLayout_3.addWidget(self.w_mat_2)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.g_output = QGroupBox(self.scrollAreaWidgetContents)
        self.g_output.setObjectName(u"g_output")
        self.g_output.setMinimumSize(QSize(200, 0))
        self.verticalLayout = QVBoxLayout(self.g_output)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.out_slot_surface = QLabel(self.g_output)
        self.out_slot_surface.setObjectName(u"out_slot_surface")

        self.verticalLayout.addWidget(self.out_slot_surface)

        self.out_magnet_surface = QLabel(self.g_output)
        self.out_magnet_surface.setObjectName(u"out_magnet_surface")

        self.verticalLayout.addWidget(self.out_magnet_surface)

        self.verticalLayout_3.addWidget(self.g_output)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_H1, self.lf_H2)
        QWidget.setTabOrder(self.lf_H2, self.lf_W0)
        QWidget.setTabOrder(self.lf_W0, self.lf_W1)
        QWidget.setTabOrder(self.lf_W1, self.lf_W2)
        QWidget.setTabOrder(self.lf_W2, self.lf_W3)
        QWidget.setTabOrder(self.lf_W3, self.lf_W4)

        self.retranslateUi(PHoleM57)

        QMetaObject.connectSlotsByName(PHoleM57)

    # setupUi

    def retranslateUi(self, PHoleM57):
        PHoleM57.setWindowTitle(QCoreApplication.translate("PHoleM57", u"Form", None))
        self.img_slot.setText("")
        self.in_W1.setText(QCoreApplication.translate("PHoleM57", u"W1", None))
        self.unit_W1.setText(QCoreApplication.translate("PHoleM57", u"m", None))
        self.unit_W2.setText(QCoreApplication.translate("PHoleM57", u"m", None))
        self.in_W3.setText(QCoreApplication.translate("PHoleM57", u"W3", None))
        self.unit_W4.setText(QCoreApplication.translate("PHoleM57", u"m", None))
        self.lf_W4.setText("")
        self.unit_W0.setText(QCoreApplication.translate("PHoleM57", u"[rad]", None))
        self.in_W2.setText(QCoreApplication.translate("PHoleM57", u"W2", None))
        self.in_W0.setText(QCoreApplication.translate("PHoleM57", u"W0", None))
        self.in_W4.setText(QCoreApplication.translate("PHoleM57", u"W4", None))
        self.unit_H1.setText(QCoreApplication.translate("PHoleM57", u"m", None))
        self.in_H2.setText(QCoreApplication.translate("PHoleM57", u"H2", None))
        self.in_H1.setText(QCoreApplication.translate("PHoleM57", u"H1", None))
        self.unit_W3.setText(QCoreApplication.translate("PHoleM57", u"m", None))
        self.unit_H2.setText(QCoreApplication.translate("PHoleM57", u"m", None))
        self.g_output.setTitle(QCoreApplication.translate("PHoleM57", u"Output", None))
        self.out_slot_surface.setText(
            QCoreApplication.translate("PHoleM57", u"Slot suface (2 part) : ?", None)
        )
        self.out_magnet_surface.setText(
            QCoreApplication.translate("PHoleM57", u"Single Magnet surface : ?", None)
        )

    # retranslateUi
