# -*- coding: utf-8 -*-

# File generated according to DXF.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ...GUI.Tools.WPathSelector.WPathSelector import WPathSelector
from ...GUI.Tools.FloatEdit import FloatEdit

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DXF(object):
    def setupUi(self, DXF):
        if not DXF.objectName():
            DXF.setObjectName(u"DXF")
        DXF.resize(745, 486)
        self.main_layout = QHBoxLayout(DXF)
        self.main_layout.setObjectName(u"main_layout")
        self.w_viewer = QWidget(DXF)
        self.w_viewer.setObjectName(u"w_viewer")

        self.main_layout.addWidget(self.w_viewer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.w_path_selector = WPathSelector(DXF)
        self.w_path_selector.setObjectName(u"w_path_selector")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.w_path_selector.sizePolicy().hasHeightForWidth()
        )
        self.w_path_selector.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.w_path_selector)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.in_zh = QLabel(DXF)
        self.in_zh.setObjectName(u"in_zh")

        self.horizontalLayout_4.addWidget(self.in_zh)

        self.si_Zh = QSpinBox(DXF)
        self.si_Zh.setObjectName(u"si_Zh")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.si_Zh.sizePolicy().hasHeightForWidth())
        self.si_Zh.setSizePolicy(sizePolicy1)
        self.si_Zh.setMinimum(1)
        self.si_Zh.setMaximum(1000)
        self.si_Zh.setSingleStep(0)
        self.si_Zh.setValue(36)

        self.horizontalLayout_4.addWidget(self.si_Zh)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.in_mag_len = QLabel(DXF)
        self.in_mag_len.setObjectName(u"in_mag_len")

        self.horizontalLayout_3.addWidget(self.in_mag_len)

        self.lf_mag_len = FloatEdit(DXF)
        self.lf_mag_len.setObjectName(u"lf_mag_len")
        sizePolicy1.setHeightForWidth(self.lf_mag_len.sizePolicy().hasHeightForWidth())
        self.lf_mag_len.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.lf_mag_len)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.in_coord_center = QLabel(DXF)
        self.in_coord_center.setObjectName(u"in_coord_center")

        self.horizontalLayout_5.addWidget(self.in_coord_center)

        self.lf_center_x = FloatEdit(DXF)
        self.lf_center_x.setObjectName(u"lf_center_x")
        sizePolicy1.setHeightForWidth(self.lf_center_x.sizePolicy().hasHeightForWidth())
        self.lf_center_x.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.lf_center_x)

        self.lf_center_y = FloatEdit(DXF)
        self.lf_center_y.setObjectName(u"lf_center_y")
        self.lf_center_y.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lf_center_y.sizePolicy().hasHeightForWidth())
        self.lf_center_y.setSizePolicy(sizePolicy1)
        self.lf_center_y.setMaximumSize(QSize(137, 16777215))

        self.horizontalLayout_5.addWidget(self.lf_center_y)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.in_axe_angle = QLabel(DXF)
        self.in_axe_angle.setObjectName(u"in_axe_angle")

        self.horizontalLayout_6.addWidget(self.in_axe_angle)

        self.lf_axe_angle = FloatEdit(DXF)
        self.lf_axe_angle.setObjectName(u"lf_axe_angle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.lf_axe_angle.sizePolicy().hasHeightForWidth()
        )
        self.lf_axe_angle.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.lf_axe_angle)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.w_surface_list = QTableWidget(DXF)
        self.w_surface_list.setObjectName(u"w_surface_list")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.w_surface_list.sizePolicy().hasHeightForWidth()
        )
        self.w_surface_list.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.w_surface_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.b_plot = QPushButton(DXF)
        self.b_plot.setObjectName(u"b_plot")

        self.horizontalLayout_2.addWidget(self.b_plot)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.b_save = QPushButton(DXF)
        self.b_save.setObjectName(u"b_save")

        self.horizontalLayout_2.addWidget(self.b_save)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.main_layout.addLayout(self.verticalLayout)

        self.retranslateUi(DXF)

        QMetaObject.connectSlotsByName(DXF)

    # setupUi

    def retranslateUi(self, DXF):
        DXF.setWindowTitle(QCoreApplication.translate("DXF", u"Material Library", None))
        self.in_zh.setText(QCoreApplication.translate("DXF", u"Number of hole", None))
        self.in_mag_len.setText(
            QCoreApplication.translate("DXF", u"Magnet length", None)
        )
        self.lf_mag_len.setText(QCoreApplication.translate("DXF", u"1", None))
        self.in_coord_center.setText(
            QCoreApplication.translate("DXF", u"Machine center (x,y)", None)
        )
        self.lf_center_x.setText(QCoreApplication.translate("DXF", u"0", None))
        self.lf_center_y.setText(QCoreApplication.translate("DXF", u"0", None))
        self.in_axe_angle.setText(
            QCoreApplication.translate("DXF", u"Hole main axe angle", None)
        )
        self.lf_axe_angle.setText(QCoreApplication.translate("DXF", u"0", None))
        self.b_plot.setText(QCoreApplication.translate("DXF", u"Plot", None))
        self.b_save.setText(QCoreApplication.translate("DXF", u"Save", None))

    # retranslateUi
