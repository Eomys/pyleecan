# -*- coding: utf-8 -*-

# File generated according to WImportLinspace.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WImportLinspace(object):
    def setupUi(self, WImportLinspace):
        WImportLinspace.setObjectName("WImportLinspace")
        WImportLinspace.resize(330, 73)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WImportLinspace.sizePolicy().hasHeightForWidth())
        WImportLinspace.setSizePolicy(sizePolicy)
        WImportLinspace.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(WImportLinspace)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.c_type_lin = QtWidgets.QComboBox(WImportLinspace)
        self.c_type_lin.setObjectName("c_type_lin")
        self.c_type_lin.addItem("")
        self.c_type_lin.addItem("")
        self.horizontalLayout.addWidget(self.c_type_lin)
        self.is_end = QtWidgets.QCheckBox(WImportLinspace)
        self.is_end.setObjectName("is_end")
        self.horizontalLayout.addWidget(self.is_end)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.in_start = QtWidgets.QLabel(WImportLinspace)
        self.in_start.setObjectName("in_start")
        self.horizontalLayout_2.addWidget(self.in_start)
        self.lf_start = FloatEdit(WImportLinspace)
        self.lf_start.setMinimumSize(QtCore.QSize(40, 0))
        self.lf_start.setObjectName("lf_start")
        self.horizontalLayout_2.addWidget(self.lf_start)
        self.in_N = QtWidgets.QLabel(WImportLinspace)
        self.in_N.setObjectName("in_N")
        self.horizontalLayout_2.addWidget(self.in_N)
        self.si_N = QtWidgets.QSpinBox(WImportLinspace)
        self.si_N.setMinimumSize(QtCore.QSize(40, 0))
        self.si_N.setMinimum(1)
        self.si_N.setMaximum(999999999)
        self.si_N.setObjectName("si_N")
        self.horizontalLayout_2.addWidget(self.si_N)
        self.in_step = QtWidgets.QLabel(WImportLinspace)
        self.in_step.setObjectName("in_step")
        self.horizontalLayout_2.addWidget(self.in_step)
        self.lf_step = FloatEdit(WImportLinspace)
        self.lf_step.setMinimumSize(QtCore.QSize(40, 0))
        self.lf_step.setObjectName("lf_step")
        self.horizontalLayout_2.addWidget(self.lf_step)
        self.in_stop = QtWidgets.QLabel(WImportLinspace)
        self.in_stop.setObjectName("in_stop")
        self.horizontalLayout_2.addWidget(self.in_stop)
        self.lf_stop = FloatEdit(WImportLinspace)
        self.lf_stop.setMinimumSize(QtCore.QSize(40, 0))
        self.lf_stop.setObjectName("lf_stop")
        self.horizontalLayout_2.addWidget(self.lf_stop)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(WImportLinspace)
        QtCore.QMetaObject.connectSlotsByName(WImportLinspace)

    def retranslateUi(self, WImportLinspace):
        _translate = QtCore.QCoreApplication.translate
        WImportLinspace.setWindowTitle(_translate("WImportLinspace", "Form"))
        self.c_type_lin.setItemText(0, _translate("WImportLinspace", "Start, End, N"))
        self.c_type_lin.setItemText(
            1, _translate("WImportLinspace", "Start, End, Step")
        )
        self.is_end.setText(_translate("WImportLinspace", "Include End Point"))
        self.in_start.setText(_translate("WImportLinspace", "Start: "))
        self.in_N.setText(_translate("WImportLinspace", "N: "))
        self.in_step.setText(_translate("WImportLinspace", "Step: "))
        self.in_stop.setText(_translate("WImportLinspace", "Stop: "))


from .....GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
