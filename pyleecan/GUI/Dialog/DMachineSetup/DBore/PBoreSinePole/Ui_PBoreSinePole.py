# -*- coding: utf-8 -*-

# File generated according to PBoreSinePole.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.DBore.WBoreOut.WBoreOut import WBoreOut

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PBoreSinePole(object):
    def setupUi(self, PBoreSinePole):
        if not PBoreSinePole.objectName():
            PBoreSinePole.setObjectName(u"PBoreSinePole")
        PBoreSinePole.resize(899, 470)
        PBoreSinePole.setMinimumSize(QSize(630, 470))
        PBoreSinePole.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PBoreSinePole)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_bore = QLabel(PBoreSinePole)
        self.img_bore.setObjectName(u"img_bore")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_bore.sizePolicy().hasHeightForWidth())
        self.img_bore.setSizePolicy(sizePolicy)
        self.img_bore.setMaximumSize(QSize(16777215, 16777215))
        self.img_bore.setPixmap(
            QPixmap(u":/images/images/MachineSetup/LamParam/BoreSinePole.png")
        )
        self.img_bore.setScaledContents(False)
        self.img_bore.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.img_bore)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(PBoreSinePole)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 446))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.unit_N = QLabel(self.scrollAreaWidgetContents)
        self.unit_N.setObjectName(u"unit_N")

        self.gridLayout.addWidget(self.unit_N, 0, 2, 1, 1)

        self.unit_k = QLabel(self.scrollAreaWidgetContents)
        self.unit_k.setObjectName(u"unit_k")

        self.gridLayout.addWidget(self.unit_k, 2, 2, 1, 1)

        self.si_N = QSpinBox(self.scrollAreaWidgetContents)
        self.si_N.setObjectName(u"si_N")
        self.si_N.setMinimum(1)
        self.si_N.setMaximum(999999)
        self.si_N.setValue(1)

        self.gridLayout.addWidget(self.si_N, 0, 1, 1, 1)

        self.in_W0 = QLabel(self.scrollAreaWidgetContents)
        self.in_W0.setObjectName(u"in_W0")

        self.gridLayout.addWidget(self.in_W0, 1, 0, 1, 1)

        self.unit_W0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W0.setObjectName(u"unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 1, 2, 1, 1)

        self.lf_W0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W0.setObjectName(u"lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 1, 1, 1, 1)

        self.in_delta_q = QLabel(self.scrollAreaWidgetContents)
        self.in_delta_q.setObjectName(u"in_delta_q")

        self.gridLayout.addWidget(self.in_delta_q, 4, 0, 1, 1)

        self.in_delta_d = QLabel(self.scrollAreaWidgetContents)
        self.in_delta_d.setObjectName(u"in_delta_d")

        self.gridLayout.addWidget(self.in_delta_d, 3, 0, 1, 1)

        self.in_k = QLabel(self.scrollAreaWidgetContents)
        self.in_k.setObjectName(u"in_k")

        self.gridLayout.addWidget(self.in_k, 2, 0, 1, 1)

        self.lf_delta_q = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_delta_q.setObjectName(u"lf_delta_q")

        self.gridLayout.addWidget(self.lf_delta_q, 4, 1, 1, 1)

        self.in_N = QLabel(self.scrollAreaWidgetContents)
        self.in_N.setObjectName(u"in_N")

        self.gridLayout.addWidget(self.in_N, 0, 0, 1, 1)

        self.lf_delta_d = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_delta_d.setObjectName(u"lf_delta_d")

        self.gridLayout.addWidget(self.lf_delta_d, 3, 1, 1, 1)

        self.lf_k = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_k.setObjectName(u"lf_k")

        self.gridLayout.addWidget(self.lf_k, 2, 1, 1, 1)

        self.unit_delta_d = QLabel(self.scrollAreaWidgetContents)
        self.unit_delta_d.setObjectName(u"unit_delta_d")

        self.gridLayout.addWidget(self.unit_delta_d, 3, 2, 1, 1)

        self.unit_delta_q = QLabel(self.scrollAreaWidgetContents)
        self.unit_delta_q.setObjectName(u"unit_delta_q")

        self.gridLayout.addWidget(self.unit_delta_q, 4, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.w_out = WBoreOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(PBoreSinePole)

        QMetaObject.connectSlotsByName(PBoreSinePole)

    # setupUi

    def retranslateUi(self, PBoreSinePole):
        PBoreSinePole.setWindowTitle(
            QCoreApplication.translate("PBoreSinePole", u"Form", None)
        )
        self.img_bore.setText("")
        self.unit_N.setText("")
        self.unit_k.setText("")
        self.in_W0.setText(QCoreApplication.translate("PBoreSinePole", u"W0", None))
        self.unit_W0.setText(QCoreApplication.translate("PBoreSinePole", u"[m]", None))
        self.in_delta_q.setText(
            QCoreApplication.translate("PBoreSinePole", u"delta_q", None)
        )
        self.in_delta_d.setText(
            QCoreApplication.translate("PBoreSinePole", u"delta_d", None)
        )
        self.in_k.setText(QCoreApplication.translate("PBoreSinePole", u"k", None))
        self.in_N.setText(QCoreApplication.translate("PBoreSinePole", u"N", None))
        self.unit_delta_d.setText(
            QCoreApplication.translate("PBoreSinePole", u"[m]", None)
        )
        self.unit_delta_q.setText(
            QCoreApplication.translate("PBoreSinePole", u"[m]", None)
        )

    # retranslateUi
