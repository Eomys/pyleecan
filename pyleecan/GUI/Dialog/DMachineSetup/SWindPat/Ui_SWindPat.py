# -*- coding: utf-8 -*-

# File generated according to SWindPat.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SWindPat(object):
    def setupUi(self, SWindPat):
        SWindPat.setObjectName("SWindPat")
        SWindPat.resize(650, 550)
        SWindPat.setMinimumSize(QtCore.QSize(650, 550))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SWindPat)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem)
        self.b_help = HelpButton(SWindPat)
        self.b_help.setText("")
        self.b_help.setPixmap(QtGui.QPixmap(":/images/images/icon/help_16.png"))
        self.b_help.setObjectName("b_help")
        self.horizontalLayout_2.addWidget(self.b_help)
        self.c_wind_type = QtWidgets.QComboBox(SWindPat)
        self.c_wind_type.setObjectName("c_wind_type")
        self.c_wind_type.addItem("")
        self.c_wind_type.addItem("")
        self.c_wind_type.addItem("")
        self.c_wind_type.addItem("")
        self.c_wind_type.addItem("")
        self.horizontalLayout_2.addWidget(self.c_wind_type)
        self.in_qs = QtWidgets.QLabel(SWindPat)
        self.in_qs.setObjectName("in_qs")
        self.horizontalLayout_2.addWidget(self.in_qs)
        self.si_qs = QtWidgets.QSpinBox(SWindPat)
        self.si_qs.setObjectName("si_qs")
        self.horizontalLayout_2.addWidget(self.si_qs)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.img_wind_pat = QtWidgets.QLabel(SWindPat)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_wind_pat.sizePolicy().hasHeightForWidth())
        self.img_wind_pat.setSizePolicy(sizePolicy)
        self.img_wind_pat.setMinimumSize(QtCore.QSize(0, 0))
        self.img_wind_pat.setMaximumSize(QtCore.QSize(16777215, 250))
        self.img_wind_pat.setText("")
        self.img_wind_pat.setPixmap(
            QtGui.QPixmap(":/images/images/MachineSetup/WindingPattern/Type_Wind_6.png")
        )
        self.img_wind_pat.setScaledContents(True)
        self.img_wind_pat.setObjectName("img_wind_pat")
        self.verticalLayout_2.addWidget(self.img_wind_pat)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_coil_pitch = QtWidgets.QLabel(SWindPat)
        self.in_coil_pitch.setObjectName("in_coil_pitch")
        self.horizontalLayout.addWidget(self.in_coil_pitch)
        self.si_coil_pitch = QtWidgets.QSpinBox(SWindPat)
        self.si_coil_pitch.setObjectName("si_coil_pitch")
        self.horizontalLayout.addWidget(self.si_coil_pitch)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.in_Nslot = QtWidgets.QLabel(SWindPat)
        self.in_Nslot.setMinimumSize(QtCore.QSize(0, 0))
        self.in_Nslot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.in_Nslot.setObjectName("in_Nslot")
        self.horizontalLayout_4.addWidget(self.in_Nslot)
        self.si_Nslot = QtWidgets.QSpinBox(SWindPat)
        self.si_Nslot.setMinimumSize(QtCore.QSize(60, 0))
        self.si_Nslot.setObjectName("si_Nslot")
        self.horizontalLayout_4.addWidget(self.si_Nslot)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.is_reverse = QtWidgets.QCheckBox(SWindPat)
        self.is_reverse.setObjectName("is_reverse")
        self.verticalLayout.addWidget(self.is_reverse)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_5.addItem(spacerItem2)
        self.groupBox = QtWidgets.QGroupBox(SWindPat)
        self.groupBox.setMinimumSize(QtCore.QSize(200, 200))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.out_shape = QtWidgets.QLabel(self.groupBox)
        self.out_shape.setMinimumSize(QtCore.QSize(175, 0))
        self.out_shape.setObjectName("out_shape")
        self.verticalLayout_3.addWidget(self.out_shape)
        self.out_ms = QtWidgets.QLabel(self.groupBox)
        self.out_ms.setObjectName("out_ms")
        self.verticalLayout_3.addWidget(self.out_ms)
        self.out_Nperw = QtWidgets.QLabel(self.groupBox)
        self.out_Nperw.setObjectName("out_Nperw")
        self.verticalLayout_3.addWidget(self.out_Nperw)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem4)
        self.b_preview = QtWidgets.QPushButton(SWindPat)
        self.b_preview.setObjectName("b_preview")
        self.horizontalLayout_3.addWidget(self.b_preview)
        self.b_previous = QtWidgets.QPushButton(SWindPat)
        self.b_previous.setObjectName("b_previous")
        self.horizontalLayout_3.addWidget(self.b_previous)
        self.b_next = QtWidgets.QPushButton(SWindPat)
        self.b_next.setObjectName("b_next")
        self.horizontalLayout_3.addWidget(self.b_next)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SWindPat)
        QtCore.QMetaObject.connectSlotsByName(SWindPat)

    def retranslateUi(self, SWindPat):
        _translate = QtCore.QCoreApplication.translate
        SWindPat.setWindowTitle(_translate("SWindPat", "Form"))
        self.c_wind_type.setItemText(
            0, _translate("SWindPat", "Double Layer Concentrated Orthoradial")
        )
        self.c_wind_type.setItemText(
            1, _translate("SWindPat", "Single Layer Concentrated")
        )
        self.c_wind_type.setItemText(
            2, _translate("SWindPat", "Double Layer Distributed")
        )
        self.c_wind_type.setItemText(
            3, _translate("SWindPat", "Single Layer Distributed")
        )
        self.c_wind_type.setItemText(
            4, _translate("SWindPat", "Double Layer Concentrated Radial")
        )
        self.in_qs.setText(_translate("SWindPat", "qs :"))
        self.in_coil_pitch.setText(_translate("SWindPat", "coil_pitch"))
        self.in_Nslot.setText(_translate("SWindPat", "Nslot_shift :"))
        self.is_reverse.setText(_translate("SWindPat", "reverse"))
        self.groupBox.setTitle(_translate("SWindPat", "Output"))
        self.out_shape.setText(_translate("SWindPat", "Winding Matrix Shape : "))
        self.out_ms.setText(_translate("SWindPat", "ms = Zs / (2*p*qs) = ?"))
        self.out_Nperw.setToolTip(_translate("SWindPat", "Winding periodicity"))
        self.out_Nperw.setText(_translate("SWindPat", "Nperw :"))
        self.b_preview.setText(_translate("SWindPat", "Preview"))
        self.b_previous.setText(_translate("SWindPat", "Previous"))
        self.b_next.setText(_translate("SWindPat", "Next"))


from pyleecan.GUI.Tools.HelpButton import HelpButton
from pyleecan.GUI.Resources import pyleecan_rc
