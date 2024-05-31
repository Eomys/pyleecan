# -*- coding: utf-8 -*-

# File generated according to DMachineSetup.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DMachineSetup(object):
    def setupUi(self, DMachineSetup):
        if not DMachineSetup.objectName():
            DMachineSetup.setObjectName("DMachineSetup")
        DMachineSetup.resize(1076, 682)
        self.main_layout = QHBoxLayout(DMachineSetup)
        self.main_layout.setObjectName("main_layout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.b_load = QPushButton(DMachineSetup)
        self.b_load.setObjectName("b_load")

        self.verticalLayout.addWidget(self.b_load)

        self.nav_step = QListWidget(DMachineSetup)
        self.nav_step.setObjectName("nav_step")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nav_step.sizePolicy().hasHeightForWidth())
        self.nav_step.setSizePolicy(sizePolicy)
        self.nav_step.setMaximumSize(QSize(190, 16777215))

        self.verticalLayout.addWidget(self.nav_step)

        self.b_save = QPushButton(DMachineSetup)
        self.b_save.setObjectName("b_save")

        self.verticalLayout.addWidget(self.b_save)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.main_layout.addLayout(self.verticalLayout)

        self.w_step = QWidget(DMachineSetup)
        self.w_step.setObjectName("w_step")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.w_step.sizePolicy().hasHeightForWidth())
        self.w_step.setSizePolicy(sizePolicy1)
        self.w_step.setMinimumSize(QSize(800, 660))

        self.main_layout.addWidget(self.w_step)

        self.retranslateUi(DMachineSetup)

        QMetaObject.connectSlotsByName(DMachineSetup)

    # setupUi

    def retranslateUi(self, DMachineSetup):
        DMachineSetup.setWindowTitle(
            QCoreApplication.translate("DMachineSetup", "Pyleecan Machine Setup", None)
        )
        self.b_load.setText(QCoreApplication.translate("DMachineSetup", "Load", None))
        self.b_save.setText(QCoreApplication.translate("DMachineSetup", "Save", None))

    # retranslateUi
