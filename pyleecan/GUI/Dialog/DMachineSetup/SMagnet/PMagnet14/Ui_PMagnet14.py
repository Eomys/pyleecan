# -*- coding: utf-8 -*-

# File generated according to PMagnet14.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SMagnet.WMagnetOut.WMagnetOut import WMagnetOut

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PMagnet14(object):
    def setupUi(self, PMagnet14):
        if not PMagnet14.objectName():
            PMagnet14.setObjectName(u"PMagnet14")
        PMagnet14.resize(531, 232)
        PMagnet14.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(PMagnet14)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.img_magnet = QLabel(PMagnet14)
        self.img_magnet.setObjectName(u"img_magnet")
        self.img_magnet.setMinimumSize(QSize(300, 200))
        self.img_magnet.setMaximumSize(QSize(550, 350))
        self.img_magnet.setPixmap(
            QPixmap(u":/images/images/MachineSetup/P_Magnet/Surface Magnet type 14.PNG")
        )
        self.img_magnet.setScaledContents(True)

        self.horizontalLayout.addWidget(self.img_magnet)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_Wmag = QLabel(PMagnet14)
        self.in_Wmag.setObjectName(u"in_Wmag")

        self.gridLayout.addWidget(self.in_Wmag, 0, 0, 1, 1)

        self.lf_Wmag = FloatEdit(PMagnet14)
        self.lf_Wmag.setObjectName(u"lf_Wmag")
        self.lf_Wmag.setMinimumSize(QSize(100, 0))
        self.lf_Wmag.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_Wmag, 0, 1, 1, 1)

        self.unit_Wmag = QLabel(PMagnet14)
        self.unit_Wmag.setObjectName(u"unit_Wmag")

        self.gridLayout.addWidget(self.unit_Wmag, 0, 2, 1, 1)

        self.in_Hmag = QLabel(PMagnet14)
        self.in_Hmag.setObjectName(u"in_Hmag")

        self.gridLayout.addWidget(self.in_Hmag, 1, 0, 1, 1)

        self.lf_Hmag = FloatEdit(PMagnet14)
        self.lf_Hmag.setObjectName(u"lf_Hmag")
        self.lf_Hmag.setMinimumSize(QSize(100, 0))
        self.lf_Hmag.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_Hmag, 1, 1, 1, 1)

        self.unit_Hmag = QLabel(PMagnet14)
        self.unit_Hmag.setObjectName(u"unit_Hmag")

        self.gridLayout.addWidget(self.unit_Hmag, 1, 2, 1, 1)

        self.in_Rtopm = QLabel(PMagnet14)
        self.in_Rtopm.setObjectName(u"in_Rtopm")

        self.gridLayout.addWidget(self.in_Rtopm, 2, 0, 1, 1)

        self.lf_Rtopm = FloatEdit(PMagnet14)
        self.lf_Rtopm.setObjectName(u"lf_Rtopm")
        self.lf_Rtopm.setMinimumSize(QSize(100, 0))
        self.lf_Rtopm.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_Rtopm, 2, 1, 1, 1)

        self.unit_Rtopm = QLabel(PMagnet14)
        self.unit_Rtopm.setObjectName(u"unit_Rtopm")

        self.gridLayout.addWidget(self.unit_Rtopm, 2, 2, 1, 1)

        self.in_H0 = QLabel(PMagnet14)
        self.in_H0.setObjectName(u"in_H0")

        self.gridLayout.addWidget(self.in_H0, 3, 0, 1, 1)

        self.lf_H0 = FloatEdit(PMagnet14)
        self.lf_H0.setObjectName(u"lf_H0")
        self.lf_H0.setMinimumSize(QSize(100, 0))
        self.lf_H0.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_H0, 3, 1, 1, 1)

        self.unit_H0 = QLabel(PMagnet14)
        self.unit_H0.setObjectName(u"unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 3, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.w_out = WMagnetOut(PMagnet14)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.verticalSpacer = QSpacerItem(
            17, 18, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout.addLayout(self.verticalLayout)

        QWidget.setTabOrder(self.lf_Wmag, self.lf_Hmag)
        QWidget.setTabOrder(self.lf_Hmag, self.lf_Rtopm)
        QWidget.setTabOrder(self.lf_Rtopm, self.lf_H0)

        self.retranslateUi(PMagnet14)

        QMetaObject.connectSlotsByName(PMagnet14)

    # setupUi

    def retranslateUi(self, PMagnet14):
        PMagnet14.setWindowTitle(QCoreApplication.translate("PMagnet14", u"Form", None))
        self.img_magnet.setText("")
        self.in_Wmag.setText(QCoreApplication.translate("PMagnet14", u"Wmag :", None))
        self.unit_Wmag.setText(QCoreApplication.translate("PMagnet14", u"rad", None))
        self.in_Hmag.setText(QCoreApplication.translate("PMagnet14", u"Hmag  :", None))
        self.unit_Hmag.setText(QCoreApplication.translate("PMagnet14", u"m", None))
        self.in_Rtopm.setText(
            QCoreApplication.translate("PMagnet14", u"Rtopm  :", None)
        )
        self.unit_Rtopm.setText(QCoreApplication.translate("PMagnet14", u"m", None))
        self.in_H0.setText(QCoreApplication.translate("PMagnet14", u"H0      :", None))
        self.unit_H0.setText(QCoreApplication.translate("PMagnet14", u"m", None))

    # retranslateUi
