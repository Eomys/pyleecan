# -*- coding: utf-8 -*-

# File generated according to SPreview.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from .....GUI.Dialog.DMachineSetup.SPreview.WMachineTable.WMachineTable import (
    WMachineTable,
)
from .....GUI.Tools.MPLCanvas import MPLCanvas

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SPreview(object):
    def setupUi(self, SPreview):
        if not SPreview.objectName():
            SPreview.setObjectName("SPreview")
        SPreview.resize(532, 450)
        SPreview.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(SPreview)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.w_plot = MPLCanvas(SPreview)
        self.w_plot.setObjectName("w_plot")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_plot.sizePolicy().hasHeightForWidth())
        self.w_plot.setSizePolicy(sizePolicy)
        self.w_plot.setMinimumSize(QSize(300, 300))
        self.w_plot.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.w_plot)

        self.tab_machine = WMachineTable(SPreview)
        self.tab_machine.setObjectName("tab_machine")

        self.horizontalLayout_2.addWidget(self.tab_machine)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.b_previous = QPushButton(SPreview)
        self.b_previous.setObjectName("b_previous")

        self.horizontalLayout.addWidget(self.b_previous)

        self.b_next = QPushButton(SPreview)
        self.b_next.setObjectName("b_next")

        self.horizontalLayout.addWidget(self.b_next)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SPreview)

        QMetaObject.connectSlotsByName(SPreview)

    # setupUi

    def retranslateUi(self, SPreview):
        SPreview.setWindowTitle(QCoreApplication.translate("SPreview", "Form", None))
        self.b_previous.setText(
            QCoreApplication.translate("SPreview", "Previous", None)
        )
        self.b_next.setText(QCoreApplication.translate("SPreview", "Next", None))

    # retranslateUi
