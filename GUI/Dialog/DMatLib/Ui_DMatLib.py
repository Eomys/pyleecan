# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\pyleecan\GUI\Dialog\DMatLib\DMatLib.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DMatLib(object):
    def setupUi(self, DMatLib):
        DMatLib.setObjectName("DMatLib")
        DMatLib.resize(746, 534)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(DMatLib)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.le_search = QtWidgets.QLineEdit(DMatLib)
        self.le_search.setObjectName("le_search")
        self.horizontalLayout_9.addWidget(self.le_search)
        self.img_search = QtWidgets.QLabel(DMatLib)
        self.img_search.setText("")
        self.img_search.setPixmap(
            QtGui.QPixmap(
                "\n"
                "                                                    :/images/images/icon/search.png\n"
                "                                                "
            )
        )
        self.img_search.setScaledContents(True)
        self.img_search.setObjectName("img_search")
        self.horizontalLayout_9.addWidget(self.img_search)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.c_search = QtWidgets.QComboBox(DMatLib)
        self.c_search.setObjectName("c_search")
        self.c_search.addItem("")
        self.c_search.addItem("")
        self.c_search.addItem("")
        self.c_search.addItem("")
        self.verticalLayout_3.addWidget(self.c_search)
        self.nav_mat = QtWidgets.QListWidget(DMatLib)
        self.nav_mat.setObjectName("nav_mat")
        self.verticalLayout_3.addWidget(self.nav_mat)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.b_edit = QtWidgets.QPushButton(DMatLib)
        self.b_edit.setObjectName("b_edit")
        self.horizontalLayout_8.addWidget(self.b_edit)
        self.b_duplicate = QtWidgets.QPushButton(DMatLib)
        self.b_duplicate.setObjectName("b_duplicate")
        self.horizontalLayout_8.addWidget(self.b_duplicate)
        self.b_delete = QtWidgets.QPushButton(DMatLib)
        self.b_delete.setObjectName("b_delete")
        self.horizontalLayout_8.addWidget(self.b_delete)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.out_name = QtWidgets.QLabel(DMatLib)
        self.out_name.setObjectName("out_name")
        self.verticalLayout_10.addWidget(self.out_name)
        self.out_type = QtWidgets.QLabel(DMatLib)
        self.out_type.setObjectName("out_type")
        self.verticalLayout_10.addWidget(self.out_type)
        self.out_iso = QtWidgets.QLabel(DMatLib)
        self.out_iso.setObjectName("out_iso")
        self.verticalLayout_10.addWidget(self.out_iso)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.g_elec = QtWidgets.QGroupBox(DMatLib)
        self.g_elec.setObjectName("g_elec")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.g_elec)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.out_rho_elec = QtWidgets.QLabel(self.g_elec)
        self.out_rho_elec.setObjectName("out_rho_elec")
        self.verticalLayout_4.addWidget(self.out_rho_elec)
        self.out_epsr = QtWidgets.QLabel(self.g_elec)
        self.out_epsr.setObjectName("out_epsr")
        self.verticalLayout_4.addWidget(self.out_epsr)
        self.gridLayout.addWidget(self.g_elec, 0, 0, 1, 1)
        self.g_eco = QtWidgets.QGroupBox(DMatLib)
        self.g_eco.setObjectName("g_eco")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.g_eco)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.out_cost_unit = QtWidgets.QLabel(self.g_eco)
        self.out_cost_unit.setObjectName("out_cost_unit")
        self.verticalLayout_5.addWidget(self.out_cost_unit)
        self.gridLayout.addWidget(self.g_eco, 0, 1, 1, 1)
        self.g_thermics = QtWidgets.QGroupBox(DMatLib)
        self.g_thermics.setObjectName("g_thermics")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.g_thermics)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.out_Cp = QtWidgets.QLabel(self.g_thermics)
        self.out_Cp.setObjectName("out_Cp")
        self.verticalLayout_6.addWidget(self.out_Cp)
        self.out_alpha = QtWidgets.QLabel(self.g_thermics)
        self.out_alpha.setObjectName("out_alpha")
        self.verticalLayout_6.addWidget(self.out_alpha)
        self.nav_iso_therm = QtWidgets.QStackedWidget(self.g_thermics)
        self.nav_iso_therm.setObjectName("nav_iso_therm")
        self.page_iso_therm = QtWidgets.QWidget()
        self.page_iso_therm.setObjectName("page_iso_therm")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_iso_therm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.out_L = QtWidgets.QLabel(self.page_iso_therm)
        self.out_L.setObjectName("out_L")
        self.verticalLayout.addWidget(self.out_L)
        self.nav_iso_therm.addWidget(self.page_iso_therm)
        self.page_niso_therm = QtWidgets.QWidget()
        self.page_niso_therm.setObjectName("page_niso_therm")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_niso_therm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.out_LX = QtWidgets.QLabel(self.page_niso_therm)
        self.out_LX.setObjectName("out_LX")
        self.verticalLayout_2.addWidget(self.out_LX)
        self.out_LY = QtWidgets.QLabel(self.page_niso_therm)
        self.out_LY.setObjectName("out_LY")
        self.verticalLayout_2.addWidget(self.out_LY)
        self.out_LZ = QtWidgets.QLabel(self.page_niso_therm)
        self.out_LZ.setObjectName("out_LZ")
        self.verticalLayout_2.addWidget(self.out_LZ)
        self.nav_iso_therm.addWidget(self.page_niso_therm)
        self.verticalLayout_6.addWidget(self.nav_iso_therm)
        self.gridLayout.addWidget(self.g_thermics, 1, 0, 1, 1)
        self.g_mechanics = QtWidgets.QGroupBox(DMatLib)
        self.g_mechanics.setObjectName("g_mechanics")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.g_mechanics)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.out_rho_meca = QtWidgets.QLabel(self.g_mechanics)
        self.out_rho_meca.setObjectName("out_rho_meca")
        self.verticalLayout_9.addWidget(self.out_rho_meca)
        self.nav_iso_meca = QtWidgets.QStackedWidget(self.g_mechanics)
        self.nav_iso_meca.setObjectName("nav_iso_meca")
        self.page_iso_meca = QtWidgets.QWidget()
        self.page_iso_meca.setObjectName("page_iso_meca")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_iso_meca)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.out_E = QtWidgets.QLabel(self.page_iso_meca)
        self.out_E.setObjectName("out_E")
        self.verticalLayout_7.addWidget(self.out_E)
        self.out_nu = QtWidgets.QLabel(self.page_iso_meca)
        self.out_nu.setObjectName("out_nu")
        self.verticalLayout_7.addWidget(self.out_nu)
        self.out_G = QtWidgets.QLabel(self.page_iso_meca)
        self.out_G.setObjectName("out_G")
        self.verticalLayout_7.addWidget(self.out_G)
        self.nav_iso_meca.addWidget(self.page_iso_meca)
        self.page_nios_meca = QtWidgets.QWidget()
        self.page_nios_meca.setObjectName("page_nios_meca")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_nios_meca)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.in_E = QtWidgets.QLabel(self.page_nios_meca)
        self.in_E.setObjectName("in_E")
        self.gridLayout_2.addWidget(self.in_E, 1, 0, 1, 1)
        self.out_EX = QtWidgets.QLabel(self.page_nios_meca)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_EX.sizePolicy().hasHeightForWidth())
        self.out_EX.setSizePolicy(sizePolicy)
        self.out_EX.setMinimumSize(QtCore.QSize(50, 20))
        self.out_EX.setMaximumSize(QtCore.QSize(50, 20))
        self.out_EX.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.out_EX.setObjectName("out_EX")
        self.gridLayout_2.addWidget(self.out_EX, 1, 1, 1, 1)
        self.out_EY = QtWidgets.QLabel(self.page_nios_meca)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_EY.sizePolicy().hasHeightForWidth())
        self.out_EY.setSizePolicy(sizePolicy)
        self.out_EY.setMinimumSize(QtCore.QSize(50, 20))
        self.out_EY.setMaximumSize(QtCore.QSize(50, 20))
        self.out_EY.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.out_EY.setObjectName("out_EY")
        self.gridLayout_2.addWidget(self.out_EY, 1, 2, 1, 1)
        self.out_EZ = QtWidgets.QLabel(self.page_nios_meca)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_EZ.sizePolicy().hasHeightForWidth())
        self.out_EZ.setSizePolicy(sizePolicy)
        self.out_EZ.setMinimumSize(QtCore.QSize(50, 20))
        self.out_EZ.setMaximumSize(QtCore.QSize(50, 20))
        self.out_EZ.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.out_EZ.setObjectName("out_EZ")
        self.gridLayout_2.addWidget(self.out_EZ, 1, 3, 1, 1)
        self.in_nu = QtWidgets.QLabel(self.page_nios_meca)
        self.in_nu.setObjectName("in_nu")
        self.gridLayout_2.addWidget(self.in_nu, 3, 0, 1, 1)
        self.out_nu_XY = QtWidgets.QLabel(self.page_nios_meca)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_nu_XY.sizePolicy().hasHeightForWidth())
        self.out_nu_XY.setSizePolicy(sizePolicy)
        self.out_nu_XY.setMinimumSize(QtCore.QSize(50, 20))
        self.out_nu_XY.setMaximumSize(QtCore.QSize(50, 20))
        self.out_nu_XY.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.out_nu_XY.setObjectName("out_nu_XY")
        self.gridLayout_2.addWidget(self.out_nu_XY, 3, 1, 1, 1)
        self.out_nu_XZ = QtWidgets.QLabel(self.page_nios_meca)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_nu_XZ.sizePolicy().hasHeightForWidth())
        self.out_nu_XZ.setSizePolicy(sizePolicy)
        self.out_nu_XZ.setMinimumSize(QtCore.QSize(50, 20))
        self.out_nu_XZ.setMaximumSize(QtCore.QSize(50, 20))
        self.out_nu_XZ.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.out_nu_XZ.setObjectName("out_nu_XZ")
        self.gridLayout_2.addWidget(self.out_nu_XZ, 3, 2, 1, 1)
        self.out_nu_YZ = QtWidgets.QLabel(self.page_nios_meca)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_nu_YZ.sizePolicy().hasHeightForWidth())
        self.out_nu_YZ.setSizePolicy(sizePolicy)
        self.out_nu_YZ.setMinimumSize(QtCore.QSize(50, 20))
        self.out_nu_YZ.setMaximumSize(QtCore.QSize(50, 20))
        self.out_nu_YZ.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.out_nu_YZ.setObjectName("out_nu_YZ")
        self.gridLayout_2.addWidget(self.out_nu_YZ, 3, 3, 1, 1)
        self.in_G = QtWidgets.QLabel(self.page_nios_meca)
        self.in_G.setObjectName("in_G")
        self.gridLayout_2.addWidget(self.in_G, 4, 0, 1, 1)
        self.out_GXY = QtWidgets.QLabel(self.page_nios_meca)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_GXY.sizePolicy().hasHeightForWidth())
        self.out_GXY.setSizePolicy(sizePolicy)
        self.out_GXY.setMinimumSize(QtCore.QSize(50, 20))
        self.out_GXY.setMaximumSize(QtCore.QSize(50, 20))
        self.out_GXY.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.out_GXY.setObjectName("out_GXY")
        self.gridLayout_2.addWidget(self.out_GXY, 4, 1, 1, 1)
        self.out_GXZ = QtWidgets.QLabel(self.page_nios_meca)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_GXZ.sizePolicy().hasHeightForWidth())
        self.out_GXZ.setSizePolicy(sizePolicy)
        self.out_GXZ.setMinimumSize(QtCore.QSize(50, 20))
        self.out_GXZ.setMaximumSize(QtCore.QSize(50, 20))
        self.out_GXZ.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.out_GXZ.setObjectName("out_GXZ")
        self.gridLayout_2.addWidget(self.out_GXZ, 4, 2, 1, 1)
        self.out_GYZ = QtWidgets.QLabel(self.page_nios_meca)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_GYZ.sizePolicy().hasHeightForWidth())
        self.out_GYZ.setSizePolicy(sizePolicy)
        self.out_GYZ.setMinimumSize(QtCore.QSize(50, 20))
        self.out_GYZ.setMaximumSize(QtCore.QSize(50, 20))
        self.out_GYZ.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.out_GYZ.setObjectName("out_GYZ")
        self.gridLayout_2.addWidget(self.out_GYZ, 4, 3, 1, 1)
        self.in_XY = QtWidgets.QLabel(self.page_nios_meca)
        self.in_XY.setObjectName("in_XY")
        self.gridLayout_2.addWidget(self.in_XY, 2, 1, 1, 1)
        self.in_XZ = QtWidgets.QLabel(self.page_nios_meca)
        self.in_XZ.setObjectName("in_XZ")
        self.gridLayout_2.addWidget(self.in_XZ, 2, 2, 1, 1)
        self.in_Y = QtWidgets.QLabel(self.page_nios_meca)
        self.in_Y.setObjectName("in_Y")
        self.gridLayout_2.addWidget(self.in_Y, 0, 2, 1, 1)
        self.in_X = QtWidgets.QLabel(self.page_nios_meca)
        self.in_X.setObjectName("in_X")
        self.gridLayout_2.addWidget(self.in_X, 0, 1, 1, 1)
        self.in_YZ = QtWidgets.QLabel(self.page_nios_meca)
        self.in_YZ.setObjectName("in_YZ")
        self.gridLayout_2.addWidget(self.in_YZ, 2, 3, 1, 1)
        self.in_Z = QtWidgets.QLabel(self.page_nios_meca)
        self.in_Z.setObjectName("in_Z")
        self.gridLayout_2.addWidget(self.in_Z, 0, 3, 1, 1)
        self.nav_iso_meca.addWidget(self.page_nios_meca)
        self.verticalLayout_9.addWidget(self.nav_iso_meca)
        self.gridLayout.addWidget(self.g_mechanics, 1, 1, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout)
        self.g_mag = QtWidgets.QGroupBox(DMatLib)
        self.g_mag.setObjectName("g_mag")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.g_mag)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.out_mur_lin = QtWidgets.QLabel(self.g_mag)
        self.out_mur_lin.setObjectName("out_mur_lin")
        self.verticalLayout_8.addWidget(self.out_mur_lin)
        self.out_Brm20 = QtWidgets.QLabel(self.g_mag)
        self.out_Brm20.setObjectName("out_Brm20")
        self.verticalLayout_8.addWidget(self.out_Brm20)
        self.out_alpha_Br = QtWidgets.QLabel(self.g_mag)
        self.out_alpha_Br.setObjectName("out_alpha_Br")
        self.verticalLayout_8.addWidget(self.out_alpha_Br)
        self.out_wlam = QtWidgets.QLabel(self.g_mag)
        self.out_wlam.setObjectName("out_wlam")
        self.verticalLayout_8.addWidget(self.out_wlam)
        self.verticalLayout_10.addWidget(self.g_mag)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_10.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.b_close = QtWidgets.QDialogButtonBox(DMatLib)
        self.b_close.setOrientation(QtCore.Qt.Horizontal)
        self.b_close.setStandardButtons(QtWidgets.QDialogButtonBox.NoButton)
        self.b_close.setObjectName("b_close")
        self.verticalLayout_11.addWidget(self.b_close)
        self.b_close.raise_()

        self.retranslateUi(DMatLib)
        self.nav_iso_therm.setCurrentIndex(0)
        self.nav_iso_meca.setCurrentIndex(1)
        self.b_close.accepted.connect(DMatLib.accept)
        self.b_close.rejected.connect(DMatLib.reject)
        QtCore.QMetaObject.connectSlotsByName(DMatLib)

    def retranslateUi(self, DMatLib):
        _translate = QtCore.QCoreApplication.translate
        DMatLib.setWindowTitle(_translate("DMatLib", "Material Library"))
        self.c_search.setItemText(0, _translate("DMatLib", "All"))
        self.c_search.setItemText(1, _translate("DMatLib", "Lamination"))
        self.c_search.setItemText(2, _translate("DMatLib", "Magnet"))
        self.c_search.setItemText(3, _translate("DMatLib", "Raw"))
        self.b_edit.setText(_translate("DMatLib", "Edit"))
        self.b_duplicate.setText(_translate("DMatLib", "New from"))
        self.b_delete.setText(_translate("DMatLib", "Delete"))
        self.out_name.setText(_translate("DMatLib", "name : M400-50A"))
        self.out_type.setText(_translate("DMatLib", "Raw Material"))
        self.out_iso.setText(_translate("DMatLib", "isotropic"))
        self.g_elec.setTitle(_translate("DMatLib", "Electrical"))
        self.out_rho_elec.setText(_translate("DMatLib", "rho = 10e-3 ohm.m"))
        self.out_epsr.setText(_translate("DMatLib", "epsr = 0.5"))
        self.g_eco.setTitle(_translate("DMatLib", "Economical"))
        self.out_cost_unit.setText(
            _translate("DMatLib", "cost_unit = 10.5 €/kg          ")
        )
        self.g_thermics.setTitle(_translate("DMatLib", "Thermics"))
        self.out_Cp.setText(_translate("DMatLib", "Cp = 0.52 W/kg/K            "))
        self.out_alpha.setText(_translate("DMatLib", "alpha = 0.52"))
        self.out_L.setText(_translate("DMatLib", "Lambda = 5200 W/K"))
        self.out_LX.setText(_translate("DMatLib", "Lambda X = 5200 W/K"))
        self.out_LY.setText(_translate("DMatLib", "Lambda Y = 5200 W/K"))
        self.out_LZ.setText(_translate("DMatLib", "Lambda Z = 5200 W/K"))
        self.g_mechanics.setTitle(_translate("DMatLib", "Mechanics"))
        self.out_rho_meca.setText(_translate("DMatLib", "rho = 7500 kg/m^3 "))
        self.out_E.setText(_translate("DMatLib", "E = 2360 Pa"))
        self.out_nu.setText(_translate("DMatLib", "nu = 0.5"))
        self.out_G.setText(_translate("DMatLib", "G = 10.000 Pa"))
        self.in_E.setText(_translate("DMatLib", "E"))
        self.out_EX.setText(
            _translate(
                "DMatLib",
                "\n"
                "                                                                                1.23e+10\n"
                "                                                                            ",
            )
        )
        self.out_EY.setText(
            _translate(
                "DMatLib",
                "\n"
                "                                                                                10\n"
                "                                                                            ",
            )
        )
        self.out_EZ.setText(
            _translate(
                "DMatLib",
                "\n"
                "                                                                                55.3\n"
                "                                                                            ",
            )
        )
        self.in_nu.setText(_translate("DMatLib", "nu"))
        self.out_nu_XY.setText(
            _translate(
                "DMatLib",
                "\n"
                "                                                                                0.5\n"
                "                                                                            ",
            )
        )
        self.out_nu_XZ.setText(
            _translate(
                "DMatLib",
                "\n"
                "                                                                                0.5\n"
                "                                                                            ",
            )
        )
        self.out_nu_YZ.setText(
            _translate(
                "DMatLib",
                "\n"
                "                                                                                0.6\n"
                "                                                                            ",
            )
        )
        self.in_G.setText(_translate("DMatLib", "G"))
        self.out_GXY.setText(
            _translate(
                "DMatLib",
                "\n"
                "                                                                                1023\n"
                "                                                                            ",
            )
        )
        self.out_GXZ.setText(
            _translate(
                "DMatLib",
                "\n"
                "                                                                                1024\n"
                "                                                                            ",
            )
        )
        self.out_GYZ.setText(
            _translate(
                "DMatLib",
                "\n"
                "                                                                                1024\n"
                "                                                                            ",
            )
        )
        self.in_XY.setText(_translate("DMatLib", "XY"))
        self.in_XZ.setText(_translate("DMatLib", "XZ"))
        self.in_Y.setText(_translate("DMatLib", "Y"))
        self.in_X.setText(_translate("DMatLib", "X"))
        self.in_YZ.setText(_translate("DMatLib", "YZ"))
        self.in_Z.setText(_translate("DMatLib", "Z"))
        self.g_mag.setTitle(_translate("DMatLib", "Magnetics"))
        self.out_mur_lin.setText(_translate("DMatLib", "mur_lin = 0.555"))
        self.out_Brm20.setText(_translate("DMatLib", "Brm20 = 1 T"))
        self.out_alpha_Br.setText(_translate("DMatLib", "alpha_Br=0.1"))
        self.out_wlam.setText(_translate("DMatLib", "wlam = 0.5 m"))


from pyleecan.GUI.Resources import pyleecan_rc
