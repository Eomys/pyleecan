# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Raphael\Desktop\Git\PyManatee\pyleecan\GUI\Dialog\DMachineSetup\SWindParam\SWindParam.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SWindParam(object):
    def setupUi(self, SWindParam):
        SWindParam.setObjectName("SWindParam")
        SWindParam.resize(650, 550)
        SWindParam.setMinimumSize(QtCore.QSize(650, 550))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(SWindParam)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.img_wind_geo = QtWidgets.QLabel(SWindParam)
        self.img_wind_geo.setMinimumSize(QtCore.QSize(300, 300))
        self.img_wind_geo.setText("")
        self.img_wind_geo.setPixmap(
            QtGui.QPixmap(":/images/images/MachineSetup/WindParam/Winding param.PNG")
        )
        self.img_wind_geo.setScaledContents(True)
        self.img_wind_geo.setObjectName("img_wind_geo")
        self.horizontalLayout_3.addWidget(self.img_wind_geo)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_Npcpp = QtWidgets.QLabel(SWindParam)
        self.in_Npcpp.setMinimumSize(QtCore.QSize(40, 0))
        self.in_Npcpp.setObjectName("in_Npcpp")
        self.horizontalLayout.addWidget(self.in_Npcpp)
        self.si_Npcpp = QtWidgets.QSpinBox(SWindParam)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.si_Npcpp.sizePolicy().hasHeightForWidth())
        self.si_Npcpp.setSizePolicy(sizePolicy)
        self.si_Npcpp.setMinimumSize(QtCore.QSize(100, 0))
        self.si_Npcpp.setMaximumSize(QtCore.QSize(100, 16777215))
        self.si_Npcpp.setProperty("value", 99)
        self.si_Npcpp.setObjectName("si_Npcpp")
        self.horizontalLayout.addWidget(self.si_Npcpp)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.in_Ntcoil = QtWidgets.QLabel(SWindParam)
        self.in_Ntcoil.setMinimumSize(QtCore.QSize(40, 0))
        self.in_Ntcoil.setObjectName("in_Ntcoil")
        self.horizontalLayout_2.addWidget(self.in_Ntcoil)
        self.si_Ntcoil = QtWidgets.QSpinBox(SWindParam)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.si_Ntcoil.sizePolicy().hasHeightForWidth())
        self.si_Ntcoil.setSizePolicy(sizePolicy)
        self.si_Ntcoil.setMinimumSize(QtCore.QSize(100, 0))
        self.si_Ntcoil.setMaximumSize(QtCore.QSize(100, 16777215))
        self.si_Ntcoil.setProperty("value", 99)
        self.si_Ntcoil.setObjectName("si_Ntcoil")
        self.horizontalLayout_2.addWidget(self.si_Ntcoil)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.in_qs = QtWidgets.QLabel(SWindParam)
        self.in_qs.setObjectName("in_qs")
        self.verticalLayout_2.addWidget(self.in_qs)
        self.in_Zs = QtWidgets.QLabel(SWindParam)
        self.in_Zs.setObjectName("in_Zs")
        self.verticalLayout_2.addWidget(self.in_Zs)
        self.in_Nlay = QtWidgets.QLabel(SWindParam)
        self.in_Nlay.setObjectName("in_Nlay")
        self.verticalLayout_2.addWidget(self.in_Nlay)
        self.groupBox = QtWidgets.QGroupBox(SWindParam)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.out_Ntspc = QtWidgets.QLabel(self.groupBox)
        self.out_Ntspc.setObjectName("out_Ntspc")
        self.verticalLayout.addWidget(self.out_Ntspc)
        self.out_Ncspc = QtWidgets.QLabel(self.groupBox)
        self.out_Ncspc.setObjectName("out_Ncspc")
        self.verticalLayout.addWidget(self.out_Ncspc)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem1)
        self.b_previous = QtWidgets.QPushButton(SWindParam)
        self.b_previous.setObjectName("b_previous")
        self.horizontalLayout_4.addWidget(self.b_previous)
        self.b_next = QtWidgets.QPushButton(SWindParam)
        self.b_next.setObjectName("b_next")
        self.horizontalLayout_4.addWidget(self.b_next)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.retranslateUi(SWindParam)
        QtCore.QMetaObject.connectSlotsByName(SWindParam)

    def retranslateUi(self, SWindParam):
        _translate = QtCore.QCoreApplication.translate
        SWindParam.setWindowTitle(_translate("SWindParam", "Form"))
        self.in_Npcpp.setText(_translate("SWindParam", "Npcpp :"))
        self.in_Ntcoil.setText(_translate("SWindParam", "Ntcoil :"))
        self.in_qs.setWhatsThis(_translate("SWindParam", "Number of phase"))
        self.in_qs.setText(_translate("SWindParam", " qs : ?"))
        self.in_Zs.setWhatsThis(_translate("SWindParam", "Number of slot"))
        self.in_Zs.setText(_translate("SWindParam", " Zs : ?"))
        self.in_Nlay.setWhatsThis(
            _translate("SWindParam", "Number of winding layer in each slot")
        )
        self.in_Nlay.setText(_translate("SWindParam", " Nlay : ?"))
        self.groupBox.setTitle(_translate("SWindParam", "Output"))
        self.out_Ntspc.setToolTip(
            _translate("SWindParam", "Winding number of turns in series per phase")
        )
        self.out_Ntspc.setWhatsThis(
            _translate("SWindParam", "Winding number of turns in series per phase")
        )
        self.out_Ntspc.setText(_translate("SWindParam", "Ntsp1 : ?"))
        self.out_Ncspc.setWhatsThis(
            _translate("SWindParam", "Number of coils in series per parallel circuit")
        )
        self.out_Ncspc.setText(_translate("SWindParam", "Ncspc1 : ?"))
        self.b_previous.setText(_translate("SWindParam", "Previous"))
        self.b_next.setText(_translate("SWindParam", "Next"))


from pyleecan.GUI.Resources import pyleecan_rc
