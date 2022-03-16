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

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PWSlot14(object):
    def setupUi(self, PWSlot14):
        if not PWSlot14.objectName():
            PWSlot14.setObjectName("PWSlot14")
        PWSlot14.resize(885, 470)
        PWSlot14.setMinimumSize(QSize(630, 470))
        PWSlot14.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PWSlot14)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_slot = QLabel(PWSlot14)
        self.img_slot.setObjectName("img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(":/images/images/MachineSetup/WSlot/SlotW14.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(PWSlot14)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 446))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_W0 = QLabel(self.scrollAreaWidgetContents)
        self.in_W0.setObjectName("in_W0")

        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)

        self.lf_W0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W0.setObjectName("lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)

        self.unit_W0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W0.setObjectName("unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 0, 2, 1, 1)

        self.in_W3 = QLabel(self.scrollAreaWidgetContents)
        self.in_W3.setObjectName("in_W3")

        self.gridLayout.addWidget(self.in_W3, 1, 0, 1, 1)

        self.lf_W3 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W3.setObjectName("lf_W3")

        self.gridLayout.addWidget(self.lf_W3, 1, 1, 1, 1)

        self.unit_W3 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W3.setObjectName("unit_W3")

        self.gridLayout.addWidget(self.unit_W3, 1, 2, 1, 1)

        self.in_H0 = QLabel(self.scrollAreaWidgetContents)
        self.in_H0.setObjectName("in_H0")

        self.gridLayout.addWidget(self.in_H0, 2, 0, 1, 1)

        self.lf_H0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H0.setObjectName("lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 2, 1, 1, 1)

        self.unit_H0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H0.setObjectName("unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 2, 2, 1, 1)

        self.in_H1 = QLabel(self.scrollAreaWidgetContents)
        self.in_H1.setObjectName("in_H1")

        self.gridLayout.addWidget(self.in_H1, 3, 0, 1, 1)

        self.lf_H1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H1.setObjectName("lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 3, 1, 1, 1)

        self.unit_H1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H1.setObjectName("unit_H1")

        self.gridLayout.addWidget(self.unit_H1, 3, 2, 1, 1)

        self.in_H3 = QLabel(self.scrollAreaWidgetContents)
        self.in_H3.setObjectName("in_H3")

        self.gridLayout.addWidget(self.in_H3, 4, 0, 1, 1)

        self.lf_H3 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H3.setObjectName("lf_H3")

        self.gridLayout.addWidget(self.lf_H3, 4, 1, 1, 1)

        self.unit_H3 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H3.setObjectName("unit_H3")

        self.gridLayout.addWidget(self.unit_H3, 4, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.w_out = WWSlotOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName("w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_W0, self.lf_W3)
        QWidget.setTabOrder(self.lf_W3, self.lf_H0)
        QWidget.setTabOrder(self.lf_H0, self.lf_H1)
        QWidget.setTabOrder(self.lf_H1, self.lf_H3)

        self.retranslateUi(PWSlot14)

        QMetaObject.connectSlotsByName(PWSlot14)

    # setupUi

    def retranslateUi(self, PWSlot14):
        PWSlot14.setWindowTitle(QCoreApplication.translate("PWSlot14", "Form", None))
        self.img_slot.setText("")
        self.in_W0.setText(QCoreApplication.translate("PWSlot14", "W0", None))
        self.unit_W0.setText(QCoreApplication.translate("PWSlot14", "m", None))
        self.in_W3.setText(QCoreApplication.translate("PWSlot14", "W3", None))
        self.unit_W3.setText(QCoreApplication.translate("PWSlot14", "m", None))
        self.in_H0.setText(QCoreApplication.translate("PWSlot14", "H0", None))
        self.unit_H0.setText(QCoreApplication.translate("PWSlot14", "m", None))
        self.in_H1.setText(QCoreApplication.translate("PWSlot14", "H1", None))
        self.unit_H1.setText(QCoreApplication.translate("PWSlot14", "m", None))
        self.in_H3.setText(QCoreApplication.translate("PWSlot14", "H3", None))
        self.unit_H3.setText(QCoreApplication.translate("PWSlot14", "m", None))

    # retranslateUi
