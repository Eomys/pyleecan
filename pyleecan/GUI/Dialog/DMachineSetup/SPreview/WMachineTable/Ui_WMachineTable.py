# -*- coding: utf-8 -*-

# File generated according to WMachineTable.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WMachineTable(object):
    def setupUi(self, WMachineTable):
        WMachineTable.setObjectName("WMachineTable")
        WMachineTable.resize(290, 357)
        WMachineTable.setMinimumSize(QtCore.QSize(290, 0))
        WMachineTable.setMaximumSize(QtCore.QSize(282, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(WMachineTable)
        self.verticalLayout.setObjectName("verticalLayout")
        self.in_name = QtWidgets.QLabel(WMachineTable)
        self.in_name.setAlignment(QtCore.Qt.AlignCenter)
        self.in_name.setObjectName("in_name")
        self.verticalLayout.addWidget(self.in_name)
        self.tab_param = QtWidgets.QTableWidget(WMachineTable)
        self.tab_param.setMinimumSize(QtCore.QSize(270, 0))
        self.tab_param.setMaximumSize(QtCore.QSize(260, 16777215))
        self.tab_param.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tab_param.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tab_param.setAlternatingRowColors(True)
        self.tab_param.setColumnCount(2)
        self.tab_param.setObjectName("tab_param")
        self.tab_param.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_param.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_param.setHorizontalHeaderItem(1, item)
        self.tab_param.horizontalHeader().setCascadingSectionResizes(False)
        self.tab_param.horizontalHeader().setStretchLastSection(True)
        self.tab_param.verticalHeader().setVisible(False)
        self.tab_param.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tab_param)
        self.b_mmf = QtWidgets.QPushButton(WMachineTable)
        self.b_mmf.setObjectName("b_mmf")
        self.verticalLayout.addWidget(self.b_mmf)

        self.retranslateUi(WMachineTable)
        QtCore.QMetaObject.connectSlotsByName(WMachineTable)

    def retranslateUi(self, WMachineTable):
        _translate = QtCore.QCoreApplication.translate
        WMachineTable.setWindowTitle(_translate("WMachineTable", "Form"))
        self.in_name.setText(_translate("WMachineTable", "Main Machine Parameters"))
        item = self.tab_param.horizontalHeaderItem(0)
        item.setText(_translate("WMachineTable", "Name"))
        item = self.tab_param.horizontalHeaderItem(1)
        item.setText(_translate("WMachineTable", "Value"))
        self.b_mmf.setText(_translate("WMachineTable", "Plot Stator Unit MMF"))


from pyleecan.GUI.Resources import pyleecan_rc
