# -*- coding: utf-8 -*-


import numpy as np

from os.path import basename, join, dirname, isfile
import os
from logging import getLogger
from ....Functions.GUI.log_error import log_error
from ....loggers import GUI_LOG_NAME
from PySide2.QtCore import Qt, Signal, QDir, QStringListModel
from PySide2.QtGui import QStandardItemModel
from PySide2.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QWidget,
    QFileSystemModel,
    QLabel,
    QLineEdit,
)

from ....Functions.load import load, load_machine_materials
from ..DMachineSetup import mach_index, mach_list
from ..DClassGenerator.Ui_DClassGenerator import Ui_DClassGenerator

# from ..DMachineSetup.SPreview.SPreview import SPreview
# from ..DMachineSetup.SSimu.SSimu import SSimu
from ....definitions import config_dict, DOC_DIR, PACKAGE_NAME

from ....Classes.Machine import Machine
from ...Tools.WPathSelector.WPathSelector import WPathSelector
from ...Tools.FloatEdit import FloatEdit
from ....Generator.read_fct import read_file

# Flag for set the enable property of w_nav (List_Widget)
DISABLE_ITEM = Qt.NoItemFlags
ENABLE_ITEM = Qt.ItemIsSelectable | Qt.ItemIsEnabled


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
        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(self.class_gen_path)
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)
        self.treeView.setModel(self.dirModel)
        self.treeView.setRootIndex(self.dirModel.index(self.class_gen_path))
        self.treeView.setHeaderHidden(True)
        self.treeView.resizeColumnToContents(0)

        # Load csv file
        folder_list = os.listdir(DOC_DIR)
        csv_path = None
        for folder in folder_list:
            file_list = os.listdir(join(DOC_DIR, folder))
            for filename in file_list:
                if len(filename) > 4 and filename[-4:] == ".csv":
                    csv_path = join(DOC_DIR, folder, filename)
                    break
            if csv_path is not None:
                break
        class_dict = read_file(csv_path, soft_name=PACKAGE_NAME)
        self.list_prop = list(class_dict["properties"][0].keys())
        # array_prop = np.array(list_prop).reshape((1, len(list_prop)))

        self.table_prop.setColumnCount(len(class_dict["properties"][0]))
        self.table_prop.setRowCount(1)
        for col in range(self.table_prop.columnCount()):
            self.table_prop.setCellWidget(0, col, QLabel(self.list_prop[col]))

        # self.table_prop.setColumnCount(len(class_dict["properties"][0]))

        # Init table of properties
        # self.table_prop = WTableView(data=array_prop, editable=True)
        # self.table_prop.setParent(self)
        # self.table_prop.setHidden(False)

        # model = QStandardItemModel()

        # model.setHorizontalHeaderLabels(list_prop)
        # self.table_prop.setModel(model)

        self.treeView.collapsed.connect(self.onItemCollapse)
        self.treeView.expanded.connect(self.onItemExpand)
        self.treeView.clicked.connect(self.tree_click)
        self.treeView.customContextMenuRequested.connect(self.openContextMenu)

        self.current_class_dict = None

    def tree_click(self, point):
        parent = point.parent()

        if self.dirModel.data(parent) == "ClassesRef":
            # Don't do anything if click on module (folder)
            pass
        else:
            if point.column() == 0:
                # User clicked directly on name, extract name
                class_name = self.dirModel.data(point)
            else:
                # User clicked on other properties than name, extract name by using parent
                class_name = self.dirModel.data(parent.child(point.row(), 0))

            module = self.dirModel.data(parent)

            # Load csv file
            csv_path = DOC_DIR + "/" + module + "/" + class_name
            self.current_class_dict = read_file(csv_path, soft_name=PACKAGE_NAME)

            self.update_class()

    def update_class(self):
        class_dict = self.current_class_dict

        self.table_prop.setRowCount(len(class_dict["properties"]) + 1)

        for row, prop_dict in enumerate(class_dict["properties"]):
            for prop, val in prop_dict.items():
                col = self.list_prop.index(prop)
                if val is None:
                    val = "None"
                elif isinstance(val, list):
                    val = str(val)
                if isinstance(val, (int, float)):
                    self.table_prop.setCellWidget(row + 1, col, FloatEdit(val))
                else:
                    self.table_prop.setCellWidget(row + 1, col, QLineEdit(val))

        pass

    def onItemCollapse(self, index):
        """Slot for item collapsed"""
        # dynamic resize
        print("toto3")
        for ii in range(3):
            self.treeView.resizeColumnToContents(ii)

    def onItemExpand(self, index):
        """Slot for item expand"""

        print("toto4")

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

        pass

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

    # def save_needed(self):
    #     """Set is_save_needed to True"""
    #     self.is_save_needed = True

    # def closeEvent(self, event):
    #     """Display a message before leaving

    #     Parameters
    #     ----------
    #     self : DMachineSetup
    #         A DMachineSetup object
    #     event :
    #         The closing event
    #     """

    #     if self.is_save_needed:
    #         quit_msg = self.tr(
    #             "Unsaved changes will be lost.\nDo you want to save the machine?"
    #         )
    #         reply = QMessageBox.question(
    #             self,
    #             self.tr("Please save before closing"),
    #             quit_msg,
    #             QMessageBox.Yes,
    #             QMessageBox.No,
    #         )
    #         self.qmessagebox_question = reply
    #         if reply == QMessageBox.Yes:
    #             self.s_save()

    # def reject(self):
    #     """ """
    #     self.rejected.emit()
    #     self.close()

    # def s_save(self):
    #     """Slot for saving the current machine to a json file

    #     Parameters
    #     ----------
    #     self : DMachineSetup
    #         A DMachineSetup object
    #     """
    #     # Ask the user to select a .m file to save
    #     if self.machine.name in ["", None]:
    #         save_file_path = QFileDialog.getSaveFileName(
    #             self, self.tr("Save file"), self.machine_path, "Json (*.json)"
    #         )[0]
    #     else:
    #         def_path = join(self.machine_path, self.machine.name + ".json")
    #         save_file_path = QFileDialog.getSaveFileName(
    #             self, self.tr("Save file"), def_path, "Json (*.json)"
    #         )[0]
    #     save_file_path = save_file_path.replace("\\", "/")

    #     # Avoid bug due to user closing the popup witout selecting a file
    #     if save_file_path != "":
    #         # Set the machine name to match the file name
    #         self.machine.name = str(basename(str(save_file_path)))[:-5]
    #         # Save the machine file
    #         getLogger(GUI_LOG_NAME).info(
    #             "Saving " + self.machine.name + " in folder " + dirname(save_file_path)
    #         )
    #         try:
    #             self.machine.save(save_file_path)
    #         except Exception as e:
    #             err_msg = (
    #                 "Error while saving machine " + self.machine.name + ":\n" + str(e)
    #             )
    #             log_error(self, err_msg)
    #             return False
    #         # To update the machine name field (if first page)
    #         self.set_nav(self.nav_step.currentRow())
    #         # Update the machine path to remember the last used folder
    #         self.machine_path = dirname(save_file_path)
    #         # Notify the project GUI that the machine has changed
    #         self.machineChanged.emit()
    #         self.is_save_needed = False
    #         return True
    #     return False

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
