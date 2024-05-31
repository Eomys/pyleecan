# -*- coding: utf-8 -*-

# File generated according to SBar.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from .....GUI.Tools.FloatEdit import FloatEdit
from .....GUI.Dialog.DMatLib.WMatSelect.WMatSelectV import WMatSelectV

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SBar(object):
    def setupUi(self, SBar):
        if not SBar.objectName():
            SBar.setObjectName("SBar")
        SBar.resize(914, 750)
        SBar.setMinimumSize(QSize(650, 550))
        self.verticalLayout_5 = QVBoxLayout(SBar)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.img_ring = QLabel(SBar)
        self.img_ring.setObjectName("img_ring")
        self.img_ring.setMaximumSize(QSize(16777215, 16777215))
        self.img_ring.setPixmap(
            QPixmap(":/images/images/MachineSetup/Bar/ShortCircuitRing_schematics.png")
        )
        self.img_ring.setScaledContents(False)
        self.img_ring.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.img_ring)

        self.scrollArea = QScrollArea(SBar)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMaximumSize(QSize(300, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 241, 687))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.g_ring = QGroupBox(self.scrollAreaWidgetContents)
        self.g_ring.setObjectName("g_ring")
        self.verticalLayout_2 = QVBoxLayout(self.g_ring)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lf_Lewout = FloatEdit(self.g_ring)
        self.lf_Lewout.setObjectName("lf_Lewout")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lf_Lewout.sizePolicy().hasHeightForWidth())
        self.lf_Lewout.setSizePolicy(sizePolicy)
        self.lf_Lewout.setMinimumSize(QSize(70, 0))
        self.lf_Lewout.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_Lewout, 2, 1, 1, 1)

        self.unit_Hscr = QLabel(self.g_ring)
        self.unit_Hscr.setObjectName("unit_Hscr")
        self.unit_Hscr.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.unit_Hscr, 0, 2, 1, 1)

        self.unit_Lscr = QLabel(self.g_ring)
        self.unit_Lscr.setObjectName("unit_Lscr")
        self.unit_Lscr.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.unit_Lscr, 1, 2, 1, 1)

        self.in_Hscr = QLabel(self.g_ring)
        self.in_Hscr.setObjectName("in_Hscr")
        self.in_Hscr.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.in_Hscr, 0, 0, 1, 1)

        self.lf_Hscr = FloatEdit(self.g_ring)
        self.lf_Hscr.setObjectName("lf_Hscr")
        sizePolicy.setHeightForWidth(self.lf_Hscr.sizePolicy().hasHeightForWidth())
        self.lf_Hscr.setSizePolicy(sizePolicy)
        self.lf_Hscr.setMinimumSize(QSize(70, 0))
        self.lf_Hscr.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_Hscr, 0, 1, 1, 1)

        self.lf_Lscr = FloatEdit(self.g_ring)
        self.lf_Lscr.setObjectName("lf_Lscr")
        sizePolicy.setHeightForWidth(self.lf_Lscr.sizePolicy().hasHeightForWidth())
        self.lf_Lscr.setSizePolicy(sizePolicy)
        self.lf_Lscr.setMinimumSize(QSize(70, 0))
        self.lf_Lscr.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_Lscr, 1, 1, 1, 1)

        self.unit_Lewout = QLabel(self.g_ring)
        self.unit_Lewout.setObjectName("unit_Lewout")
        self.unit_Lewout.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.unit_Lewout, 2, 2, 1, 1)

        self.in_Lewout = QLabel(self.g_ring)
        self.in_Lewout.setObjectName("in_Lewout")
        self.in_Lewout.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.in_Lewout, 2, 0, 1, 1)

        self.in_Lscr = QLabel(self.g_ring)
        self.in_Lscr.setObjectName("in_Lscr")
        self.in_Lscr.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.in_Lscr, 1, 0, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.w_mat_scr = WMatSelectV(self.g_ring)
        self.w_mat_scr.setObjectName("w_mat_scr")
        self.w_mat_scr.setMinimumSize(QSize(100, 0))

        self.verticalLayout_2.addWidget(self.w_mat_scr)

        self.verticalLayout_4.addWidget(self.g_ring)

        self.g_bar = QGroupBox(self.scrollAreaWidgetContents)
        self.g_bar.setObjectName("g_bar")
        self.verticalLayout = QVBoxLayout(self.g_bar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.c_bar_type = QComboBox(self.g_bar)
        self.c_bar_type.addItem("")
        self.c_bar_type.addItem("")
        self.c_bar_type.setObjectName("c_bar_type")
        self.c_bar_type.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.c_bar_type)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.w_bar = QWidget(self.g_bar)
        self.w_bar.setObjectName("w_bar")
        self.w_bar.setMaximumSize(QSize(299, 16777215))

        self.verticalLayout.addWidget(self.w_bar)

        self.verticalLayout_4.addWidget(self.g_bar)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.b_plot = QPushButton(SBar)
        self.b_plot.setObjectName("b_plot")

        self.horizontalLayout_3.addWidget(self.b_plot)

        self.b_previous = QPushButton(SBar)
        self.b_previous.setObjectName("b_previous")

        self.horizontalLayout_3.addWidget(self.b_previous)

        self.b_next = QPushButton(SBar)
        self.b_next.setObjectName("b_next")
        self.b_next.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.b_next)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        QWidget.setTabOrder(self.b_previous, self.b_plot)

        self.retranslateUi(SBar)

        QMetaObject.connectSlotsByName(SBar)

    # setupUi

    def retranslateUi(self, SBar):
        SBar.setWindowTitle(QCoreApplication.translate("SBar", "Form", None))
        self.img_ring.setText("")
        self.g_ring.setTitle(
            QCoreApplication.translate("SBar", "Short Circuit Ring", None)
        )
        self.unit_Hscr.setText(QCoreApplication.translate("SBar", "m", None))
        self.unit_Lscr.setText(QCoreApplication.translate("SBar", "m", None))
        self.in_Hscr.setText(QCoreApplication.translate("SBar", "Hscr :", None))
        self.unit_Lewout.setText(QCoreApplication.translate("SBar", "m", None))
        self.in_Lewout.setText(QCoreApplication.translate("SBar", "Lewout :", None))
        self.in_Lscr.setText(QCoreApplication.translate("SBar", "Lscr :", None))
        self.g_bar.setTitle(QCoreApplication.translate("SBar", "Bar", None))
        self.c_bar_type.setItemText(
            0, QCoreApplication.translate("SBar", "Rectangular bar", None)
        )
        self.c_bar_type.setItemText(
            1, QCoreApplication.translate("SBar", "Die cast bar", None)
        )

        self.b_plot.setText(QCoreApplication.translate("SBar", "Preview", None))
        self.b_previous.setText(QCoreApplication.translate("SBar", "Previous", None))
        self.b_next.setText(QCoreApplication.translate("SBar", "Save", None))

    # retranslateUi
