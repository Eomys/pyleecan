# -*- coding: utf-8 -*-

# File generated according to DMatLib.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DMatLib(object):
    def setupUi(self, DMatLib):
        if not DMatLib.objectName():
            DMatLib.setObjectName(u"DMatLib")
        DMatLib.resize(746, 536)
        icon = QIcon()
        icon.addFile(
            u":/images/images/icon/pyleecan_64.png", QSize(), QIcon.Normal, QIcon.Off
        )
        DMatLib.setWindowIcon(icon)
        self.verticalLayout_11 = QVBoxLayout(DMatLib)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.le_search = QLineEdit(DMatLib)
        self.le_search.setObjectName(u"le_search")

        self.horizontalLayout_9.addWidget(self.le_search)

        self.img_search = QLabel(DMatLib)
        self.img_search.setObjectName(u"img_search")
        self.img_search.setPixmap(
            QPixmap(
                u"\n"
                "                                                    :/images/images/icon/search.png\n"
                "                                                "
            )
        )
        self.img_search.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.img_search)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.in_reference_mat_lib = QLabel(DMatLib)
        self.in_reference_mat_lib.setObjectName(u"in_reference_mat_lib")

        self.verticalLayout_12.addWidget(self.in_reference_mat_lib)

        self.nav_mat = QListWidget(DMatLib)
        self.nav_mat.setObjectName(u"nav_mat")

        self.verticalLayout_12.addWidget(self.nav_mat)

        self.in_machine_mat = QLabel(DMatLib)
        self.in_machine_mat.setObjectName(u"in_machine_mat")

        self.verticalLayout_12.addWidget(self.in_machine_mat)

        self.nav_mat_mach = QListWidget(DMatLib)
        self.nav_mat_mach.setObjectName(u"nav_mat_mach")

        self.verticalLayout_12.addWidget(self.nav_mat_mach)

        self.verticalLayout_3.addLayout(self.verticalLayout_12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.b_edit = QPushButton(DMatLib)
        self.b_edit.setObjectName(u"b_edit")

        self.horizontalLayout_8.addWidget(self.b_edit)

        self.b_duplicate = QPushButton(DMatLib)
        self.b_duplicate.setObjectName(u"b_duplicate")

        self.horizontalLayout_8.addWidget(self.b_duplicate)

        self.b_delete = QPushButton(DMatLib)
        self.b_delete.setObjectName(u"b_delete")

        self.horizontalLayout_8.addWidget(self.b_delete)

        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.out_name = QLabel(DMatLib)
        self.out_name.setObjectName(u"out_name")

        self.verticalLayout_10.addWidget(self.out_name)

        self.out_iso = QLabel(DMatLib)
        self.out_iso.setObjectName(u"out_iso")

        self.verticalLayout_10.addWidget(self.out_iso)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.g_elec = QGroupBox(DMatLib)
        self.g_elec.setObjectName(u"g_elec")
        self.verticalLayout_4 = QVBoxLayout(self.g_elec)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.out_rho_elec = QLabel(self.g_elec)
        self.out_rho_elec.setObjectName(u"out_rho_elec")

        self.verticalLayout_4.addWidget(self.out_rho_elec)

        self.out_epsr = QLabel(self.g_elec)
        self.out_epsr.setObjectName(u"out_epsr")

        self.verticalLayout_4.addWidget(self.out_epsr)

        self.gridLayout.addWidget(self.g_elec, 0, 0, 1, 1)

        self.g_eco = QGroupBox(DMatLib)
        self.g_eco.setObjectName(u"g_eco")
        self.verticalLayout_5 = QVBoxLayout(self.g_eco)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.out_cost_unit = QLabel(self.g_eco)
        self.out_cost_unit.setObjectName(u"out_cost_unit")

        self.verticalLayout_5.addWidget(self.out_cost_unit)

        self.gridLayout.addWidget(self.g_eco, 0, 1, 1, 1)

        self.g_thermics = QGroupBox(DMatLib)
        self.g_thermics.setObjectName(u"g_thermics")
        self.verticalLayout_6 = QVBoxLayout(self.g_thermics)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.out_Cp = QLabel(self.g_thermics)
        self.out_Cp.setObjectName(u"out_Cp")

        self.verticalLayout_6.addWidget(self.out_Cp)

        self.out_alpha = QLabel(self.g_thermics)
        self.out_alpha.setObjectName(u"out_alpha")

        self.verticalLayout_6.addWidget(self.out_alpha)

        self.nav_iso_therm = QStackedWidget(self.g_thermics)
        self.nav_iso_therm.setObjectName(u"nav_iso_therm")
        self.page_iso_therm = QWidget()
        self.page_iso_therm.setObjectName(u"page_iso_therm")
        self.verticalLayout = QVBoxLayout(self.page_iso_therm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.out_L = QLabel(self.page_iso_therm)
        self.out_L.setObjectName(u"out_L")

        self.verticalLayout.addWidget(self.out_L)

        self.nav_iso_therm.addWidget(self.page_iso_therm)
        self.page_niso_therm = QWidget()
        self.page_niso_therm.setObjectName(u"page_niso_therm")
        self.verticalLayout_2 = QVBoxLayout(self.page_niso_therm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.out_LX = QLabel(self.page_niso_therm)
        self.out_LX.setObjectName(u"out_LX")

        self.verticalLayout_2.addWidget(self.out_LX)

        self.out_LY = QLabel(self.page_niso_therm)
        self.out_LY.setObjectName(u"out_LY")

        self.verticalLayout_2.addWidget(self.out_LY)

        self.out_LZ = QLabel(self.page_niso_therm)
        self.out_LZ.setObjectName(u"out_LZ")

        self.verticalLayout_2.addWidget(self.out_LZ)

        self.nav_iso_therm.addWidget(self.page_niso_therm)

        self.verticalLayout_6.addWidget(self.nav_iso_therm)

        self.gridLayout.addWidget(self.g_thermics, 1, 0, 1, 1)

        self.g_mechanics = QGroupBox(DMatLib)
        self.g_mechanics.setObjectName(u"g_mechanics")
        self.verticalLayout_9 = QVBoxLayout(self.g_mechanics)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.out_rho_meca = QLabel(self.g_mechanics)
        self.out_rho_meca.setObjectName(u"out_rho_meca")

        self.verticalLayout_9.addWidget(self.out_rho_meca)

        self.nav_iso_meca = QStackedWidget(self.g_mechanics)
        self.nav_iso_meca.setObjectName(u"nav_iso_meca")
        self.page_iso_meca = QWidget()
        self.page_iso_meca.setObjectName(u"page_iso_meca")
        self.verticalLayout_7 = QVBoxLayout(self.page_iso_meca)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.out_E = QLabel(self.page_iso_meca)
        self.out_E.setObjectName(u"out_E")

        self.verticalLayout_7.addWidget(self.out_E)

        self.out_nu = QLabel(self.page_iso_meca)
        self.out_nu.setObjectName(u"out_nu")

        self.verticalLayout_7.addWidget(self.out_nu)

        self.out_G = QLabel(self.page_iso_meca)
        self.out_G.setObjectName(u"out_G")

        self.verticalLayout_7.addWidget(self.out_G)

        self.nav_iso_meca.addWidget(self.page_iso_meca)
        self.page_nios_meca = QWidget()
        self.page_nios_meca.setObjectName(u"page_nios_meca")
        self.gridLayout_2 = QGridLayout(self.page_nios_meca)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.in_E = QLabel(self.page_nios_meca)
        self.in_E.setObjectName(u"in_E")

        self.gridLayout_2.addWidget(self.in_E, 1, 0, 1, 1)

        self.out_EX = QLabel(self.page_nios_meca)
        self.out_EX.setObjectName(u"out_EX")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_EX.sizePolicy().hasHeightForWidth())
        self.out_EX.setSizePolicy(sizePolicy)
        self.out_EX.setMinimumSize(QSize(50, 20))
        self.out_EX.setMaximumSize(QSize(50, 20))
        self.out_EX.setFrameShape(QFrame.NoFrame)

        self.gridLayout_2.addWidget(self.out_EX, 1, 1, 1, 1)

        self.out_EY = QLabel(self.page_nios_meca)
        self.out_EY.setObjectName(u"out_EY")
        sizePolicy.setHeightForWidth(self.out_EY.sizePolicy().hasHeightForWidth())
        self.out_EY.setSizePolicy(sizePolicy)
        self.out_EY.setMinimumSize(QSize(50, 20))
        self.out_EY.setMaximumSize(QSize(50, 20))
        self.out_EY.setFrameShape(QFrame.NoFrame)

        self.gridLayout_2.addWidget(self.out_EY, 1, 2, 1, 1)

        self.out_EZ = QLabel(self.page_nios_meca)
        self.out_EZ.setObjectName(u"out_EZ")
        sizePolicy.setHeightForWidth(self.out_EZ.sizePolicy().hasHeightForWidth())
        self.out_EZ.setSizePolicy(sizePolicy)
        self.out_EZ.setMinimumSize(QSize(50, 20))
        self.out_EZ.setMaximumSize(QSize(50, 20))
        self.out_EZ.setFrameShape(QFrame.NoFrame)

        self.gridLayout_2.addWidget(self.out_EZ, 1, 3, 1, 1)

        self.in_nu = QLabel(self.page_nios_meca)
        self.in_nu.setObjectName(u"in_nu")

        self.gridLayout_2.addWidget(self.in_nu, 3, 0, 1, 1)

        self.out_nu_XY = QLabel(self.page_nios_meca)
        self.out_nu_XY.setObjectName(u"out_nu_XY")
        sizePolicy.setHeightForWidth(self.out_nu_XY.sizePolicy().hasHeightForWidth())
        self.out_nu_XY.setSizePolicy(sizePolicy)
        self.out_nu_XY.setMinimumSize(QSize(50, 20))
        self.out_nu_XY.setMaximumSize(QSize(50, 20))
        self.out_nu_XY.setFrameShape(QFrame.NoFrame)

        self.gridLayout_2.addWidget(self.out_nu_XY, 3, 1, 1, 1)

        self.out_nu_XZ = QLabel(self.page_nios_meca)
        self.out_nu_XZ.setObjectName(u"out_nu_XZ")
        sizePolicy.setHeightForWidth(self.out_nu_XZ.sizePolicy().hasHeightForWidth())
        self.out_nu_XZ.setSizePolicy(sizePolicy)
        self.out_nu_XZ.setMinimumSize(QSize(50, 20))
        self.out_nu_XZ.setMaximumSize(QSize(50, 20))
        self.out_nu_XZ.setFrameShape(QFrame.NoFrame)

        self.gridLayout_2.addWidget(self.out_nu_XZ, 3, 2, 1, 1)

        self.out_nu_YZ = QLabel(self.page_nios_meca)
        self.out_nu_YZ.setObjectName(u"out_nu_YZ")
        sizePolicy.setHeightForWidth(self.out_nu_YZ.sizePolicy().hasHeightForWidth())
        self.out_nu_YZ.setSizePolicy(sizePolicy)
        self.out_nu_YZ.setMinimumSize(QSize(50, 20))
        self.out_nu_YZ.setMaximumSize(QSize(50, 20))
        self.out_nu_YZ.setFrameShape(QFrame.NoFrame)

        self.gridLayout_2.addWidget(self.out_nu_YZ, 3, 3, 1, 1)

        self.in_G = QLabel(self.page_nios_meca)
        self.in_G.setObjectName(u"in_G")

        self.gridLayout_2.addWidget(self.in_G, 4, 0, 1, 1)

        self.out_GXY = QLabel(self.page_nios_meca)
        self.out_GXY.setObjectName(u"out_GXY")
        sizePolicy.setHeightForWidth(self.out_GXY.sizePolicy().hasHeightForWidth())
        self.out_GXY.setSizePolicy(sizePolicy)
        self.out_GXY.setMinimumSize(QSize(50, 20))
        self.out_GXY.setMaximumSize(QSize(50, 20))
        self.out_GXY.setFrameShape(QFrame.NoFrame)

        self.gridLayout_2.addWidget(self.out_GXY, 4, 1, 1, 1)

        self.out_GXZ = QLabel(self.page_nios_meca)
        self.out_GXZ.setObjectName(u"out_GXZ")
        sizePolicy.setHeightForWidth(self.out_GXZ.sizePolicy().hasHeightForWidth())
        self.out_GXZ.setSizePolicy(sizePolicy)
        self.out_GXZ.setMinimumSize(QSize(50, 20))
        self.out_GXZ.setMaximumSize(QSize(50, 20))
        self.out_GXZ.setFrameShape(QFrame.NoFrame)

        self.gridLayout_2.addWidget(self.out_GXZ, 4, 2, 1, 1)

        self.out_GYZ = QLabel(self.page_nios_meca)
        self.out_GYZ.setObjectName(u"out_GYZ")
        sizePolicy.setHeightForWidth(self.out_GYZ.sizePolicy().hasHeightForWidth())
        self.out_GYZ.setSizePolicy(sizePolicy)
        self.out_GYZ.setMinimumSize(QSize(50, 20))
        self.out_GYZ.setMaximumSize(QSize(50, 20))
        self.out_GYZ.setFrameShape(QFrame.NoFrame)

        self.gridLayout_2.addWidget(self.out_GYZ, 4, 3, 1, 1)

        self.in_XY = QLabel(self.page_nios_meca)
        self.in_XY.setObjectName(u"in_XY")

        self.gridLayout_2.addWidget(self.in_XY, 2, 1, 1, 1)

        self.in_XZ = QLabel(self.page_nios_meca)
        self.in_XZ.setObjectName(u"in_XZ")

        self.gridLayout_2.addWidget(self.in_XZ, 2, 2, 1, 1)

        self.in_Y = QLabel(self.page_nios_meca)
        self.in_Y.setObjectName(u"in_Y")

        self.gridLayout_2.addWidget(self.in_Y, 0, 2, 1, 1)

        self.in_X = QLabel(self.page_nios_meca)
        self.in_X.setObjectName(u"in_X")

        self.gridLayout_2.addWidget(self.in_X, 0, 1, 1, 1)

        self.in_YZ = QLabel(self.page_nios_meca)
        self.in_YZ.setObjectName(u"in_YZ")

        self.gridLayout_2.addWidget(self.in_YZ, 2, 3, 1, 1)

        self.in_Z = QLabel(self.page_nios_meca)
        self.in_Z.setObjectName(u"in_Z")

        self.gridLayout_2.addWidget(self.in_Z, 0, 3, 1, 1)

        self.nav_iso_meca.addWidget(self.page_nios_meca)

        self.verticalLayout_9.addWidget(self.nav_iso_meca)

        self.gridLayout.addWidget(self.g_mechanics, 1, 1, 1, 1)

        self.verticalLayout_10.addLayout(self.gridLayout)

        self.g_mag = QGroupBox(DMatLib)
        self.g_mag.setObjectName(u"g_mag")
        self.verticalLayout_8 = QVBoxLayout(self.g_mag)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.out_mur_lin = QLabel(self.g_mag)
        self.out_mur_lin.setObjectName(u"out_mur_lin")

        self.verticalLayout_8.addWidget(self.out_mur_lin)

        self.out_Brm20 = QLabel(self.g_mag)
        self.out_Brm20.setObjectName(u"out_Brm20")

        self.verticalLayout_8.addWidget(self.out_Brm20)

        self.out_alpha_Br = QLabel(self.g_mag)
        self.out_alpha_Br.setObjectName(u"out_alpha_Br")

        self.verticalLayout_8.addWidget(self.out_alpha_Br)

        self.out_wlam = QLabel(self.g_mag)
        self.out_wlam.setObjectName(u"out_wlam")

        self.verticalLayout_8.addWidget(self.out_wlam)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.in_BH_curve = QLabel(self.g_mag)
        self.in_BH_curve.setObjectName(u"in_BH_curve")

        self.horizontalLayout.addWidget(self.in_BH_curve)

        self.out_BH = QLabel(self.g_mag)
        self.out_BH.setObjectName(u"out_BH")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.out_BH.sizePolicy().hasHeightForWidth())
        self.out_BH.setSizePolicy(sizePolicy1)
        self.out_BH.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.out_BH)

        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalLayout_10.addWidget(self.g_mag)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.horizontalLayout_2.addLayout(self.verticalLayout_10)

        self.verticalLayout_11.addLayout(self.horizontalLayout_2)

        self.b_close = QDialogButtonBox(DMatLib)
        self.b_close.setObjectName(u"b_close")
        self.b_close.setOrientation(Qt.Horizontal)
        self.b_close.setStandardButtons(QDialogButtonBox.NoButton)

        self.verticalLayout_11.addWidget(self.b_close)

        self.b_close.raise_()

        self.retranslateUi(DMatLib)
        self.b_close.accepted.connect(DMatLib.accept)
        self.b_close.rejected.connect(DMatLib.reject)

        self.nav_iso_therm.setCurrentIndex(1)
        self.nav_iso_meca.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(DMatLib)

    # setupUi

    def retranslateUi(self, DMatLib):
        DMatLib.setWindowTitle(
            QCoreApplication.translate("DMatLib", u"Material Library", None)
        )
        self.img_search.setText("")
        self.in_reference_mat_lib.setText(
            QCoreApplication.translate("DMatLib", u"Material library", None)
        )
        self.in_machine_mat.setText(
            QCoreApplication.translate("DMatLib", u"Machine materials", None)
        )
        self.b_edit.setText(QCoreApplication.translate("DMatLib", u"Edit", None))
        self.b_duplicate.setText(
            QCoreApplication.translate("DMatLib", u"New from", None)
        )
        self.b_delete.setText(QCoreApplication.translate("DMatLib", u"Delete", None))
        self.out_name.setText(
            QCoreApplication.translate("DMatLib", u"name : M400-50A", None)
        )
        self.out_iso.setText(QCoreApplication.translate("DMatLib", u"isotropic", None))
        self.g_elec.setTitle(QCoreApplication.translate("DMatLib", u"Electrical", None))
        self.out_rho_elec.setText(
            QCoreApplication.translate("DMatLib", u"rho = 10e-3 ohm.m", None)
        )
        self.out_epsr.setText(
            QCoreApplication.translate("DMatLib", u"epsr = 0.5", None)
        )
        self.g_eco.setTitle(QCoreApplication.translate("DMatLib", u"Economical", None))
        self.out_cost_unit.setText(
            QCoreApplication.translate(
                "DMatLib", u"cost_unit = 10.5 \u20ac/kg          ", None
            )
        )
        self.g_thermics.setTitle(
            QCoreApplication.translate("DMatLib", u"Thermics", None)
        )
        self.out_Cp.setText(
            QCoreApplication.translate("DMatLib", u"Cp = 0.52 W/kg/K            ", None)
        )
        self.out_alpha.setText(
            QCoreApplication.translate("DMatLib", u"alpha = 0.52", None)
        )
        self.out_L.setText(
            QCoreApplication.translate("DMatLib", u"Lambda = 5200 W/K", None)
        )
        self.out_LX.setText(
            QCoreApplication.translate("DMatLib", u"Lambda X = 5200 W/K", None)
        )
        self.out_LY.setText(
            QCoreApplication.translate("DMatLib", u"Lambda Y = 5200 W/K", None)
        )
        self.out_LZ.setText(
            QCoreApplication.translate("DMatLib", u"Lambda Z = 5200 W/K", None)
        )
        self.g_mechanics.setTitle(
            QCoreApplication.translate("DMatLib", u"Mechanics", None)
        )
        self.out_rho_meca.setText(
            QCoreApplication.translate("DMatLib", u"rho = 7500 kg/m^3 ", None)
        )
        self.out_E.setText(QCoreApplication.translate("DMatLib", u"E = 2360 Pa", None))
        self.out_nu.setText(QCoreApplication.translate("DMatLib", u"nu = 0.5", None))
        self.out_G.setText(
            QCoreApplication.translate("DMatLib", u"G = 10.000 Pa", None)
        )
        self.in_E.setText(QCoreApplication.translate("DMatLib", u"E", None))
        self.out_EX.setText(
            QCoreApplication.translate(
                "DMatLib",
                u"\n"
                "                                                                                1.23e+10\n"
                "                                                                            ",
                None,
            )
        )
        self.out_EY.setText(
            QCoreApplication.translate(
                "DMatLib",
                u"\n"
                "                                                                                10\n"
                "                                                                            ",
                None,
            )
        )
        self.out_EZ.setText(
            QCoreApplication.translate(
                "DMatLib",
                u"\n"
                "                                                                                55.3\n"
                "                                                                            ",
                None,
            )
        )
        self.in_nu.setText(QCoreApplication.translate("DMatLib", u"nu", None))
        self.out_nu_XY.setText(
            QCoreApplication.translate(
                "DMatLib",
                u"\n"
                "                                                                                0.5\n"
                "                                                                            ",
                None,
            )
        )
        self.out_nu_XZ.setText(
            QCoreApplication.translate(
                "DMatLib",
                u"\n"
                "                                                                                0.5\n"
                "                                                                            ",
                None,
            )
        )
        self.out_nu_YZ.setText(
            QCoreApplication.translate(
                "DMatLib",
                u"\n"
                "                                                                                0.6\n"
                "                                                                            ",
                None,
            )
        )
        self.in_G.setText(QCoreApplication.translate("DMatLib", u"G", None))
        self.out_GXY.setText(
            QCoreApplication.translate(
                "DMatLib",
                u"\n"
                "                                                                                1023\n"
                "                                                                            ",
                None,
            )
        )
        self.out_GXZ.setText(
            QCoreApplication.translate(
                "DMatLib",
                u"\n"
                "                                                                                1024\n"
                "                                                                            ",
                None,
            )
        )
        self.out_GYZ.setText(
            QCoreApplication.translate(
                "DMatLib",
                u"\n"
                "                                                                                1024\n"
                "                                                                            ",
                None,
            )
        )
        self.in_XY.setText(QCoreApplication.translate("DMatLib", u"XY", None))
        self.in_XZ.setText(QCoreApplication.translate("DMatLib", u"XZ", None))
        self.in_Y.setText(QCoreApplication.translate("DMatLib", u"Y", None))
        self.in_X.setText(QCoreApplication.translate("DMatLib", u"X", None))
        self.in_YZ.setText(QCoreApplication.translate("DMatLib", u"YZ", None))
        self.in_Z.setText(QCoreApplication.translate("DMatLib", u"Z", None))
        self.g_mag.setTitle(QCoreApplication.translate("DMatLib", u"Magnetics", None))
        self.out_mur_lin.setText(
            QCoreApplication.translate("DMatLib", u"mur_lin = 0.555", None)
        )
        self.out_Brm20.setText(
            QCoreApplication.translate("DMatLib", u"Brm20 = 1 T", None)
        )
        self.out_alpha_Br.setText(
            QCoreApplication.translate("DMatLib", u"alpha_Br=0.1", None)
        )
        self.out_wlam.setText(
            QCoreApplication.translate("DMatLib", u"wlam = 0.5 m", None)
        )
        self.in_BH_curve.setText(
            QCoreApplication.translate("DMatLib", u"BH curve:", None)
        )
        self.out_BH.setText(QCoreApplication.translate("DMatLib", u"-", None))

    # retranslateUi
