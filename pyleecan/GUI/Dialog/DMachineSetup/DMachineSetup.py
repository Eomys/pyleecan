# -*- coding: utf-8 -*-

from os.path import basename, join, dirname

from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import QFileDialog, QMessageBox, QWidget

from ....Functions.load import load, load_machine_materials
from ....GUI.Dialog.DMachineSetup import mach_index, mach_list
from ....GUI.Dialog.DMachineSetup.Ui_DMachineSetup import Ui_DMachineSetup
from ....GUI.Dialog.DMachineSetup.SPreview.SPreview import SPreview
from ....GUI.Dialog.DMachineSetup.SSimu.SSimu import SSimu
from ....definitions import config_dict
from ....Classes.Machine import Machine

# Flag for set the enable property of w_nav (List_Widget)
DISABLE_ITEM = Qt.NoItemFlags
ENABLE_ITEM = Qt.ItemIsSelectable | Qt.ItemIsEnabled


class DMachineSetup(Ui_DMachineSetup, QWidget):
    """Main windows of the Machine Setup Tools"""

    # Signal to update the simulation
    machineChanged = Signal()
    rejected = Signal()

    def __init__(self, machine=None, material_dict=None, machine_path=""):
        """Initialize the GUI according to machine type

        Parameters
        ----------
        self : DMachineSetup
            a DMachineSetup object
        machine : Machine
            Machine to edit
        material_dict: dict
            Materials dictionary (library + machine)
        machine_path : str
            Default loading path for machine
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.is_save_needed = False
        self.material_dict = material_dict
        self.last_index = 0  # Index of the last step available

        # Saving arguments
        self.machine = machine
        if machine_path == "":
            self.machine_path = config_dict["MAIN"]["MACHINE_DIR"]
        else:
            self.machine_path = machine_path

        # Initialize the machine if needed
        if machine is None:
            self.machine = type(mach_list[0]["init_machine"])(
                init_dict=mach_list[0]["init_machine"].as_dict()
            )

        self.update_nav()
        self.set_nav(self.last_index)

        # Connect save/load button
        self.nav_step.currentRowChanged.connect(self.set_nav)
        self.b_save.clicked.connect(self.s_save)
        self.b_load.clicked.connect(self.s_load)

        self.qmessagebox_question = None

    def save_needed(self):
        """Set is_save_needed to True"""
        self.is_save_needed = True

    def closeEvent(self, event):
        """Display a message before leaving

        Parameters
        ----------
        self : DMachineSetup
            A DMachineSetup object
        event :
            The closing event
        """

        if self.is_save_needed:
            quit_msg = self.tr(
                "Unsaved changes will be lost.\nDo you want to save the machine?"
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
                self.s_save()

    def reject(self):
        """ """
        self.rejected.emit()
        self.close()

    def s_save(self):
        """Slot for saving the current machine to a json file

        Parameters
        ----------
        self : DMachineSetup
            A DMachineSetup object
        """
        # Ask the user to select a .m file to save
        if self.machine.name in ["", None]:
            save_file_path = QFileDialog.getSaveFileName(
                self, self.tr("Save file"), self.machine_path, "Json (*.json)"
            )[0]
        else:
            def_path = join(self.machine_path, self.machine.name + ".json")
            save_file_path = QFileDialog.getSaveFileName(
                self, self.tr("Save file"), def_path, "Json (*.json)"
            )[0]

        # Avoid bug due to user closing the popup witout selecting a file
        if save_file_path != "":
            # Set the machine name to match the file name
            self.machine.name = str(basename(str(save_file_path)))[:-5]
            # Save the machine file
            self.machine.save(save_file_path)
            # To update the machine name field (if first page)
            self.set_nav(self.nav_step.currentRow())
            # Update the machine path to remember the last used folder
            self.machine_path = dirname(save_file_path)
            # Notify the project GUI that the machine has changed
            self.machineChanged.emit()
            self.is_save_needed = False
            return True
        return False

    def s_save_close(self):
        """Signal to save and close

        Parameters
        ----------
        self : DMachineSetup
            A DMachineSetup object
        """
        to_close = self.s_save()
        if to_close:
            self.close()

    def s_load(self):
        """Slot to load a machine from a .json file (triggered by b_load)

        Parameters
        ----------
        self : DMachineSetup
            A DMachineSetup object
        """
        ### TODO: handle material data, i.e. "connect", set new material, etc.

        # Ask the user to select a .json file to load
        load_path = str(
            QFileDialog.getOpenFileName(
                self, self.tr("Load file"), self.machine_path, "Json (*.json)"
            )[0]
        )
        if load_path != "":
            try:
                # Update the machine path to remember the last used folder
                self.machine_path = dirname(load_path)
                # Load and check type of instance
                machine = load(load_path)
                if isinstance(machine, Machine):
                    self.machine = machine
                    load_machine_materials(self.material_dict, self.machine)
                else:
                    QMessageBox().critical(
                        self,
                        self.tr("Error"),
                        self.tr("The choosen file is not a machine file."),
                    )
                    return
                self.machineChanged.emit()
                self.is_save_needed = False
            except Exception as e:
                QMessageBox().critical(
                    self,
                    self.tr("Error"),
                    self.tr(
                        "The machine file is incorrect:\n",
                        "Please keep the \n, another " "message is following this one",
                    )
                    + type(e).__name__
                    + ": "
                    + str(e),
                )
                return
            self.update_nav()

    def update_nav(self, next_step=None):
        """Update the nav list to match the step of the current machine"""
        mach_dict = mach_list[self.get_machine_index()]
        self.nav_step.blockSignals(True)
        self.nav_step.clear()
        index = 1
        for step in mach_dict["start_step"]:
            self.nav_step.addItem(" " + str(index) + ": " + step.step_name)
            index += 1
        for step in mach_dict["stator_step"]:
            self.nav_step.addItem(" " + str(index) + ": Stator " + step.step_name)
            index += 1
        for step in mach_dict["rotor_step"]:
            if index < 10:
                self.nav_step.addItem(" " + str(index) + ": Rotor " + step.step_name)
            else:
                self.nav_step.addItem(str(index) + ": Rotor " + step.step_name)
            index += 1
        # Adding step Machine Summary
        if index < 10:
            self.nav_step.addItem(" " + str(index) + ": " + SPreview.step_name)
        else:
            self.nav_step.addItem(str(index) + ": " + SPreview.step_name)
        index += 1
        # Adding Simulation Step
        if index < 10:
            self.nav_step.addItem(" " + str(index) + ": " + SSimu.step_name)
        else:
            self.nav_step.addItem(str(index) + ": " + SSimu.step_name)
        # Update GUI and select correct step
        self.update_enable_nav()
        self.nav_step.blockSignals(False)
        if next_step is None:
            self.nav_step.setCurrentRow(self.last_index)
        else:
            self.nav_step.setCurrentRow(next_step)

    def update_enable_nav(self):
        # Load for readibility
        nav = self.nav_step
        machine = self.machine
        mach_dict = mach_list[self.get_machine_index()]
        # First we disable all the item in the navigation widget
        for ii in range(0, nav.count()):
            nav.item(ii).setFlags(DISABLE_ITEM)
        # First step is always available
        nav.item(0).setFlags(ENABLE_ITEM)
        index = 1
        # Check the start steps
        for step in mach_dict["start_step"]:
            if step.check(machine) is not None:
                self.last_index = index - 1
                return None  # Exit at the first fail
            nav.item(index).setFlags(ENABLE_ITEM)
            index += 1
        # Check the stator steps
        for step in mach_dict["stator_step"]:
            if step.check(machine.stator) is not None:
                self.last_index = index - 1
                return None  # Exit at the first fail
            nav.item(index).setFlags(ENABLE_ITEM)
            index += 1
        # Check the rotor steps
        for step in mach_dict["rotor_step"]:
            if step.check(machine.rotor) is not None:
                self.last_index = index - 1
                return None  # Exit at the first fail
            nav.item(index).setFlags(ENABLE_ITEM)
            index += 1
        # Enable and select FEMM Simulation
        nav.item(index).setFlags(ENABLE_ITEM)
        self.last_index = index

    def get_machine_index(self):
        """Get the index corresponding to the current machine in the mach_list"""
        # Get the correct machine dictionary
        index = mach_index.index(type(self.machine))
        if index == -1:
            QMessageBox().critical(
                self, self.tr("Error"), self.tr("Unknown machine type")
            )
            self.machine = type(mach_list[0]["init_machine"])(
                init_dict=mach_list[0]["init_machine"].as_dict()
            )
            return self.get_machine_index()
        return index

    def set_nav(self, index):
        """Select the current widget according to the current machine type
        and the current nav index

        Parameters
        ----------
        self : DMachineSetup
            A DMachineSetup object
        index : int
            Current index of nav_step
        """
        # Get the step list of the current machine
        mach_dict = mach_list[self.get_machine_index()]
        step_list = list()
        step_list.extend(mach_dict["start_step"])
        step_list.extend(mach_dict["stator_step"])
        step_list.extend(mach_dict["rotor_step"])
        step_list.append(SPreview)
        step_list.append(SSimu)
        is_stator = "Stator" in self.nav_step.currentItem().text()

        # Regenerate the step with the current values
        self.w_step.setParent(None)
        self.w_step = step_list[index](
            machine=self.machine, material_dict=self.material_dict, is_stator=is_stator
        )
        self.w_step.b_previous.clicked.connect(self.s_previous)
        if index != len(step_list) - 1:
            self.w_step.b_next.setText(self.tr("Next"))
            self.w_step.b_next.clicked.connect(self.s_next)
        # else:
        #     self.w_step.b_next.setText(self.tr("Save and Close"))
        #     self.w_step.b_next.clicked.connect(self.s_save_close)

        self.w_step.saveNeeded.connect(self.save_needed)
        # Refresh the GUI
        self.main_layout.insertWidget(1, self.w_step)

    def s_next(self):
        """Signal to set the next step as accessible (and selected)

        Parameters
        ----------
        self : DMachineSetup
            A DMachineSetup object
        """
        next_index = self.nav_step.currentRow() + 1
        mach_dict = mach_list[self.get_machine_index()]

        if next_index - 1 < len(mach_dict["start_step"]):
            error = self.w_step.check(self.machine)
        elif next_index - 1 < len(mach_dict["start_step"]) + len(
            mach_dict["stator_step"]
        ):
            error = self.w_step.check(self.machine.stator)
        else:
            error = self.w_step.check(self.machine.rotor)

        if error is not None:  # An error: display it in a popup
            QMessageBox().critical(self, self.tr("Error"), error)
        else:  # No error => Go to the next page
            self.nav_step.item(next_index).setFlags(ENABLE_ITEM)
            self.last_index = next_index
            self.nav_step.setCurrentRow(next_index)
            # As the current row have changed, set_nav is called

    def s_previous(self):
        """Signal to set the previous page of w_page_stack as accessible (and selected)

        Parameters
        ----------
        self : DMachineSetup
            A DMachineSetup object
        """
        next_index = self.nav_step.currentRow() - 1
        self.nav_step.setCurrentRow(next_index)
        # As the current row have change, set_nav is called
