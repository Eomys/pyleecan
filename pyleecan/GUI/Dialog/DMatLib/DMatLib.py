# -*- coding: utf-8 -*-

from os import getcwd, remove, rename
from os.path import abspath, dirname, join, split
from re import match

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QFileDialog, QListWidget, QMessageBox

from ....Classes.ImportMatrixVal import ImportMatrixVal
from ....Classes.ImportMatrixXls import ImportMatrixXls
from ....Functions.load import load_matlib
from ....Functions.path_tools import abs_file_path
from ....GUI import GUI_logger
from ....GUI.Dialog.DMatLib.DMatSetup.DMatSetup import DMatSetup
from ....GUI.Dialog.DMatLib.Gen_DMatLib import Gen_DMatLib


class DMatLib(Gen_DMatLib, QDialog):
    """Material Library Dialog to view and modify material data."""

    # Signal to W_MachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()

    def __init__(self, matlib, key="RefMatLib", selected=0):
        """Init the Matlib GUI

        Parameters
        ----------
        self :
            a DMatLib object
        matlib : MatLib
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

        # Load the material library
        self.matlib = matlib

        # bool to know if the material selected is in MatLib
        self.mat_selected_in_matlib = True

        # Unknow material => Use the first one
        if selected == -1:
            selected = 0
        self.update_list_mat()

        # Select the material
        if key == "RefMatLib":
            self.nav_mat.setCurrentRow(selected)
            self.update_out(on_matlib=True)
        else:
            self.nav_mat_mach.setCurrentRow(selected)
            self.update_out(on_matlib=False)

        # Hide since unused
        # self.out_iso.hide()
        self.out_epsr.hide()

        self.nav_mat.itemSelectionChanged.connect(
            lambda: self.update_out(on_matlib=True)
        )
        self.nav_mat_mach.itemSelectionChanged.connect(
            lambda: self.update_out(on_matlib=False)
        )

        self.le_search.textChanged.connect(self.filter_material)

        self.b_edit.clicked.connect(self.edit_material)
        self.b_delete.clicked.connect(self.delete_material)
        self.b_duplicate.clicked.connect(self.new_material)
        self.nav_mat.doubleClicked.connect(self.edit_material)
        self.nav_mat_mach.doubleClicked.connect(self.edit_material)

    def load(self):
        """Load the material library

        Parameters
        ----------
        self :
            A DMatLib object

        Returns
        -------

        """

        load_path = str(
            QFileDialog.getExistingDirectory(
                self, self.tr("Select Material Library Directory"), self.matlib_path
            )
        )

        if load_path != "":
            try:
                self.matlib.load_mat_ref(load_path)
                self.update_list_mat()
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

    def edit_material(self):
        """
        Open the setup material GUI to edit the current material.
        Changes will be saved to the corresponding material file.

        Parameters
        ----------
        self :
            A DMatLib object
        """

        # Get the current material
        if self.nav_mat.currentRow() != -1:
            mat_id = self.nav_mat.currentRow()
            dict_key = "RefMatLib"
        elif self.nav_mat_mach.currentRow() != -1:
            mat_id = self.nav_mat_mach.currentRow()
            dict_key = "MachineMatLib"
        else:
            mat_id = 0
            dict_key = "RefMatLib"

        # Open the setup GUI
        # (creates a copy of the material, i.e. self.matlib won't be edited directly)
        self.mat_win = DMatSetup(
            self.matlib.dict_mat[dict_key][mat_id], self.mat_selected_in_matlib
        )
        return_code = self.mat_win.exec_()

        if return_code > 0:
            # Change the material
            is_change = self.matlib.replace_material(
                dict_key, mat_id, self.mat_win.mat, save=return_code == 1
            )

            # Emit saveNeeded if the machine has been change
            if is_change:
                self.saveNeeded.emit()

            # Move the material
            if return_code == 2:
                if dict_key == "MachineMatLib":
                    # Move the material into the Material library
                    self.matlib.move_mach_mat_to_ref(dict_key, mat_id)

                    # Set the pointer on the ref matlib if machine material list is empty
                    if len(self.matlib.dict_mat["MachineMatLib"]) == 0:
                        self.on_matlib = True
                else:
                    # Move the material into the machine materials list
                    self.matlib.move_ref_mat_to_mach("MachineMatLib", mat_id)

            # Update material list
            self.update_list_mat()

            if self.mat_selected_in_matlib:
                self.nav_mat.setCurrentRow(self.nav_mat.count() - 1)
                self.update_out(on_matlib=True)
            else:
                self.nav_mat_mach.setCurrentRow(self.nav_mat_mach.count() - 1)
                self.update_out(on_matlib=False)

            # Signal set by WMatSelect to update Combobox
            self.accepted.emit()

    def new_material(self):
        """Open the setup material GUI to create a new material according to
        the current material

        Parameters
        ----------
        self :
            A DMatLib object

        Returns
        -------

        """
        # Get the current material (filtering index)
        if self.mat_selected_in_matlib:
            mat_id = int(self.nav_mat.currentItem().text()[:3]) - 1
            dict_key = "RefMatLib"
        else:
            mat_id = self.nav_mat_mach.currentRow()
            dict_key = "MachineMatLib"

        # Open the setup GUI
        # (creates a copy of the material, i.e. self.matlib won't be edited directly)
        self.mat_win = DMatSetup(
            self.matlib.dict_mat[dict_key][mat_id], self.mat_selected_in_matlib
        )
        return_code = self.mat_win.exec_()
        if return_code > 0:
            # Update the material only if the user validate at the end
            if (self.mat_selected_in_matlib and return_code == 1) or (
                not self.mat_selected_in_matlib and return_code == 2
            ):
                self.mat_selected_in_matlib = True

                # Add the material to the mat_ref
                self.matlib.add_new_mat_ref(self.mat_win.mat)

                self.update_list_mat()
                self.nav_mat.setCurrentRow(self.nav_mat.count() - 1)
                self.update_out()

            else:
                # Add the material to the machine materials
                self.matlib.add_new_mat_mach(self.mat_win.mat)

                self.update_list_mat()
                self.nav_mat_mach.setCurrentRow(self.nav_mat_mach.count() - 1)
                self.update_out(on_matlib=False)

            # Signal set by WMatSelect to update Combobox
            self.accepted.emit()

    def delete_material(self):
        """Delete the selected material

        Parameters
        ----------
        self :
            A DMatLib object

        Returns
        -------

        """
        if self.nav_mat.currentRow() != -1:
            dict_key = "RefMatLib"
            mat_id = self.nav_mat.currentRow()
        else:
            dict_key = "MachineMatLib"
            mat_id = self.nav_mat_mach.currentRow()
            self.mat_selected_in_matlib = False
        # Do not delete machine material
        # if not self.mat_selected_in_matlib:
        #     QMessageBox.information(self, "", "Cannot delete machine material.")
        #     return

        if len(self.matlib.dict_mat["RefMatLib"]) > 1 or dict_key != "RefMatLib":

            del_msg = (
                "Are you sure you want to delete "
                + self.matlib.dict_mat[dict_key][mat_id].name
                + " ?"
            )
            reply = QMessageBox.question(
                self, "Confirmation", del_msg, QMessageBox.Yes, QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                # delete only if confirmed
                self.matlib.delete_material(dict_key, mat_id)
                index = self.nav_mat.currentRow()
                self.update_list_mat()
                if index < self.nav_mat.count() - 1:
                    self.nav_mat.setCurrentRow(index)
                else:
                    self.nav_mat.setCurrentRow(self.nav_mat.count() - 1)
                # Signal set by WMatSelect to update Combobox
                self.accepted.emit()
                self.update_list_mat()
        else:
            QMessageBox.information(
                self, "", "Reference MatLib must contain at least one material."
            )

    def filter_material(self, index=None):
        """

        Parameters
        ----------
        index :
             (Default value = None)

        Returns
        -------

        """
        self.update_list_mat()
        self.nav_mat.setCurrentRow(0)

    def update_list_mat(self, selected_id=-1):
        """Update the list of Material with the current content of MatLib

        Parameters
        ----------
        self :
            A DMatLib object

        Returns
        -------

        """
        dict_mat = self.matlib.dict_mat
        self.nav_mat.blockSignals(True)
        self.nav_mat.clear()

        # Filter the material
        for ii, mat in enumerate(dict_mat["RefMatLib"]):
            # todo: add new filter
            if self.le_search.text() != "" and not match(
                ".*" + self.le_search.text().lower() + ".*", mat.name.lower()
            ):
                continue
            self.nav_mat.addItem("%03d" % (ii + 1) + " - " + mat.name)
        self.nav_mat.blockSignals(False)

        self.nav_mat_mach.blockSignals(True)
        self.nav_mat_mach.clear()

        # Filter the material
        for ii, mat in enumerate(dict_mat["MachineMatLib"]):
            # todo: add new filter
            if self.le_search.text() != "" and not match(
                ".*" + self.le_search.text().lower() + ".*", mat.name.lower()
            ):
                continue
            self.nav_mat_mach.addItem(
                "%03d" % (len(dict_mat["RefMatLib"]) + ii + 1) + " - " + mat.name
            )
        self.nav_mat_mach.blockSignals(False)
        # Hide the widget if machine material list is empty
        if len(dict_mat["MachineMatLib"]) == 0:
            self.in_machine_mat.setVisible(False)
            self.nav_mat_mach.setVisible(False)
        elif not self.in_machine_mat.isVisible():
            self.in_machine_mat.setVisible(True)
            self.nav_mat_mach.setVisible(True)

    def update_out(self, on_matlib=True):
        """Update all the output widget for material preview

        Parameters
        ----------
        self :
            A DMatLib object
        index :
            Current index of nav_mat (Default value = 0)

        Returns
        -------

        """
        # Get the selected material
        if on_matlib:
            # Return if no material is selected
            if self.nav_mat.currentRow() == -1 and self.nav_mat_mach.currentRow() != -1:
                return
            elif self.nav_mat.currentRow() == -1:
                self.nav_mat.setCurrentRow(0)

            # Set dict_key and mat_id to select the right material in MatLib
            dict_key = "RefMatLib"
            mat_id = self.nav_mat.currentRow()

            self.mat_selected_in_matlib = True

            # Deselect item in nav_mat_mach by setting its current row to -1
            self.nav_mat_mach.setCurrentRow(-1)
        else:
            # Return if no material is selected
            if self.nav_mat_mach.currentRow() == -1:
                return

            # Set dict_key and mat_id to select the right material in MatLib
            dict_key = "MachineMatLib"
            mat_id = self.nav_mat_mach.currentRow()

            self.mat_selected_in_matlib = False

            # Deselect item in nav_mat by setting its current row to -1
            self.nav_mat.setCurrentRow(-1)

        mat = self.matlib.dict_mat[dict_key][mat_id]

        # Update Main parameters
        self.out_name.setText(self.tr("name: ") + mat.name)
        if mat.is_isotropic:
            self.out_iso.setText(self.tr("type: isotropic"))
        else:
            self.out_iso.setText(self.tr("type: anisotropic"))

        # Update Electrical parameters
        if mat.elec is not None:
            update_text(self.out_rho_elec, "rho", mat.elec.rho, "ohm.m")
            # update_text(self.out_epsr,"epsr",mat.elec.epsr,None)

        # Update Economical parameters
        if mat.eco is not None:
            update_text(self.out_cost_unit, "cost_unit", mat.eco.cost_unit, u"€/kg")

        # Update Thermics parameters
        if mat.HT is not None:
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
        if mat.struct is not None:
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
        if mat.mag is not None:
            update_text(self.out_mur_lin, "mur_lin", mat.mag.mur_lin, None)
            update_text(self.out_Brm20, "Brm20", mat.mag.Brm20, "T")
            update_text(self.out_alpha_Br, "alpha_Br", mat.mag.alpha_Br, None)
            update_text(self.out_wlam, "wlam", mat.mag.Wlam, "m")
            if isinstance(mat.mag.BH_curve, ImportMatrixXls):
                BH_text = split(mat.mag.BH_curve.file_path)[1]
            elif isinstance(mat.mag.BH_curve, ImportMatrixVal):
                BH_text = "Matrix " + str(mat.mag.BH_curve.get_data().shape)
            else:
                BH_text = "-"
            self.out_BH.setText(BH_text)


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
