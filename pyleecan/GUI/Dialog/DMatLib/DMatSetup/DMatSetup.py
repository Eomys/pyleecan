# -*- coding: utf-8 -*-
from os.path import join, dirname, split
from PySide2.QtWidgets import QDialog, QMessageBox, QFileDialog
from PySide2.QtCore import Qt

from .....GUI.Dialog.DMatLib.DMatSetup.Gen_DMatSetup import Gen_DMatSetup
from .....GUI.Tools.MPLCanvas import MPLCanvas

from .....Classes.Material import Material
from .....Classes.MatMagnetics import MatMagnetics
from .....Classes.ImportMatrixXls import ImportMatrixXls
from .....Classes.ImportMatrixVal import ImportMatrixVal

from .....Functions.path_tools import abs_file_path, rel_file_path

from numpy import array


class DMatSetup(Gen_DMatSetup, QDialog):
    def __init__(self, material, is_matlib=True):
        """
        Dialog for editing material data.

        Parameters
        ----------
        material : Material
            material to edit
        is_matlib : bool
            material already in matlib
        """
        # Build the interface according to the .ui file
        QDialog.__init__(self)
        self.setupUi(self)

        self.is_save_needed = False

        # Copy to set the modification only if validated
        self.mat = Material(init_dict=material.as_dict())

        self.le_name.setText(self.mat.name)
        if self.mat.is_isotropic:
            self.is_isotropic.setCheckState(Qt.Checked)
            self.nav_meca.setCurrentIndex(1)
            self.nav_ther.setCurrentIndex(1)
        else:
            self.is_isotropic.setCheckState(Qt.Unchecked)
            self.nav_meca.setCurrentIndex(0)
            self.nav_ther.setCurrentIndex(0)

        # Edit button text if the Material selected is in the ref matlib
        if is_matlib:
            self.b_add_matlib.setText("Add to machine")

        # Three button to close
        self.b_cancel.clicked.connect(self.close)
        self.b_save.clicked.connect(lambda: self.done(1))
        self.b_add_matlib.clicked.connect(lambda: self.done(2))

        # === check material attribute and set values ===
        # Elec
        if self.mat.elec is None:
            self.set_default("elec", "electrical")
        self.lf_rho_elec.setValue(self.mat.elec.rho)

        # Economical
        if self.mat.eco is None:
            self.set_default("eco", "economical")
        self.lf_cost_unit.setValue(self.mat.eco.cost_unit)

        # Thermics
        if self.mat.HT is None:
            self.set_default("HT", "thermaical")
        self.lf_Cp.setValue(self.mat.HT.Cp)
        self.lf_alpha.setValue(self.mat.HT.alpha)
        self.lf_L.setValue(self.mat.HT.lambda_x)
        self.lf_Lx.setValue(self.mat.HT.lambda_x)
        self.lf_Ly.setValue(self.mat.HT.lambda_y)
        self.lf_Lz.setValue(self.mat.HT.lambda_z)
        # Structural
        if self.mat.struct is None:
            self.set_default("struct", "structural")
        self.lf_rho_meca.setValue(self.mat.struct.rho)
        self.lf_E.setValue(self.mat.struct.Ex)
        self.lf_Ex.setValue(self.mat.struct.Ex)
        self.lf_Ey.setValue(self.mat.struct.Ey)
        self.lf_Ez.setValue(self.mat.struct.Ez)
        self.lf_G.setValue(self.mat.struct.Gxy)
        self.lf_Gxy.setValue(self.mat.struct.Gxy)
        self.lf_Gxz.setValue(self.mat.struct.Gxz)
        self.lf_Gyz.setValue(self.mat.struct.Gyz)
        self.lf_nu.setValue(self.mat.struct.nu_xy)
        self.lf_nu_xy.setValue(self.mat.struct.nu_xy)
        self.lf_nu_xz.setValue(self.mat.struct.nu_xz)
        self.lf_nu_yz.setValue(self.mat.struct.nu_yz)

        # Magnetical
        if self.mat.mag is None:
            self.set_default("mag", "magnetical")
        self.lf_mur_lin.setValue(self.mat.mag.mur_lin)
        self.lf_Brm20.setValue(self.mat.mag.Brm20)
        self.lf_alpha_Br.setValue(self.mat.mag.alpha_Br)
        self.lf_Wlam.setValue(self.mat.mag.Wlam)
        # Setup import B(H) widget
        self.w_BH_import.verbose_name = "B(H) curve"
        self.w_BH_import.obj = self.mat.mag
        self.w_BH_import.param_name = "BH_curve"
        self.w_BH_import.expected_shape = (None, 2)
        self.w_BH_import.update()

        # Hide useless widget
        self.in_epsr.hide()
        self.lf_epsr.hide()

        # === setup signals ===
        # Misc.
        self.le_name.editingFinished.connect(self.set_name)
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

    def closeEvent(self, event):
        """Display a message before leaving

        Parameters
        ----------
        self : DMatSetup
            A DMatSetup object
        event :
            The closing event
        """

        if self.is_save_needed:
            quit_msg = self.tr(
                "Unsaved changes will be lost.\nDo you want to save the material?"
            )
            reply = QMessageBox.question(
                self,
                self.tr("Please save before closing"),
                quit_msg,
                QMessageBox.Yes,
                QMessageBox.No,
            )
            self.qmessagebox_question = reply
            if reply == QMessageBox.Yes:
                self.done(1)

    def set_default(self, attr, attr_name):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(
            "Material "
            + attr_name
            + " property is None.\nDefault values set. Please check values."
        )
        msg.setWindowTitle("Warning")
        msg.exec_()
        setattr(self.mat, attr, type(getattr(Material(), attr))())

    def set_name(self):
        """Signal to update the value of name according to the line edit

        Parameters
        ----------
        self : DMatSetup
            A DMatSetup object

        Returns
        -------
        None
        """

        file_name = str(self.le_name.text())
        # Update name and path
        self.mat.name = file_name
        self.le_name.setText(self.mat.name)
        self.mat.path = rel_file_path(
            join(dirname(self.mat.path), file_name + ".json"), "MATLIB_DIR"
        )
        self.is_save_needed = True

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
        print(self.mat.mag.BH_curve)
        self.mat.elec.rho = self.lf_rho_elec.value()
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True

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
        self.is_save_needed = True
