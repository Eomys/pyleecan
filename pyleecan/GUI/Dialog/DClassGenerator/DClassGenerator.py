import os
import subprocess

from os.path import join, isfile, isdir, realpath, basename
from shutil import copyfile, rmtree, copytree
from functools import partial
from types import MethodType

from PySide2.QtCore import Qt, QDir
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (
    QMessageBox,
    QWidget,
    QFileSystemModel,
    QLabel,
    QLineEdit,
    QHeaderView,
    QPushButton,
    QMenu,
)

from ...Resources import pixmap_dict
from ..DClassGenerator.Ui_DClassGenerator import Ui_DClassGenerator

from ....definitions import DOC_DIR, MAIN_DIR

from ....Generator.read_fct import read_file, read_all
from ....Generator.run_generate_classes import run_generate_classes
from ....Generator.write_fct import (
    write_file,
    MATCH_META_DICT,
    MATCH_PROP_DICT,
    MATCH_CONST_DICT,
)


class DClassGenerator(Ui_DClassGenerator, QWidget):
    """Main windows of the Machine Setup Tools"""

    def __init__(self, path_editor_py="", path_editor_csv=""):
        """Initialize the class generator GUI

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        path_editor_py : str
            Path to default program to open python files
        path_editor_csv : str
            Path to default program to open csv files
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        self.setupUi(self)

        # Setup windows icon
        self.setWindowIcon(QIcon(pixmap_dict["soft_icon"]))

        # Get parent dict containing all children of each class
        gen_dict = read_all(DOC_DIR, is_update_mother_of_mother=False)
        self.parent_dict = dict()
        for class_name, class_dict in gen_dict.items():
            self.parent_dict[class_name] = sorted(
                class_dict["daughters"], key=str.lower
            )

        # Init current variables
        self.current_class_dict = None
        self.current_class_index = None
        self.list_class_modified = list()
        if is_app(path_editor_py):
            self.path_editor_py = path_editor_py
        else:
            raise Exception(
                "Application to edit python files doesn't exit at path: "
                + path_editor_py
            )
        if is_app(path_editor_csv):
            self.path_editor_csv = path_editor_csv
        else:
            raise Exception(
                "Application to edit csv files doesn't exit at path: " + path_editor_csv
            )
        self.class_gen_path = DOC_DIR.replace("\\", "/")

        # Show path to class generator
        self.le_path_classgen.setText(DOC_DIR)
        self.le_path_classgen.setDisabled(True)
        self.le_path_classgen.setHidden(False)

        # Store list of properties for further use
        self.list_prop = list(MATCH_PROP_DICT.keys())

        # Store list of metadata for further use
        self.list_meta = list(MATCH_META_DICT.keys())

        # Store list of constants for further use
        self.list_const = list(MATCH_CONST_DICT.keys())

        # Init treeview
        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(self.class_gen_path)
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)
        self.dirModel.setReadOnly(False)
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.setModel(self.dirModel)
        self.treeView.setRootIndex(self.dirModel.index(self.class_gen_path))
        self.treeView.setHeaderHidden(True)
        self.treeView.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        # Init tables and buttons
        self.init_tables_buttons()

        # Connect treeview to methods
        self.dirModel.fileRenamed.connect(self.renameClassMethods)
        self.treeView.collapsed.connect(self.onItemCollapse)
        self.treeView.expanded.connect(self.onItemExpand)
        self.treeView.clicked.connect(self.update_class_selected)
        self.treeView.customContextMenuRequested.connect(self.openContextMenu)

        # Connect save class button
        self.le_classname.editingFinished.connect(self.renameClass)

        # Connect save class button
        self.b_saveclass.clicked.connect(self.saveClass)

        # Connect add property button
        self.b_addprop.clicked.connect(self.addProp)

        # Connect add method button
        self.b_addmeth.clicked.connect(self.addMethod)

        # Connect method folder button
        self.b_browse.clicked.connect(self.browseMethod)

        # Connect add constant button
        self.b_addconst.clicked.connect(self.addConst)

        # Connect generate class button
        self.b_genclass.clicked.connect(self.genClass)
        self.is_black.setChecked(True)

    def init_tables_buttons(self):
        """Init all tables and buttons of class properties and methods

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object

        """
        # Init class name line edit
        self.le_classname.setEnabled(False)
        self.le_classname.setText("Class name")

        # Disable save_class button
        self.b_saveclass.setEnabled(False)

        # Disable add property button
        self.b_addprop.setEnabled(False)

        # Disable add method button
        self.b_addmeth.setEnabled(False)

        # Disable browse button
        self.b_browse.setEnabled(False)

        # Disable add constant button
        self.b_addconst.setEnabled(False)

        # Disable generate class button
        self.b_genclass.setEnabled(False)

        # Init table of properties
        self.table_prop.setColumnCount(len(self.list_prop) + 2)
        self.table_prop.setRowCount(1)
        for col, prop_name in enumerate(self.list_prop):
            qlabel = QLabel(prop_name)
            qlabel.setAlignment(Qt.AlignCenter)
            self.table_prop.setCellWidget(0, col, qlabel)
            self.table_prop.cellWidget(0, col).setStyleSheet("background-color: grey")
        self.table_prop.horizontalHeader().hide()
        self.table_prop.verticalHeader().hide()

        # Init table of methods
        self.table_meth.setColumnCount(4)
        self.table_meth.setRowCount(0)
        self.table_meth.horizontalHeader().hide()
        self.table_meth.verticalHeader().hide()

        # Init table of metadata
        self.table_meta.setRowCount(1)
        self.table_meta.setColumnCount(len(self.list_meta))
        # Loop on columns to write metadata
        for col, meta_name in enumerate(self.list_meta):
            # Create QLabel for each metadata label
            qlabel = QLabel(str(meta_name))
            qlabel.setAlignment(Qt.AlignCenter)
            self.table_meta.setCellWidget(0, col, qlabel)
            self.table_meta.cellWidget(0, col).setStyleSheet("background-color: grey")
        self.table_meta.horizontalHeader().hide()
        self.table_meta.verticalHeader().hide()

        # Init table of constants
        self.table_const.setRowCount(1)
        self.table_const.setColumnCount(len(self.list_const) + 2)
        # Loop on columns to write metadata
        for col, const_name in enumerate(self.list_const):
            # Create QLabel for each constant label
            qlabel = QLabel(str(const_name))
            qlabel.setAlignment(Qt.AlignCenter)
            self.table_const.setCellWidget(0, col, qlabel)
            self.table_const.cellWidget(0, col).setStyleSheet("background-color: grey")
        self.table_const.horizontalHeader().hide()
        self.table_const.verticalHeader().hide()

    def update_class_selected(self, index):
        """Update GUI with selected class from TreeView by loading csv file

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        index : QModelIndex
            Model index of current selected item in treeview

        """

        if self.dirModel.isDir(index):
            # Don't do anything if click on folder
            return

        # Get class name of selected csv file
        class_name = self.get_obj_name(index)

        if class_name[-4:] != ".csv":
            # Check if file is a csv
            return

        if self.current_class_dict is not None:
            # Check if current class has been modified
            is_modified = self.check_class_modified(index)
            if not is_modified and index == self.current_class_index:
                # No need to reload interface with saved class since saveClass already did it
                return

        # Store current class index to save class after modifications
        self.current_class_index = index

        # Import csv at csv_path and store class in self.current_class_dict
        csv_path = realpath(self.dirModel.filePath(index))
        self.import_class_from_csv(csv_path)

        if self.current_class_dict is not None:
            # Update GUI with data contained in self.current_class_dict
            print("Selecting class " + class_name[-4:] + ": " + csv_path)
            self.set_class_selected()

    def set_class_selected(self):
        """Update GUI with data contained in

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        """
        # Fill all tables
        self.fill_table_prop()
        self.fill_table_meth()
        self.fill_table_meta()
        self.fill_table_const()

        # Change head label to current class name
        self.le_classname.setText(self.current_class_dict["name"])
        self.le_classname.setEnabled(True)

        # Disable save class button
        self.b_saveclass.setEnabled(False)

        # Enable add property button
        self.b_addprop.setEnabled(True)

        # Enable add method button
        self.b_addmeth.setEnabled(True)

        # Enable browse button
        self.b_browse.setEnabled(True)

        # Enable add constant button
        self.b_addconst.setEnabled(True)

    def check_class_modified(self, index=None):
        """Check if class is modified (ignore daughters since it is generated automatically)

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        index : QModelIndex
            Treeview index of current selected object

        Returns
        -------
        is_modified_class : bool
            True if class has been modified in comparison with class csv file content
        """

        # Init return bool
        is_modified_class = False

        # Get current class dict from tables
        current_class_dict = self.get_current_class_dict_from_tables()

        # Check if current_class_dict is different from class_dict in .csv file
        csv_path = realpath(self.dirModel.filePath(self.current_class_index))

        # Load csv file (meaning current class without modifications)
        try:
            class_dict_ref = read_file(csv_path)
        except Exception as e:
            print("Cannot check reference csv file: " + csv_path)
            return True

        # Compare class dict keys
        list_key_ref = list(class_dict_ref.keys())
        list_key_current = list(current_class_dict.keys())

        if list_key_ref.sort() != list_key_current.sort():
            is_modified_class = True

        if str(class_dict_ref["name"]) != str(current_class_dict["name"]):
            is_modified_class = True

        if realpath(class_dict_ref["path"]) != realpath(current_class_dict["path"]):
            is_modified_class = True

        if str(class_dict_ref["desc"]) != str(current_class_dict["desc"]):
            is_modified_class = True

        if str(class_dict_ref["package"]) != str(current_class_dict["package"]):
            is_modified_class = True

        if str(class_dict_ref["mother"]) != str(current_class_dict["mother"]):
            is_modified_class = True

        if len(class_dict_ref["properties"]) != len(current_class_dict["properties"]):
            is_modified_class = True

        if len(class_dict_ref["constants"]) != len(current_class_dict["constants"]):
            is_modified_class = True

        if len(class_dict_ref["methods"]) != len(current_class_dict["methods"]):
            is_modified_class = True

        if not is_modified_class:
            # Compare property and constants values inside list of dict
            for key in ["properties", "constants"]:
                val0 = class_dict_ref[key]
                val1 = current_class_dict[key]
                for ii, dict0 in enumerate(val0):
                    for name, data0 in dict0.items():
                        if name not in val1[ii]:
                            # Property/Constant dicts are different if they don't have same keys
                            is_modified_class = True
                        else:
                            data1 = val1[ii][name]
                        if data0 != data1:
                            try:
                                # Try to set variables as float for comparison
                                if float(data0) != float(data1):
                                    is_modified_class = True
                            except Exception as e:
                                # Try to set variables as str for comparison
                                if str(data0) != str(data1):
                                    is_modified_class = True

        if not is_modified_class:
            # Compare methods name list
            for meth_name in class_dict_ref["methods"]:
                if meth_name not in current_class_dict["methods"]:
                    is_modified_class = True

        if is_modified_class:
            if index is None:
                text = "Save current class modifications before generating classes ?"
            elif index == self.current_class_index:
                text = "Save current class modifications before reloading same class ?"
            else:
                text = "Save current class modifications before loading another class?"
            # Send toggle window to ask if save is required
            reply = QMessageBox().question(
                self,
                "Warning: modifications not saved",
                text,
                QMessageBox.Yes,
                QMessageBox.No,
            )

            if reply == QMessageBox.Yes:
                # Save current class if yes
                self.saveClass()
                is_modified_class = False

        return is_modified_class

    def import_class_from_csv(self, csv_path):
        """Import class from csv file when clicking on a csv in TreeView

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        csv_path : str
            Path to csv file to import
        """

        # Load csv file
        try:
            current_class_dict = read_file(csv_path)
        except Exception as e:
            print("Cannot load csv file: " + csv_path)
            return

        # Set children list from generation dict
        if current_class_dict["name"] in self.parent_dict:
            current_class_dict["daughters"] = self.parent_dict[
                current_class_dict["name"]
            ]
        else:
            print("Cannot set children class list from parent_dict")
            current_class_dict["daughters"] = list()

        # Store current class information for further use
        self.current_class_dict = current_class_dict

    def fill_table_prop(self):
        """Fill tables of properties with current class dict content

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object

        """
        # Fill table of properties
        prop_list = self.current_class_dict["properties"]

        # Set the number of rows to the number of properties (first row are labels)
        self.table_prop.setRowCount(len(prop_list) + 1)

        # Loop on rows to write properties
        for row, prop_dict in enumerate(prop_list):
            # Loop on columns to write parameters associated to each property
            for col, val in enumerate(self.list_prop):
                data = prop_dict[MATCH_PROP_DICT[val]]
                # Create QLineEdit for each parameter
                line_edit = QLineEdit(str(data))
                line_edit.setAlignment(Qt.AlignLeft)
                if col == 0:
                    # Add method to check that property can't be renamed to an existing one
                    line_edit.editingFinished.connect(
                        partial(self.renameProp, line_edit)
                    )
                else:
                    # Add method to check if value of line edit has changed and save is requested
                    line_edit.mousePressEvent = MethodType(
                        partial(self.line_edit_clicked, line_edit=line_edit), line_edit
                    )
                    line_edit.editingFinished.connect(
                        partial(self.saveRequested, line_edit)
                    )
                self.table_prop.setCellWidget(row + 1, col, line_edit)
            # Add property buttons
            self.addRowButtonsProp(row + 1)

        # Adjust column width
        self.table_prop.resizeColumnsToContents()

    def addRowButtonsProp(self, row_index):
        """Delete row in table of properties given row index to delete

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        row_index : int
            Index of row to delete

        """

        # Add delete button
        b_del_prop = QPushButton(text="Delete", parent=self.table_prop)
        b_del_prop.clicked.connect(partial(self.deleteProp, b_del_prop))
        self.table_prop.setCellWidget(row_index, len(self.list_prop), b_del_prop)
        # Add duplicate button
        b_dup_prop = QPushButton(text="Duplicate", parent=self.table_prop)
        b_dup_prop.clicked.connect(partial(self.duplicateProp, b_dup_prop))
        self.table_prop.setCellWidget(row_index, len(self.list_prop) + 1, b_dup_prop)

    def addProp(self):
        """Add one empty row at the end of table of properties

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object

        """

        self.table_prop.setRowCount(self.table_prop.rowCount() + 1)

        last_row = self.table_prop.rowCount() - 1

        for col in range(len(self.list_prop)):
            line_edit = QLineEdit("")
            line_edit.setAlignment(Qt.AlignLeft)
            self.table_prop.setCellWidget(last_row, col, line_edit)

        # Connect name QLineEdit to renameProp method
        self.table_prop.cellWidget(last_row, 0).editingFinished.connect(
            partial(self.renameProp, self.table_prop.cellWidget(last_row, 0))
        )

        # Add Delete and Duplicate buttons
        self.addRowButtonsProp(last_row)

        # Set Duplicate button to disabled since Name is empty
        self.table_prop.cellWidget(last_row, len(self.list_prop) + 1).setEnabled(False)

        # Add empty prop in current class dict
        self.current_class_dict["properties"].append({"name": ""})

        # Adjust column width
        self.table_prop.resizeColumnsToContents()

        # Enable save class button
        self.b_saveclass.setEnabled(True)

    def deleteProp(self, button):
        """Delete row in table of properties

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        button : QPushButton
            Button that emits signal

        """

        # Get row_index of clicked delete button
        for row in range(1, self.table_prop.rowCount(), 1):
            if self.table_prop.cellWidget(row, len(self.list_prop)) == button:
                row_index = row
                break

        # Remove row at given index
        self.table_prop.removeRow(row_index)

        # Delete row in current class dict
        del self.current_class_dict["properties"][row_index - 1]

        # Enable save class button
        self.b_saveclass.setEnabled(True)

    def duplicateProp(self, button):
        """Duplicate row in table of properties

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        button : QPushButton
            Button that emits signal

        """

        # Get row_index of clicked duplicate button
        for row in range(1, self.table_prop.rowCount(), 1):
            if self.table_prop.cellWidget(row, len(self.list_prop) + 1) == button:
                row_index = row
                break

        # Add empty row at the end
        self.table_prop.setRowCount(self.table_prop.rowCount() + 1)
        last_row = self.table_prop.rowCount() - 1

        # Browse columns of the row to duplicate and add same items in last row
        for col in range(len(self.list_prop)):
            val = self.table_prop.cellWidget(row_index, col).text()
            if col == 0:
                # Check that property name doesn't already exist
                for row in range(1, self.table_prop.rowCount() - 1, 1):
                    other = self.table_prop.cellWidget(row, col).text()
                    if val == other:
                        val += "_copy"
            cell_widget = type(self.table_prop.cellWidget(row_index, col))(val)
            cell_widget.setAlignment(Qt.AlignLeft)
            self.table_prop.setCellWidget(last_row, col, cell_widget)

        # Connect name QLineEdit to renameProp method
        self.table_prop.cellWidget(last_row, 0).editingFinished.connect(
            partial(self.renameProp, self.table_prop.cellWidget(last_row, 0))
        )

        # Duplicate row in current class dict
        self.current_class_dict["properties"].append(
            dict(self.current_class_dict["properties"][row_index - 1])
        )
        self.current_class_dict["properties"][-1]["name"] = self.table_prop.cellWidget(
            last_row, 0
        ).text()

        # Add buttons in last row
        self.addRowButtonsProp(last_row)

        # Enable save class button
        self.b_saveclass.setEnabled(True)

    def renameProp(self, line_edit):
        """Check that renamed property doesn't already exists

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        line_edit : QLineEdit
            Line edit that emits signal
        """

        # Get row_index of clicked button
        for row in range(1, self.table_prop.rowCount(), 1):
            if self.table_prop.cellWidget(row, 0) == line_edit:
                row_index = row
                break

        # Get property name that has been renamed
        prop_name = self.table_prop.cellWidget(row_index, 0).text()

        # Get old property name from current class dict
        old_name = self.current_class_dict["properties"][row_index - 1]["name"]

        # Check that renamed property has changed and is not empty otherwise exit method
        if prop_name == "" or prop_name == old_name:
            return

        # Get the list of property names
        prop_name_list = [
            self.table_prop.cellWidget(row, 0).text()
            for row in range(1, self.table_prop.rowCount(), 1)
            if row != row_index
        ]

        if prop_name in prop_name_list and prop_name_list.index(prop_name) != row_index:
            print("Cannot rename property with an existing name in property list")
            # Cancel rename and use old property name
            self.table_prop.cellWidget(row_index, 0).setText(
                self.current_class_dict["properties"][row_index - 1]["name"]
            )
            return

        # Edit current class dict
        self.current_class_dict["properties"][row_index - 1]["name"] = prop_name

        # Enable save class button
        self.b_saveclass.setEnabled(True)

        # Enable Duplicate button
        self.table_prop.cellWidget(row_index, len(self.list_prop) + 1).setEnabled(True)

    def fill_table_meth(self):
        """Fill tables of methods with current class dict content

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object

        """

        # Enable browse button
        self.b_browse.setEnabled(True)

        # Fill table of methods
        # Set the number of rows to the number of methods (first row are labels)
        self.table_meth.setRowCount(len(self.current_class_dict["methods"]))
        for row, meth in enumerate(self.current_class_dict["methods"]):
            # Write method name in cell
            line_edit = QLineEdit(str(meth))
            line_edit.setAlignment(Qt.AlignLeft)
            line_edit.editingFinished.connect(partial(self.renameMethod, line_edit))
            self.table_meth.setCellWidget(row, 0, line_edit)
            # Add open, duplicate and delete buttons
            self.addRowButtonsMethod(row)

        # Adjust column width
        self.table_meth.resizeColumnsToContents()

        # Sort table of methods
        self.sortMethod()

    def addRowButtonsMethod(self, row_index):
        """Delete row in table of properties given row index to delete

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        row_index : int
            Index of row to delete

        """

        # Add delete button
        b_del_meth = QPushButton(text="Delete", parent=self.table_meth)
        b_del_meth.clicked.connect(partial(self.deleteMethod, b_del_meth))
        self.table_meth.setCellWidget(row_index, 1, b_del_meth)
        # Add duplicate button
        b_dup_meth = QPushButton(text="Duplicate", parent=self.table_meth)
        b_dup_meth.clicked.connect(partial(self.duplicateMethod, b_dup_meth))
        self.table_meth.setCellWidget(row_index, 2, b_dup_meth)
        # Add open button
        b_open_meth = QPushButton(text="Open", parent=self.table_meth)
        b_open_meth.clicked.connect(partial(self.openMethod, b_open_meth))
        self.table_meth.setCellWidget(row_index, 3, b_open_meth)

    def addMethod(self):
        """Add one empty row at the end of table of methods

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object

        """

        self.table_meth.setRowCount(self.table_meth.rowCount() + 1)

        last_row = self.table_meth.rowCount() - 1

        # Add line edit at first column to enter method name
        line_edit = QLineEdit("")
        line_edit.setAlignment(Qt.AlignLeft)
        self.table_meth.setCellWidget(last_row, 0, line_edit)

        # Connect name QLineEdit to renameMeth method
        self.table_meth.cellWidget(last_row, 0).editingFinished.connect(
            partial(self.renameMethod, self.table_meth.cellWidget(last_row, 0))
        )

        # Add Delete and Duplicate buttons
        self.addRowButtonsMethod(last_row)

        # Set Duplicate and Open buttons to disabled since Name is empty
        self.table_meth.cellWidget(last_row, 2).setEnabled(False)
        self.table_meth.cellWidget(last_row, 3).setEnabled(False)

        # Add empty prop in current class dict
        self.current_class_dict["methods"].append("")

        # Adjust column width
        self.table_meth.resizeColumnsToContents()

        # Enable save class button
        self.b_saveclass.setEnabled(True)

    def sortMethod(self):
        """Alphabetically sort table of methods

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object

        """

        # Get the list of methods names
        meth_name_list = [
            self.table_meth.cellWidget(row, 0).text()
            for row in range(self.table_meth.rowCount())
        ]

        # Sort alphebetically
        meth_name_list.sort(key=str.lower)

        # Fill table with sorted list (no need to change buttons as they are identical)
        for row, meth_name in enumerate(meth_name_list):
            self.table_meth.cellWidget(row, 0).setText(meth_name)

        # Update current class dict with sorted list
        self.current_class_dict["methods"] = meth_name_list

    def deleteMethod(self, button):
        """Delete row in table of methods

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        button : QPushButton
            Button that emits signal

        """

        # Get row_index of clicked delete button
        for row in range(self.table_meth.rowCount()):
            if self.table_meth.cellWidget(row, 1) == button:
                row_index = row
                break

        # Get method name
        meth_name = self.table_meth.cellWidget(row_index, 0).text()

        # Delete row at row_index
        self.table_meth.removeRow(row_index)

        # Delete method in current_class_dict for renaming purpose
        self.current_class_dict["methods"].remove(meth_name)

        # Check if there is a folder in method name
        if "." in meth_name:
            meth_split = meth_name.split(".")
            meth_name = join(*meth_split)

        # Delete method if it exists
        current_method_folder_path = self.get_current_method_folder_path()
        method_path = join(current_method_folder_path, meth_name + ".py")
        if isfile(method_path):
            os.remove(method_path)

            if isfile(method_path):
                print("Cannot delete method file: " + method_path)
            else:
                print("Deleting method file: " + method_path)

        # Enable save class button
        self.b_saveclass.setEnabled(True)

    def duplicateMethod(self, button):
        """Duplicate method in table of methods

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        button : QPushButton
            Button that emits signal

        """
        # Get row_index of clicked duplicate button
        for row in range(self.table_meth.rowCount()):
            if self.table_meth.cellWidget(row, 2) == button:
                row_index = row
                break

        # Add empty row at the end
        self.table_meth.setRowCount(self.table_meth.rowCount() + 1)
        last_row = self.table_meth.rowCount() - 1

        # Get name of method to duplicate
        meth_name = self.table_meth.cellWidget(row_index, 0).text()

        # Check that method name doesn't already exist, otherwise add _copy in the end
        meth_name_dup = meth_name
        for row in range(0, self.table_meth.rowCount() - 1, 1):
            other = self.table_meth.cellWidget(row, 0).text()
            if meth_name_dup == other:
                meth_name_dup += "_copy"

        # Set duplicated method name
        self.table_meth.setCellWidget(
            last_row, 0, type(self.table_meth.cellWidget(row_index, 0))(meth_name_dup)
        )

        # Connect name QLineEdit to renameMeth method
        self.table_meth.cellWidget(last_row, 0).editingFinished.connect(
            partial(self.renameMethod, self.table_meth.cellWidget(last_row, 0))
        )

        # Add method name in current_class_dict for renaming purpose
        self.current_class_dict["methods"].append(meth_name_dup)

        # Check if there is a folder in method name
        if "." in meth_name:
            meth_split = meth_name.split(".")
            meth_name = join(*meth_split)
            meth_split_dup = meth_name_dup.split(".")
            meth_name_dup = join(*meth_split_dup)

        # Copy method file
        current_method_folder_path = self.get_current_method_folder_path()
        method_path = join(current_method_folder_path, meth_name + ".py")
        if isfile(method_path):
            method_path_dup = join(current_method_folder_path, meth_name_dup + ".py")
            copyfile(method_path, method_path_dup)
            if isfile(method_path_dup):
                print("Duplicating method file at: " + method_path_dup)
            else:
                print("Cannot duplicate method file: " + method_path_dup)

        # Add buttons in last row
        self.addRowButtonsMethod(last_row)

        # Sort table of methods
        self.sortMethod()

        # Enable save class button
        self.b_saveclass.setEnabled(True)

    def renameMethod(self, line_edit):
        """Rename method

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        line_edit : QLineEdit
            Line edit that emits signal
        """

        # Get row_index of method name line edit
        for row in range(self.table_meth.rowCount()):
            if self.table_meth.cellWidget(row, 0) == line_edit:
                row_index = row
                break

        # Get new method name from widget
        meth_name = self.table_meth.cellWidget(row_index, 0).text()

        # Get old method name from current class dict
        old_name = self.current_class_dict["methods"][row_index]

        # Check that renamed method has changed and is not empty otherwise exit method
        if meth_name == "" or meth_name == old_name:
            return

        # Check that renamed method doesn't already exists to avoid duplicates
        if (
            meth_name in self.current_class_dict["methods"]
            and self.current_class_dict["methods"].index(meth_name) != row_index
        ):
            print("Cannot rename method with an existing name in method list")
            # Set old method name
            self.table_meth.cellWidget(row_index, 0).setText(
                self.current_class_dict["methods"][row_index]
            )
            return

        # Get old method name path
        current_method_folder_path = self.get_current_method_folder_path()
        old_meth_path = join(
            current_method_folder_path,
            self.current_class_dict["methods"][row_index] + ".py",
        )
        # Get new method name path
        new_meth_path = join(current_method_folder_path, meth_name + ".py")

        # Rename file if old file exists
        if isfile(old_meth_path):
            # Can't rename to new file if it already exists otherwise os.rename will crash
            if isfile(new_meth_path):
                print(
                    "Cannot rename method to: "
                    + meth_name
                    + " since the file already exists"
                )
                return
            print("Renaming method file " + old_name + " to " + meth_name)
            os.rename(old_meth_path, new_meth_path)

        # Store new name in current class dict
        self.current_class_dict["methods"][row_index] = meth_name

        # Enable save class button
        self.b_saveclass.setEnabled(True)

        # Enable Duplicate and Open buttons
        self.table_meth.cellWidget(row_index, 2).setEnabled(True)
        self.table_meth.cellWidget(row_index, 3).setEnabled(True)

        # Sort table of methods
        self.sortMethod()

    def browseMethod(self):
        """Open explorer at folder path containing methods

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        """
        # Get full path to method folder
        method_folder_path = realpath(self.get_current_method_folder_path())

        # Create folder if not existing
        if method_folder_path is not None and not isdir(method_folder_path):
            print(
                "Method folder doesn't exist. Creating method folder at: "
                + method_folder_path
            )
            os.mkdir(method_folder_path)

        # Open folder in explorer
        os.startfile(method_folder_path)

    def openMethod(self, button):
        """Open method in editor given by path_editor_py

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        button : QPushButton
            Button that emits signal

        """

        # Get row_index of clicked open button
        for row in range(self.table_meth.rowCount()):
            if self.table_meth.cellWidget(row, 3) == button:
                row_index = row
                break

        # Get method name at given row index
        meth = self.table_meth.cellWidget(row_index, 0).text()

        # Check if there is a folder in the method name
        if "." in meth:
            meth_split = meth.split(".")
            meth = join(*meth_split)

        # Get method path
        current_method_folder_path = self.get_current_method_folder_path()
        method_path = join(current_method_folder_path, meth + ".py")

        if not isdir(current_method_folder_path):
            print(
                "Method folder doesn't exist. Creating method folder at: "
                + current_method_folder_path
            )
            os.mkdir(current_method_folder_path)

        if not isfile(method_path):
            print("Method file doesn't exist. Creating method file at: " + method_path)
            # open a new python file and fill it with method template
            class_name = self.le_classname.text()
            load_file = open(method_path, "w+")
            load_file.write("def " + meth + "(self):\n")
            load_file.write('    """Method description \n')
            load_file.write("\n")
            load_file.write("    Parameters\n")
            load_file.write("    ----------\n")
            load_file.write("    self: " + class_name + "\n")
            load_file.write("        a " + class_name + " object\n")
            load_file.write("\n")
            load_file.write("    Returns\n")
            load_file.write("    ----------\n")
            load_file.write("    var: type\n")
            load_file.write("        var description\n")
            load_file.write('    """\n')
            load_file.write("\n")
            load_file.write(
                '    raise Exception("Method ' + meth + ' not implemented yet")\n'
            )
            load_file.write("\n")
            load_file.write("    return var")
            load_file.close()

        # Open method with editor
        p = subprocess.Popen([self.path_editor_py, method_path])

    def fill_table_meta(self):
        """Fill tables of metadata with current class dict content

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object

        """

        # Set the number of rows to the number of metadata (first row are labels)
        Nrow = max([2, 1 + len(self.current_class_dict["daughters"])])
        self.table_meta.setRowCount(Nrow)
        for col, meta_name in enumerate(self.list_meta[:-1]):
            meta_prop = self.current_class_dict[MATCH_META_DICT[meta_name]]
            # Create QLineEdit
            line_edit = QLineEdit(str(meta_prop))
            line_edit.setAlignment(Qt.AlignLeft)
            if col == 0:
                # Disable package edition since it is necessarily the folder containing the csv file
                line_edit.setEnabled(False)
            elif col == 1:
                # Add method to track parent change and update children in other classes
                line_edit.editingFinished.connect(partial(self.editParent, line_edit))
            else:
                # Add method to check if value of line edit has changed and save is requested
                line_edit.mousePressEvent = MethodType(
                    partial(self.line_edit_clicked, line_edit=line_edit), line_edit
                )
                line_edit.editingFinished.connect(
                    partial(self.saveRequested, line_edit)
                )
            self.table_meta.setCellWidget(1, col, line_edit)

        if len(self.current_class_dict["daughters"]) > 0:
            # Get list of children
            meta_prop = self.current_class_dict[MATCH_META_DICT[self.list_meta[-1]]]
            for row, child_class in enumerate(meta_prop):
                # Create QLineEdit for each children
                line_edit = QLineEdit(str(child_class))
                line_edit.setAlignment(Qt.AlignLeft)
                # Disable daughters edition since it is automatically updated by class generator
                line_edit.setEnabled(False)
                self.table_meta.setCellWidget(row + 1, 3, line_edit)
        else:
            # Create empty QLineEdit
            line_edit = QLineEdit("")
            line_edit.setAlignment(Qt.AlignLeft)
            line_edit.setEnabled(False)
            self.table_meta.setCellWidget(1, 3, line_edit)

        # Adjust column width
        self.table_meta.resizeColumnsToContents()

    def editParent(self, line_edit):
        """Update daughters in other classes if a parent is defined

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object

        """

        class_name = self.current_class_dict["name"]

        # Get new and old parent names
        parent_new = line_edit.text()
        parent_old = self.current_class_dict["mother"]

        if parent_new == parent_old:
            # No change
            return

        if parent_new != "" and parent_new not in self.parent_dict:
            # Revert changes to parent
            print(
                "Cannot set "
                + parent_new
                + " as parent to "
                + class_name
                + ", class not found"
            )
            line_edit.blockSignals(True)
            line_edit.setText("")
            line_edit.blockSignals(False)
            return

        if parent_old != "" and parent_old not in self.parent_dict:
            # Revert changes to parent
            print(
                "Removing "
                + parent_old
                + " as parent of "
                + class_name
                + ", class not found"
            )
            line_edit.blockSignals(True)
            line_edit.setText("")
            line_edit.blockSignals(False)
            return

        # Update parent dict
        if parent_old != "" and parent_new != parent_old:
            # Remove current class name from parent_dict list
            if class_name in self.parent_dict[parent_old]:
                print(
                    "Removing child class "
                    + class_name
                    + " from parent class "
                    + parent_old
                )
                self.parent_dict[parent_old].remove(class_name)
                self.current_class_dict["mother"] = parent_new
                # Activate save button
                self.b_saveclass.setEnabled(True)

        if parent_new != "" and parent_new != parent_old:
            # Add current class name in parent_dict list
            print("Adding child class " + class_name + " to parent class " + parent_new)
            self.parent_dict[parent_new].append(self.current_class_dict["name"])
            self.parent_dict[parent_new].sort(key=str.lower)
            self.current_class_dict["mother"] = parent_new
            # Activate save button
            self.b_saveclass.setEnabled(True)

    def fill_table_const(self):
        """Fill tables of constants with current class dict content

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object

        """
        # Set the number of rows to the number of metadata (first row are labels)
        self.table_const.setRowCount(2)
        for col, const_name in enumerate(self.list_const):
            meta_const = self.current_class_dict[MATCH_CONST_DICT[const_name][0]]
            # Add rows if there is more than one constant
            if self.table_const.rowCount() < len(meta_const) + 1:
                self.table_const.setRowCount(len(meta_const) + 1)

            # Browse list of constants
            for row, const_dict in enumerate(meta_const):
                val = const_dict[MATCH_CONST_DICT[const_name][1]]
                # Create line edit for each parameter
                line_edit = QLineEdit(str(val))
                line_edit.setAlignment(Qt.AlignLeft)
                if col == 0:
                    # Add method to check that property can't be renamed to an existing one
                    line_edit.editingFinished.connect(
                        partial(self.renameConst, line_edit)
                    )
                    # Add property buttons
                    self.addRowButtonsConst(row + 1)
                else:
                    # Add method to check if value of line edit has changed and save is requested
                    line_edit.mousePressEvent = MethodType(
                        partial(self.line_edit_clicked, line_edit=line_edit), line_edit
                    )
                    line_edit.editingFinished.connect(
                        partial(self.saveRequested, line_edit)
                    )
                self.table_const.setCellWidget(row + 1, col, line_edit)

        # Adjust column width
        self.table_const.resizeColumnsToContents()

    def addRowButtonsConst(self, row_index):
        """Delete row in table of constants given row index to delete

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        row_index : int
            Index of row to delete

        """

        # Add delete button
        b_del_const = QPushButton(text="Delete", parent=self.table_const)
        b_del_const.clicked.connect(partial(self.deleteConst, b_del_const))
        self.table_const.setCellWidget(row_index, len(self.list_const), b_del_const)
        # Add duplicate button
        b_dup_const = QPushButton(text="Duplicate", parent=self.table_const)
        b_dup_const.clicked.connect(partial(self.duplicateConst, b_dup_const))
        self.table_const.setCellWidget(row_index, len(self.list_const) + 1, b_dup_const)

    def addConst(self):
        """Add one empty row at the end of table of properties

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object

        """

        self.table_const.setRowCount(self.table_const.rowCount() + 1)

        last_row = self.table_const.rowCount() - 1

        for col in range(len(self.list_const)):
            line_edit = QLineEdit("")
            line_edit.setAlignment(Qt.AlignLeft)
            self.table_const.setCellWidget(last_row, col, line_edit)

        # Connect name QLineEdit to renameconst method
        self.table_const.cellWidget(last_row, 0).editingFinished.connect(
            partial(self.renameConst, self.table_const.cellWidget(last_row, 0))
        )

        # Add Delete and Duplicate buttons
        self.addRowButtonsConst(last_row)

        # Set Duplicate button to disabled since Name is empty
        self.table_const.cellWidget(last_row, len(self.list_const) + 1).setEnabled(
            False
        )

        # Add constant in current class dict
        self.current_class_dict["constants"].append({"name": "", "value": ""})

        # Adjust column width
        self.table_const.resizeColumnsToContents()

        # Enable save class button
        self.b_saveclass.setEnabled(True)

    def deleteConst(self, button):
        """Delete row in table of constants

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        button : QPushButton
            Button that emits signal

        """

        # Get row_index of clicked delete button
        for row in range(1, self.table_const.rowCount(), 1):
            if self.table_const.cellWidget(row, len(self.list_const)) == button:
                row_index = row
                break

        # Remove row at given index
        self.table_const.removeRow(row_index)

        # Delete row in current class dict
        del self.current_class_dict["constants"][row_index - 1]

        # Enable save class button
        self.b_saveclass.setEnabled(True)

    def duplicateConst(self, button):
        """Duplicate row in table of constants

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        button : QPushButton
            Button that emits signal

        """

        # Get row_index of clicked duplicate button
        for row in range(1, self.table_const.rowCount(), 1):
            if self.table_const.cellWidget(row, len(self.list_const) + 1) == button:
                row_index = row
                break

        # Add empty row at the end
        self.table_const.setRowCount(self.table_const.rowCount() + 1)
        last_row = self.table_const.rowCount() - 1

        # Browse columns of the row to duplicate and add same items in last row
        for col in range(len(self.list_const)):
            val = self.table_const.cellWidget(row_index, col).text()
            if col == 0:
                # Check that property name doesn't already exist
                for row in range(1, self.table_const.rowCount() - 1, 1):
                    other = self.table_const.cellWidget(row, col).text()
                    if val == other:
                        val += "_copy"
            self.table_const.setCellWidget(
                last_row, col, type(self.table_const.cellWidget(row_index, col))(val)
            )

        # Connect name QLineEdit to renameConst method
        self.table_const.cellWidget(last_row, 0).editingFinished.connect(
            partial(self.renameConst, self.table_const.cellWidget(last_row, 0))
        )

        # Duplicate row in current class dict
        self.current_class_dict["constants"].append(
            dict(self.current_class_dict["constants"][row_index - 1])
        )
        self.current_class_dict["constants"][-1]["name"] = self.table_const.cellWidget(
            last_row, 0
        ).text()

        # Add buttons in last row
        self.addRowButtonsConst(last_row)

        # Enable save class button
        self.b_saveclass.setEnabled(True)

    def renameConst(self, line_edit):
        """Check that renamed constant doesn't already exists

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        line_edit : QLineEdit
            Line edit that emits signal
        """

        # Get row_index of clicked button
        for row in range(1, self.table_const.rowCount(), 1):
            if self.table_const.cellWidget(row, 0) == line_edit:
                row_index = row
                break

        # Get constant name that has been renamed
        const_name = self.table_const.cellWidget(row_index, 0).text()

        # Get old constant name from current class dict
        old_name = self.current_class_dict["constants"][row_index - 1]["name"]

        # Check that renamed constant has changed and is not empty otherwise exit method
        if const_name == "" or const_name == old_name:
            return

        # Get the list of constant names
        const_name_list = [
            self.table_const.cellWidget(row, 0).text()
            for row in range(1, self.table_const.rowCount(), 1)
            if row != row_index
        ]

        if (
            const_name in const_name_list
            and const_name_list.index(const_name) != row_index
        ):
            # Cancel rename and use old constant name
            print("Cannot rename constant with an existing name in constant list")
            self.table_const.cellWidget(row_index, 0).setText(
                self.current_class_dict["constants"][row_index - 1]["name"]
            )
            return

        # Edit current class dict
        self.current_class_dict["constants"][row_index - 1]["name"] = const_name

        # Enable Duplicate button
        self.table_const.cellWidget(row_index, len(self.list_const) + 1).setEnabled(
            True
        )

        # Enable save class button
        self.b_saveclass.setEnabled(True)

    def renameClass(self):
        """Rename class with line edit -> triggers fileRenamed signal so
        this methods is run twice.

        Parameters
        ----------
        self : DClassGenerator
            A DClassGenerator object
        """

        # Get old and new class names
        oldName = self.get_obj_name(self.current_class_index)
        newName = self.le_classname.text() + ".csv"

        # Get path to old csv file before renaming
        path_old = self.dirModel.filePath(self.current_class_index)

        # Get path to module folder
        path = path_old.replace(oldName, "")

        # Get path to new csv file after renaming
        path_new = realpath(join(path, newName))

        # Check that path_old is not the same as path_new to avoid second run
        if isfile(path_old) and realpath(path_old) != realpath(path_new):
            # Perform renaming
            os.rename(path_old, path_new)
            index = self.dirModel.index(path_new)
            self.treeView.setCurrentIndex(index)
            self.current_class_index = index
            self.sortTreeView()

            # Call same method as for renaming with double click on csv name in treeview
            self.renameClassMethods(path, oldName, newName)

    def saveClass(self):
        """Save class as csv file

        Parameters
        ----------
        self : DClassGenerator
            A DClassGenerator object
        """

        # Get current class dict from tables
        class_dict = self.get_current_class_dict_from_tables()

        # Write class into csv format
        write_file(class_dict)

        # Reload csv to ignore empty fields and update current_class_dict
        csv_path = realpath(self.dirModel.filePath(self.current_class_index))
        self.import_class_from_csv(csv_path)

        # Update tables in GUI
        self.set_class_selected()

        # Store class csv file path in list of modified classes
        if csv_path not in self.list_class_modified:
            self.list_class_modified.append(csv_path)
            self.b_genclass.setEnabled(True)

        # Disable save class button
        self.b_saveclass.setEnabled(False)

    def get_current_class_dict_from_tables(self):
        """Get current class dict by reading property, method and metadata tables

        Parameters
        ----------
        self : DClassGenerator
            A DClassGenerator object

        Returns
        -------
        class_dict : dict
            Dict containing all the class informations (properties, package, methods...)

        """

        # Init class dict
        class_dict = dict()
        class_dict["name"] = self.dirModel.fileName(self.current_class_index)[:-4]
        class_dict["path"] = realpath(self.dirModel.filePath(self.current_class_index))
        class_dict["daughters"] = list()

        # Read property table
        prop_list = list()
        for row in range(1, self.table_prop.rowCount(), 1):
            prop_dict = dict()
            for col in range(len(self.list_prop)):
                val = self.table_prop.cellWidget(row, col).text()
                prop_dict[MATCH_PROP_DICT[self.list_prop[col]]] = val
            if prop_dict["name"] != "" and prop_dict["type"] != "":
                prop_list.append(prop_dict)
            else:
                # Ignore property with empty name or type since they will fail in class generator
                print("Ignoring property with empty name or type at row=" + str(row))
        class_dict["properties"] = prop_list

        # Read method table
        class_dict["methods"] = list()
        for row in range(self.table_meth.rowCount()):
            val = self.table_meth.cellWidget(row, 0).text()
            if val != "":
                class_dict["methods"].append(val)
            else:
                # Ignore method with empty name since it will fail in class generator
                print("Ignoring method with empty name at row=" + str(row))

        # Read meta data table except children column (automatically updated by class generator)
        for col in range(len(self.list_meta) - 1):
            val = self.table_meta.cellWidget(1, col).text()
            class_dict[MATCH_META_DICT[self.list_meta[col]]] = val

        # Read constants table
        cst_list = list()
        for col in range(len(self.list_const)):
            # Recreate list of constants dict
            for row in range(1, self.table_const.rowCount(), 1):
                val = self.table_const.cellWidget(row, col).text()
                if len(cst_list) < row:
                    cst_list.append(dict())
                cst_list[row - 1][MATCH_CONST_DICT[self.list_const[col]][1]] = val
            class_dict["constants"] = cst_list
        for row, const_dict in enumerate(class_dict["constants"]):
            if const_dict["name"] == "":
                class_dict["constants"].remove(const_dict)
                # Ignore constant with empty name since it will fail in class generator
                print("Ignoring constant with empty name at row=" + str(row))

        return class_dict

    def genClass(self):
        """Generate class from csv files

        Parameters
        ----------
        self : DClassGenerator
            A DClassGenerator object
        """

        # Check if current class is modified and should be saved
        self.check_class_modified()

        list_class_modified = list()
        for c in self.list_class_modified:
            if c is not None and c not in list_class_modified:
                list_class_modified.append(c)

        # Check if each modified class has children and regenerate them
        modified_list = [basename(csv_path)[:-4] for csv_path in list_class_modified]
        children_list = list()

        # 6 nested for loops to include childs up to 6 generations
        for modified_class in modified_list:
            if modified_class in self.parent_dict:
                children_list.extend(self.parent_dict[modified_class])
                for modified_class1 in self.parent_dict[modified_class]:
                    if modified_class1 in self.parent_dict:
                        children_list.extend(self.parent_dict[modified_class1])
                        for modified_class2 in self.parent_dict[modified_class1]:
                            if modified_class2 in self.parent_dict:
                                children_list.extend(self.parent_dict[modified_class2])
                                for modified_class3 in self.parent_dict[
                                    modified_class2
                                ]:
                                    if modified_class3 in self.parent_dict:
                                        children_list.extend(
                                            self.parent_dict[modified_class3]
                                        )
                                        for modified_class4 in self.parent_dict[
                                            modified_class4
                                        ]:
                                            if modified_class4 in self.parent_dict:
                                                children_list.extend(
                                                    self.parent_dict[modified_class4]
                                                )
                                                for modified_class5 in self.parent_dict[
                                                    modified_class4
                                                ]:
                                                    if (
                                                        modified_class5
                                                        in self.parent_dict
                                                    ):
                                                        children_list.extend(
                                                            self.parent_dict[
                                                                modified_class5
                                                            ]
                                                        )
        # Only keep unique children
        children_list_unique = list()
        for c in children_list:
            if c is not None and c not in children_list_unique:
                children_list_unique.append(c)

        if len(children_list_unique) > 0:
            for child in children_list_unique:
                # Store child csv path if the file exists
                child_path = self.get_child_path(child)
                if (
                    child_path is not None
                    and child_path not in list_class_modified
                    and isfile(child_path)
                ):
                    print(
                        "Adding child class "
                        + child
                        + " to the list of classes to regenerate"
                    )
                    list_class_modified.append(child_path)

        # Generate classes in list of modified classes
        run_generate_classes(
            is_black=self.is_black.isChecked(), class_list=list_class_modified
        )

        # Empty the list of modified classes
        self.list_class_modified = list()

        # Disable generate classes button
        self.b_genclass.setEnabled(False)

    def openContextMenu(self, position):
        """Generate and open context the menu at the given position

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        position : QPoint
            Position of treeview clicked element

        """

        index = self.treeView.indexAt(position)

        if not index.isValid():
            return

        class_name = self.get_obj_name(index)

        menu = QMenu()

        if self.dirModel.isDir(index):
            # Generate context menu for right click on folder
            # delete_module = menu.addAction(self.tr("Delete module"))
            # delete_module.triggered.connect(partial(self.deleteModule, index))
            # new_module = menu.addAction(self.tr("New module"))
            # new_module.triggered.connect(partial(self.createModule, index))
            new_class = menu.addAction(self.tr("New class"))
            new_class.triggered.connect(partial(self.createClass, index))
            open_module = menu.addAction(self.tr("Browse folder"))
            open_module.triggered.connect(partial(self.browseModule, index))

        elif class_name[-4:] == ".csv":
            # Generate context menu for right click on csv file
            delete_class = menu.addAction(self.tr("Delete class"))
            delete_class.triggered.connect(partial(self.deleteClass, index))
            dupli_class = menu.addAction(self.tr("Duplicate class"))
            dupli_class.triggered.connect(partial(self.duplicateClass, index))
            open_class = menu.addAction(self.tr("Open class"))
            open_class.triggered.connect(partial(self.openClass, index))

        else:
            return

        menu.exec_(self.treeView.viewport().mapToGlobal(position))

    def renameClassMethods(self, path, oldName, newName):
        """Rename methods after class renaming and prevent from folder renaming
        to avoid conflict with package

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        path : str
            folder path of renamed csv file
        oldName : str
            old csv file name
        newName : str
            new csv file name

        """

        # Get old and new csv file paths
        path_old = realpath(join(path, oldName))
        path_new = realpath(join(path, newName))

        # Get treeview index of renamed object
        index = self.dirModel.index(path_new)

        if self.dirModel.data(index) in ["", None]:
            return

        if self.dirModel.isDir(index):
            print("Cannot rename module")
            # Rename folder back to original name to prevent issues with package attribute
            os.rename(path_new, path_old)

        elif newName[-4:] == ".csv":
            # Check if class has daughters before renaming it
            if len(self.current_class_dict["daughters"]) > 0:
                # Send toggle window to ask if the class should still be renamed
                reply = QMessageBox().question(
                    self,
                    "Warning: renaming class with children",
                    "Class "
                    + newName[:-4]
                    + ' has children, press "yes" to resume renaming process',
                    QMessageBox.Yes,
                    QMessageBox.No,
                )

                if reply == QMessageBox.No:
                    # Rename class back
                    self.le_classname.setText(oldName[:-4])
                    # Check that path_old is different from path_new to avoid second run
                    if isfile(path_new) and realpath(path_old) != realpath(path_new):
                        # Perform renaming
                        print("Renaming back " + newName[:-4] + " to " + oldName[:-4])
                        os.rename(path_new, path_old)
                        index = self.dirModel.index(path_old)
                        self.treeView.setCurrentIndex(index)
                        self.current_class_index = index
                        self.sortTreeView()
                    return

            print("Renaming class " + oldName + " to " + newName)

            if self.current_class_dict is not None:
                # Update class name in current class dict
                self.current_class_dict["name"] = newName[:-4]

            # Update class name label
            self.le_classname.setText(newName[:-4])

            if oldName[:-4] in self.parent_dict:
                # Update class name in parent_dict
                children_list = self.parent_dict.pop(oldName[:-4])
                self.parent_dict[newName[:-4]] = children_list

            if path_old in self.list_class_modified:
                # Update class name in list of modified class
                ii = self.list_class_modified.index(path_old)
                self.list_class_modified[ii] = path_new
            else:
                # Add class name in list of modified class
                self.list_class_modified.append(path_new)
            self.b_genclass.setEnabled(True)

            # Get new path to method folder after class renaming
            method_folder_path_new = self.get_current_method_folder_path(index)

            # Get old path to method folder before class renaming
            method_folder_path_old = method_folder_path_new.replace(
                newName[:-4], oldName[:-4]
            )

            if isdir(method_folder_path_old):
                # Rename methods folder if it exists
                print(
                    "Renaming method folder of "
                    + oldName[:-4]
                    + " to: "
                    + method_folder_path_new
                )
                os.rename(method_folder_path_old, method_folder_path_new)

            # Rename current class in children csv files
            for child_class in self.current_class_dict["daughters"]:
                print(
                    "Rename parent class "
                    + newName[:-4]
                    + " in child class "
                    + child_class
                )
                child_path = self.get_child_path(child_class)
                # Load csv file
                try:
                    child_class_dict = read_file(child_path)
                except Exception as e:
                    print("Cannot load csv file: " + child_path)
                    return
                child_class_dict["mother"] = newName[:-4]
                write_file(child_class_dict)
                self.list_class_modified.append(child_path)
                self.b_genclass.setEnabled(True)

            # Sort treeview alphabetically
            self.sortTreeView()

    def deleteClass(self, index):
        """Delete csv file associated to class

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        index : QModelIndex
            Model index of current selected item in treeview

        """

        # Get class csv path
        csv_path = realpath(self.dirModel.filePath(index))

        # Get class name
        class_name = self.get_obj_name(index)

        # Check if class has daughters before deleting it
        if len(self.current_class_dict["daughters"]) > 0:
            # Send toggle window to ask if the class should still be deleted
            reply = QMessageBox().question(
                self,
                "Warning: deleting class with children",
                "Class "
                + class_name[:-4]
                + ' has children, press "yes" to resume deleting process',
                QMessageBox.Yes,
                QMessageBox.No,
            )

            if reply == QMessageBox.No:
                # Don't delete class
                return

        # Delete current class from children
        for child_class in self.current_class_dict["daughters"]:
            print(
                "Remove deleted parent class "
                + class_name[:-4]
                + " from child class "
                + child_class
            )
            child_path = self.get_child_path(child_class)
            # Load csv file
            try:
                child_class_dict = read_file(child_path)
            except Exception as e:
                print("Cannot load csv file: " + child_path)
                return
            child_class_dict["mother"] = ""
            write_file(child_class_dict)
            self.list_class_modified.append(child_path)
            self.b_genclass.setEnabled(True)

        # Delete csv file associated to class
        self.dirModel.remove(index)

        if isfile(csv_path):
            print("Cannot delete class csv file: " + csv_path)
            print("Please check that file is not opened in csv editor")
            return
        else:
            print("Deleting class csv file: " + csv_path)
            if csv_path in self.list_class_modified:
                # Remove deleted class from modified classes list
                self.list_class_modified.remove(csv_path)
                # Enable class generation to regenerate load and import class files
                self.b_genclass.setEnabled(True)

        # Delete python class file
        py_path = realpath(join(MAIN_DIR, "Classes", class_name[:-4] + ".py"))
        if isfile(py_path):
            os.remove(py_path)
            if isfile(py_path):
                print("Cannot delete class python file: " + py_path)
                print("Please check that file is not opened in python editor")
                return
            else:
                print("Deleting class python file: " + py_path)

        # Delete methods folder
        current_method_folder_path = self.get_current_method_folder_path(index)
        if current_method_folder_path is not None and isdir(current_method_folder_path):
            rmtree(current_method_folder_path, ignore_errors=True)

            if isdir(current_method_folder_path):
                print(
                    "Cannot delete class method folder: " + current_method_folder_path
                )
            else:
                print("Deleting class method folder: " + current_method_folder_path)

        if (
            self.current_class_dict is not None
            and self.current_class_dict["name"] == class_name[:-4]
        ):
            # Reinit tables if deleted class is the selected class
            self.init_tables_buttons()
            self.current_class_dict = None
            self.current_class_index = None
            self.b_genclass.setEnabled(True)

        # Update parent dict
        if class_name in self.parent_dict:
            self.parent_dict.pop(class_name)

    def duplicateClass(self, index):
        """Duplicate class by copying csv file

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        index : QModelIndex
            Model index of current selected item in treeview

        """

        # Copy csv file to the same folder
        csv_path = realpath(self.dirModel.filePath(index))
        file_name = self.dirModel.fileName(index)
        if isfile(csv_path):
            csv_path_dup = realpath(
                csv_path.replace(file_name, file_name[:-4] + "_copy.csv")
            )
            copyfile(csv_path, csv_path_dup)
            if isfile(csv_path_dup):
                print("Duplicating csv file " + file_name[:-4] + " at: " + csv_path_dup)
                self.list_class_modified.append(csv_path_dup)
                self.b_genclass.setEnabled(True)
            else:
                print(
                    "Cannot duplicate csv file "
                    + file_name[:-4]
                    + " at: "
                    + csv_path_dup
                )

        # Copy methods folder if it exists
        meth_folder = self.get_current_method_folder_path(index)
        if meth_folder is not None and isdir(meth_folder):
            meth_folder_dup = meth_folder + "_copy"
            if isdir(meth_folder_dup):
                rmtree(meth_folder_dup, ignore_errors=True)
            copytree(meth_folder, meth_folder_dup)
            if isdir(meth_folder_dup):
                print(
                    "Duplicating method files "
                    + file_name[:-4]
                    + " at: "
                    + meth_folder_dup
                )
            else:
                print(
                    "Cannot duplicate method files "
                    + file_name[:-4]
                    + " at: "
                    + meth_folder_dup
                )

        # Update parent dict
        if file_name[:-4] in self.parent_dict:
            self.parent_dict[file_name[:-4] + "_copy"] = list(
                self.parent_dict[file_name[:-4]]
            )

    def createClass(self, index):
        """Create class by saving empty csv file

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        index : QModelIndex
            Model index of current selected item in treeview

        """

        # Init new class name
        class_name = "new_class"

        # Get file path
        folder_path = self.dirModel.filePath(index)
        csv_path = realpath(join(folder_path, class_name + ".csv"))

        # Loop on class name if file already exists
        while isfile(csv_path):
            class_name += "_copy"
            csv_path = realpath(join(folder_path, class_name + ".csv"))

        # Init class dict
        class_dict = dict()
        class_dict["name"] = class_name
        class_dict["path"] = csv_path
        class_dict["properties"] = list()
        class_dict["methods"] = list()
        class_dict["package"] = self.dirModel.data(index)
        class_dict["mother"] = ""
        class_dict["desc"] = ""
        class_dict["daughters"] = list()
        class_dict["constants"] = [{"name": "VERSION", "value": 1}]

        # Write empty class into csv format
        write_file(class_dict)

        # Store current class information for further use
        self.current_class_dict = class_dict

        # Store new class index in treeview
        self.current_class_index = self.dirModel.index(csv_path)

        # Set treeview to new class index
        self.treeView.setCurrentIndex(self.current_class_index)

        # Sort treeview alphabetically
        self.sortTreeView()

        # Update tables
        self.set_class_selected()
        print("Selecting class: " + csv_path)

        # Store class csv file path in list of modified classes
        if csv_path not in self.list_class_modified:
            self.list_class_modified.append(csv_path)
            self.b_genclass.setEnabled(True)

        # Update parent dict
        self.parent_dict[class_name] = list()

    def openClass(self, index):
        """Open class csv file in editor given by path_editor_csv

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        index : QModelIndex
            Model index of current selected item in treeview

        """

        # Get full path to class csv file
        csv_path = self.dirModel.filePath(index)

        # Open class csv file with editor
        p = subprocess.Popen([self.path_editor_csv, csv_path])

    def browseModule(self, index):
        """Open explorer at module folder path containing classes

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        index : QModelIndex
            Model index of current selected item in treeview
        """

        # Get full path to module folder
        folder_path = self.dirModel.filePath(index)

        # Open folder in explorer
        os.startfile(folder_path)

    def deleteModule(self, index):
        """Delete folder associated to current module

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        index : QModelIndex
            Model index of current selected item in treeview

        """

        folder_path = self.dirModel.filePath(index)

        if folder_path is not None and isdir(folder_path):
            rmtree(folder_path, ignore_errors=True)

            if isdir(folder_path):
                print("Cannot delete folder: " + folder_path)
            else:
                print("Deleting folder: " + folder_path)

    def createModule(self, index):
        """Create new module by creating new folder

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        index : QModelIndex
            Model index of current selected item in treeview

        """

        self.dirModel.mkdir(index.parent(), "new_module")

    def get_current_method_folder_path(self, index=None):
        """get current method folder path for given index"""

        if index is None:
            if self.current_class_index is not None:
                index = self.current_class_index
            else:
                print("Cannot get current method folder path if index is None")
                return
        elif self.dirModel.filePath(index) == "":
            print("Cannot get current method folder path if index points to no file")
            return

        # Get parent index
        parent = index.parent()

        # Check if parent name is ClassesRef folder
        if self.dirModel.data(parent) == "ClassesRef" and self.dirModel.isDir(index):
            # Get folder name at index
            folder_name = self.dirModel.data(index)

        else:
            # Get higher folder path name by recursion on parent folders
            parent_name = self.dirModel.data(parent)
            folder_name = parent_name
            count = 0
            while parent_name != "ClassesRef":
                parent = parent.parent()
                parent_name = self.dirModel.data(parent)
                if parent_name != "ClassesRef":
                    folder_name = parent_name
                count += 1
                if count > 1000:
                    # Prevent from overflow
                    print("Cannot find current method path by recursion")
                    return

        # Get full method folder path
        class_name = self.dirModel.fileName(index)[:-4]
        method_folder_path = realpath(
            join(MAIN_DIR, "Methods", folder_name, class_name)
        )

        return method_folder_path

    def get_obj_name(self, index):
        """get object name from treeview at first column for given index"""
        if index.column() == 0:
            # User clicked directly on name, extract name
            obj_name = self.dirModel.data(index)
        else:
            # User clicked on other properties than name, extract name by using parent
            obj_name = self.dirModel.data(index.parent().child(index.row(), 0))

        return obj_name

    def line_edit_clicked(self, *arg, **kwargs):
        """Save current value in line edit when it is clicked on"""
        self.temp_val = kwargs["line_edit"].text()
        self.temp_le = kwargs["line_edit"]

    def saveRequested(self, line_edit):
        """Activate save class button if save is requested"""
        if line_edit == self.temp_le and line_edit.text() != self.temp_val:
            self.b_saveclass.setEnabled(True)
        self.temp_val = None
        self.temp_le = None

    def onItemCollapse(self, index):
        """Slot for item collapsed"""
        # dynamic resize
        for ii in range(3):
            self.treeView.resizeColumnToContents(ii)

    def onItemExpand(self, index):
        """Slot for item expand"""
        # dynamic resize
        for ii in range(3):
            self.treeView.resizeColumnToContents(ii)

    def sortTreeView(self):
        """Sort treeview alphabetically"""
        # Sort 2nd column first to trigger 1st column sort
        self.dirModel.sort(1)
        self.dirModel.sort(0)

    def get_child_path(self, child_class):
        """Get path to given child class name

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        child_class : str
            child class name

        Returns
        ----------
        child_path : str
            path to child class

        """

        for root, _, files in os.walk(self.class_gen_path):
            for name in files:
                if name == child_class + ".csv":
                    child_path = realpath(join(root, name))
                    return child_path

        return None


def is_app(app_path):
    """Check if application pointed by app_path exists"""

    # Check if file exists
    if isfile(app_path):
        return True
    
    # Check in all folders of environment path if file exists
    else:
        for dir in os.environ["PATH"].split(os.pathsep):
            if os.path.exists(os.path.join(dir, app_path)):
                return True

    return False

