# -*- coding: utf-8 -*-

# File generated according to SWindParam.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SWindParam(object):
    def setupUi(self, SWindParam):
        if not SWindParam.objectName():
            SWindParam.setObjectName(u"SWindParam")
        SWindParam.resize(650, 550)
        SWindParam.setMinimumSize(QSize(650, 550))
        self.verticalLayout_3 = QVBoxLayout(SWindParam)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.img_wind_geo = QLabel(SWindParam)
        self.img_wind_geo.setObjectName(u"img_wind_geo")
        self.img_wind_geo.setMinimumSize(QSize(300, 300))
        self.img_wind_geo.setPixmap(
            QPixmap(u":/images/images/MachineSetup/WindParam/Winding param.PNG")
        )
        self.img_wind_geo.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.img_wind_geo)

        self.widget = QWidget(SWindParam)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 0))
        self.widget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.in_Npcpp = QLabel(self.widget)
        self.in_Npcpp.setObjectName(u"in_Npcpp")
        self.in_Npcpp.setMinimumSize(QSize(40, 0))

        self.horizontalLayout.addWidget(self.in_Npcpp)

        self.si_Npcpp = QSpinBox(self.widget)
        self.si_Npcpp.setObjectName(u"si_Npcpp")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.si_Npcpp.sizePolicy().hasHeightForWidth())
        self.si_Npcpp.setSizePolicy(sizePolicy)
        self.si_Npcpp.setMinimumSize(QSize(100, 0))
        self.si_Npcpp.setMaximumSize(QSize(100, 16777215))
        self.si_Npcpp.setValue(99)

        self.horizontalLayout.addWidget(self.si_Npcpp)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.in_Ntcoil = QLabel(self.widget)
        self.in_Ntcoil.setObjectName(u"in_Ntcoil")
        self.in_Ntcoil.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_2.addWidget(self.in_Ntcoil)

        self.si_Ntcoil = QSpinBox(self.widget)
        self.si_Ntcoil.setObjectName(u"si_Ntcoil")
        sizePolicy.setHeightForWidth(self.si_Ntcoil.sizePolicy().hasHeightForWidth())
        self.si_Ntcoil.setSizePolicy(sizePolicy)
        self.si_Ntcoil.setMinimumSize(QSize(100, 0))
        self.si_Ntcoil.setMaximumSize(QSize(100, 16777215))
        self.si_Ntcoil.setValue(99)

        self.horizontalLayout_2.addWidget(self.si_Ntcoil)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.in_qs = QLabel(self.widget)
        self.in_qs.setObjectName(u"in_qs")

        self.verticalLayout_2.addWidget(self.in_qs)

        self.in_Zs = QLabel(self.widget)
        self.in_Zs.setObjectName(u"in_Zs")

        self.verticalLayout_2.addWidget(self.in_Zs)

        self.in_Nlay = QLabel(self.widget)
        self.in_Nlay.setObjectName(u"in_Nlay")

        self.verticalLayout_2.addWidget(self.in_Nlay)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.out_Ntspc = QLabel(self.groupBox)
        self.out_Ntspc.setObjectName(u"out_Ntspc")

        self.verticalLayout.addWidget(self.out_Ntspc)

        self.out_Ncspc = QLabel(self.groupBox)
        self.out_Ncspc.setObjectName(u"out_Ncspc")

        self.verticalLayout.addWidget(self.out_Ncspc)

        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(
            20, 247, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_3.addWidget(self.widget)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.b_previous = QPushButton(SWindParam)
        self.b_previous.setObjectName(u"b_previous")

        self.horizontalLayout_4.addWidget(self.b_previous)

        self.b_next = QPushButton(SWindParam)
        self.b_next.setObjectName(u"b_next")

        self.horizontalLayout_4.addWidget(self.b_next)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.retranslateUi(SWindParam)

        QMetaObject.connectSlotsByName(SWindParam)

    # setupUi

    def retranslateUi(self, SWindParam):
        SWindParam.setWindowTitle(
            QCoreApplication.translate("SWindParam", u"Form", None)
        )
        self.img_wind_geo.setText("")
        self.in_Npcpp.setText(
            QCoreApplication.translate("SWindParam", u"Npcpp :", None)
        )
        self.in_Ntcoil.setText(
            QCoreApplication.translate("SWindParam", u"Ntcoil :", None)
        )
        # if QT_CONFIG(whatsthis)
        self.in_qs.setWhatsThis(
            QCoreApplication.translate("SWindParam", u"Number of phase", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.in_qs.setText(QCoreApplication.translate("SWindParam", u" qs : ?", None))
        # if QT_CONFIG(whatsthis)
        self.in_Zs.setWhatsThis(
            QCoreApplication.translate("SWindParam", u"Number of slot", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.in_Zs.setText(QCoreApplication.translate("SWindParam", u" Zs : ?", None))
        # if QT_CONFIG(whatsthis)
        self.in_Nlay.setWhatsThis(
            QCoreApplication.translate(
                "SWindParam", u"Number of winding layer in each slot", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.in_Nlay.setText(
            QCoreApplication.translate("SWindParam", u" Nlay : ?", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("SWindParam", u"Output", None)
        )
        # if QT_CONFIG(tooltip)
        self.out_Ntspc.setToolTip(
            QCoreApplication.translate(
                "SWindParam", u"Winding number of turns in series per phase", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.out_Ntspc.setWhatsThis(
            QCoreApplication.translate(
                "SWindParam", u"Winding number of turns in series per phase", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.out_Ntspc.setText(
            QCoreApplication.translate("SWindParam", u"Ntsp1 : ?", None)
        )
        # if QT_CONFIG(whatsthis)
        self.out_Ncspc.setWhatsThis(
            QCoreApplication.translate(
                "SWindParam", u"Number of coils in series per parallel circuit", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.out_Ncspc.setText(
            QCoreApplication.translate("SWindParam", u"Ncspc1 : ?", None)
        )
        self.b_previous.setText(
            QCoreApplication.translate("SWindParam", u"Previous", None)
        )
        self.b_next.setText(QCoreApplication.translate("SWindParam", u"Next", None))

    # retranslateUi
