# -*- coding: utf-8 -*-

# File generated according to DXF_Slot.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ...GUI.Tools.WPathSelector.WPathSelector import WPathSelector
from ...GUI.Tools.FloatEdit import FloatEdit
from ...GUI.Tools.MPLCanvas import MPLCanvas2

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DXF_Slot(object):
    def setupUi(self, DXF_Slot):
        if not DXF_Slot.objectName():
            DXF_Slot.setObjectName(u"DXF_Slot")
        DXF_Slot.resize(745, 486)
        self.horizontalLayout = QHBoxLayout(DXF_Slot)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.w_viewer = MPLCanvas2(DXF_Slot)
        self.w_viewer.setObjectName(u"w_viewer")

        self.horizontalLayout.addWidget(self.w_viewer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.in_Zs = QLabel(DXF_Slot)
        self.in_Zs.setObjectName(u"in_Zs")

        self.horizontalLayout_4.addWidget(self.in_Zs)

        self.si_Zs = QSpinBox(DXF_Slot)
        self.si_Zs.setObjectName(u"si_Zs")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.si_Zs.sizePolicy().hasHeightForWidth())
        self.si_Zs.setSizePolicy(sizePolicy)
        self.si_Zs.setMinimum(1)
        self.si_Zs.setMaximum(1000)
        self.si_Zs.setSingleStep(0)
        self.si_Zs.setValue(36)

        self.horizontalLayout_4.addWidget(self.si_Zs)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.in_coord_center = QLabel(DXF_Slot)
        self.in_coord_center.setObjectName(u"in_coord_center")

        self.horizontalLayout_5.addWidget(self.in_coord_center)

        self.lf_center_x = FloatEdit(DXF_Slot)
        self.lf_center_x.setObjectName(u"lf_center_x")
        sizePolicy.setHeightForWidth(self.lf_center_x.sizePolicy().hasHeightForWidth())
        self.lf_center_x.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.lf_center_x)

        self.lf_center_y = FloatEdit(DXF_Slot)
        self.lf_center_y.setObjectName(u"lf_center_y")
        self.lf_center_y.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lf_center_y.sizePolicy().hasHeightForWidth())
        self.lf_center_y.setSizePolicy(sizePolicy)
        self.lf_center_y.setMaximumSize(QSize(137, 16777215))

        self.horizontalLayout_5.addWidget(self.lf_center_y)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.in_axe_angle = QLabel(DXF_Slot)
        self.in_axe_angle.setObjectName(u"in_axe_angle")

        self.horizontalLayout_6.addWidget(self.in_axe_angle)

        self.lf_axe_angle = FloatEdit(DXF_Slot)
        self.lf_axe_angle.setObjectName(u"lf_axe_angle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.lf_axe_angle.sizePolicy().hasHeightForWidth()
        )
        self.lf_axe_angle.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.lf_axe_angle)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.b_plot = QPushButton(DXF_Slot)
        self.b_plot.setObjectName(u"b_plot")

        self.horizontalLayout_2.addWidget(self.b_plot)

        self.b_save = QPushButton(DXF_Slot)
        self.b_save.setObjectName(u"b_save")

        self.horizontalLayout_2.addWidget(self.b_save)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.w_path_selector = WPathSelector(DXF_Slot)
        self.w_path_selector.setObjectName(u"w_path_selector")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.w_path_selector.sizePolicy().hasHeightForWidth()
        )
        self.w_path_selector.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.w_path_selector)

        self.retranslateUi(DXF_Slot)

        QMetaObject.connectSlotsByName(DXF_Slot)

    # setupUi

    def retranslateUi(self, DXF_Slot):
        DXF_Slot.setWindowTitle(
            QCoreApplication.translate("DXF_Slot", u"Material Library", None)
        )
        self.in_Zs.setText(
            QCoreApplication.translate("DXF_Slot", u"Number of slot", None)
        )
        self.in_coord_center.setText(
            QCoreApplication.translate("DXF_Slot", u"Machine center (x,y)", None)
        )
        self.lf_center_x.setText(QCoreApplication.translate("DXF_Slot", u"0", None))
        self.lf_center_y.setText(QCoreApplication.translate("DXF_Slot", u"0", None))
        self.in_axe_angle.setText(
            QCoreApplication.translate("DXF_Slot", u"Slot axe angle shift", None)
        )
        self.lf_axe_angle.setText(QCoreApplication.translate("DXF_Slot", u"0", None))
        self.b_plot.setText(QCoreApplication.translate("DXF_Slot", u"Plot", None))
        self.b_save.setText(QCoreApplication.translate("DXF_Slot", u"Save", None))

    # retranslateUi
