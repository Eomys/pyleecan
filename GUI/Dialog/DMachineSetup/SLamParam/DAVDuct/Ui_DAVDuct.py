# -*- coding: utf-8 -*-

# File generated according to DAVDuct.ui
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DAVDuct(object):
    def setupUi(self, DAVDuct):
        DAVDuct.setObjectName("DAVDuct")
        DAVDuct.resize(767, 630)
        self.verticalLayout = QtWidgets.QVBoxLayout(DAVDuct)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.b_new = QtWidgets.QPushButton(DAVDuct)
        self.b_new.setObjectName("b_new")
        self.horizontalLayout_2.addWidget(self.b_new)
        self.b_remove = QtWidgets.QPushButton(DAVDuct)
        self.b_remove.setObjectName("b_remove")
        self.horizontalLayout_2.addWidget(self.b_remove)
        self.b_help = HelpButton(DAVDuct)
        self.b_help.setText("")
        self.b_help.setPixmap(QtGui.QPixmap(":/images/images/icon/help_16.png"))
        self.b_help.setObjectName("b_help")
        self.horizontalLayout_2.addWidget(self.b_help)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tab_vent = QtWidgets.QTabWidget(DAVDuct)
        self.tab_vent.setObjectName("tab_vent")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab_vent.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_vent.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tab_vent)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.b_plot = QtWidgets.QPushButton(DAVDuct)
        self.b_plot.setObjectName("b_plot")
        self.horizontalLayout_4.addWidget(self.b_plot)
        self.b_cancel = QtWidgets.QPushButton(DAVDuct)
        self.b_cancel.setObjectName("b_cancel")
        self.horizontalLayout_4.addWidget(self.b_cancel)
        self.b_ok = QtWidgets.QPushButton(DAVDuct)
        self.b_ok.setObjectName("b_ok")
        self.horizontalLayout_4.addWidget(self.b_ok)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(DAVDuct)
        QtCore.QMetaObject.connectSlotsByName(DAVDuct)

    def retranslateUi(self, DAVDuct):
        _translate = QtCore.QCoreApplication.translate
        DAVDuct.setWindowTitle(_translate("DAVDuct", "Set axial ventilation duct"))
        self.b_new.setText(_translate("DAVDuct", "Add New Set"))
        self.b_remove.setText(_translate("DAVDuct", "Remove Last Set"))
        self.tab_vent.setTabText(self.tab_vent.indexOf(self.tab), _translate("DAVDuct", "Tab 1"))
        self.tab_vent.setTabText(self.tab_vent.indexOf(self.tab_2), _translate("DAVDuct", "Tab 2"))
        self.b_plot.setText(_translate("DAVDuct", "Preview"))
        self.b_cancel.setText(_translate("DAVDuct", "Cancel"))
        self.b_ok.setText(_translate("DAVDuct", "Ok"))
from pyleecan.GUI.Tools.HelpButton import HelpButton
from pyleecan.GUI.Resources import pyleecan_rc
