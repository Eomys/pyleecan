# -*- coding: utf-8 -*-

# File generated according to SWindPat.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyleecan.GUI.Tools.HelpButton import HelpButton
from .....GUI.Tools.MPLCanvas import MPLCanvas2

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SWindPat(object):
    def setupUi(self, SWindPat):
        if not SWindPat.objectName():
            SWindPat.setObjectName(u"SWindPat")
        SWindPat.resize(650, 550)
        SWindPat.setMinimumSize(QSize(650, 550))
        self.verticalLayout_4 = QVBoxLayout(SWindPat)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.b_help = HelpButton(SWindPat)
        self.b_help.setObjectName(u"b_help")
        self.b_help.setPixmap(QPixmap(u":/images/images/icon/help_16.png"))

        self.horizontalLayout_2.addWidget(self.b_help)

        self.c_wind_type = QComboBox(SWindPat)
        self.c_wind_type.addItem("")
        self.c_wind_type.addItem("")
        self.c_wind_type.addItem("")
        self.c_wind_type.addItem("")
        self.c_wind_type.addItem("")
        self.c_wind_type.setObjectName(u"c_wind_type")

        self.horizontalLayout_2.addWidget(self.c_wind_type)

        self.in_qs = QLabel(SWindPat)
        self.in_qs.setObjectName(u"in_qs")

        self.horizontalLayout_2.addWidget(self.in_qs)

        self.si_qs = QSpinBox(SWindPat)
        self.si_qs.setObjectName(u"si_qs")

        self.horizontalLayout_2.addWidget(self.si_qs)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.w_viewer = MPLCanvas2(SWindPat)
        self.w_viewer.setObjectName(u"w_viewer")

        self.horizontalLayout_5.addWidget(self.w_viewer)

        self.widget = QWidget(SWindPat)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 0))
        self.widget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.in_coil_pitch = QLabel(self.widget)
        self.in_coil_pitch.setObjectName(u"in_coil_pitch")

        self.horizontalLayout.addWidget(self.in_coil_pitch)

        self.si_coil_pitch = QSpinBox(self.widget)
        self.si_coil_pitch.setObjectName(u"si_coil_pitch")

        self.horizontalLayout.addWidget(self.si_coil_pitch)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.in_Nslot = QLabel(self.widget)
        self.in_Nslot.setObjectName(u"in_Nslot")
        self.in_Nslot.setMinimumSize(QSize(0, 0))
        self.in_Nslot.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.in_Nslot)

        self.si_Nslot = QSpinBox(self.widget)
        self.si_Nslot.setObjectName(u"si_Nslot")
        self.si_Nslot.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_4.addWidget(self.si_Nslot)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.is_reverse = QCheckBox(self.widget)
        self.is_reverse.setObjectName(u"is_reverse")

        self.verticalLayout.addWidget(self.is_reverse)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(200, 200))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.out_shape = QLabel(self.groupBox)
        self.out_shape.setObjectName(u"out_shape")
        self.out_shape.setMinimumSize(QSize(175, 0))

        self.verticalLayout_3.addWidget(self.out_shape)

        self.out_ms = QLabel(self.groupBox)
        self.out_ms.setObjectName(u"out_ms")

        self.verticalLayout_3.addWidget(self.out_ms)

        self.out_Nperw = QLabel(self.groupBox)
        self.out_Nperw.setObjectName(u"out_Nperw")

        self.verticalLayout_3.addWidget(self.out_Nperw)

        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_5.addWidget(self.widget)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.b_preview = QPushButton(SWindPat)
        self.b_preview.setObjectName(u"b_preview")

        self.horizontalLayout_3.addWidget(self.b_preview)

        self.b_previous = QPushButton(SWindPat)
        self.b_previous.setObjectName(u"b_previous")

        self.horizontalLayout_3.addWidget(self.b_previous)

        self.b_next = QPushButton(SWindPat)
        self.b_next.setObjectName(u"b_next")

        self.horizontalLayout_3.addWidget(self.b_next)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SWindPat)

        QMetaObject.connectSlotsByName(SWindPat)

    # setupUi

    def retranslateUi(self, SWindPat):
        SWindPat.setWindowTitle(QCoreApplication.translate("SWindPat", u"Form", None))
        self.b_help.setText("")
        self.c_wind_type.setItemText(
            0,
            QCoreApplication.translate(
                "SWindPat", u"Double Layer Concentrated Orthoradial", None
            ),
        )
        self.c_wind_type.setItemText(
            1,
            QCoreApplication.translate("SWindPat", u"Single Layer Concentrated", None),
        )
        self.c_wind_type.setItemText(
            2, QCoreApplication.translate("SWindPat", u"Double Layer Distributed", None)
        )
        self.c_wind_type.setItemText(
            3, QCoreApplication.translate("SWindPat", u"Single Layer Distributed", None)
        )
        self.c_wind_type.setItemText(
            4,
            QCoreApplication.translate(
                "SWindPat", u"Double Layer Concentrated Radial", None
            ),
        )

        self.in_qs.setText(QCoreApplication.translate("SWindPat", u"qs :", None))
        self.in_coil_pitch.setText(
            QCoreApplication.translate("SWindPat", u"coil_pitch", None)
        )
        self.in_Nslot.setText(
            QCoreApplication.translate("SWindPat", u"Nslot_shift", None)
        )
        self.is_reverse.setText(
            QCoreApplication.translate("SWindPat", u"reverse", None)
        )
        self.groupBox.setTitle(QCoreApplication.translate("SWindPat", u"Output", None))
        self.out_shape.setText(
            QCoreApplication.translate("SWindPat", u"Winding Matrix Shape : ", None)
        )
        self.out_ms.setText(
            QCoreApplication.translate("SWindPat", u"ms = Zs / (2*p*qs) = ?", None)
        )
        # if QT_CONFIG(tooltip)
        self.out_Nperw.setToolTip(
            QCoreApplication.translate("SWindPat", u"Winding periodicity", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.out_Nperw.setText(QCoreApplication.translate("SWindPat", u"Nperw :", None))
        self.b_preview.setText(QCoreApplication.translate("SWindPat", u"Preview", None))
        self.b_previous.setText(
            QCoreApplication.translate("SWindPat", u"Previous", None)
        )
        self.b_next.setText(QCoreApplication.translate("SWindPat", u"Next", None))

    # retranslateUi
