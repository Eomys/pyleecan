# -*- coding: utf-8 -*-

# File generated according to WImportLinspace.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from .....GUI.Tools.FloatEdit import FloatEdit

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_WImportLinspace(object):
    def setupUi(self, WImportLinspace):
        if not WImportLinspace.objectName():
            WImportLinspace.setObjectName("WImportLinspace")
        WImportLinspace.resize(330, 73)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WImportLinspace.sizePolicy().hasHeightForWidth())
        WImportLinspace.setSizePolicy(sizePolicy)
        WImportLinspace.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(WImportLinspace)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.c_type_lin = QComboBox(WImportLinspace)
        self.c_type_lin.addItem("")
        self.c_type_lin.addItem("")
        self.c_type_lin.setObjectName("c_type_lin")

        self.horizontalLayout.addWidget(self.c_type_lin)

        self.is_end = QCheckBox(WImportLinspace)
        self.is_end.setObjectName("is_end")

        self.horizontalLayout.addWidget(self.is_end)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.in_start = QLabel(WImportLinspace)
        self.in_start.setObjectName("in_start")

        self.horizontalLayout_2.addWidget(self.in_start)

        self.lf_start = FloatEdit(WImportLinspace)
        self.lf_start.setObjectName("lf_start")
        self.lf_start.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_2.addWidget(self.lf_start)

        self.in_N = QLabel(WImportLinspace)
        self.in_N.setObjectName("in_N")

        self.horizontalLayout_2.addWidget(self.in_N)

        self.si_N = QSpinBox(WImportLinspace)
        self.si_N.setObjectName("si_N")
        self.si_N.setMinimumSize(QSize(40, 0))
        self.si_N.setMinimum(1)
        self.si_N.setMaximum(999999999)

        self.horizontalLayout_2.addWidget(self.si_N)

        self.in_step = QLabel(WImportLinspace)
        self.in_step.setObjectName("in_step")

        self.horizontalLayout_2.addWidget(self.in_step)

        self.lf_step = FloatEdit(WImportLinspace)
        self.lf_step.setObjectName("lf_step")
        self.lf_step.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_2.addWidget(self.lf_step)

        self.in_stop = QLabel(WImportLinspace)
        self.in_stop.setObjectName("in_stop")

        self.horizontalLayout_2.addWidget(self.in_stop)

        self.lf_stop = FloatEdit(WImportLinspace)
        self.lf_stop.setObjectName("lf_stop")
        self.lf_stop.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_2.addWidget(self.lf_stop)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(WImportLinspace)

        QMetaObject.connectSlotsByName(WImportLinspace)

    # setupUi

    def retranslateUi(self, WImportLinspace):
        WImportLinspace.setWindowTitle(
            QCoreApplication.translate("WImportLinspace", "Form", None)
        )
        self.c_type_lin.setItemText(
            0, QCoreApplication.translate("WImportLinspace", "Start, End, N", None)
        )
        self.c_type_lin.setItemText(
            1, QCoreApplication.translate("WImportLinspace", "Start, End, Step", None)
        )

        self.is_end.setText(
            QCoreApplication.translate("WImportLinspace", "Include End Point", None)
        )
        self.in_start.setText(
            QCoreApplication.translate("WImportLinspace", "Start: ", None)
        )
        self.in_N.setText(QCoreApplication.translate("WImportLinspace", "N: ", None))
        self.in_step.setText(
            QCoreApplication.translate("WImportLinspace", "Step: ", None)
        )
        self.in_stop.setText(
            QCoreApplication.translate("WImportLinspace", "Stop: ", None)
        )

    # retranslateUi
