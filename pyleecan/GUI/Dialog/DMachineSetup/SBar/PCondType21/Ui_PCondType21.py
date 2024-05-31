# -*- coding: utf-8 -*-

# File generated according to PCondType21.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelectV import WMatSelectV
from ......GUI.Dialog.DMachineSetup.SBar.WBarOut.WBarOut import WBarOut


class Ui_PCondType21(object):
    def setupUi(self, PCondType21):
        if not PCondType21.objectName():
            PCondType21.setObjectName("PCondType21")
        PCondType21.resize(360, 124)
        self.verticalLayout = QVBoxLayout(PCondType21)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lf_Hbar = FloatEdit(PCondType21)
        self.lf_Hbar.setObjectName("lf_Hbar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lf_Hbar.sizePolicy().hasHeightForWidth())
        self.lf_Hbar.setSizePolicy(sizePolicy)
        self.lf_Hbar.setMinimumSize(QSize(70, 0))
        self.lf_Hbar.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_Hbar, 0, 1, 1, 1)

        self.in_Hbar = QLabel(PCondType21)
        self.in_Hbar.setObjectName("in_Hbar")
        sizePolicy.setHeightForWidth(self.in_Hbar.sizePolicy().hasHeightForWidth())
        self.in_Hbar.setSizePolicy(sizePolicy)
        self.in_Hbar.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.in_Hbar, 0, 0, 1, 1)

        self.unit_Hbar = QLabel(PCondType21)
        self.unit_Hbar.setObjectName("unit_Hbar")
        self.unit_Hbar.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.unit_Hbar, 0, 2, 1, 1)

        self.lf_Wbar = FloatEdit(PCondType21)
        self.lf_Wbar.setObjectName("lf_Wbar")
        sizePolicy.setHeightForWidth(self.lf_Wbar.sizePolicy().hasHeightForWidth())
        self.lf_Wbar.setSizePolicy(sizePolicy)
        self.lf_Wbar.setMinimumSize(QSize(70, 0))
        self.lf_Wbar.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_Wbar, 1, 1, 1, 1)

        self.unit_Wbar = QLabel(PCondType21)
        self.unit_Wbar.setObjectName("unit_Wbar")
        self.unit_Wbar.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.unit_Wbar, 1, 2, 1, 1)

        self.in_Wbar = QLabel(PCondType21)
        self.in_Wbar.setObjectName("in_Wbar")
        self.in_Wbar.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.in_Wbar, 1, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.w_mat = WMatSelectV(PCondType21)
        self.w_mat.setObjectName("w_mat")
        self.w_mat.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.w_mat)

        self.w_out = WBarOut(PCondType21)
        self.w_out.setObjectName("w_out")

        self.verticalLayout.addWidget(self.w_out)

        QWidget.setTabOrder(self.lf_Hbar, self.lf_Wbar)

        self.retranslateUi(PCondType21)

        QMetaObject.connectSlotsByName(PCondType21)

    # setupUi

    def retranslateUi(self, PCondType21):
        PCondType21.setWindowTitle(
            QCoreApplication.translate("PCondType21", "Form", None)
        )
        self.in_Hbar.setText(QCoreApplication.translate("PCondType21", "Hbar :", None))
        self.unit_Hbar.setText(QCoreApplication.translate("PCondType21", "m", None))
        self.unit_Wbar.setText(QCoreApplication.translate("PCondType21", "m", None))
        self.in_Wbar.setText(QCoreApplication.translate("PCondType21", "Wbar :", None))

    # retranslateUi
