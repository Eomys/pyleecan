# -*- coding: utf-8 -*-

# File generated according to DXF.ui
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
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
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
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.in_zh = QtWidgets.QLabel(DXF)
        self.in_zh.setObjectName("in_zh")
        self.horizontalLayout_4.addWidget(self.in_zh)
        self.le_zh = QtWidgets.QSpinBox(DXF)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_zh.sizePolicy().hasHeightForWidth())
        self.le_zh.setSizePolicy(sizePolicy)
        self.le_zh.setMinimum(1)
        self.le_zh.setMaximum(1000)
        self.le_zh.setSingleStep(0)
        self.le_zh.setProperty("value", 36)
        self.le_zh.setObjectName("le_zh")
        self.horizontalLayout_4.addWidget(self.le_zh)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
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
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint
        )
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.in_coord_center = QtWidgets.QLabel(DXF)
        self.in_coord_center.setObjectName("in_coord_center")
        self.horizontalLayout_5.addWidget(self.in_coord_center)
        self.le_center_x = FloatEdit(DXF)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_center_x.sizePolicy().hasHeightForWidth())
        self.le_center_x.setSizePolicy(sizePolicy)
        self.le_center_x.setObjectName("le_center_x")
        self.horizontalLayout_5.addWidget(self.le_center_x)
        self.le_center_y = FloatEdit(DXF)
        self.le_center_y.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_center_y.sizePolicy().hasHeightForWidth())
        self.le_center_y.setSizePolicy(sizePolicy)
        self.le_center_y.setMaximumSize(QtCore.QSize(137, 16777215))
        self.le_center_y.setObjectName("le_center_y")
        self.horizontalLayout_5.addWidget(self.le_center_y)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.in_axe_angle = QtWidgets.QLabel(DXF)
        self.in_axe_angle.setObjectName("in_axe_angle")
        self.horizontalLayout_6.addWidget(self.in_axe_angle)
        self.le_axe_angle = FloatEdit(DXF)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_axe_angle.sizePolicy().hasHeightForWidth())
        self.le_axe_angle.setSizePolicy(sizePolicy)
        self.le_axe_angle.setObjectName("le_axe_angle")
        self.horizontalLayout_6.addWidget(self.le_axe_angle)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.w_surface_list = QtWidgets.QTableWidget(DXF)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
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
        self.b_plot = QtWidgets.QPushButton(DXF)
        self.b_plot.setObjectName("b_plot")
        self.horizontalLayout_2.addWidget(self.b_plot)
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
        self.in_zh.setText(_translate("DXF", "Number of hole"))
        self.in_mag_len.setText(_translate("DXF", "Magnet length"))
        self.le_mag_len.setText(_translate("DXF", "1"))
        self.in_coord_center.setText(_translate("DXF", "Machine center (x,y)"))
        self.le_center_x.setText(_translate("DXF", "0"))
        self.le_center_y.setText(_translate("DXF", "0"))
        self.in_axe_angle.setText(_translate("DXF", "Hole main axe angle"))
        self.le_axe_angle.setText(_translate("DXF", "0"))
        self.b_plot.setText(_translate("DXF", "Plot"))
        self.b_save.setText(_translate("DXF", "Save"))


from ...GUI.Tools.FloatEdit import FloatEdit
from ...GUI.Tools.WPathSelector.WPathSelector import WPathSelector
from .DXFGraphicsView import DXFGraphicsView
from pyleecan.GUI.Resources import pyleecan_rc
