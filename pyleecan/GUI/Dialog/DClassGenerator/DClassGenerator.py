from os.path import join, isfile, isdir
from shutil import copyfile
import os
from PySide2.QtCore import Qt, Signal, QDir

from functools import partial

from PySide2.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QWidget,
    QFileSystemModel,
    QLabel,
    QLineEdit,
    QDesktopWidget,
    QHeaderView,
    QPushButton,
    QTableWidgetItem,
)

import subprocess

from ..DClassGenerator.Ui_DClassGenerator import Ui_DClassGenerator

from ....definitions import DOC_DIR, PACKAGE_NAME, MAIN_DIR

from ...Tools.WPathSelector.WPathSelector import WPathSelector
from ...Tools.FloatEdit import FloatEdit
from ....Generator.read_fct import read_file
from ....Generator.run_generate_classes import run_generate_classes
from ....Generator.write_fct import write_file, MATCH_META_DICT, MATCH_PROP_DICT

MAX_WIDTH_TREEVIEW = 300

EDITOR_PATH = "C:\\Users\\emile\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
# EDITOR_PATH = "notepad.exe" ;


class DClassGenerator(Ui_DClassGenerator, QWidget):
    """Main windows of the Machine Setup Tools"""

    # Signal to update the simulation
    path_Changed = Signal()
    rejected = Signal()

    def __init__(self, class_gen_path=""):
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

        self.is_save_needed = False
        # self.material_dict = material_dict
        self.last_index = 0  # Index of the last step available

        # Init class dict of current class
        self.current_class_dict = None
        self.current_module = None

        # Saving arguments
        self.class_gen_path = class_gen_path
        if class_gen_path == "":
            self.class_gen_path = DOC_DIR.replace("\\", "/")
        else:
            self.class_gen_path = class_gen_path.replace("\\", "/")

        # Init path selector and disable it for the moment
        self.path_selector = WPathSelector(parent=self)
        self.path_selector.set_path_txt(path=DOC_DIR)
        self.path_selector.setDisabled(True)
        self.path_selector.setHidden(False)
        self.path_selector.in_path.setText("Class generator path")

        # Init treeview
        self.treeView.setMinimumWidth(200)
        self.treeView.setMaximumWidth(MAX_WIDTH_TREEVIEW)
        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(self.class_gen_path)
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)
        self.treeView.setModel(self.dirModel)
        self.treeView.setRootIndex(self.dirModel.index(self.class_gen_path))
        self.treeView.setHeaderHidden(True)
        self.treeView.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        # Get screen size
        sizeObject = QDesktopWidget().screenGeometry(-1)
        max_height = sizeObject.height()
        max_width = sizeObject.width()
        self.setMinimumWidth(max_width)

        # Store list of properties for further use
        self.list_prop = list(MATCH_PROP_DICT.keys())

        # Store list of metadata for further use
        self.list_meta = list(MATCH_META_DICT.keys())

        # Init table of properties
        self.table_prop.setMinimumWidth(max_width - MAX_WIDTH_TREEVIEW)
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
        self.table_meth.setMinimumWidth(max_width - MAX_WIDTH_TREEVIEW)
        self.table_meth.setColumnCount(4)
        self.table_meth.horizontalHeader().hide()
        self.table_meth.verticalHeader().hide()

        # Init tables of metadata
        self.table_meta.setMinimumWidth(max_width - MAX_WIDTH_TREEVIEW)
        self.table_meta.setRowCount(1)
        self.table_meta.setColumnCount(len(self.list_meta))
        # Loop on columns to write metadata
        for col, meta_name in enumerate(self.list_meta):
            # Create FloatEdit or QLineEdit depending on parameter type
            qlabel = QLabel(str(meta_name))
            qlabel.setAlignment(Qt.AlignCenter)
            self.table_meta.setCellWidget(0, col, qlabel)
            self.table_meta.cellWidget(0, col).setStyleSheet("background-color: grey")
        self.table_meta.horizontalHeader().hide()
        self.table_meta.verticalHeader().hide()

        # Connect treeview to methods
        self.treeView.collapsed.connect(self.onItemCollapse)
        self.treeView.expanded.connect(self.onItemExpand)
        self.treeView.clicked.connect(self.update_class_selected)
        self.treeView.customContextMenuRequested.connect(self.openContextMenu)

        # Disable browse button
        self.b_browse.setEnabled(False)

        # Connect save class button
        self.b_saveclass.clicked.connect(self.saveClass)

        # Connect generate class button
        self.b_genclass.clicked.connect(self.genClass)
        self.is_black.setChecked(True)

    def update_class_selected(self, point):
        """Update GUI with selected class from TreeView

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        point : QModelIndex
            Model index of current selected item in treeview

        """

        self.import_class_from_csv(point)
        self.fill_table_prop()
        self.fill_table_meth()
        self.fill_table_meta()

    def import_class_from_csv(self, point):
        """Import class from csv file when clicking on a csv in TreeView

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        point : QModelIndex
            Model index of current selected item in treeview

        """

        # Get parent folder in which the csv file is
        parent = point.parent()

        if self.dirModel.data(parent) == "ClassesRef":
            # Don't do anything if click on module (folder)
            return

        if point.column() == 0:
            # User clicked directly on name, extract name
            class_name = self.dirModel.data(point)
        else:
            # User clicked on other properties than name, extract name by using parent
            class_name = self.dirModel.data(parent.child(point.row(), 0))

        # Get full module name by recursion on parent folders
        module = self.dirModel.data(parent)
        parent_name = module
        while parent_name != "ClassesRef":
            parent = parent.parent()
            parent_name = self.dirModel.data(parent)
            if parent_name != "ClassesRef":
                module = join(parent_name, module)

        # Load csv file
        csv_path = join(DOC_DIR, module, class_name)
        current_class_dict = read_file(
            csv_path, soft_name=PACKAGE_NAME, is_get_size=True
        )

        # Store current class information for further use
        self.current_class_dict = current_class_dict
        self.current_module = module

        # Store path to method folder
        self.path_method_folder = join(
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
                # Create FloatEdit or QLineEdit depending on parameter type
                if isinstance(data, (int, float)):
                    self.table_prop.setCellWidget(row + 1, col, FloatEdit(data))
                else:
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
            self.table_prop.setCellWidget(
                last_row, col, type(self.table_prop.cellWidget(row_index, col))(val)
            )

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
            # Cancel rename and use old property name
            self.table_prop.cellWidget(row_index, 0).setText(
                self.current_class_dict["properties"][row_index - 1]["name"]
            )
        else:
            # Edit current class dict
            self.current_class_dict["properties"][row_index - 1]["name"] = prop_name

    def fill_table_meth(self):
        """Fill tables of methods with current class dict content

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object

        """

        # Connect method folder button
        try:
            # Disconnect browse button in case it already contains a folder_path from previous class
            self.b_browse.clicked.disconnect()
        except Exception:
            pass
        self.b_browse.clicked.connect(
            partial(self.browseMethod, self.path_method_folder)
        )

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
        # Add open button
        b_open_meth = QPushButton(text="Open", parent=self.table_meth)
        b_open_meth.clicked.connect(partial(self.openMethod, b_open_meth))
        self.table_meth.setCellWidget(row_index, 1, b_open_meth)
        # Add delete button
        b_del_meth = QPushButton(text="Delete", parent=self.table_meth)
        b_del_meth.clicked.connect(partial(self.deleteMethod, b_del_meth))
        self.table_meth.setCellWidget(row_index, 2, b_del_meth)
        # Add duplicate button
        b_dup_meth = QPushButton(text="Duplicate", parent=self.table_meth)
        b_dup_meth.clicked.connect(partial(self.duplicateMethod, b_dup_meth))
        self.table_meth.setCellWidget(row_index, 3, b_dup_meth)

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
            if self.table_meth.cellWidget(row, 2) == button:
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
        method_path = join(self.path_method_folder, meth_name + ".py")
        if isfile(method_path):
            os.remove(method_path)

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
            if self.table_meth.cellWidget(row, 3) == button:
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
        method_path = join(self.path_method_folder, meth_name + ".py")
        method_path_dup = join(self.path_method_folder, meth_name_dup + ".py")
        copyfile(method_path, method_path_dup)

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

        # Get row_index of clicked button
        for row in range(self.table_meth.rowCount()):
            if self.table_meth.cellWidget(row, 0) == line_edit:
                row_index = row
                break

        # Get new method name from widget
        meth_name = self.table_meth.cellWidget(row_index, 0).text()

        # Check that renamed method doesn't already exists to avoid duplicates
        if meth_name not in self.current_class_dict["methods"]:
            # Get old method name path
            old_meth_path = join(
                self.path_method_folder,
                self.current_class_dict["methods"][row_index] + ".py",
            )
            # Get new method name path
            new_meth_path = join(self.path_method_folder, meth_name + ".py")

            # Delete new file if it already exists
            if isfile(new_meth_path):
                os.remove(new_meth_path)

            # Rename file if old file exists
            if isfile(old_meth_path):
                os.rename(old_meth_path, new_meth_path)

            # Store new name in current class dict
            self.current_class_dict["methods"][row_index] = meth_name
        else:
            # Set old method name
            self.table_meth.cellWidget(row_index, 0).setText(
                self.current_class_dict["methods"][row_index]
            )

    def browseMethod(self):
        """Open explorer at folder path containing methods

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        """
        # Get full path to folder
        path = os.path.realpath(self.path_method_folder)

        # Create folder if not existing
        if not isdir(path):
            os.mkdir(path)

        # Open folder in explorer
        os.startfile(path)

    def openMethod(self, button):
        """Open method in editor given by EDITOR PATH

        Parameters
        ----------
        self : DClassGenerator
            a DClassGenerator object
        button : QPushButton
            Button that emits signal

        """

        # Get row_index of clicked duplicate button
        for row in range(self.table_meth.rowCount()):
            if self.table_meth.cellWidget(row, 1) == button:
                row_index = row
                break

        # Get method name at given row index
        meth = self.table_meth.cellWidget(row_index, 0).text()

        # Check if there is a folder in the method name
        if "." in meth:
            meth_split = meth.split(".")
            meth = join(*meth_split)

        # Get method path
        method_path = join(self.path_method_folder, meth + ".py")

        if not isfile(method_path):
            # Create method file
            pass

        # Open method with editor
        p = subprocess.Popen([EDITOR_PATH, method_path])

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
            if isinstance(MATCH_META_DICT[meta_name], list):
                meta_prop = self.current_class_dict[MATCH_META_DICT[meta_name][0]]
                # Add rows if there is more than one constant
                if self.table_meta.rowCount() < len(meta_prop) + 1:
                    self.table_meta.setRowCount(len(meta_prop) + 1)
                # Browse list of constants
                for row, const_dict in enumerate(meta_prop):
                    val = const_dict[MATCH_META_DICT[meta_name][1]]
                    # Create FloatEdit or QLineEdit depending on parameter type
                    if isinstance(val, (int, float)):
                        self.table_meta.setCellWidget(row + 1, col + 1, FloatEdit(val))
                    else:
                        line_edit = QLineEdit(str(val))
                        line_edit.setAlignment(Qt.AlignLeft)
                        self.table_meta.setCellWidget(row + 1, col, line_edit)

            else:
                meta_prop = self.current_class_dict[MATCH_META_DICT[meta_name]]
                # Create QLineEdit
                line_edit = QLineEdit(str(meta_prop))
                line_edit.setAlignment(Qt.AlignLeft)
                self.table_meta.setCellWidget(1, col, line_edit)

        # Disable unused rows in case of several constants
        if self.table_meta.rowCount() > 2:
            for row in range(2, self.table_meta.rowCount(), 1):
                for col, meta_name in enumerate(self.list_meta):
                    if "Constant" not in meta_name:
                        item = QTableWidgetItem("")
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                        self.table_meta.setItem(row, col, item)

    def get_current_class_dict_from_tables(self):
        """Get current class dict by reading property, method and metadata tables

        Parameters
        ----------
        self : DClassGenerator
            A DClassGenerator object
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
                prop_dict[MATCH_PROP_DICT[self.list_prop[col]]] = val
            prop_list.append(prop_dict)
        class_dict["properties"] = prop_list

        # Read method table
        class_dict["methods"] = [
            self.table_meth.cellWidget(row, 0).text()
            for row in range(self.table_meth.rowCount())
        ]

        # Read meta data table
        # Handle constants separately
        cst_list = list()
        for col in range(self.table_meta.columnCount()):
            if "Constant" in self.list_meta[col]:
                # Recreate list of constants dict
                for row in range(1, self.table_meta.rowCount(), 1):
                    val = self.table_meta.cellWidget(row, col).text()
                    if len(cst_list) < row:
                        cst_list.append(dict())
                    cst_list[row - 1][MATCH_META_DICT[self.list_meta[col]][1]] = val
                class_dict[MATCH_META_DICT[self.list_meta[col]][0]] = cst_list
            else:
                val = self.table_meta.cellWidget(1, col).text()
                class_dict[MATCH_META_DICT[self.list_meta[col]]] = val

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

    def genClass(self):
        """Generate class from csv files

        Parameters
        ----------
        self : DClassGenerator
            A DClassGenerator object
        """
        run_generate_classes(is_black=self.is_black.isChecked())

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

    def openContextMenu(self, point):
        """Generate and open context the menu at the given point position."""

        index = self.treeView.indexAt(point)
        # pos = QtGui.QCursor.pos()

        # if not index.isValid():
        #     return

        # # get the data
        # item = self.model.item(index)
        # obj_info = self.model.get_obj_info(item)

        # # init the menu
        # menu = TreeEditContextMenu(obj_dict=obj_info, parent=self)
        # menu.exec_(pos)

        # self.onSelectionChanged(self.selectionModel.selection())

        print("toto5")

        # """Generate and open context the menu at the given point position."""
        # index = self.treeView.indexAt(point)
        # pos = QtGui.QCursor.pos()

        # if not index.isValid():
        #     return

        # # get the data
        # item = self.model.item(index)
        # obj_info = self.model.get_obj_info(item)

        # # init the menu
        # menu = TreeEditContextMenu(obj_dict=obj_info, parent=self)
        # menu.exec_(pos)

        # self.onSelectionChanged(self.selectionModel.selection())

        # # Initialize the machine if needed
        # if machine is None:
        #     self.machine = type(mach_list[0]["init_machine"])(
        #         init_dict=mach_list[0]["init_machine"].as_dict()
        #     )

        # self.update_nav()
        # self.set_nav(self.last_index)

        # # Connect save/load button
        # self.nav_step.currentRowChanged.connect(self.set_nav)
        # self.b_save.clicked.connect(self.s_save)
        # self.b_load.clicked.connect(self.s_load)

        # self.qmessagebox_question = None

    # def s_save_close(self):
    #     """Signal to save and close

    #     Parameters
    #     ----------
    #     self : DMachineSetup
    #         A DMachineSetup object
    #     """
    #     to_close = self.s_save()
    #     if to_close:
    #         self.close()

    # def s_load(self):
    #     """Slot to load a machine from a .json file (triggered by b_load)

    #     Parameters
    #     ----------
    #     self : DMachineSetup
    #         A DMachineSetup object
    #     """
    #     ### TODO: handle material data, i.e. "connect", set new material, etc.

    #     # Ask the user to select a .json file to load
    #     load_path = str(
    #         QFileDialog.getOpenFileName(
    #             self, self.tr("Load file"), self.machine_path, "Json (*.json)"
    #         )[0]
    #     )
    #     if load_path != "":
    #         try:
    #             # Update the machine path to remember the last used folder
    #             self.machine_path = dirname(load_path)
    #             # Load and check type of instance
    #             machine = load(load_path)
    #             if isinstance(machine, Machine):
    #                 self.machine = machine
    #                 load_machine_materials(self.material_dict, self.machine)
    #             else:
    #                 QMessageBox().critical(
    #                     self,
    #                     self.tr("Error"),
    #                     self.tr("The choosen file is not a machine file."),
    #                 )
    #                 return
    #             self.machineChanged.emit()
    #             self.is_save_needed = False
    #         except Exception as e:
    #             QMessageBox().critical(
    #                 self,
    #                 self.tr("Error"),
    #                 self.tr(
    #                     "The machine file is incorrect:\n",
    #                     "Please keep the \n, another " "message is following this one",
    #                 )
    #                 + type(e).__name__
    #                 + ": "
    #                 + str(e),
    #             )
    #             return
    #         self.update_nav()

    # def update_nav(self, next_step=None):
    #     """Update the nav list to match the step of the current machine"""
    #     mach_dict = mach_list[self.get_machine_index()]
    #     self.nav_step.blockSignals(True)
    #     self.nav_step.clear()
    #     index = 1
    #     for step in mach_dict["start_step"]:
    #         self.nav_step.addItem(" " + str(index) + ": " + step.step_name)
    #         index += 1
    #     for step in mach_dict["stator_step"]:
    #         self.nav_step.addItem(" " + str(index) + ": Stator " + step.step_name)
    #         index += 1
    #     for step in mach_dict["rotor_step"]:
    #         if index < 10:
    #             self.nav_step.addItem(" " + str(index) + ": Rotor " + step.step_name)
    #         else:
    #             self.nav_step.addItem(str(index) + ": Rotor " + step.step_name)
    #         index += 1
    #     # Adding step Machine Summary
    #     if index < 10:
    #         self.nav_step.addItem(" " + str(index) + ": " + SPreview.step_name)
    #     else:
    #         self.nav_step.addItem(str(index) + ": " + SPreview.step_name)
    #     index += 1
    #     # Adding Simulation Step
    #     if index < 10:
    #         self.nav_step.addItem(" " + str(index) + ": " + SSimu.step_name)
    #     else:
    #         self.nav_step.addItem(str(index) + ": " + SSimu.step_name)
    #     # Update GUI and select correct step
    #     self.update_enable_nav()
    #     self.nav_step.blockSignals(False)
    #     if next_step is None:
    #         self.nav_step.setCurrentRow(self.last_index)
    #     else:
    #         self.nav_step.setCurrentRow(next_step)

    # def update_enable_nav(self):
    #     # Load for readibility
    #     nav = self.nav_step
    #     machine = self.machine
    #     mach_dict = mach_list[self.get_machine_index()]
    #     # First we disable all the item in the navigation widget
    #     for ii in range(0, nav.count()):
    #         nav.item(ii).setFlags(DISABLE_ITEM)
    #     # First step is always available
    #     nav.item(0).setFlags(ENABLE_ITEM)
    #     index = 1
    #     # Check the start steps
    #     for step in mach_dict["start_step"]:
    #         if step.check(machine) is not None:
    #             self.last_index = index - 1
    #             return None  # Exit at the first fail
    #         nav.item(index).setFlags(ENABLE_ITEM)
    #         index += 1
    #     # Check the stator steps
    #     for step in mach_dict["stator_step"]:
    #         if step.check(machine.stator) is not None:
    #             self.last_index = index - 1
    #             return None  # Exit at the first fail
    #         nav.item(index).setFlags(ENABLE_ITEM)
    #         index += 1
    #     # Check the rotor steps
    #     for step in mach_dict["rotor_step"]:
    #         if step.check(machine.rotor) is not None:
    #             self.last_index = index - 1
    #             return None  # Exit at the first fail
    #         nav.item(index).setFlags(ENABLE_ITEM)
    #         index += 1
    #     # Enable and select FEMM Simulation
    #     nav.item(index).setFlags(ENABLE_ITEM)
    #     self.last_index = index

    # def get_machine_index(self):
    #     """Get the index corresponding to the current machine in the mach_list"""
    #     # Get the correct machine dictionary
    #     index = mach_index.index(type(self.machine))
    #     if index == -1:
    #         QMessageBox().critical(
    #             self, self.tr("Error"), self.tr("Unknown machine type")
    #         )
    #         self.machine = type(mach_list[0]["init_machine"])(
    #             init_dict=mach_list[0]["init_machine"].as_dict()
    #         )
    #         return self.get_machine_index()
    #     return index

    # def set_nav(self, index):
    #     """Select the current widget according to the current machine type
    #     and the current nav index

    #     Parameters
    #     ----------
    #     self : DMachineSetup
    #         A DMachineSetup object
    #     index : int
    #         Current index of nav_step
    #     """
    #     # Get the step list of the current machine
    #     mach_dict = mach_list[self.get_machine_index()]
    #     step_list = list()
    #     step_list.extend(mach_dict["start_step"])
    #     step_list.extend(mach_dict["stator_step"])
    #     step_list.extend(mach_dict["rotor_step"])
    #     step_list.append(SPreview)
    #     step_list.append(SSimu)
    #     is_stator = "Stator" in self.nav_step.currentItem().text()

    #     # Regenerate the step with the current values
    #     self.w_step.setParent(None)
    #     self.w_step = step_list[index](
    #         machine=self.machine, material_dict=self.material_dict, is_stator=is_stator
    #     )
    #     self.w_step.b_previous.clicked.connect(self.s_previous)
    #     if index != len(step_list) - 1:
    #         self.w_step.b_next.setText(self.tr("Next"))
    #         self.w_step.b_next.clicked.connect(self.s_next)
    #     # else:
    #     #     self.w_step.b_next.setText(self.tr("Save and Close"))
    #     #     self.w_step.b_next.clicked.connect(self.s_save_close)

    #     self.w_step.saveNeeded.connect(self.save_needed)
    #     # Refresh the GUI
    #     self.main_layout.insertWidget(1, self.w_step)

    # def s_next(self):
    #     """Signal to set the next step as accessible (and selected)

    #     Parameters
    #     ----------
    #     self : DMachineSetup
    #         A DMachineSetup object
    #     """
    #     next_index = self.nav_step.currentRow() + 1
    #     mach_dict = mach_list[self.get_machine_index()]

    #     if next_index - 1 < len(mach_dict["start_step"]):
    #         error = self.w_step.check(self.machine)
    #     elif next_index - 1 < len(mach_dict["start_step"]) + len(
    #         mach_dict["stator_step"]
    #     ):
    #         error = self.w_step.check(self.machine.stator)
    #     else:
    #         error = self.w_step.check(self.machine.rotor)

    #     if error is not None:  # An error: display it in a popup
    #         QMessageBox().critical(self, self.tr("Error"), error)
    #     else:  # No error => Go to the next page
    #         self.nav_step.item(next_index).setFlags(ENABLE_ITEM)
    #         self.last_index = next_index
    #         self.nav_step.setCurrentRow(next_index)
    #         # As the current row have changed, set_nav is called

    # def s_previous(self):
    #     """Signal to set the previous page of w_page_stack as accessible (and selected)

    #     Parameters
    #     ----------
    #     self : DMachineSetup
    #         A DMachineSetup object
    #     """
    #     next_index = self.nav_step.currentRow() - 1
    #     self.nav_step.setCurrentRow(next_index)
    #     # As the current row have change, set_nav is called
