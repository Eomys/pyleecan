# -*- coding: utf-8 -*-

# File generated according to PWSlotUD.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut
from ......GUI.Tools.MPLCanvas import MPLCanvas
from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelectV import WMatSelectV
from ......GUI.Tools.WPathSelector.WPathSelectorV import WPathSelectorV

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PWSlotUD(object):
    def setupUi(self, PWSlotUD):
        if not PWSlotUD.objectName():
            PWSlotUD.setObjectName("PWSlotUD")
        PWSlotUD.resize(641, 440)
        PWSlotUD.setMinimumSize(QSize(0, 440))
        PWSlotUD.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PWSlotUD)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.w_viewer = MPLCanvas(PWSlotUD)
        self.w_viewer.setObjectName("w_viewer")

        self.horizontalLayout.addWidget(self.w_viewer)

        self.scrollArea = QScrollArea(PWSlotUD)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 416))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.b_dxf = QPushButton(self.scrollAreaWidgetContents)
        self.b_dxf.setObjectName("b_dxf")

        self.verticalLayout_2.addWidget(self.b_dxf)

        self.w_path_json = WPathSelectorV(self.scrollAreaWidgetContents)
        self.w_path_json.setObjectName("w_path_json")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_path_json.sizePolicy().hasHeightForWidth())
        self.w_path_json.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.w_path_json)

        self.g_wedge = QGroupBox(self.scrollAreaWidgetContents)
        self.g_wedge.setObjectName("g_wedge")
        self.g_wedge.setCheckable(True)
        self.g_wedge.setChecked(False)
        self.verticalLayout = QVBoxLayout(self.g_wedge)
        self.verticalLayout.setObjectName("verticalLayout")
        self.w_wedge_mat = WMatSelectV(self.g_wedge)
        self.w_wedge_mat.setObjectName("w_wedge_mat")
        self.w_wedge_mat.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.w_wedge_mat)

        self.verticalLayout_2.addWidget(self.g_wedge)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.w_out = WWSlotOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName("w_out")

        self.verticalLayout_2.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(PWSlotUD)

        QMetaObject.connectSlotsByName(PWSlotUD)

    # setupUi

    def retranslateUi(self, PWSlotUD):
        PWSlotUD.setWindowTitle(QCoreApplication.translate("PWSlotUD", "Form", None))
        self.b_dxf.setText(
            QCoreApplication.translate("PWSlotUD", "Define Slot from DXF", None)
        )
        self.g_wedge.setTitle(QCoreApplication.translate("PWSlotUD", "Wedge", None))

    # retranslateUi
