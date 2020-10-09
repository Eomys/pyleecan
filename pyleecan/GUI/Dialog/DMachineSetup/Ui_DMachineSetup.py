# -*- coding: utf-8 -*-

# File generated according to DMachineSetup.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DMachineSetup(object):
    def setupUi(self, DMachineSetup):
        if not DMachineSetup.objectName():
            DMachineSetup.setObjectName(u"DMachineSetup")
        DMachineSetup.resize(996, 711)
        self.horizontalLayout_2 = QHBoxLayout(DMachineSetup)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.nav_step = QListWidget(DMachineSetup)
        self.nav_step.setObjectName(u"nav_step")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nav_step.sizePolicy().hasHeightForWidth())
        self.nav_step.setSizePolicy(sizePolicy)
        self.nav_step.setMaximumSize(QSize(170, 16777215))

        self.horizontalLayout_2.addWidget(self.nav_step)

        self.main_layout = QVBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.b_save = QPushButton(DMachineSetup)
        self.b_save.setObjectName(u"b_save")

        self.horizontalLayout.addWidget(self.b_save)

        self.b_load = QPushButton(DMachineSetup)
        self.b_load.setObjectName(u"b_load")

        self.horizontalLayout.addWidget(self.b_load)

        self.main_layout.addLayout(self.horizontalLayout)

        self.w_step = QWidget(DMachineSetup)
        self.w_step.setObjectName(u"w_step")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.w_step.sizePolicy().hasHeightForWidth())
        self.w_step.setSizePolicy(sizePolicy1)
        self.w_step.setMinimumSize(QSize(800, 660))

        self.main_layout.addWidget(self.w_step)

        self.horizontalLayout_2.addLayout(self.main_layout)

        self.retranslateUi(DMachineSetup)

        QMetaObject.connectSlotsByName(DMachineSetup)

    # setupUi

    def retranslateUi(self, DMachineSetup):
        DMachineSetup.setWindowTitle(
            QCoreApplication.translate("DMachineSetup", u"Pyleecan Machine Setup", None)
        )
        self.b_save.setText(QCoreApplication.translate("DMachineSetup", u"Save", None))
        self.b_load.setText(QCoreApplication.translate("DMachineSetup", u"Load", None))

    # retranslateUi
