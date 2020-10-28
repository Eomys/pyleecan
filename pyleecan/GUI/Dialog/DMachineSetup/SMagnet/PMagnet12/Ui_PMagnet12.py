# -*- coding: utf-8 -*-

# File generated according to PMagnet12.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SMagnet.WMagnetOut.WMagnetOut import WMagnetOut

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PMagnet12(object):
    def setupUi(self, PMagnet12):
        if not PMagnet12.objectName():
            PMagnet12.setObjectName(u"PMagnet12")
        PMagnet12.resize(531, 222)
        PMagnet12.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(PMagnet12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.img_magnet = QLabel(PMagnet12)
        self.img_magnet.setObjectName(u"img_magnet")
        self.img_magnet.setMinimumSize(QSize(300, 200))
        self.img_magnet.setMaximumSize(QSize(550, 350))
        self.img_magnet.setPixmap(
            QPixmap(u":/images/images/MachineSetup/P_Magnet/Surface Magnet type 12.PNG")
        )
        self.img_magnet.setScaledContents(True)

        self.horizontalLayout.addWidget(self.img_magnet)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lf_Wmag = FloatEdit(PMagnet12)
        self.lf_Wmag.setObjectName(u"lf_Wmag")
        self.lf_Wmag.setMinimumSize(QSize(100, 0))
        self.lf_Wmag.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_Wmag, 0, 1, 1, 1)

        self.in_H0 = QLabel(PMagnet12)
        self.in_H0.setObjectName(u"in_H0")

        self.gridLayout.addWidget(self.in_H0, 2, 0, 1, 1)

        self.unit_Hmag = QLabel(PMagnet12)
        self.unit_Hmag.setObjectName(u"unit_Hmag")

        self.gridLayout.addWidget(self.unit_Hmag, 1, 2, 1, 1)

        self.lf_Hmag = FloatEdit(PMagnet12)
        self.lf_Hmag.setObjectName(u"lf_Hmag")
        self.lf_Hmag.setMinimumSize(QSize(100, 0))
        self.lf_Hmag.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_Hmag, 1, 1, 1, 1)

        self.unit_Wmag = QLabel(PMagnet12)
        self.unit_Wmag.setObjectName(u"unit_Wmag")

        self.gridLayout.addWidget(self.unit_Wmag, 0, 2, 1, 1)

        self.lf_H0 = FloatEdit(PMagnet12)
        self.lf_H0.setObjectName(u"lf_H0")
        self.lf_H0.setMinimumSize(QSize(100, 0))
        self.lf_H0.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_H0, 2, 1, 1, 1)

        self.in_Hmag = QLabel(PMagnet12)
        self.in_Hmag.setObjectName(u"in_Hmag")

        self.gridLayout.addWidget(self.in_Hmag, 1, 0, 1, 1)

        self.unit_H0 = QLabel(PMagnet12)
        self.unit_H0.setObjectName(u"unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 2, 2, 1, 1)

        self.in_Wmag = QLabel(PMagnet12)
        self.in_Wmag.setObjectName(u"in_Wmag")

        self.gridLayout.addWidget(self.in_Wmag, 0, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.w_out = WMagnetOut(PMagnet12)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.verticalSpacer = QSpacerItem(
            17, 18, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout.addLayout(self.verticalLayout)

        QWidget.setTabOrder(self.lf_Wmag, self.lf_Hmag)
        QWidget.setTabOrder(self.lf_Hmag, self.lf_H0)

        self.retranslateUi(PMagnet12)

        QMetaObject.connectSlotsByName(PMagnet12)

    # setupUi

    def retranslateUi(self, PMagnet12):
        PMagnet12.setWindowTitle(QCoreApplication.translate("PMagnet12", u"Form", None))
        self.img_magnet.setText("")
        self.in_H0.setText(QCoreApplication.translate("PMagnet12", u"H0      :", None))
        self.unit_Hmag.setText(QCoreApplication.translate("PMagnet12", u"m", None))
        self.unit_Wmag.setText(QCoreApplication.translate("PMagnet12", u"m", None))
        self.in_Hmag.setText(QCoreApplication.translate("PMagnet12", u"Hmag  :", None))
        self.unit_H0.setText(QCoreApplication.translate("PMagnet12", u"m", None))
        self.in_Wmag.setText(QCoreApplication.translate("PMagnet12", u"Wmag :", None))

    # retranslateUi
