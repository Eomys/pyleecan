# -*- coding: utf-8 -*-

# File generated according to SPreview.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SPreview(object):
    def setupUi(self, SPreview):
        SPreview.setObjectName("SPreview")
        SPreview.resize(532, 450)
        SPreview.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(SPreview)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.w_plot = MPLCanvas2(SPreview)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_plot.sizePolicy().hasHeightForWidth())
        self.w_plot.setSizePolicy(sizePolicy)
        self.w_plot.setMinimumSize(QtCore.QSize(300, 300))
        self.w_plot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.w_plot.setObjectName("w_plot")
        self.horizontalLayout_2.addWidget(self.w_plot)
        self.tab_machine = WMachineTable(SPreview)
        self.tab_machine.setObjectName("tab_machine")
        self.horizontalLayout_2.addWidget(self.tab_machine)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.b_previous = QtWidgets.QPushButton(SPreview)
        self.b_previous.setObjectName("b_previous")
        self.horizontalLayout.addWidget(self.b_previous)
        self.b_next = QtWidgets.QPushButton(SPreview)
        self.b_next.setObjectName("b_next")
        self.horizontalLayout.addWidget(self.b_next)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SPreview)
        QtCore.QMetaObject.connectSlotsByName(SPreview)

    def retranslateUi(self, SPreview):
        _translate = QtCore.QCoreApplication.translate
        SPreview.setWindowTitle(_translate("SPreview", "Form"))
        self.b_previous.setText(_translate("SPreview", "Previous"))
        self.b_next.setText(_translate("SPreview", "Next"))


from .....GUI.Dialog.DMachineSetup.SPreview.WMachineTable.WMachineTable import (
    WMachineTable,
)
from .....GUI.Tools.MPLCanvas import MPLCanvas2
from pyleecan.GUI.Resources import pyleecan_rc
