# -*- coding: utf-8 -*-

from os import getcwd, rename, remove
from os.path import join, dirname, abspath, split
from re import match

from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox, QListWidget

from ....Functions.load import load_matlib
from ....GUI.Dialog.DMatLib.Gen_DMatLib import Gen_DMatLib
from ....GUI.Dialog.DMatLib.DMatSetup.DMatSetup import DMatSetup
from ....definitions import DATA_DIR, MATLIB_DIR
from ....GUI import GUI_logger
from ....Functions.path_tools import abs_file_path


class DMatLib(Gen_DMatLib, QDialog):
    """Material Library Dialog to view and modify material data."""

    def __init__(self, matlib_path, matlib=[], index_first_matlib_mach=0, selected=0):
        """Init the Matlib GUI

        Parameters
        ----------
        self :
            a DMatLib object
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

        # do not copy to set the modification here (i.e. within DMatLib)
        if matlib_path == "":
            self.matlib_path = abspath(MATLIB_DIR)
        else:
            self.matlib_path = matlib_path

        # Load the material library
        self.matlib = load_matlib(matlib_path)
        # self.matlib contains the material library and the non referenced machine material
        # index_first_matlib_mach locate the first non referenced machine material in the list
        self.index_first_matlib_mach = len(self.matlib)

        # bool to know if the material selected is in MatLib
        self.mat_selected_in_matlib = True

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

        self.nav_mat.clicked.connect(lambda: self.update_out(on_matlib=True))
        self.nav_mat_mach.clicked.connect(lambda: self.update_out(on_matlib=False))
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

    def edit_material(self):
        """
        Open the setup material GUI to edit the current material.
        Changes will be saved to the corresponding material file.

        Parameters
        ----------
        self :
            A DMatLib object

        Returns
        -------

        """

        # Get the current material (filtering index)
        if len(self.nav_mat.selectedItems()) > 0:
            mat_id = int(self.nav_mat.currentItem().text()[:3]) - 1
        else:
            mat_id = int(self.nav_mat_mach.currentItem().text()[:3]) - 1
        # Open the setup GUI
        # (creates a copy of the material, i.e. self.matlib won't be edited directly)
        self.mat_win = DMatSetup(self.matlib[mat_id], self.mat_selected_in_matlib)
        return_code = self.mat_win.exec_()

        if return_code > 0:
            # Update the material only if the user save changes
            old_name = self.matlib[mat_id].name
            old_path = self.matlib[mat_id].path
            # keep material object
            self.matlib[mat_id].__init__(init_dict=self.mat_win.mat.as_dict())
            # Check if the material name is duplicated
            self.check_duplicated_material(mat_id)
            new_path = abs_file_path(self.matlib[mat_id].path, is_check=False)
            if old_name != self.matlib[mat_id].name:
                # Update the material name list only if modified
                index = self.nav_mat.currentRow()
                self.update_mat_list()
                if index < self.nav_mat.count() - 1:
                    self.nav_mat.setCurrentRow(index)
                else:
                    self.nav_mat.setCurrentRow(self.nav_mat.count() - 1)
                if self.mat_selected_in_matlib:
                    # Rename the saving file
                    rename(old_path, new_path)
            if return_code == 2:
                # Move the material into the Material library
                mat = self.matlib.pop(mat_id)
                mat_id = self.index_first_matlib_mach
                self.index_first_matlib_mach += 1
                self.matlib.insert(mat_id, mat)
                self.update_mat_list()
                # Set the path of the new matlib material
                new_path = join(MATLIB_DIR, self.matlib[mat_id].name + ".json").replace(
                    "\\", "/"
                )
                self.matlib[mat_id].path = new_path

            if self.mat_selected_in_matlib or return_code == 2:
                self.matlib[mat_id].save(new_path)

            self.update_mat_list()
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
        else:
            mat_id = int(self.nav_mat_mach.currentItem().text()[:3]) - 1

        # Open the setup GUI
        # (creates a copy of the material, i.e. self.matlib won't be edited directly)
        self.mat_win = DMatSetup(self.matlib[mat_id], self.mat_selected_in_matlib)
        return_code = self.mat_win.exec_()
        if return_code > 0:
            # Update the material only if the user validate at the end
            if self.mat_selected_in_matlib or return_code == 2:
                self.matlib.insert(self.index_first_matlib_mach, self.mat_win.mat)
                index_machine = self.index_first_matlib_mach
                self.index_first_matlib_mach += 1
                # Check if the name is duplicated
                self.check_duplicated_material(index_machine)
                GUI_logger.info(
                    "Creating the material: " + self.matlib[index_machine].path
                )
                if self.mat_selected_in_matlib:
                    new_path = abs_file_path(
                        self.matlib[index_machine].path, is_check=False
                    )
                else:  # Edit material path
                    new_path = join(
                        MATLIB_DIR, self.matlib[index_machine].name + ".json"
                    ).replace("\\", "/")
                    self.matlib[index_machine].path = new_path
                    self.mat_selected_in_matlib = True

                self.matlib[index_machine].save(new_path)
                self.nav_mat.setCurrentRow(self.nav_mat.count() - 1)
            else:
                self.matlib.append(self.mat_win.mat)
                # Check if the name is duplicated
                self.check_duplicated_material(len(self.matlib) - 1)
                self.nav_mat_mach.setCurrentRow(self.nav_mat_mach.count() - 1)

            self.update_mat_list()
            if self.mat_selected_in_matlib:
                self.nav_mat.setCurrentRow(self.nav_mat.count() - 1)
                self.update_out()
            else:
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
        if self.nav_mat.currentItem() != None:
            mat_id = int(self.nav_mat.currentItem().text()[:3]) - 1
        else:
            self.mat_selected_in_matlib = False
        # Do not delete machine material
        if not self.mat_selected_in_matlib:
            QMessageBox.information(self, "", "Cannot delete machine material.")
            return

        if len(self.matlib) > 1:

            del_msg = (
                "Are you sure you want to delete " + self.matlib[mat_id].name + " ?"
            )
            reply = QMessageBox.question(
                self, "Confirmation", del_msg, QMessageBox.Yes, QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                # delete only if confirmed
                GUI_logger.info("Deleting the material: " + self.matlib[mat_id].path)
                remove(self.matlib[mat_id].path)
                self.matlib.pop(mat_id)
                index = self.nav_mat.currentRow()
                self.update_mat_list()
                if index < self.nav_mat.count() - 1:
                    self.nav_mat.setCurrentRow(index)
                else:
                    self.nav_mat.setCurrentRow(self.nav_mat.count() - 1)
                # Change index_first_matlib_mach
                self.index_first_matlib_mach -= 1
                # Signal set by WMatSelect to update Combobox
                self.accepted.emit()
                self.update_mat_list()
        else:
            QMessageBox.information(
                self, "", "MatLib must contain at least one material."
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
        self.update_mat_list()
        self.nav_mat.setCurrentRow(0)

    def update_mat_list(self, selected_id=-1):
        """Update the list of Material with the current content of MatLib

        Parameters
        ----------
        self :
            A DMatLib object

        Returns
        -------

        """
        mat_list = self.matlib
        self.nav_mat.blockSignals(True)
        self.nav_mat.clear()

        # Filter the material
        for ii, mat in enumerate(mat_list[: self.index_first_matlib_mach]):
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
        index_first_matlib_mach = self.index_first_matlib_mach
        for ii, mat in enumerate(mat_list[index_first_matlib_mach:]):
            # todo: add new filter
            if self.le_search.text() != "" and not match(
                ".*" + self.le_search.text().lower() + ".*", mat.name.lower()
            ):
                continue
            self.nav_mat_mach.addItem(
                "%03d" % (index_first_matlib_mach + ii + 1) + " - " + mat.name
            )
        self.nav_mat_mach.blockSignals(False)
        # Hide the widget if machine material list is empty
        if len(mat_list[index_first_matlib_mach:]) == 0:
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
            mat_id = int(self.nav_mat.currentItem().text()[:3]) - 1  # for filtering
            self.mat_selected_in_matlib = True
            # Deselect item in nav_mat_mach
            self.nav_mat_mach.clearSelection()
        else:
            mat_id = (
                int(self.nav_mat_mach.currentItem().text()[:3]) - 1
            )  # for filtering
            self.mat_selected_in_matlib = False
            # Deselect item in nav_mat
            self.nav_mat.clearSelection()
        mat = self.matlib[mat_id]

        # mat = [mat for mat in self.matlib if mat.name == curr_name][0]

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
            if type(mat.mag.BH_curve).__name__ == "ImportMatrixXls":
                text = split(mat.mag.BH_curve.file_path)[1]
            else:
                text = "-"
            self.out_BH.setText(text)

    def add_material(self, material):
        """
        Add an existing material in the matlib
        """
        self.matlib.append(material)
        self.check_duplicated_material(-1)

    def check_duplicated_material(self, index):
        """
        Check if a material name is already used, modify it and its path if needed

        Parameters
        """
        # Check if the material is duplicated and rename it
        is_renamed = False
        mat_duplicated = True

        # Get the material name
        name = self.matlib[index].name

        # Browse the material list name and change the name while the name exist
        while mat_duplicated:
            mat_duplicated = False
            for i, mat in enumerate(self.matlib):
                if i != index:
                    if mat.name == name:
                        is_renamed = True
                        if name.endswith(")") and "(" in name:
                            idx = name.rfind("(")
                            num = int(name[idx + 1 : -1]) + 1
                            name = "{}({})".format(name[:idx], num)
                        else:
                            name += "(1)"
                        mat_duplicated = True
                        break
        # Change path to save the material
        if is_renamed:
            self.matlib[index].name = name
            path = self.matlib[index].path.replace("\\", "/")
            idx = path.rfind("/")
            if idx == -1:
                self.matlib[index].path = self.matlib[index].name + ".json"
            else:
                self.matlib[index].path = (
                    path[: idx + 1] + self.matlib[index].name + ".json"
                )


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
