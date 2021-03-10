# -*- coding: utf-8 -*-

# File generated according to DXF_Hole.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ...GUI.Tools.WPathSelector.WPathSelector import WPathSelector
from ...GUI.Tools.MPLCanvas import MPLCanvas2
from ...GUI.Tools.FloatEdit import FloatEdit

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DXF_Hole(object):
    def setupUi(self, DXF_Hole):
        if not DXF_Hole.objectName():
            DXF_Hole.setObjectName(u"DXF_Hole")
        DXF_Hole.resize(653, 360)
        icon = QIcon()
        icon.addFile(
            u":/images/images/icon/pyleecan_64.png", QSize(), QIcon.Normal, QIcon.Off
        )
        DXF_Hole.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(DXF_Hole)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.w_viewer = MPLCanvas2(DXF_Hole)
        self.w_viewer.setObjectName(u"w_viewer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_viewer.sizePolicy().hasHeightForWidth())
        self.w_viewer.setSizePolicy(sizePolicy)
        self.w_viewer.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.w_viewer)

        self.w_side = QWidget(DXF_Hole)
        self.w_side.setObjectName(u"w_side")
        self.w_side.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout = QVBoxLayout(self.w_side)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.w_path_selector = WPathSelector(self.w_side)
        self.w_path_selector.setObjectName(u"w_path_selector")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.w_path_selector.sizePolicy().hasHeightForWidth()
        )
        self.w_path_selector.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.w_path_selector)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.in_zh = QLabel(self.w_side)
        self.in_zh.setObjectName(u"in_zh")

        self.gridLayout.addWidget(self.in_zh, 0, 0, 1, 1)

        self.si_Zh = QSpinBox(self.w_side)
        self.si_Zh.setObjectName(u"si_Zh")
        sizePolicy.setHeightForWidth(self.si_Zh.sizePolicy().hasHeightForWidth())
        self.si_Zh.setSizePolicy(sizePolicy)
        self.si_Zh.setMinimum(1)
        self.si_Zh.setMaximum(1000)
        self.si_Zh.setSingleStep(0)
        self.si_Zh.setValue(36)

        self.gridLayout.addWidget(self.si_Zh, 0, 1, 1, 1)

        self.in_mag_len = QLabel(self.w_side)
        self.in_mag_len.setObjectName(u"in_mag_len")

        self.gridLayout.addWidget(self.in_mag_len, 1, 0, 1, 1)

        self.lf_mag_len = FloatEdit(self.w_side)
        self.lf_mag_len.setObjectName(u"lf_mag_len")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lf_mag_len.sizePolicy().hasHeightForWidth())
        self.lf_mag_len.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lf_mag_len, 1, 1, 1, 1)

        self.in_axe_angle = QLabel(self.w_side)
        self.in_axe_angle.setObjectName(u"in_axe_angle")

        self.gridLayout.addWidget(self.in_axe_angle, 2, 0, 1, 1)

        self.lf_axe_angle = FloatEdit(self.w_side)
        self.lf_axe_angle.setObjectName(u"lf_axe_angle")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.lf_axe_angle.sizePolicy().hasHeightForWidth()
        )
        self.lf_axe_angle.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.lf_axe_angle, 2, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.in_coord_center = QLabel(self.w_side)
        self.in_coord_center.setObjectName(u"in_coord_center")

        self.horizontalLayout_5.addWidget(self.in_coord_center)

        self.lf_center_x = FloatEdit(self.w_side)
        self.lf_center_x.setObjectName(u"lf_center_x")
        sizePolicy2.setHeightForWidth(self.lf_center_x.sizePolicy().hasHeightForWidth())
        self.lf_center_x.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.lf_center_x)

        self.lf_center_y = FloatEdit(self.w_side)
        self.lf_center_y.setObjectName(u"lf_center_y")
        self.lf_center_y.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.lf_center_y.sizePolicy().hasHeightForWidth())
        self.lf_center_y.setSizePolicy(sizePolicy2)
        self.lf_center_y.setMaximumSize(QSize(137, 16777215))

        self.horizontalLayout_5.addWidget(self.lf_center_y)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.w_surface_list = QTableWidget(self.w_side)
        self.w_surface_list.setObjectName(u"w_surface_list")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.w_surface_list.sizePolicy().hasHeightForWidth()
        )
        self.w_surface_list.setSizePolicy(sizePolicy4)
        self.w_surface_list.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.w_surface_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.b_plot = QPushButton(self.w_side)
        self.b_plot.setObjectName(u"b_plot")

        self.horizontalLayout_2.addWidget(self.b_plot)

        self.b_save = QPushButton(self.w_side)
        self.b_save.setObjectName(u"b_save")

        self.horizontalLayout_2.addWidget(self.b_save)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout.addWidget(self.w_side)

        self.retranslateUi(DXF_Hole)

        QMetaObject.connectSlotsByName(DXF_Hole)

    # setupUi

    def retranslateUi(self, DXF_Hole):
        DXF_Hole.setWindowTitle(
            QCoreApplication.translate("DXF_Hole", u"Define Hole from DXF", None)
        )
        self.in_zh.setText(
            QCoreApplication.translate("DXF_Hole", u"Number of hole", None)
        )
        self.in_mag_len.setText(
            QCoreApplication.translate("DXF_Hole", u"Magnet length", None)
        )
        self.lf_mag_len.setText(QCoreApplication.translate("DXF_Hole", u"1", None))
        self.in_axe_angle.setText(
            QCoreApplication.translate("DXF_Hole", u"Hole main axe angle", None)
        )
        self.lf_axe_angle.setText(QCoreApplication.translate("DXF_Hole", u"0", None))
        self.in_coord_center.setText(
            QCoreApplication.translate("DXF_Hole", u"Machine center (x,y)", None)
        )
        self.lf_center_x.setText(QCoreApplication.translate("DXF_Hole", u"0", None))
        self.lf_center_y.setText(QCoreApplication.translate("DXF_Hole", u"0", None))
        self.b_plot.setText(QCoreApplication.translate("DXF_Hole", u"Plot", None))
        self.b_save.setText(QCoreApplication.translate("DXF_Hole", u"Save", None))

    # retranslateUi
