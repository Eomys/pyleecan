# -*- coding: utf-8 -*-

from os import remove, rename
from os.path import join, dirname
from re import match
from logging import getLogger
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QDialog, QMessageBox

from ....Classes.Material import Material

from ....Functions.load import load_machine_materials, LIB_KEY, MACH_KEY, PATH_KEY
from ....GUI.Dialog.DMatLib.Ui_DMatLib import Ui_DMatLib
from ....loggers import GUI_LOG_NAME


class DMatLib(Ui_DMatLib, QDialog):
    """Material Library Dialog to view and modify material data."""

    # Signal to W_MachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    materialListChanged = Signal()

    def __init__(self, material_dict, machine=None, is_lib_mat=True, selected_id=0):
        """Init the Matlib GUI

        Parameters
        ----------
        self : DMatLib
            a DMatLib object
        material_dict: dict
            Materials dictionary (library + machine)
        machine : Machine
            A Machine object to update (if None, material library only)
        is_lib_mat : bool
            True: Selected material is part of the Library (False machine)
        selected_id :
            Index of the currently selected material
        """

        # Build the interface according to the .ui file
        QDialog.__init__(self)
        self.setupUi(self)

        # material_dict contains two list, library or machine
        # Current selected material in is the Library (false machine)
        self.is_lib_mat = is_lib_mat

        # Deep copy of material dict (edit only on save)
        self.material_dict_ref = material_dict  # Backup for revert
        self.material_dict = dict()  # Current library being edited
        for key in material_dict:
            if isinstance(material_dict[key], list):
                self.material_dict[key] = list()
                for mat in material_dict[key]:
                    self.material_dict[key].append(mat.copy())
            elif isinstance(material_dict[key], str):
                self.material_dict[key] = material_dict[key]
            else:
                raise Exception("Unknow type in material_dict")
        self.edited_material_list = list()  # Material from library with modifications

        # keep machine to edit materials (while closing)
        if machine is not None:
            self.machine = machine
            if self.machine.name not in ["", None]:
                self.in_machine_mat.setText("Materials in " + self.machine.name)
        else:
            self.machine = None
            self.b_switch.hide()  # No material in the machine

        # Scan material_dict to create treeview
        self.update_treeview_material()

        # Default current material is first line of library
        self.select_current_material(selected_id, is_lib_mat)

        # Connect Slot/Signals
        self.nav_mat.clicked.connect(
            lambda: self.select_current_material(index=None, is_lib_mat=True)
        )
        self.nav_mat_mach.clicked.connect(
            lambda: self.select_current_material(index=None, is_lib_mat=False)
        )
        self.le_search.textChanged.connect(self.update_treeview_material)

        self.b_copy.clicked.connect(lambda: self.new_material(is_copy=True))
        self.b_new.clicked.connect(lambda: self.new_material(is_copy=False))
        self.b_switch.clicked.connect(self.edit_in_machine)

        self.w_setup.materialToDelete.connect(self.delete_material)
        self.w_setup.materialToRename.connect(self.rename_material)
        self.w_setup.materialToRevert.connect(self.revert_material)
        self.w_setup.materialToSave.connect(self.save_material)
        self.w_setup.saveNeededChanged.connect(self.update_material_edit_status)

    def update_treeview_material(self):
        """Update the list of Material with the current content of MatLib/Machine

        Parameters
        ----------
        self : DMatLib
            A DMatLib object
        """
        material_dict = self.material_dict

        # Filter the material Library
        self.nav_mat.blockSignals(True)
        self.nav_mat.clear()
        for ii, mat in enumerate(material_dict[LIB_KEY]):
            if self.le_search.text() != "" and not match(
                ".*" + self.le_search.text().lower() + ".*", str(mat.name).lower()
            ):
                continue  # Skip add if not matching filter
            # Add material name as "005 - M400_50A"
            mat_text = "%03d" % (ii + 1) + " - " + str(mat.name)
            if mat in self.edited_material_list:
                mat_text += " *"
            self.nav_mat.addItem(mat_text)
        self.nav_mat.blockSignals(False)

        # Filter the Machine materials
        self.nav_mat_mach.blockSignals(True)
        self.nav_mat_mach.clear()
        for ii, mat in enumerate(material_dict[MACH_KEY]):
            if self.le_search.text() != "" and not match(
                ".*" + self.le_search.text().lower() + ".*", str(mat.name).lower()
            ):
                continue  # Skip add if not matching filter
            # Add material name as "005 - M400_50A"
            mat_text = (
                "%03d" % (len(material_dict[LIB_KEY]) + ii + 1) + " - " + str(mat.name)
            )
            if mat in self.edited_material_list:
                mat_text += " *"
            self.nav_mat_mach.addItem(mat_text)
        self.nav_mat_mach.blockSignals(False)

        # Hide the machine treeview if machine material list is empty
        if len(material_dict[MACH_KEY]) == 0:
            self.in_machine_mat.setVisible(False)
            self.nav_mat_mach.setVisible(False)
        elif not self.in_machine_mat.isVisible():
            self.in_machine_mat.setVisible(True)
            self.nav_mat_mach.setVisible(True)

    def get_current_material(self, is_reference=False):
        """Return the current selected material

        Parameters
        ----------
        self : DMatLib
            A DMatLib object
        is_reference : bool
            False (default): return from edited matlib else from reference
        """
        if is_reference:
            mat_dict = self.material_dict_ref
        else:
            mat_dict = self.material_dict

        # Get the selected material
        if self.is_lib_mat:
            if self.nav_mat.currentRow() == -1:  # No material selected
                return None, None, None
            index = int(self.nav_mat.currentItem().text()[:3]) - 1
            key = LIB_KEY
        else:
            if self.nav_mat_mach.currentRow() == -1:  # No material selected
                return None, None, None
            index = (
                int(self.nav_mat_mach.currentItem().text()[:3])
                - 1
                - len(self.material_dict[LIB_KEY])
            )
            key = MACH_KEY

        return mat_dict[key][index], key, index

    def select_current_material(self, index=None, is_lib_mat=True):
        """Change the current selected material

        Paramaters
        ----------
        self : DMatLib
            A DMatLib object
        index : int
            Row indew to select in the treeview (None use current)
        is_lib_mat : bool
            True: new current is from Library, False from machine
        """
        self.is_lib_mat = is_lib_mat
        if self.is_lib_mat:
            self.b_switch.setEnabled(True)
        else:
            self.b_switch.setEnabled(False)
        # Set the selected treeview currentRow (if needed)
        if index is not None:
            if self.is_lib_mat:
                self.nav_mat.setCurrentRow(index)
            else:
                self.nav_mat_mach.setCurrentRow(index)
        self.update_material_wid()

    def update_material_wid(self):
        """Display the current selected material"""
        material, _, _ = self.get_current_material()
        is_save_needed = material in self.edited_material_list
        self.w_setup.set_material(material=material, is_save_needed=is_save_needed)

    def revert_material(self):
        """Revert current material"""

        mat_ref, key, index = self.get_current_material(is_reference=True)
        mat = mat_ref.copy()
        getLogger(GUI_LOG_NAME).debug("DMatLib: reverting " + str(mat.name))
        self.material_dict[key][index] = mat
        self.w_setup.set_material(material=mat, is_save_needed=False)
        self.update_material_edit_status()  # Set Material to no longer edited

    def save_material(self):
        """Material have been saved => Update references"""
        mat, key, index = self.get_current_material()

        # Saving material (if in Library only)
        if self.is_lib_mat:
            try:
                mat.save(mat.path)
            except Exception as e:
                err_msg = (
                    "Error while saving material "
                    + str(mat.name)
                    + " at "
                    + str(mat.path)
                    + ":\n"
                    + str(e)
                )
                QMessageBox().critical(
                    self,
                    self.tr("Error"),
                    self.tr(err_msg),
                )
                getLogger(GUI_LOG_NAME).error(err_msg)
                return
            getLogger(GUI_LOG_NAME).debug(mat.path + " saved")

        # Updating reference
        getLogger(GUI_LOG_NAME).debug(
            "DMatLib: Updating reference for " + str(mat.name)
        )
        self.material_dict_ref[key][index] = mat.copy()

        # Update materials in the machine
        if self.machine is not None:
            mach_mat_dict = self.machine.get_material_dict(path="self.machine")
            for mat_path, mach_mat in mach_mat_dict.items():
                if mach_mat.name == mat.name:  # Use original name
                    mat_path_split = mat_path.split(".")
                    setattr(
                        eval(".".join(mat_path_split[:-1])),
                        mat_path_split[-1],
                        self.material_dict_ref[key][index],
                    )
                    self.saveNeeded.emit()
        self.w_setup.set_save_needed(is_save_needed=False)

    def update_material_edit_status(self):
        """Keep track that the current material is different from the reference
        and not saved yet
        """
        if self.is_lib_mat:  # Available only for library materials
            mat, _, _ = self.get_current_material()
            item = self.nav_mat.currentItem()
            if self.w_setup.is_save_needed:
                if mat not in self.edited_material_list:
                    self.edited_material_list.append(mat)
                # Add "*" in treeview if needed
                if "*" not in item.text():
                    item.setText(item.text() + " *")
            else:
                if mat in self.edited_material_list:
                    self.edited_material_list.remove(mat)
                # Remove "*" in treeview if needed
                if "*" in item.text():
                    item.setText(item.text()[:-2])

    #########################################
    def new_material(self, is_copy=True):
        """Open the setup material GUI to create a new material according to
        the current material

        Parameters
        ----------
        self : DMatLib
            A DMatLib object
        is_copy : bool
            True copy current material, else use empty material
        """
        # Create new material
        if is_copy:
            current_mat, _, _ = self.get_current_material()
            new_mat = current_mat.copy()
            if "_copy" not in str(new_mat.name):
                new_mat.name = str(new_mat.name) + "_copy"
                new_mat.path = new_mat.path[:-5] + "_copy.json"
        else:
            new_mat = Material()
            new_mat._set_None()
            new_mat.name = "New Material"
            new_mat.path = join(self.material_dict[PATH_KEY], new_mat.name + ".json")
        # Adapt name to be unique
        name_list = [mat.name for mat in self.material_dict[LIB_KEY]]
        name_list.extend([mat.name for mat in self.material_dict[MACH_KEY]])

        # Renaming the material so that we have "_copy","_copy_2","_copy_3"...
        if new_mat.name in name_list:
            # Adding number after copy
            if new_mat.name[-4:] == "copy":
                new_mat.name = new_mat.name + "_2"
            # Setting the index after the current one
            else:
                index = 1
                while int(new_mat.name[-1]) >= index:
                    index += 1
                new_mat.name = new_mat.name[:-1]
                new_mat.name = new_mat.name + str(index)
            new_mat.path = join(dirname(new_mat.path), new_mat.name + ".json")

        # Save if in MatLib
        if self.is_lib_mat:
            try:
                new_mat.save(new_mat.path)
            except Exception as e:
                err_msg = (
                    "Error while saving new material at "
                    + str(new_mat.path)
                    + ":\n"
                    + str(e)
                )
                QMessageBox().critical(
                    self,
                    self.tr("Error"),
                    self.tr(err_msg),
                )
                getLogger(GUI_LOG_NAME).error(err_msg)
                return

        # Add material to proper list
        key = LIB_KEY if self.is_lib_mat else MACH_KEY
        self.material_dict[key].append(new_mat)
        self.material_dict_ref[key].append(new_mat)
        # Update treeview and select current material
        self.le_search.setText("")
        self.update_treeview_material()
        self.select_current_material(
            index=len(self.material_dict[key]) - 1, is_lib_mat=self.is_lib_mat
        )
        # Signal set by WMatSelect to update Combobox
        self.materialListChanged.emit()

    def edit_in_machine(self):
        """Copy the material to be edited in the machine only"""
        # Create new material from unmodified version of material
        current_mat, _, _ = self.get_current_material(is_reference=True)
        new_mat = current_mat.copy()
        if "_edit" not in str(new_mat.name):
            new_mat.name = str(new_mat.name) + "_edit"
            new_mat.path = new_mat.path[:-5] + "_edit.json"

        # Adapt name to be unique
        name_list = [mat.name for mat in self.material_dict[LIB_KEY]]
        name_list.extend([mat.name for mat in self.material_dict[MACH_KEY]])
        if new_mat.name in name_list:
            index = 1
            while new_mat.name + "_" + str(index) in name_list:
                index += 1
            new_mat.name = new_mat.name + "_" + str(index)
            new_mat.path = join(dirname(new_mat.path), new_mat.name + ".json")

        # Add material to machine list
        key = MACH_KEY
        self.material_dict[key].append(new_mat)
        self.material_dict_ref[key].append(new_mat)
        # Update treeview and select current material
        self.le_search.setText("")
        self.update_treeview_material()
        self.select_current_material(
            index=len(self.material_dict[key]) - 1, is_lib_mat=False
        )
        # Update machine to use new material
        if self.machine is not None:
            mach_mat_dict = self.machine.get_material_dict(path="self.machine")
            for mat_path, mach_mat in mach_mat_dict.items():
                if mach_mat.name == current_mat.name:
                    mat_path_split = mat_path.split(".")
                    setattr(
                        eval(".".join(mat_path_split[:-1])),
                        mat_path_split[-1],
                        new_mat.copy(),
                    )
                    self.saveNeeded.emit()
        # Signal set by WMatSelect to update Combobox
        self.materialListChanged.emit()

    def delete_material(self):
        """Delete the selected material from the Library

        Parameters
        ----------
        self : DMatLib
            A DMatLib object
        """
        current_mat, key, index = self.get_current_material()

        # Ask before delete
        msg = self.tr(
            "Do you want to remove material "
            + str(current_mat.name)
            + " from the library?"
        )
        reply = QMessageBox.question(
            self,
            self.tr("Deleting material"),
            msg,
            QMessageBox.Yes,
            QMessageBox.No,
        )
        self.qmessagebox_question = reply
        if reply == QMessageBox.No:
            return

        # Delete the material (only if in library)
        if self.is_lib_mat:
            try:
                remove(current_mat.path)
                self.material_dict[key].pop(index)
                self.material_dict_ref[key].pop(index)
            except Exception as e:
                err_msg = (
                    "Error while deleting material from "
                    + str(current_mat.path)
                    + ":\n"
                    + str(e)
                )
                QMessageBox().critical(
                    self,
                    self.tr("Error"),
                    self.tr(err_msg),
                )
                getLogger(GUI_LOG_NAME).error(err_msg)
                return
            getLogger(GUI_LOG_NAME).info(str(current_mat.name) + " was deleted")

        # Check that material was not part of the machine
        if self.machine is not None:
            load_machine_materials(
                machine=self.machine, material_dict=self.material_dict_ref
            )
            load_machine_materials(
                machine=self.machine, material_dict=self.material_dict
            )
        self.update_treeview_material()
        # Select first material (if any)
        if self.is_lib_mat:
            if self.nav_mat.count() > 1:
                self.nav_mat.setCurrentRow(0)
        else:
            if self.nav_mat_mach.count() > 1:
                self.nav_mat_mach.setCurrentRow(0)
        self.select_current_material()
        # Signal set by WMatSelect to update Combobox
        self.materialListChanged.emit()

    def rename_material(self):
        """Rename the selected material from the Library/Machine

        Parameters
        ----------
        self : DMatLib
            A DMatLib object
        """

        # Path have been updated in the widget
        old_path = self.w_setup.init_path
        new_path = self.w_setup.mat.path

        # Rename file only if in Library
        if self.is_lib_mat:
            try:
                remove(old_path)
                self.w_setup.mat.save(new_path)
            except Exception as e:
                err_msg = (
                    "Error while renaming material from "
                    + str(self.w_setup.init_path)
                    + " to "
                    + str(self.w_setup.mat.path)
                    + ":\n"
                    + str(e)
                )
                QMessageBox().critical(
                    self,
                    self.tr("Error"),
                    self.tr(err_msg),
                )
                getLogger(GUI_LOG_NAME).error(err_msg)
                return

        getLogger(GUI_LOG_NAME).info(
            self.w_setup.init_name + " was renamed to " + str(self.w_setup.mat.name)
        )
        # Update reference (material_dict is already updated)
        mat, key, index = self.get_current_material()
        self.material_dict_ref[key][index] = mat.copy()

        # Update materials in the machine
        if self.machine is not None:
            mach_mat_dict = self.machine.get_material_dict(path="self.machine")
            for mat_path, mach_mat in mach_mat_dict.items():
                if mach_mat.name == self.w_setup.init_name:
                    mat_path_split = mat_path.split(".")
                    setattr(
                        eval(".".join(mat_path_split[:-1])),
                        mat_path_split[-1],
                        self.material_dict_ref[key][index],
                    )
                    self.saveNeeded.emit()

        # Update list of material from the machine
        if self.machine is not None:
            load_machine_materials(
                machine=self.machine, material_dict=self.material_dict
            )
        self.le_search.setText("")  # Remove filter
        self.update_treeview_material()
        if self.is_lib_mat:
            self.nav_mat.setCurrentRow(index)
        else:
            self.nav_mat_mach.setCurrentRow(index)

        # Signal set by WMatSelect to update Combobox
        self.materialListChanged.emit()


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
    if val[-2:] == ".0":  # Remove ".0" sufix
        val = val[:-2]

    if name is None:  # For E, G, nu table
        txt = val
    else:
        if unit is None:
            txt = name + " = " + val
        else:
            txt = name + " = " + val + " [" + unit + "]"
    label.setText(txt)
