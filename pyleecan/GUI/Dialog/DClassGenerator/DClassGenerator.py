import os
import subprocess

from os.path import join, isfile, isdir, realpath
from shutil import copyfile, rmtree, copytree
from functools import partial

from PySide2.QtCore import Qt, Signal, QDir
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

from ....definitions import DOC_DIR, PACKAGE_NAME, MAIN_DIR

from ....Generator.read_fct import read_file
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
        class_gen_path : str
            Default path for csv class files
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        self.setupUi(self)

        # Setup windows icon
        self.setWindowIcon(QIcon(pixmap_dict["soft_icon"]))

        # Init current variables
        self.current_class_dict = None
        self.current_module = None
        self.current_method_folder_path = None
        self.current_class_index = None
        self.list_class_modified = list()
        self.path_editor_py = path_editor_py
        self.path_editor_csv = path_editor_csv
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
        # Init label
        self.set_label_classname("ClassName")

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
        self.table_prop.setRowCount(2)
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
            is_modified_class = self.check_class_modified()

            if is_modified_class:
                if index == self.current_class_index:
                    text = (
                        "Save current class modifications before reloading same class ?"
                    )
                else:
                    text = (
                        "Save current class modifications before loading another class?"
                    )
                # Send toggel window to ask if save is required
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
                    if index == self.current_class_index:
                        # No need to reload interface with saved class since saveClass already did it
                        return

        # Store current class index to save class after modifications
        self.current_class_index = index

        # Get parent folder in which the csv file is
        parent = index.parent()

        # Get full module name by recursion on parent folders
        module = self.dirModel.data(parent)
        parent_name = module
        while parent_name != "ClassesRef":
            parent = parent.parent()
            parent_name = self.dirModel.data(parent)
            if parent_name != "ClassesRef":
                module = join(parent_name, module)

        self.current_module = module

        # Import csv at csv_path and store class in self.current_class_dict
        csv_path = join(DOC_DIR, module, class_name)
        self.import_class_from_csv(csv_path)

        if self.current_class_dict is not None:
            # Update GUI with data contained in self.current_class_dict
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
        self.set_label_classname(self.current_class_dict["name"])

        # Enable save class button
        self.b_saveclass.setEnabled(True)

        # Disable add property button
        self.b_addprop.setEnabled(True)

        # Disable add method button
        self.b_addmeth.setEnabled(True)

        # Disable browse button
        self.b_browse.setEnabled(True)

        # Disable add constant button
        self.b_addconst.setEnabled(True)

        # Enable generate class button
        self.b_genclass.setEnabled(True)

    def check_class_modified(self):
        """Check if class is modified

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object

        Returns
        -------
        is_modified_class : bool
            True if class has been modified in comparison with class csv file content
        """

        # Get current class dict from tables
        current_class_dict = self.get_current_class_dict_from_tables()

        # Check if current_class_dict is different from class_dict in .csv file
        csv_path = join(
            DOC_DIR, self.current_module, self.get_obj_name(self.current_class_index)
        )

        # Load csv file (meaning current class without modifications)
        try:
            class_dict_ref = read_file(
                csv_path, soft_name=PACKAGE_NAME, is_get_size=True
            )
        except Exception as e:
            print("Cannot load csv file: " + csv_path)
            return True

        # Compare class dict
        is_modified_class = False
        for key, val0 in class_dict_ref.items():
            if key in ["daughters"]:
                # Ignore daughters entry since it is not used
                pass
            elif key not in current_class_dict:
                # Class dict are different if they don't have same keys
                return True
            else:
                val1 = current_class_dict[key]
                # Comparison of property and constant which are lists of dict
                if (
                    isinstance(val0, list)
                    and len(val0) > 0
                    and isinstance(val0[0], dict)
                ):
                    if (
                        not isinstance(val1, list)
                        or len(val1) == 0
                        or not isinstance(val1[0], dict)
                    ):
                        return True

                    for ii, dict0 in enumerate(val0):
                        for name, data0 in dict0.items():
                            if name not in val1[ii]:
                                # Property/Constant dicts are different if they don't have same keys
                                return True
                            else:
                                data1 = val1[ii][name]
                            if data0 != data1:
                                try:
                                    # Try to set variables as float for comparison
                                    is_modified_class = float(data0) != float(data1)
                                    if is_modified_class:
                                        return True
                                except Exception as e:
                                    # Try to set variables as str for comparison
                                    is_modified_class = str(data0) != str(data1)
                                    if is_modified_class:
                                        return True

                elif val0 != val1:
                    # Comparison of other data: path, methods, class name etc
                    try:
                        # Try to set variables as float for comparison
                        is_modified_class = float(val0) != float(val1)
                        if is_modified_class:
                            return True
                    except Exception as e:
                        # Try to set variables as str for comparison
                        is_modified_class = str(val0) != str(val1)
                        if is_modified_class:
                            return True

        return is_modified_class

    def import_class_from_csv(self, csv_path):
        """Import class from csv file when clicking on a csv in TreeView

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        csv_path : str
            Path to csv file

        """

        # Load csv file
        try:
            current_class_dict = read_file(
                csv_path, soft_name=PACKAGE_NAME, is_get_size=True
            )
        except Exception as e:
            print("Cannot load csf file: " + csv_path)
            return

        # Store current class information for further use
        self.current_class_dict = current_class_dict

        # Store path to method folder
        self.current_method_folder_path = join(
            MAIN_DIR, "Methods", self.current_module, self.current_class_dict["name"]
        )

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

        # Get the list of property names
        prop_name_list = [
            self.table_prop.cellWidget(row, 0).text()
            for row in range(1, self.table_prop.rowCount(), 1)
            if row != row_index
        ]

        if prop_name in prop_name_list:
            print("Cannot rename property with an existing name in property list")
            # Cancel rename and use old property name
            self.table_prop.cellWidget(row_index, 0).setText(
                self.current_class_dict["properties"][row_index - 1]["name"]
            )
        else:
            # Edit current class dict
            self.current_class_dict["properties"][row_index - 1]["name"] = prop_name

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

        # Set Duplicate button to disabled since Name is empty
        self.table_meth.cellWidget(last_row, 2).setEnabled(False)

        # Add empty prop in current class dict
        self.current_class_dict["methods"].append("")

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
        method_path = join(self.current_method_folder_path, meth_name + ".py")
        if isfile(method_path):
            os.remove(method_path)

            if isfile(method_path):
                print("Cannot delete method file: " + method_path)
            else:
                print("Deleted method file: " + method_path)

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
        method_path = join(self.current_method_folder_path, meth_name + ".py")
        if isfile(method_path):
            method_path_dup = join(
                self.current_method_folder_path, meth_name_dup + ".py"
            )
            copyfile(method_path, method_path_dup)
            if isfile(method_path_dup):
                print("Duplicated method file at: " + method_path_dup)
            else:
                print("Cannot duplicate method file: " + method_path_dup)

        # Add buttons in last row
        self.addRowButtonsMethod(last_row)

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

        # Check that renamed method doesn't already exists to avoid duplicates
        if meth_name in self.current_class_dict["methods"]:
            print("Cannot rename method with an existing name in method list")
            # Set old method name
            self.table_meth.cellWidget(row_index, 0).setText(
                self.current_class_dict["methods"][row_index]
            )

        else:
            # Get old method name path
            old_meth_path = join(
                self.current_method_folder_path,
                self.current_class_dict["methods"][row_index] + ".py",
            )
            # Get new method name path
            new_meth_path = join(self.current_method_folder_path, meth_name + ".py")

            # Delete new file if it already exists
            if isfile(new_meth_path):
                os.remove(new_meth_path)

            # Rename file if old file exists
            if isfile(old_meth_path):
                os.rename(old_meth_path, new_meth_path)

            # Store new name in current class dict
            self.current_class_dict["methods"][row_index] = meth_name

        # Enable Duplicate button
        self.table_meth.cellWidget(row_index, 2).setEnabled(True)

    def browseMethod(self):
        """Open explorer at folder path containing methods

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        """
        # Get full path to folder
        path = realpath(self.current_method_folder_path)

        # Create folder if not existing
        if not isdir(path):
            print("Method folder doesn't exist. Create method folder at: " + path)
            os.mkdir(path)

        # Open folder in explorer
        os.startfile(path)

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
        method_path = join(self.current_method_folder_path, meth + ".py")

        if not isdir(self.current_method_folder_path):
            print(
                "Method folder doesn't exist. Create method folder at: "
                + self.current_method_folder_path
            )

        if not isfile(method_path):
            print("Method file doesn't exist. Create method file at: " + method_path)

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
        self.table_meta.setRowCount(2)
        for col, meta_name in enumerate(self.list_meta):
            meta_prop = self.current_class_dict[MATCH_META_DICT[meta_name]]
            # Create QLineEdit
            line_edit = QLineEdit(str(meta_prop))
            line_edit.setAlignment(Qt.AlignLeft)
            if col == 0:
                # Disable package edition since it is necessarily the folder containing the csv file
                line_edit.setEnabled(False)
            self.table_meta.setCellWidget(1, col, line_edit)

        # Adjust column width
        self.table_meta.resizeColumnsToContents()

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

        # Get the list of constant names
        const_name_list = [
            self.table_const.cellWidget(row, 0).text()
            for row in range(1, self.table_const.rowCount(), 1)
            if row != row_index
        ]

        if const_name in const_name_list:
            # Cancel rename and use old constant name
            print("Cannot rename constant with an existing name in constant list")
            self.table_const.cellWidget(row_index, 0).setText(
                self.current_class_dict["constants"][row_index - 1]["name"]
            )
        else:
            # Edit current class dict
            self.current_class_dict["constants"][row_index - 1]["name"] = const_name

        # Enable Duplicate button
        self.table_const.cellWidget(row_index, len(self.list_const) + 1).setEnabled(
            True
        )

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
        class_dict["name"] = self.current_class_dict["name"]
        class_dict["path"] = self.current_class_dict["path"]

        # Read property table
        prop_list = list()
        for row in range(1, self.table_prop.rowCount(), 1):
            prop_dict = dict()
            for col in range(len(self.list_prop)):
                val = self.table_prop.cellWidget(row, col).text()
                try:
                    val = float(val)
                except Exception as e:
                    pass
                prop_dict[MATCH_PROP_DICT[self.list_prop[col]]] = val
            if prop_dict["name"] != "" and prop_dict["type"] != "":
                prop_list.append(prop_dict)
            else:
                # Ignore property with empty name or type since they will fail in class generator
                print(
                    "Ignore property with empty name or type at row="
                    + str(row)
                    + " in saved csv file"
                )
        class_dict["properties"] = prop_list

        # Read method table
        class_dict["methods"] = list()
        for row in range(self.table_meth.rowCount()):
            val = self.table_meth.cellWidget(row, 0).text()
            if val != "":
                class_dict["methods"].append(val)
            else:
                # Ignore method with empty name since it will fail in class generator
                print(
                    "Ignore method with empty name at row="
                    + str(row)
                    + " in saved csv file"
                )

        # Read meta data table
        for col in range(self.table_meta.columnCount()):
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
                print(
                    "Ignore constant with empty name at row="
                    + str(row)
                    + " in saved csv file"
                )

        return class_dict

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
        csv_path = join(
            DOC_DIR, self.current_module, self.get_obj_name(self.current_class_index)
        )
        self.import_class_from_csv(csv_path)
        self.set_class_selected()

        # Store class csv file path in list
        if csv_path not in self.list_class_modified:
            self.list_class_modified.append(csv_path)

    def genClass(self):
        """Generate class from csv files

        Parameters
        ----------
        self : DClassGenerator
            A DClassGenerator object
        """
        run_generate_classes(is_black=self.is_black.isChecked())

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
        index = self.dirModel.index(join(path, newName))

        if self.dirModel.isDir(index):
            print("Cannot rename module")
            # Rename folder back to original name to prevent issues with package attribute
            os.rename(join(path, newName), join(path, oldName))

        elif newName[-4:] == ".csv":
            if self.current_class_dict is not None:
                # Update class name in current class dict
                self.current_class_dict["name"] = newName[:-4]

            # Update class name label
            self.set_label_classname(newName[:-4])

            # Update class name in list of modified class
            if join(path, oldName) in self.list_class_modified:
                ii = self.list_class_modified.index(join(path, oldName))
                self.list_class_modified[ii] = join(path, newName)
            elif realpath(oldName) in self.list_class_modified:
                ii = self.list_class_modified.index(realpath(oldName))
                self.list_class_modified[ii] = join(path, newName)

            # New path to method folder after class renaming
            method_path_new = self.current_method_folder_path.replace(
                oldName[:-4], newName[:-4]
            )

            if isdir(self.current_method_folder_path):
                # Rename methods folder if it exists
                os.rename(self.current_method_folder_path, method_path_new)

            # Update method folder path
            self.current_method_folder_path = method_path_new

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
        file_path = self.dirModel.filePath(index)

        # Get class name
        class_name = self.get_obj_name(index)

        # Delete csv file associated to class
        self.dirModel.remove(index)

        if isfile(file_path):
            print("Cannot delete class file: " + file_path)
            print("Please check that file is not opened in csv editor")
            return
        else:
            print("Deleted class file: " + file_path)

        # Delete methods folder
        if isdir(self.current_method_folder_path):
            rmtree(self.current_method_folder_path, ignore_errors=True)

            if isdir(self.current_method_folder_path):
                print(
                    "Cannot delete class method folder: "
                    + self.current_method_folder_path
                )
            else:
                print("Deleted class method folder: " + self.current_method_folder_path)

        if self.current_class_dict["name"] == class_name[:-4]:
            # Reinit tables if deleted class is the selected class
            self.init_tables_buttons()
            self.current_class_dict = None
            self.current_module = None
            self.current_method_folder_path = None
            self.current_class_index = None

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
        file_path = self.dirModel.filePath(index)
        file_name = self.dirModel.fileName(index)
        if isfile(file_path):
            file_path_dup = file_path.replace(file_name, file_name[:-4] + "_copy.csv")
            copyfile(file_path, file_path_dup)
            if isfile(file_path_dup):
                print("Duplicated csv file at: " + file_path_dup)
            else:
                print("Cannot duplicate csv file at: " + file_path_dup)

        # Copy methods folder if it exists
        meth_folder = self.current_method_folder_path
        if isdir(meth_folder):
            meth_folder_dup = self.current_method_folder_path + "_copy"
            copytree(meth_folder, meth_folder_dup)
            if isdir(meth_folder):
                print("Duplicated method files at: " + meth_folder_dup)
            else:
                print("Cannot duplicate method files at: " + meth_folder_dup)

    def createClass(self, index):
        """Create class by saving empty csv file

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        index : QModelIndex
            Model index of current selected item in treeview

        """

        # Get file path
        file_path = join(self.dirModel.filePath(index), "new_class.csv")

        # Init class dict
        class_dict = dict()
        class_dict["name"] = "new_class"
        class_dict["path"] = file_path

        # Init property table
        prop_dict = dict()
        for col in range(len(self.list_prop)):
            prop_dict[MATCH_PROP_DICT[self.list_prop[col]]] = ""
        class_dict["properties"] = [prop_dict]
        class_dict["properties"][0]["name"] = "new_prop"

        # Init method table
        class_dict["methods"] = ["new_method"]

        # Init meta data table
        class_dict["package"] = self.dirModel.data(index)
        class_dict["mother"] = ""
        class_dict["desc"] = ""
        class_dict["constants"] = [{"name": "VERSION", "value": 1}]

        # Write empty class into csv format
        write_file(class_dict)

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

        if isdir(folder_path):
            rmtree(folder_path, ignore_errors=True)

            if isdir(folder_path):
                print("Cannot delete folder: " + folder_path)
            else:
                print("Deleted folder: " + folder_path)

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

    def get_obj_name(self, index):
        """get object name from treeview at first column for given index"""
        if index.column() == 0:
            # User clicked directly on name, extract name
            obj_name = self.dirModel.data(index)
        else:
            # User clicked on other properties than name, extract name by using parent
            obj_name = self.dirModel.data(index.parent().child(index.row(), 0))

        return obj_name

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

    def set_label_classname(self, class_name):
        """Set label of class name with proper font"""
        # Set class name as title
        self.label_classname.setText(
            '<html><head/><body><p><span style=" font-size:14pt; font-weight:700; text-decoration: underline;">'
            + class_name
            + " </span></p></body></html>"
        )