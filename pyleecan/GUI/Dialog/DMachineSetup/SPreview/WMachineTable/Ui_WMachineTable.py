# -*- coding: utf-8 -*-

# File generated according to WMachineTable.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_WMachineTable(object):
    def setupUi(self, WMachineTable):
        if not WMachineTable.objectName():
            WMachineTable.setObjectName("WMachineTable")
        WMachineTable.resize(290, 357)
        WMachineTable.setMinimumSize(QSize(290, 0))
        WMachineTable.setMaximumSize(QSize(282, 16777215))
        self.verticalLayout = QVBoxLayout(WMachineTable)
        self.verticalLayout.setObjectName("verticalLayout")
        self.in_name = QLabel(WMachineTable)
        self.in_name.setObjectName("in_name")
        self.in_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.in_name)

        self.tab_param = QTableWidget(WMachineTable)
        if self.tab_param.columnCount() < 2:
            self.tab_param.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tab_param.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tab_param.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tab_param.setObjectName("tab_param")
        self.tab_param.setMinimumSize(QSize(270, 0))
        self.tab_param.setMaximumSize(QSize(260, 16777215))
        self.tab_param.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tab_param.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tab_param.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tab_param.setAlternatingRowColors(True)
        self.tab_param.setColumnCount(2)
        self.tab_param.horizontalHeader().setCascadingSectionResizes(False)
        self.tab_param.horizontalHeader().setStretchLastSection(True)
        self.tab_param.verticalHeader().setVisible(False)
        self.tab_param.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout.addWidget(self.tab_param)

        self.b_plot_machine = QPushButton(WMachineTable)
        self.b_plot_machine.setObjectName("b_plot_machine")

        self.verticalLayout.addWidget(self.b_plot_machine)

        self.b_mmf = QPushButton(WMachineTable)
        self.b_mmf.setObjectName("b_mmf")

        self.verticalLayout.addWidget(self.b_mmf)

        self.b_FEMM = QPushButton(WMachineTable)
        self.b_FEMM.setObjectName("b_FEMM")

        self.verticalLayout.addWidget(self.b_FEMM)

        self.b_GMSH = QPushButton(WMachineTable)
        self.b_GMSH.setObjectName("b_GMSH")

        self.verticalLayout.addWidget(self.b_GMSH)

        self.b_GMSH_3D = QPushButton(WMachineTable)
        self.b_GMSH_3D.setObjectName("b_GMSH_3D")

        self.verticalLayout.addWidget(self.b_GMSH_3D)

        self.retranslateUi(WMachineTable)

        QMetaObject.connectSlotsByName(WMachineTable)

    # setupUi

    def retranslateUi(self, WMachineTable):
        WMachineTable.setWindowTitle(
            QCoreApplication.translate("WMachineTable", "Form", None)
        )
        self.in_name.setText(
            QCoreApplication.translate("WMachineTable", "Main Machine Parameters", None)
        )
        ___qtablewidgetitem = self.tab_param.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("WMachineTable", "Name", None)
        )
        ___qtablewidgetitem1 = self.tab_param.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("WMachineTable", "Value", None)
        )
        self.b_plot_machine.setText(
            QCoreApplication.translate("WMachineTable", "Plot Machine", None)
        )
        self.b_mmf.setText(
            QCoreApplication.translate("WMachineTable", "Plot Stator Unit MMF", None)
        )
        self.b_FEMM.setText(
            QCoreApplication.translate("WMachineTable", "Draw in FEMM", None)
        )
        self.b_GMSH.setText(
            QCoreApplication.translate("WMachineTable", "Draw in GMSH", None)
        )
        self.b_GMSH_3D.setText(
            QCoreApplication.translate("WMachineTable", "3D stator in GMSH", None)
        )

    # retranslateUi
