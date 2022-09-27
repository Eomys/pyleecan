# -*- coding: utf-8 -*-

# File generated according to PCondType12.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWindCond.WCondOut.WCondOut import WCondOut

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PCondType12(object):
    def setupUi(self, PCondType12):
        if not PCondType12.objectName():
            PCondType12.setObjectName(u"PCondType12")
        PCondType12.resize(1189, 672)
        self.horizontalLayout = QHBoxLayout(PCondType12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.img_cond = QLabel(PCondType12)
        self.img_cond.setObjectName(u"img_cond")
        self.img_cond.setMinimumSize(QSize(0, 0))
        self.img_cond.setMaximumSize(QSize(16777215, 16777215))
        self.img_cond.setPixmap(
            QPixmap(u":/images/images/MachineSetup/WindParam/CondType12.png")
        )
        self.img_cond.setScaledContents(True)

        self.horizontalLayout.addWidget(self.img_cond)

        self.scrollArea = QScrollArea(PCondType12)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 648))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.in_Nwpc1 = QLabel(self.scrollAreaWidgetContents)
        self.in_Nwpc1.setObjectName(u"in_Nwpc1")
        self.in_Nwpc1.setMinimumSize(QSize(90, 0))

        self.gridLayout_2.addWidget(self.in_Nwpc1, 0, 0, 1, 1)

        self.si_Nwpc1 = QSpinBox(self.scrollAreaWidgetContents)
        self.si_Nwpc1.setObjectName(u"si_Nwpc1")
        self.si_Nwpc1.setMinimumSize(QSize(0, 0))
        self.si_Nwpc1.setValue(99)

        self.gridLayout_2.addWidget(self.si_Nwpc1, 0, 1, 1, 1)

        self.in_Wwire = QLabel(self.scrollAreaWidgetContents)
        self.in_Wwire.setObjectName(u"in_Wwire")
        self.in_Wwire.setMinimumSize(QSize(90, 0))

        self.gridLayout_2.addWidget(self.in_Wwire, 1, 0, 1, 1)

        self.lf_Wwire = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_Wwire.setObjectName(u"lf_Wwire")
        self.lf_Wwire.setMinimumSize(QSize(0, 0))
        self.lf_Wwire.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.lf_Wwire, 1, 1, 1, 1)

        self.unit_Wwire = QLabel(self.scrollAreaWidgetContents)
        self.unit_Wwire.setObjectName(u"unit_Wwire")
        self.unit_Wwire.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.unit_Wwire, 1, 2, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.g_ins = QGroupBox(self.scrollAreaWidgetContents)
        self.g_ins.setObjectName(u"g_ins")
        self.g_ins.setCheckable(True)
        self.g_ins.setChecked(False)
        self.gridLayout = QGridLayout(self.g_ins)
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_Wins_cond = QLabel(self.g_ins)
        self.in_Wins_cond.setObjectName(u"in_Wins_cond")
        self.in_Wins_cond.setMinimumSize(QSize(90, 0))

        self.gridLayout.addWidget(self.in_Wins_cond, 0, 0, 1, 1)

        self.lf_Wins_cond = FloatEdit(self.g_ins)
        self.lf_Wins_cond.setObjectName(u"lf_Wins_cond")
        self.lf_Wins_cond.setMinimumSize(QSize(50, 0))
        self.lf_Wins_cond.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.lf_Wins_cond, 0, 1, 1, 1)

        self.unit_Wins_cond = QLabel(self.g_ins)
        self.unit_Wins_cond.setObjectName(u"unit_Wins_cond")

        self.gridLayout.addWidget(self.unit_Wins_cond, 0, 2, 1, 1)

        self.in_Wins_wire = QLabel(self.g_ins)
        self.in_Wins_wire.setObjectName(u"in_Wins_wire")
        self.in_Wins_wire.setMinimumSize(QSize(90, 0))

        self.gridLayout.addWidget(self.in_Wins_wire, 1, 0, 1, 1)

        self.lf_Wins_wire = FloatEdit(self.g_ins)
        self.lf_Wins_wire.setObjectName(u"lf_Wins_wire")
        self.lf_Wins_wire.setMinimumSize(QSize(50, 0))
        self.lf_Wins_wire.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.lf_Wins_wire, 1, 1, 1, 1)

        self.unit_Wins_wire = QLabel(self.g_ins)
        self.unit_Wins_wire.setObjectName(u"unit_Wins_wire")
        self.unit_Wins_wire.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.unit_Wins_wire, 1, 2, 1, 1)

        self.gridLayout_3.addWidget(self.g_ins, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.in_Lewout = QLabel(self.scrollAreaWidgetContents)
        self.in_Lewout.setObjectName(u"in_Lewout")
        self.in_Lewout.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_2.addWidget(self.in_Lewout)

        self.lf_Lewout = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_Lewout.setObjectName(u"lf_Lewout")
        self.lf_Lewout.setMinimumSize(QSize(50, 0))
        self.lf_Lewout.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.lf_Lewout)

        self.unit_Lewout = QLabel(self.scrollAreaWidgetContents)
        self.unit_Lewout.setObjectName(u"unit_Lewout")
        self.unit_Lewout.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.unit_Lewout)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.w_out = WCondOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName(u"w_out")

        self.gridLayout_3.addWidget(self.w_out, 4, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.si_Nwpc1, self.lf_Wwire)
        QWidget.setTabOrder(self.lf_Wwire, self.lf_Wins_wire)

        self.retranslateUi(PCondType12)

        QMetaObject.connectSlotsByName(PCondType12)

    # setupUi

    def retranslateUi(self, PCondType12):
        PCondType12.setWindowTitle(
            QCoreApplication.translate("PCondType12", u"Form", None)
        )
        self.img_cond.setText("")
        self.in_Nwpc1.setText(QCoreApplication.translate("PCondType12", u"Nwppc", None))
        self.in_Wwire.setText(QCoreApplication.translate("PCondType12", u"Wwire", None))
        self.unit_Wwire.setText(QCoreApplication.translate("PCondType12", u"m", None))
        self.g_ins.setTitle(
            QCoreApplication.translate("PCondType12", u"Insulation", None)
        )
        self.in_Wins_cond.setText(
            QCoreApplication.translate("PCondType12", u"Wins_cond", None)
        )
        self.unit_Wins_cond.setText(
            QCoreApplication.translate("PCondType12", u"m", None)
        )
        self.in_Wins_wire.setText(
            QCoreApplication.translate("PCondType12", u"Wins_wire", None)
        )
        self.unit_Wins_wire.setText(
            QCoreApplication.translate("PCondType12", u"m", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_Lewout.setToolTip(
            QCoreApplication.translate(
                "PCondType12", u"End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.in_Lewout.setWhatsThis(
            QCoreApplication.translate(
                "PCondType12",
                u"End-winding length on one side for a half-turn (only used in voltage driven simulations)",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.in_Lewout.setText(
            QCoreApplication.translate("PCondType12", u"Lewout", None)
        )
        # if QT_CONFIG(tooltip)
        self.lf_Lewout.setToolTip(
            QCoreApplication.translate(
                "PCondType12", u"End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lf_Lewout.setWhatsThis(
            QCoreApplication.translate(
                "PCondType12", u"End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.unit_Lewout.setToolTip(
            QCoreApplication.translate(
                "PCondType12", u"End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.unit_Lewout.setWhatsThis(
            QCoreApplication.translate(
                "PCondType12", u"End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.unit_Lewout.setText(QCoreApplication.translate("PCondType12", u"m", None))

    # retranslateUi
