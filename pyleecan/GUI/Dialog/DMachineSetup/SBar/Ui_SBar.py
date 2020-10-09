# -*- coding: utf-8 -*-

# File generated according to SBar.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .....GUI.Tools.FloatEdit import FloatEdit
from .....GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SBar(object):
    def setupUi(self, SBar):
        if not SBar.objectName():
            SBar.setObjectName(u"SBar")
        SBar.resize(650, 550)
        SBar.setMinimumSize(QSize(650, 550))
        self.verticalLayout_2 = QVBoxLayout(SBar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.g_bar = QGroupBox(SBar)
        self.g_bar.setObjectName(u"g_bar")
        self.verticalLayout = QVBoxLayout(self.g_bar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.c_bar_type = QComboBox(self.g_bar)
        self.c_bar_type.addItem("")
        self.c_bar_type.addItem("")
        self.c_bar_type.setObjectName(u"c_bar_type")
        self.c_bar_type.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.c_bar_type)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.w_bar = QWidget(self.g_bar)
        self.w_bar.setObjectName(u"w_bar")

        self.verticalLayout.addWidget(self.w_bar)

        self.verticalLayout_2.addWidget(self.g_bar)

        self.g_ring = QGroupBox(SBar)
        self.g_ring.setObjectName(u"g_ring")
        self.horizontalLayout_2 = QHBoxLayout(self.g_ring)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.img_ring = QLabel(self.g_ring)
        self.img_ring.setObjectName(u"img_ring")
        self.img_ring.setMaximumSize(QSize(300, 300))
        self.img_ring.setPixmap(QPixmap(u":/images/images/MachineSetup/Bar/Ring.PNG"))
        self.img_ring.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.img_ring)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lf_Lewout = FloatEdit(self.g_ring)
        self.lf_Lewout.setObjectName(u"lf_Lewout")
        self.lf_Lewout.setMinimumSize(QSize(70, 0))
        self.lf_Lewout.setMaximumSize(QSize(100, 20))

        self.gridLayout.addWidget(self.lf_Lewout, 2, 1, 1, 1)

        self.unit_Hscr = QLabel(self.g_ring)
        self.unit_Hscr.setObjectName(u"unit_Hscr")
        self.unit_Hscr.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.unit_Hscr, 0, 2, 1, 1)

        self.unit_Lscr = QLabel(self.g_ring)
        self.unit_Lscr.setObjectName(u"unit_Lscr")
        self.unit_Lscr.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.unit_Lscr, 1, 2, 1, 1)

        self.in_Hscr = QLabel(self.g_ring)
        self.in_Hscr.setObjectName(u"in_Hscr")
        self.in_Hscr.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.in_Hscr, 0, 0, 1, 1)

        self.lf_Hscr = FloatEdit(self.g_ring)
        self.lf_Hscr.setObjectName(u"lf_Hscr")
        self.lf_Hscr.setMinimumSize(QSize(70, 0))
        self.lf_Hscr.setMaximumSize(QSize(100, 20))

        self.gridLayout.addWidget(self.lf_Hscr, 0, 1, 1, 1)

        self.lf_Lscr = FloatEdit(self.g_ring)
        self.lf_Lscr.setObjectName(u"lf_Lscr")
        self.lf_Lscr.setMinimumSize(QSize(70, 0))
        self.lf_Lscr.setMaximumSize(QSize(100, 20))

        self.gridLayout.addWidget(self.lf_Lscr, 1, 1, 1, 1)

        self.unit_Lewout = QLabel(self.g_ring)
        self.unit_Lewout.setObjectName(u"unit_Lewout")
        self.unit_Lewout.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.unit_Lewout, 2, 2, 1, 1)

        self.in_Lewout = QLabel(self.g_ring)
        self.in_Lewout.setObjectName(u"in_Lewout")
        self.in_Lewout.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.in_Lewout, 2, 0, 1, 1)

        self.in_Lscr = QLabel(self.g_ring)
        self.in_Lscr.setObjectName(u"in_Lscr")
        self.in_Lscr.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.in_Lscr, 1, 0, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.w_mat = WMatSelect(self.g_ring)
        self.w_mat.setObjectName(u"w_mat")

        self.verticalLayout_3.addWidget(self.w_mat)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2.addWidget(self.g_ring)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.b_plot = QPushButton(SBar)
        self.b_plot.setObjectName(u"b_plot")

        self.horizontalLayout_3.addWidget(self.b_plot)

        self.b_previous = QPushButton(SBar)
        self.b_previous.setObjectName(u"b_previous")

        self.horizontalLayout_3.addWidget(self.b_previous)

        self.b_next = QPushButton(SBar)
        self.b_next.setObjectName(u"b_next")
        self.b_next.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.b_next)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        QWidget.setTabOrder(self.lf_Hscr, self.lf_Lscr)
        QWidget.setTabOrder(self.lf_Lscr, self.lf_Lewout)
        QWidget.setTabOrder(self.lf_Lewout, self.b_previous)
        QWidget.setTabOrder(self.b_previous, self.b_plot)
        QWidget.setTabOrder(self.b_plot, self.c_bar_type)

        self.retranslateUi(SBar)

        QMetaObject.connectSlotsByName(SBar)

    # setupUi

    def retranslateUi(self, SBar):
        SBar.setWindowTitle(QCoreApplication.translate("SBar", u"Form", None))
        self.g_bar.setTitle(QCoreApplication.translate("SBar", u"Bar", None))
        self.c_bar_type.setItemText(
            0, QCoreApplication.translate("SBar", u"Rectangular bar", None)
        )
        self.c_bar_type.setItemText(
            1, QCoreApplication.translate("SBar", u"Die cast bar", None)
        )

        self.g_ring.setTitle(
            QCoreApplication.translate("SBar", u"Short Circuit Ring", None)
        )
        self.img_ring.setText("")
        self.unit_Hscr.setText(QCoreApplication.translate("SBar", u"m", None))
        self.unit_Lscr.setText(QCoreApplication.translate("SBar", u"m", None))
        self.in_Hscr.setText(QCoreApplication.translate("SBar", u"Hscr :", None))
        self.unit_Lewout.setText(QCoreApplication.translate("SBar", u"m", None))
        self.in_Lewout.setText(QCoreApplication.translate("SBar", u"Lewout :", None))
        self.in_Lscr.setText(QCoreApplication.translate("SBar", u"Lscr :", None))
        self.b_plot.setText(QCoreApplication.translate("SBar", u"Preview", None))
        self.b_previous.setText(QCoreApplication.translate("SBar", u"Previous", None))
        self.b_next.setText(QCoreApplication.translate("SBar", u"Save", None))

    # retranslateUi
