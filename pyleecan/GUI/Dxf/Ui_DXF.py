# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\pyleecan\pyleecan\GUI\Dxf\DXF.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DXF(object):
    def setupUi(self, DXF):
        DXF.setObjectName("DXF")
        DXF.resize(746, 536)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(DXF)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.viewer = DXFGraphicsView(DXF)
        self.viewer.setObjectName("viewer")
        self.horizontalLayout.addWidget(self.viewer)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.w_path_selector = WPathSelector(DXF)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.w_path_selector.sizePolicy().hasHeightForWidth()
        )
        self.w_path_selector.setSizePolicy(sizePolicy)
        self.w_path_selector.setObjectName("w_path_selector")
        self.verticalLayout.addWidget(self.w_path_selector)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.in_mag_len = QtWidgets.QLabel(DXF)
        self.in_mag_len.setObjectName("in_mag_len")
        self.horizontalLayout_3.addWidget(self.in_mag_len)
        self.le_mag_len = FloatEdit(DXF)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_mag_len.sizePolicy().hasHeightForWidth())
        self.le_mag_len.setSizePolicy(sizePolicy)
        self.le_mag_len.setObjectName("le_mag_len")
        self.horizontalLayout_3.addWidget(self.le_mag_len)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.w_surface_list = QtWidgets.QTableWidget(DXF)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.w_surface_list.sizePolicy().hasHeightForWidth()
        )
        self.w_surface_list.setSizePolicy(sizePolicy)
        self.w_surface_list.setObjectName("w_surface_list")
        self.w_surface_list.setColumnCount(0)
        self.w_surface_list.setRowCount(0)
        self.verticalLayout.addWidget(self.w_surface_list)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(DXF)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem)
        self.b_save = QtWidgets.QPushButton(DXF)
        self.b_save.setObjectName("b_save")
        self.horizontalLayout_2.addWidget(self.b_save)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.retranslateUi(DXF)
        QtCore.QMetaObject.connectSlotsByName(DXF)

    def retranslateUi(self, DXF):
        _translate = QtCore.QCoreApplication.translate
        DXF.setWindowTitle(_translate("DXF", "Material Library"))
        self.in_mag_len.setText(_translate("DXF", "Magnet length"))
        self.pushButton.setText(_translate("DXF", "PushButton"))
        self.b_save.setText(_translate("DXF", "Save"))


from ...GUI.Tools.FloatEdit import FloatEdit
from ...GUI.Tools.WPathSelector.WPathSelector import WPathSelector
from .DXFGraphicsView import DXFGraphicsView
from pyleecan.GUI.Resources import pyleecan_rc
