# -*- coding: utf-8 -*-

# File generated according to DMachineSetup.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DMachineSetup(object):
    def setupUi(self, DMachineSetup):
        DMachineSetup.setObjectName("DMachineSetup")
        DMachineSetup.resize(583, 356)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(DMachineSetup)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nav_step = QtWidgets.QListWidget(DMachineSetup)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nav_step.sizePolicy().hasHeightForWidth())
        self.nav_step.setSizePolicy(sizePolicy)
        self.nav_step.setMaximumSize(QtCore.QSize(170, 16777215))
        self.nav_step.setObjectName("nav_step")
        self.horizontalLayout_2.addWidget(self.nav_step)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.b_save = QtWidgets.QPushButton(DMachineSetup)
        self.b_save.setObjectName("b_save")
        self.horizontalLayout.addWidget(self.b_save)
        self.b_load = QtWidgets.QPushButton(DMachineSetup)
        self.b_load.setObjectName("b_load")
        self.horizontalLayout.addWidget(self.b_load)
        self.main_layout.addLayout(self.horizontalLayout)
        self.w_step = QtWidgets.QWidget(DMachineSetup)
        self.w_step.setObjectName("w_step")
        self.main_layout.addWidget(self.w_step)
        self.horizontalLayout_2.addLayout(self.main_layout)

        self.retranslateUi(DMachineSetup)
        QtCore.QMetaObject.connectSlotsByName(DMachineSetup)

    def retranslateUi(self, DMachineSetup):
        _translate = QtCore.QCoreApplication.translate
        DMachineSetup.setWindowTitle(
            _translate("DMachineSetup", "Pyleecan Machine Setup")
        )
        self.b_save.setText(_translate("DMachineSetup", "Save"))
        self.b_load.setText(_translate("DMachineSetup", "Load"))


from pyleecan.GUI.Resources import pyleecan_rc
