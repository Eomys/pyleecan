# -*- coding: utf-8 -*-

from os import remove, rename
from os.path import join, dirname
from re import match
from logging import getLogger
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QDialog, QMessageBox

from ....Classes.Material import Material

from ....Functions.load import load_machine_materials, LIB_KEY, MACH_KEY
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

        self.w_setup.materialToDelete.connect(self.delete_material)
        self.w_setup.materialToRename.connect(self.rename_material)
        self.w_setup.materialToRevert.connect(self.revert_material)
        self.w_setup.materialSaved.connect(self.update_reference)
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
                ".*" + self.le_search.text().lower() + ".*", mat.name.lower()
            ):
                continue  # Skip add if not matching filter
            # Add material name as "005 - M400_50A"
            self.nav_mat.addItem("%03d" % (ii + 1) + " - " + mat.name)
        self.nav_mat.blockSignals(False)

        # Filter the Machine materials
        self.nav_mat_mach.blockSignals(True)
        self.nav_mat_mach.clear()
        for ii, mat in enumerate(material_dict[MACH_KEY]):
            if self.le_search.text() != "" and not match(
                ".*" + self.le_search.text().lower() + ".*", mat.name.lower()
            ):
                continue  # Skip add if not matching filter
            # Add material name as "005 - M400_50A"
            self.nav_mat_mach.addItem(
                "%03d" % (len(material_dict[LIB_KEY]) + ii + 1) + " - " + mat.name
            )
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
            index = int(self.nav_mat_mach.currentItem().text()[:3]) - 1
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
        getLogger(GUI_LOG_NAME).debug("DMatLib: reverting " + mat.name)
        self.material_dict[key][index] = mat
        self.w_setup.set_material(material=mat, is_save_needed=False)
        self.update_material_edit_status()  # Set Material to no longer edited

    def update_reference(self):
        """Material have been saved => Update references"""
        mat, key, index = self.get_current_material()
        getLogger(GUI_LOG_NAME).debug("DMatLib: Updating reference for " + mat.name)
        self.material_dict_ref[key][index] = mat.copy()

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
            new_mat.name = new_mat.name + "_copy"
            new_mat.path = new_mat.path[:-5] + "_copy.json"
        else:
            new_mat = Material()
            new_mat._set_None()
            new_mat.name = "New Material"
        # Adapt name to be unique
        # TODO

        # Add material to proper list
        key = MACH_KEY if self.is_lib_mat else LIB_KEY
        self.material_dict[key].append(new_mat)
        # Update treeview and select current material
        self.le_search.setText("")
        self.update_treeview_material()
        self.select_current_material(
            index=len(self.material_dict[key]) - 1, is_lib_mat=self.is_lib_mat
        )

    def delete_material(self):
        """Delete the selected material from the Library

        Parameters
        ----------
        self : DMatLib
            A DMatLib object
        """
        current_mat, _, _ = self.get_current_material()

        try:
            remove(current_mat.path)
            self.material_dict[LIB_KEY].remove(current_mat)
        except:
            # TODO better log
            return

        # Check that material was not part of the machine
        if self.machine is not None:
            load_machine_materials(
                machine=self.machine, material_dict=self.material_dict
            )
        self.update_treeview_material()
        if self.nav_mat.count() > 1:
            self.nav_mat.setCurrentRow(0)
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
        old_path = self.w_setup.mat_backup.path
        new_path = self.w_setup.mat.path

        try:
            rename(old_path, new_path)
        except:
            # TODO better log
            return

        # Check that material was not part of the machine
        if self.machine is not None:
            load_machine_materials(
                machine=self.machine, material_dict=self.material_dict
            )
        self.update_treeview_material()
        if self.nav_mat.count() > 1:
            self.nav_mat.setCurrentRow(0)
        # Signal set by WMatSelect to update Combobox
        self.materialListChanged.emit()

    #####################################################
    def validate_setup(self, return_code):
        is_lib_mat = self.current_dialog.is_lib_mat
        index = self.current_dialog.index
        mat_edit = self.current_dialog.mat
        init_name = self.current_dialog.init_name
        # Reset dialog
        self.current_dialog = None
        # 0: Cancel, 1: Save, 2: Add to Matlib (from Machine)
        if return_code > 0:
            if return_code == 2:  # Matlib=> machine or machine => Matlib
                if is_lib_mat:  # Library to machine
                    mat_edit.name = mat_edit.name + "_edit"
                    self.material_dict[MACH_KEY].append(mat_edit)
                    index = len(self.material_dict[MACH_KEY]) - 1
                else:
                    index = None  # will be handled as "New material" in Lib
                    mat_edit.path = join(
                        self.material_dict["MATLIB_PATH"], mat_edit.name + ".json"
                    )
                is_lib_mat = not is_lib_mat

            # Update materials in the machine
            if self.machine is not None:
                mach_mat_dict = self.machine.get_material_dict(path="self.machine")
                for mat_path, mach_mat in mach_mat_dict.items():
                    if mach_mat.name == init_name:  # Use original name
                        mat_path_split = mat_path.split(".")
                        setattr(
                            eval(".".join(mat_path_split[:-1])),
                            mat_path_split[-1],
                            mat_edit,
                        )
                        self.saveNeeded.emit()

            if mat_edit.name != init_name and is_lib_mat and index is not None:
                # Renaming a Library material => Delete original one
                remove(join(dirname(mat_edit.path), init_name + ".json"))
                self.material_dict[LIB_KEY][index] = mat_edit
                mat_edit.save(mat_edit.path)
                self.materialListChanged.emit()
            elif is_lib_mat and index is not None:  # Update
                self.material_dict[LIB_KEY][index] = mat_edit
                mat_edit.save(mat_edit.path)
            elif is_lib_mat and index is None:  # New in Library
                self.material_dict[LIB_KEY].append(mat_edit)
                index = len(self.material_dict[LIB_KEY]) - 1
                mat_edit.save(mat_edit.path)
                self.materialListChanged.emit()
            elif not is_lib_mat and index is None:  # New in Machine
                self.material_dict[MACH_KEY].append(mat_edit)
                index = len(self.material_dict[MACH_KEY]) - 1
                self.materialListChanged.emit()
            else:
                self.material_dict[MACH_KEY][index] = mat_edit
                if mat_edit.name != init_name:  # Rename
                    self.materialListChanged.emit()

            # Update machine material (Machine => Lib)
            if return_code == 2 and is_lib_mat:
                load_machine_materials(
                    machine=self.machine, material_dict=self.material_dict
                )
                self.materialListChanged.emit()
            # Update material list
            self.update_treeview_material()
            if is_lib_mat:
                self.nav_mat.setCurrentRow(index)
            else:
                self.nav_mat_mach.setCurrentRow(index)

            # Signal set by WMatSelect to update Combobox
            self.accepted.emit()

    def closeEvent(self, event):
        """Display a message before leaving

        Parameters
        ----------
        self : DMatSetup
            A DMatSetup object
        event :
            The closing event
        """
        # Close popup if needed
        if self.current_dialog is not None:
            self.current_dialog.close()


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
