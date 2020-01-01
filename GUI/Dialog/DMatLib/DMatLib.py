# -*- coding: utf-8 -*-
"""@package

@date Created on Mon Sep 26 10:16:16 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from os import getcwd, rename
from os.path import join, dirname, abspath
from re import match

from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

from pyleecan.Classes.MatLamination import MatLamination
from pyleecan.Classes.MatMagnet import MatMagnet
from pyleecan.Functions.load import load_matlib
from pyleecan.GUI.Dialog.DMatLib.Gen_DMatLib import Gen_DMatLib
from pyleecan.GUI.Dialog.DMatLib.DMatSetup.DMatSetup import DMatSetup
from pyleecan.GUI import DATA_DIR


class DMatLib(Gen_DMatLib, QDialog):
    def __init__(self, matlib, selected=0):
        """Init the Matlib GUI

        Parameters
        ----------
        self :
            a W_Matlib object
        matlib :
            The current state of the Material library (list of
            material)
        selected :
            Index of the currently selected material

        Returns
        -------

        """

        # Build the interface according to the .ui file
        QDialog.__init__(self)
        self.setupUi(self)

        # Copy to set the modification only if validated
        self.matlib = list(matlib)
        self.matlib_path = abspath(join(DATA_DIR, "Material"))

        if len(self.matlib) == 0:
            self.load()
        # Unknow material => Use the first one
        if selected == -1:
            selected = 0
        self.update_mat_list()
        self.nav_mat.setCurrentRow(selected)
        self.update_out()

        # Hide since unused
        # self.out_iso.hide()
        self.out_epsr.hide()

        self.nav_mat.currentRowChanged.connect(self.update_out)
        self.c_search.currentIndexChanged.connect(self.filter_material)
        self.le_search.textChanged.connect(self.filter_material)

        self.b_edit.clicked.connect(self.edit_material)
        self.b_delete.clicked.connect(self.delete_material)
        self.b_duplicate.clicked.connect(self.new_material)
        self.nav_mat.doubleClicked.connect(self.edit_material)

    def load(self):
        """Load the material library

        Parameters
        ----------
        self :
            A W_MatLib object

        Returns
        -------

        """

        load_path = str(
            QFileDialog.getExistingDirectory(
                self, self.tr("Select Directory"), matlib_path
            )
        )

        if load_path != "":
            try:
                self.matlib = load_matlib(load_path)
                self.update_mat_list()
                self.nav_mat.setCurrentRow(0)
                self.update_out()
                self.matlib_path = dirname(load_path)
            except Exception as e:
                QMessageBox().critical(
                    self,
                    self.tr("Error"),
                    self.tr(
                        "The material library file is " "incorrect:\n",
                        "Please keep the \n, another " "message is following this one",
                    )
                    + type(e).__name__
                    + ": "
                    + str(e),
                )
                self.reject()
        else:
            self.reject()

    def edit_material(self, item=None):
        """Open the setup material GUI to edit the current material

        Parameters
        ----------
        self :
            A W_MatLib object
        item :
             (Default value = None)

        Returns
        -------

        """
        # Get the current material (filtering index)
        mat_id = int(self.nav_mat.currentItem().text()[:3]) - 1
        # Open the setup GUI
        self.mat_win = DMatSetup(self.matlib[mat_id])
        return_code = self.mat_win.exec_()
        if return_code == QDialog.Accepted:
            # Update the material only if the user validate at the end
            old_name = self.matlib[mat_id].name
            old_path = self.matlib[mat_id].path
            self.matlib[mat_id] = self.mat_win.mat
            if old_name != self.matlib[mat_id].name:
                # Update the material name list only if modified
                index = self.nav_mat.currentRow()
                self.update_mat_list()
                if index < self.nav_mat.count() - 1:
                    self.nav_mat.setCurrentRow(index)
                else:
                    self.nav_mat.setCurrentRow(self.nav_mat.count() - 1)
                # Rename the saving file
                rename(old_path, self.matlib[mat_id].path)
            self.matlib[mat_id].save(self.matlib[mat_id].path)
            self.update_out()

    def new_material(self):
        """Open the setup material GUI to create a new material according to
        the current material

        Parameters
        ----------
        self :
            A W_MatLib object

        Returns
        -------

        """
        # Get the current material (filtering index)
        mat_id = int(self.nav_mat.currentItem().text()[:3]) - 1
        # Open the setup GUI (creates a copy of the material)
        self.mat_win = DMatSetup(self.matlib[mat_id])
        return_code = self.mat_win.exec_()
        if return_code == QDialog.Accepted:
            # Update the material only if the user validate at the end
            self.matlib.append(self.mat_win.mat)
            self.matlib[-1].save(self.matlib[-1].path)
            self.update_mat_list()
            self.nav_mat.setCurrentRow(self.nav_mat.count() - 1)
            self.update_out()

    def delete_material(self):
        """Delete the selected material

        Parameters
        ----------
        self :
            A W_MatLib object

        Returns
        -------

        """
        mat_id = int(self.nav_mat.currentItem().text()[:3]) - 1
        del_msg = "Are you sure you want to delete " + self.matlib[mat_id].name + " ?"
        reply = QMessageBox.question(
            self, "Confirmation", del_msg, QMessageBox.Yes, QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # delete only if confirmed
            self.matlib.pop(mat_id)
            index = self.nav_mat.currentRow()
            self.update_mat_list()
            if index < self.nav_mat.count() - 1:
                self.nav_mat.setCurrentRow(index)
            else:
                self.nav_mat.setCurrentRow(self.nav_mat.count() - 1)

    def filter_material(self, index=None):
        """

        Parameters
        ----------
        index :
             (Default value = None)

        Returns
        -------

        """
        self.update_mat_list()
        self.nav_mat.setCurrentRow(0)

    def update_mat_list(self):
        """Update the list of Material with the current content of MatLib

        Parameters
        ----------
        self :
            A W_MatLib object

        Returns
        -------

        """
        self.nav_mat.blockSignals(True)
        self.nav_mat.clear()
        mat_list = self.matlib

        # Filter the material
        for ii, mat in enumerate(mat_list):
            if self.c_search.currentIndex() == 1 and type(mat.mag) is not MatLamination:
                # Lamination only
                continue
            if self.c_search.currentIndex() == 2 and type(mat.mag) is not MatMagnet:
                # Magnet only
                continue
            if self.c_search.currentIndex() == 3 and mat.mag is not None:
                # Raw mat only
                continue
            if self.le_search.text() != "" and not match(
                ".*" + self.le_search.text().lower() + ".*", mat.name.lower()
            ):
                continue
            self.nav_mat.addItem("%03d" % (ii + 1) + " - " + mat.name)
        self.nav_mat.blockSignals(False)

    def update_out(self, index=0):
        """Update all the output widget for material preview

        Parameters
        ----------
        self :
            A W_MatLib object
        index :
            Current index of nav_mat (Default value = 0)

        Returns
        -------

        """
        # Get the selected material
        mat_id = int(self.nav_mat.currentItem().text()[:3]) - 1  # for filtering
        mat = self.matlib[mat_id]

        # mat = [mat for mat in self.matlib if mat.name == curr_name][0]

        # Update Main parameters
        self.out_name.setText(self.tr("name: ") + mat.name)
        if mat.is_isotropic:
            self.out_iso.setText(self.tr("type: isotropic"))
        else:
            self.out_iso.setText(self.tr("type: anisotropic"))

        # Update Electrical parameters
        update_text(self.out_rho_elec, "rho", mat.elec.rho, "ohm.m")
        # Update_text(self.out_epsr,"epsr",mat.elec.epsr,None)

        # Update Economical parameters
        update_text(self.out_cost_unit, "cost_unit", mat.eco.cost_unit, u"€/kg")

        # Update Thermics parameters
        update_text(self.out_Cp, "Cp", mat.HT.Cp, "W/kg/K")
        update_text(self.out_alpha, "alpha", mat.HT.alpha, None)
        if mat.is_isotropic:
            self.nav_iso_therm.setCurrentIndex(0)
            update_text(self.out_L, "Lambda", mat.HT.lambda_x, "W/K")
        else:
            self.nav_iso_therm.setCurrentIndex(1)
            update_text(self.out_LX, "Lambda X", mat.HT.lambda_x, "W/K")
            update_text(self.out_LY, "Lambda Y", mat.HT.lambda_y, "W/K")
            update_text(self.out_LZ, "Lambda Z", mat.HT.lambda_z, "W/K")

        # Update Structural parameters
        update_text(self.out_rho_meca, "rho", mat.struct.rho, "kg/m^3")
        if mat.is_isotropic:
            self.nav_iso_meca.setCurrentIndex(0)
            update_text(self.out_E, "E", mat.struct.Ex, "Pa")
            update_text(self.out_G, "G", mat.struct.Gxy, "Pa")
            update_text(self.out_nu, "nu", mat.struct.nu_xy, None)
        else:
            self.nav_iso_meca.setCurrentIndex(1)
            update_text(self.out_EX, None, mat.struct.Ex, None)
            update_text(self.out_GXY, None, mat.struct.Gxy, None)
            update_text(self.out_nu_XY, None, mat.struct.nu_xy, None)
            update_text(self.out_EY, None, mat.struct.Ey, None)
            update_text(self.out_GYZ, None, mat.struct.Gyz, None)
            update_text(self.out_nu_YZ, None, mat.struct.nu_yz, None)
            update_text(self.out_EZ, None, mat.struct.Ez, None)
            update_text(self.out_GXZ, None, mat.struct.Gxz, None)
            update_text(self.out_nu_XZ, None, mat.struct.nu_xz, None)

        # Update Magnetics parameters
        if mat.mag is None:
            self.out_type.setText(self.tr("Raw Material"))
            self.g_mag.hide()
        else:
            self.g_mag.show()
            update_text(self.out_mur_lin, "mur_lin", mat.mag.mur_lin, None)
            if type(mat.mag) is MatMagnet:
                self.out_type.setText(self.tr("Magnet Material"))
                update_text(self.out_Brm20, "Brm20", mat.mag.Brm20, "T")
                self.out_Brm20.show()
                update_text(self.out_alpha_Br, "alpha_Br", mat.mag.alpha_Br, None)
                self.out_alpha_Br.show()
                self.out_wlam.hide()
            elif type(mat.mag) is MatLamination:
                self.out_type.setText(self.tr("Lamination Material"))
                self.out_Brm20.hide()
                self.out_alpha_Br.hide()
                update_text(self.out_wlam, "wlam", mat.mag.Wlam, "m")
                self.out_wlam.show()


def update_text(label, name, value, unit):
    """Update a Qlabel with the value if not None

    Parameters
    ----------
    label :
        Qlabel to update
    name :
        Name of the variable
    value :
        Current value of the variable (can be None)
    unit :
        Variable unit (can be None)

    Returns
    -------

    """
    if value is None:
        val = "?"
    else:
        val = str(value)
        if len(val) > 8:
            val = "%1.2e" % value  # formating: 1.23e+08

    if name is None:  # For E, G, nu table
        txt = val
    else:
        if unit is None:
            txt = name + " = " + val
        else:
            txt = name + " = " + val + " " + unit
    label.setText(txt)
