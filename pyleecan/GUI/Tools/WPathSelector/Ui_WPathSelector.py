# -*- coding: utf-8 -*-

# File generated according to WPathSelector.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WPathSelector(object):
    def setupUi(self, WPathSelector):
        WPathSelector.setObjectName("WPathSelector")
        WPathSelector.resize(280, 32)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WPathSelector.sizePolicy().hasHeightForWidth())
        WPathSelector.setSizePolicy(sizePolicy)
        WPathSelector.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout = QtWidgets.QHBoxLayout(WPathSelector)
        self.horizontalLayout.setContentsMargins(4, 2, 4, 2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_path = QtWidgets.QLabel(WPathSelector)
        self.in_path.setObjectName("in_path")
        self.horizontalLayout.addWidget(self.in_path)
        self.le_path = QtWidgets.QLineEdit(WPathSelector)
        self.le_path.setMinimumSize(QtCore.QSize(150, 0))
        self.le_path.setObjectName("le_path")
        self.horizontalLayout.addWidget(self.le_path)
        self.b_path = QtWidgets.QPushButton(WPathSelector)
        self.b_path.setObjectName("b_path")
        self.horizontalLayout.addWidget(self.b_path)

        self.retranslateUi(WPathSelector)
        QtCore.QMetaObject.connectSlotsByName(WPathSelector)

    def retranslateUi(self, WPathSelector):
        _translate = QtCore.QCoreApplication.translate
        WPathSelector.setWindowTitle(_translate("WPathSelector", "Form"))
        self.in_path.setText(_translate("WPathSelector", "path"))
        self.b_path.setText(_translate("WPathSelector", "Select Path"))


from pyleecan.GUI.Resources import pyleecan_rc
