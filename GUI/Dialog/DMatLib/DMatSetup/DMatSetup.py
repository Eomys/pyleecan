# -*- coding: utf-8 -*-

from os.path import join, dirname
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt

from pyleecan.GUI.Dialog.DMatLib.DMatSetup.Gen_DMatSetup import Gen_DMatSetup

from pyleecan.Classes.Material import Material
from pyleecan.Classes.MatMagnet import MatMagnet
from pyleecan.Classes.MatLamination import MatLamination


class DMatSetup(Gen_DMatSetup, QDialog):
    """ """

    def __init__(self, material):
        # Build the interface according to the .ui file
        QDialog.__init__(self)
        self.setupUi(self)

        # Copy to set the modification only if validated
        self.mat = Material(init_dict=material.as_dict())

        self.le_name.setText(material.name)
        if material.is_isotropic:
            self.is_isotropic.setCheckState(Qt.Checked)
            self.nav_meca.setCurrentIndex(1)
            self.nav_ther.setCurrentIndex(1)
        else:
            self.is_isotropic.setCheckState(Qt.Unchecked)
            self.nav_meca.setCurrentIndex(0)
            self.nav_ther.setCurrentIndex(0)
        # Elec
        self.lf_rho_elec.setValue(material.elec.rho)
        # Economical
        self.lf_cost_unit.setValue(material.eco.cost_unit)
        # Thermics
        self.lf_Cp.setValue(material.HT.Cp)
        self.lf_alpha.setValue(material.HT.alpha)
        self.lf_L.setValue(material.HT.lambda_x)
        self.lf_Lx.setValue(material.HT.lambda_x)
        self.lf_Ly.setValue(material.HT.lambda_y)
        self.lf_Lz.setValue(material.HT.lambda_z)
        # Structural
        self.lf_rho_meca.setValue(material.struct.rho)
        self.lf_E.setValue(material.struct.Ex)
        self.lf_Ex.setValue(material.struct.Ex)
        self.lf_Ey.setValue(material.struct.Ey)
        self.lf_Ez.setValue(material.struct.Ez)
        self.lf_G.setValue(material.struct.Gxy)
        self.lf_Gxy.setValue(material.struct.Gxy)
        self.lf_Gxz.setValue(material.struct.Gxz)
        self.lf_Gyz.setValue(material.struct.Gyz)
        self.lf_nu.setValue(material.struct.nu_xy)
        self.lf_nu_xy.setValue(material.struct.nu_xy)
        self.lf_nu_xz.setValue(material.struct.nu_xz)
        self.lf_nu_yz.setValue(material.struct.nu_yz)

        if type(material.mag) is MatLamination:
            self.c_type_mat.setCurrentIndex(2)
            self.nav_mag.setCurrentIndex(1)
            self.lf_mur_lin.setValue(material.mag.mur_lin)
            self.lf_Wlam.setValue(material.mag.Wlam)
        elif type(material.mag) is MatMagnet:
            self.c_type_mat.setCurrentIndex(1)
            self.nav_mag.setCurrentIndex(0)
            self.lf_mur_lin.setValue(material.mag.mur_lin)
            self.lf_Brm20.setValue(material.mag.Brm20)
            self.lf_alpha_Br.setValue(material.mag.alpha_Br)
        else:  # Mat_Raw
            self.c_type_mat.setCurrentIndex(0)
            self.nav_phy.removeTab(1)

        # Hide useless widget
        self.in_epsr.hide()
        self.lf_epsr.hide()

        self.le_name.editingFinished.connect(self.set_name)
        self.c_type_mat.currentIndexChanged.connect(self.set_type_mat)
        self.is_isotropic.toggled.connect(self.set_is_isotropic)
        self.lf_rho_elec.editingFinished.connect(self.set_rho_elec)
        # Magnetics
        self.lf_mur_lin.editingFinished.connect(self.set_mur_lin)
        self.lf_Brm20.editingFinished.connect(self.set_Brm20)
        self.lf_alpha_Br.editingFinished.connect(self.set_alpha_Br)
        self.lf_Wlam.editingFinished.connect(self.set_Wlam)
        # Economical
        self.lf_cost_unit.editingFinished.connect(self.set_cost_unit)
        # Thermics
        self.lf_Cp.editingFinished.connect(self.set_Cp)
        self.lf_alpha.editingFinished.connect(self.set_alpha)
        self.lf_L.editingFinished.connect(self.set_lambda)
        self.lf_Lx.editingFinished.connect(self.set_lambda_x)
        self.lf_Ly.editingFinished.connect(self.set_lambda_y)
        self.lf_Lz.editingFinished.connect(self.set_lambda_z)
        # Mechanics
        self.lf_rho_meca.editingFinished.connect(self.set_rho_meca)
        self.lf_E.editingFinished.connect(self.set_E)
        self.lf_Ex.editingFinished.connect(self.set_Ex)
        self.lf_Ey.editingFinished.connect(self.set_Ey)
        self.lf_Ez.editingFinished.connect(self.set_Ez)
        self.lf_G.editingFinished.connect(self.set_G)
        self.lf_Gxy.editingFinished.connect(self.set_Gxy)
        self.lf_Gxz.editingFinished.connect(self.set_Gxz)
        self.lf_Gyz.editingFinished.connect(self.set_Gyz)
        self.lf_nu.editingFinished.connect(self.set_nu)
        self.lf_nu_xy.editingFinished.connect(self.set_nu_xy)
        self.lf_nu_xz.editingFinished.connect(self.set_nu_xz)
        self.lf_nu_yz.editingFinished.connect(self.set_nu_yz)

    def set_name(self):
        """Signal to update the value of name according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """

        file_name = str(self.le_name.text())
        # Update name and path
        self.mat.name = file_name
        self.le_name.setText(self.mat.name)
        self.mat.path = join(dirname(self.mat.path), file_name + ".json")

    def set_type_mat(self, index):
        """Signal to update the material type according to the combobox

        Parameters
        ----------
        self :
            A DMatSetup object
        index :
            Current index of the combobox

        Returns
        -------
        None
        """
        if index == 0:  # Raw Mat
            self.mat.mag = None
            self.nav_phy.removeTab(1)
        elif index == 1:  # Magnet
            self.mat.mag = MatMagnet()
            self.mat.mag._set_None()
            self.nav_phy.insertTab(1, self.tab_mag, self.tr("Magnetics"))
            self.nav_mag.setCurrentIndex(0)
        else:  # Lamination
            self.mat.mag = MatLamination()
            self.mat.mag._set_None()
            self.nav_phy.insertTab(1, self.tab_mag, self.tr("Magnetics"))
            self.nav_mag.setCurrentIndex(1)

    def set_is_isotropic(self, is_checked):
        """Signal to update the value of is_isotropic according to the checkbox

        Parameters
        ----------
        self :
            A DMatSetup object
        is_checked :
            State of the checkbox

        Returns
        -------
        None
        """
        self.mat.is_isotropic = is_checked
        self.nav_meca.setCurrentIndex(int(is_checked))
        self.nav_ther.setCurrentIndex(int(is_checked))

    def set_rho_elec(self):
        """Signal to update the value of rho_elec according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.elec.rho = self.lf_rho_elec.value()

    def set_mur_lin(self):
        """Signal to update the value of mur_lin according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.mag.mur_lin = self.lf_mur_lin.value()

    def set_Brm20(self):
        """Signal to update the value of Brm20 according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.mag.Brm20 = self.lf_Brm20.value()

    def set_alpha_Br(self):
        """Signal to update the value of alpha_Br according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.mag.alpha_Br = self.lf_alpha_Br.value()

    def set_Wlam(self):
        """Signal to update the value of Wlam according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.mag.Wlam = self.lf_Wlam.value()

    def set_cost_unit(self):
        """Signal to update the value of cost_unit according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.eco.cost_unit = self.lf_cost_unit.value()

    def set_Cp(self):
        """Signal to update the value of Cp according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.HT.Cp = self.lf_Cp.value()

    def set_alpha(self):
        """Signal to update the value of alpha according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.HT.alpha = self.lf_alpha.value()

    def set_lambda(self):
        """Signal to update the value of lambda according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.HT.lambda_x = self.lf_L.value()
        self.mat.HT.lambda_y = self.lf_L.value()
        self.mat.HT.lambda_z = self.lf_L.value()

    def set_lambda_x(self):
        """Signal to update the value of lambda_x according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.HT.lambda_x = self.lf_Lx.value()

    def set_lambda_y(self):
        """Signal to update the value of lambda_y according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.HT.lambda_y = self.lf_Ly.value()

    def set_lambda_z(self):
        """Signal to update the value of lambda_z according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.HT.lambda_z = self.lf_Lz.value()

    def set_rho_meca(self):
        """Signal to update the value of rho_meca according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.struct.rho = self.lf_rho_meca.value()

    def set_E(self):
        """Signal to update the value of Ex according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.struct.Ex = self.lf_E.value()
        self.mat.struct.Ey = self.lf_E.value()
        self.mat.struct.Ez = self.lf_E.value()

    def set_Ex(self):
        """Signal to update the value of Ex according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.struct.Ex = self.lf_Ex.value()

    def set_Ey(self):
        """Signal to update the value of Ey according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.struct.Ey = self.lf_Ey.value()

    def set_Ez(self):
        """Signal to update the value of Ez according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.struct.Ez = self.lf_Ez.value()

    def set_G(self):
        """Signal to update the value of G according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.struct.Gxy = self.lf_G.value()
        self.mat.struct.Gxz = self.lf_G.value()
        self.mat.struct.Gyz = self.lf_G.value()

    def set_Gxy(self):
        """Signal to update the value of Gxy according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.struct.Gxy = self.lf_Gxy.value()

    def set_Gxz(self):
        """Signal to update the value of Gxz according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.struct.Gxz = self.lf_Gxz.value()

    def set_Gyz(self):
        """Signal to update the value of Gyz according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.struct.Gyz = self.lf_Gyz.value()

    def set_nu(self):
        """Signal to update the value of nu_xy according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.struct.nu_xy = self.lf_nu.value()
        self.mat.struct.nu_xz = self.lf_nu.value()
        self.mat.struct.nu_yz = self.lf_nu.value()

    def set_nu_xy(self):
        """Signal to update the value of nu_xy according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.struct.nu_xy = self.lf_nu_xy.value()

    def set_nu_xz(self):
        """Signal to update the value of nu_xz according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.struct.nu_xz = self.lf_nu_xz.value()

    def set_nu_yz(self):
        """Signal to update the value of nu_yz according to the line edit

        Parameters
        ----------
        self :
            A DMatSetup object

        Returns
        -------
        None
        """
        self.mat.struct.nu_yz = self.lf_nu_yz.value()
