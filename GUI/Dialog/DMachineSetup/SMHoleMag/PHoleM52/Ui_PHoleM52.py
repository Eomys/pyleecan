# -*- coding: utf-8 -*-

# File generated according to PHoleM52.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PHoleM52(object):
    def setupUi(self, PHoleM52):
        PHoleM52.setObjectName("PHoleM52")
        PHoleM52.resize(740, 440)
        PHoleM52.setMinimumSize(QtCore.QSize(740, 440))
        PHoleM52.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(PHoleM52)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.img_slot = QtWidgets.QLabel(PHoleM52)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMinimumSize(QtCore.QSize(500, 213))
        self.img_slot.setMaximumSize(QtCore.QSize(500, 213))
        self.img_slot.setText("")
        self.img_slot.setPixmap(
            QtGui.QPixmap(":/images/images/MachineSetup/WSlot/Slot_52.PNG")
        )
        self.img_slot.setScaledContents(True)
        self.img_slot.setObjectName("img_slot")
        self.verticalLayout_3.addWidget(self.img_slot)
        self.txt_constraint = QtWidgets.QTextEdit(PHoleM52)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy)
        self.txt_constraint.setMinimumSize(QtCore.QSize(200, 0))
        self.txt_constraint.setMaximumSize(QtCore.QSize(16777215, 60))
        self.txt_constraint.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_constraint.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse
        )
        self.txt_constraint.setObjectName("txt_constraint")
        self.verticalLayout_3.addWidget(self.txt_constraint)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_W3 = QtWidgets.QLabel(PHoleM52)
        self.in_W3.setObjectName("in_W3")
        self.gridLayout.addWidget(self.in_W3, 4, 0, 1, 1)
        self.lf_W3 = FloatEdit(PHoleM52)
        self.lf_W3.setObjectName("lf_W3")
        self.gridLayout.addWidget(self.lf_W3, 4, 1, 1, 1)
        self.unit_W3 = QtWidgets.QLabel(PHoleM52)
        self.unit_W3.setObjectName("unit_W3")
        self.gridLayout.addWidget(self.unit_W3, 4, 2, 1, 1)
        self.lf_H0 = FloatEdit(PHoleM52)
        self.lf_H0.setObjectName("lf_H0")
        self.gridLayout.addWidget(self.lf_H0, 0, 1, 1, 1)
        self.in_H0 = QtWidgets.QLabel(PHoleM52)
        self.in_H0.setObjectName("in_H0")
        self.gridLayout.addWidget(self.in_H0, 0, 0, 1, 1)
        self.unit_H1 = QtWidgets.QLabel(PHoleM52)
        self.unit_H1.setObjectName("unit_H1")
        self.gridLayout.addWidget(self.unit_H1, 1, 2, 1, 1)
        self.lf_H1 = FloatEdit(PHoleM52)
        self.lf_H1.setObjectName("lf_H1")
        self.gridLayout.addWidget(self.lf_H1, 1, 1, 1, 1)
        self.in_H1 = QtWidgets.QLabel(PHoleM52)
        self.in_H1.setObjectName("in_H1")
        self.gridLayout.addWidget(self.in_H1, 1, 0, 1, 1)
        self.unit_H0 = QtWidgets.QLabel(PHoleM52)
        self.unit_H0.setObjectName("unit_H0")
        self.gridLayout.addWidget(self.unit_H0, 0, 2, 1, 1)
        self.in_H2 = QtWidgets.QLabel(PHoleM52)
        self.in_H2.setObjectName("in_H2")
        self.gridLayout.addWidget(self.in_H2, 2, 0, 1, 1)
        self.lf_H2 = FloatEdit(PHoleM52)
        self.lf_H2.setObjectName("lf_H2")
        self.gridLayout.addWidget(self.lf_H2, 2, 1, 1, 1)
        self.unit_H2 = QtWidgets.QLabel(PHoleM52)
        self.unit_H2.setObjectName("unit_H2")
        self.gridLayout.addWidget(self.unit_H2, 2, 2, 1, 1)
        self.in_W0 = QtWidgets.QLabel(PHoleM52)
        self.in_W0.setObjectName("in_W0")
        self.gridLayout.addWidget(self.in_W0, 3, 0, 1, 1)
        self.lf_W0 = FloatEdit(PHoleM52)
        self.lf_W0.setObjectName("lf_W0")
        self.gridLayout.addWidget(self.lf_W0, 3, 1, 1, 1)
        self.unit_W0 = QtWidgets.QLabel(PHoleM52)
        self.unit_W0.setObjectName("unit_W0")
        self.gridLayout.addWidget(self.unit_W0, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.w_mat_0 = WMatSelect(PHoleM52)
        self.w_mat_0.setMinimumSize(QtCore.QSize(100, 0))
        self.w_mat_0.setObjectName("w_mat_0")
        self.verticalLayout_2.addWidget(self.w_mat_0)
        self.g_output = QtWidgets.QGroupBox(PHoleM52)
        self.g_output.setMinimumSize(QtCore.QSize(200, 0))
        self.g_output.setObjectName("g_output")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.g_output)
        self.verticalLayout.setObjectName("verticalLayout")
        self.out_slot_surface = QtWidgets.QLabel(self.g_output)
        self.out_slot_surface.setObjectName("out_slot_surface")
        self.verticalLayout.addWidget(self.out_slot_surface)
        self.out_magnet_surface = QtWidgets.QLabel(self.g_output)
        self.out_magnet_surface.setObjectName("out_magnet_surface")
        self.verticalLayout.addWidget(self.out_magnet_surface)
        self.out_alpha = QtWidgets.QLabel(self.g_output)
        self.out_alpha.setObjectName("out_alpha")
        self.verticalLayout.addWidget(self.out_alpha)
        self.out_W1 = QtWidgets.QLabel(self.g_output)
        self.out_W1.setObjectName("out_W1")
        self.verticalLayout.addWidget(self.out_W1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.g_output)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(PHoleM52)
        QtCore.QMetaObject.connectSlotsByName(PHoleM52)
        PHoleM52.setTabOrder(self.lf_H0, self.lf_H1)
        PHoleM52.setTabOrder(self.lf_H1, self.lf_H2)
        PHoleM52.setTabOrder(self.lf_H2, self.lf_W0)
        PHoleM52.setTabOrder(self.lf_W0, self.lf_W3)
        PHoleM52.setTabOrder(self.lf_W3, self.txt_constraint)

    def retranslateUi(self, PHoleM52):
        _translate = QtCore.QCoreApplication.translate
        PHoleM52.setWindowTitle(_translate("PHoleM52", "Form"))
        self.txt_constraint.setHtml(
            _translate(
                "PHoleM52",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\'; font-size:14pt;">H2 &lt; H1</span></p>\n'
                '<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;"><br /></p></body></html>',
            )
        )
        self.in_W3.setText(_translate("PHoleM52", "W3 :"))
        self.unit_W3.setText(_translate("PHoleM52", "m"))
        self.in_H0.setText(_translate("PHoleM52", "H0 :"))
        self.unit_H1.setText(_translate("PHoleM52", "m"))
        self.in_H1.setText(_translate("PHoleM52", "H1 :"))
        self.unit_H0.setText(_translate("PHoleM52", "m"))
        self.in_H2.setText(_translate("PHoleM52", "H2 :"))
        self.unit_H2.setText(_translate("PHoleM52", "m"))
        self.in_W0.setText(_translate("PHoleM52", "W0 :"))
        self.unit_W0.setText(_translate("PHoleM52", "m"))
        self.g_output.setTitle(_translate("PHoleM52", "Output"))
        self.out_slot_surface.setText(_translate("PHoleM52", "Slot suface : ?"))
        self.out_magnet_surface.setText(_translate("PHoleM52", "Magnet surface : ?"))
        self.out_alpha.setText(_translate("PHoleM52", "Alpha : ?"))
        self.out_W1.setText(_translate("PHoleM52", "W1 : ?"))


from pyleecan.GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect
from pyleecan.GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
