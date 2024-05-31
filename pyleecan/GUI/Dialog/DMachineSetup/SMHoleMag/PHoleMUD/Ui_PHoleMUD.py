# -*- coding: utf-8 -*-

# File generated according to PHoleMUD.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Tools.WPathSelector.WPathSelectorV import WPathSelectorV
from ......GUI.Tools.MPLCanvas import MPLCanvas
from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PHoleMUD(object):
    def setupUi(self, PHoleMUD):
        if not PHoleMUD.objectName():
            PHoleMUD.setObjectName("PHoleMUD")
        PHoleMUD.resize(1103, 588)
        PHoleMUD.setMinimumSize(QSize(740, 440))
        PHoleMUD.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PHoleMUD)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.w_viewer = MPLCanvas(PHoleMUD)
        self.w_viewer.setObjectName("w_viewer")

        self.horizontalLayout.addWidget(self.w_viewer)

        self.scrollArea = QScrollArea(PHoleMUD)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 564))
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

        self.g_mat = QGroupBox(self.scrollAreaWidgetContents)
        self.g_mat.setObjectName("g_mat")
        self.g_mat_layout = QVBoxLayout(self.g_mat)
        self.g_mat_layout.setObjectName("g_mat_layout")
        self.w_mat_0 = WMatSelect(self.g_mat)
        self.w_mat_0.setObjectName("w_mat_0")
        self.w_mat_0.setMinimumSize(QSize(100, 0))

        self.g_mat_layout.addWidget(self.w_mat_0)

        self.verticalLayout_2.addWidget(self.g_mat)

        self.verticalSpacer = QSpacerItem(
            20, 179, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.g_output = QGroupBox(self.scrollAreaWidgetContents)
        self.g_output.setObjectName("g_output")
        self.g_output.setMinimumSize(QSize(200, 0))
        self.verticalLayout = QVBoxLayout(self.g_output)
        self.verticalLayout.setObjectName("verticalLayout")
        self.out_slot_surface = QLabel(self.g_output)
        self.out_slot_surface.setObjectName("out_slot_surface")

        self.verticalLayout.addWidget(self.out_slot_surface)

        self.out_magnet_surface = QLabel(self.g_output)
        self.out_magnet_surface.setObjectName("out_magnet_surface")

        self.verticalLayout.addWidget(self.out_magnet_surface)

        self.out_Rmin = QLabel(self.g_output)
        self.out_Rmin.setObjectName("out_Rmin")

        self.verticalLayout.addWidget(self.out_Rmin)

        self.out_Rmax = QLabel(self.g_output)
        self.out_Rmax.setObjectName("out_Rmax")

        self.verticalLayout.addWidget(self.out_Rmax)

        self.verticalLayout_2.addWidget(self.g_output)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(PHoleMUD)

        QMetaObject.connectSlotsByName(PHoleMUD)

    # setupUi

    def retranslateUi(self, PHoleMUD):
        PHoleMUD.setWindowTitle(QCoreApplication.translate("PHoleMUD", "Form", None))
        self.b_dxf.setText(
            QCoreApplication.translate("PHoleMUD", "Define Hole from DXF", None)
        )
        self.g_mat.setTitle(QCoreApplication.translate("PHoleMUD", "Materials", None))
        self.g_output.setTitle(QCoreApplication.translate("PHoleMUD", "Output", None))
        self.out_slot_surface.setText(
            QCoreApplication.translate("PHoleMUD", "Hole full surface : ?", None)
        )
        self.out_magnet_surface.setText(
            QCoreApplication.translate("PHoleMUD", "Hole magnet surface : ?", None)
        )
        self.out_Rmin.setText(QCoreApplication.translate("PHoleMUD", "Rmin : ?", None))
        self.out_Rmax.setText(QCoreApplication.translate("PHoleMUD", "Rmax : ?", None))

    # retranslateUi
