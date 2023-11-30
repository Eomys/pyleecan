# -*- coding: utf-8 -*-


from PySide2.QtCore import Signal, Qt
from PySide2.QtWidgets import QMessageBox, QDialog
from logging import getLogger


from .....loggers import GUI_LOG_NAME
from .....Methods.Slot.Slot import SlotCheckError
from .....GUI.Dialog.DMachineSetup.DNotchTab.WNotch.WNotch import WNotch
from .....GUI.Dialog.DMachineSetup.DNotchTab.Ui_DNotchTab import Ui_DNotchTab
from .....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon
from .....Classes.NotchEvenDist import NotchEvenDist
from .....Classes.SlotM10 import SlotM10
from .....Functions.Geometry.merge_notch_list import NotchError


class DNotchTab(Ui_DNotchTab, QDialog):
    """Step to set several notches"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()

    def __init__(self, machine, is_stator=False, material_dict=None):
        """Initialize the widget according to machine

        Parameters
        ----------
        self : DNotchTab
            A DNotchTab widget
        machine : Machine
            current machine to edit
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        material_dict: dict
            Materials dictionary (library + machine)
        """
        # Build the interface according to the .ui file
        QDialog.__init__(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        self.setupUi(self)

        # Saving arguments
        self.machine = machine.copy()
        self.is_stator = is_stator
        self.material_dict = material_dict

        # String storing the last error message (used in test)
        self.err_msg = None

        # Get the correct object to set
        if self.is_stator:
            self.obj = self.machine.stator
        else:
            self.obj = self.machine.rotor

        # Init notch
        if self.obj.notch is None:
            self.obj.notch = list()
        if len(self.obj.notch) == 0:  # Add first notch
            self.obj.notch.append(
                NotchEvenDist(
                    alpha=0, notch_shape=SlotM10(Zs=self.obj.get_Zs(), W0=None, H0=None)
                )
            )

        # Update all the notch tab
        # (the current notches types will be initialized)
        self.tab_notch.clear()
        for idx_notch, notch in enumerate(self.obj.notch):
            self.s_add(notch, idx_notch)
        self.tab_notch.setCurrentIndex(0)

        # Set Help URL
        # self.b_help.hide()

        # Connect the slot
        self.b_add.clicked.connect(self.s_add)
        self.tab_notch.tabCloseRequested.connect(self.s_remove)
        self.b_ok.clicked.connect(self.update_and_close)
        self.b_cancel.clicked.connect(self.reject)
        self.b_plot.clicked.connect(self.s_plot)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def s_add(self, notch=None, idx_notch=None):
        """Signal to add a new notch

        Parameters
        ----------
        self : DNotchTab
            A DNotchTab widget
        notch : Notch
            Notch to initialize in the new page
            if None create a new Notch
        """
        # Create a new notch if needed
        if notch is None:
            self.obj.notch.append(
                NotchEvenDist(
                    alpha=0,
                    key_mat=None,
                    notch_shape=SlotM10(
                        Zs=self.obj.get_Zs(),
                        W0=None,
                        H0=None,
                    ),
                )
            )
            notch = self.obj.notch[-1]
            notch_index = len(self.obj.notch) - 1
        else:
            notch_index = idx_notch
        tab = WNotch(self, index=notch_index, material_dict=self.material_dict)
        tab.saveNeeded.connect(self.emit_save)
        self.tab_notch.addTab(tab, "Notch Set " + str(notch_index + 1))

    def s_remove(self, index):
        """Signal to remove the last notch

        Parameters
        ----------
        self : DNotchTab
            A DNotchTab widget
        """
        if len(self.obj.notch) > 1:
            self.tab_notch.removeTab(index)
            self.obj.notch.pop(index)

        # Make sure that the tab have the correct number in their name
        self.tab_notch.clear()
        for idx_notch, notch in enumerate(self.obj.notch):
            self.s_add(notch, idx_notch)
        self.tab_notch.setCurrentIndex(0)

    def s_plot(self):
        """Try to plot the lamination

        Parameters
        ----------
        self : DNotchTab
            a DNotchTab object
        """
        self.err_msg = None
        # We have to make sure the notches are right before trying to plot it
        error = self.check()
        if error:  # Error => Display it
            self.err_msg = "Error in Notch definition:\n" + error
            getLogger(GUI_LOG_NAME).debug(self.err_msg)
            QMessageBox().critical(self, self.tr("Error"), self.err_msg)
        else:  # No error => Plot the lamination
            try:
                self.obj.plot(is_show_fig=True)
                set_plot_gui_icon()
            except Exception as e:
                self.err_msg = (
                    "Error while plotting Lamination in Notch definition:\n" + str(e)
                )
                getLogger(GUI_LOG_NAME).error(self.err_msg)
                QMessageBox().critical(self, self.tr("Error"), self.err_msg)

    def check(self):
        """Check that the notches are correctly defined

        Parameters
        ----------
        self : DNotchTab
            A DNotchTab object

        Returns
        -------
        error : str
            Error message (return None if no error)
        """
        self.err_msg = None
        # Check that everything is set
        for ii in range(len(self.obj.notch)):
            try:
                wid = self.tab_notch.widget(ii)
                self.err_msg = wid.check()
                if self.err_msg is not None:
                    return "Notch " + str(ii + 1) + ": " + self.err_msg
            except SlotCheckError as error:
                return "Notch " + str(ii + 1) + ": " + str(error)

    def update_and_close(self):
        """Method called when clicking on ok button to check the machine before sending acceted signal

        Parameters
        ----------
        self : DNotchTab
            A DNotchTab object

        """
        self.err_msg = None
        error = None

        # We have to make sure the notches are correct before accepting it
        error = self.check()

        if error == None:
            try:
                self.obj.build_geometry()
            except NotchError as e:
                error = str(e)

        if error:  # Error => Display it
            self.err_msg = "Error in Notch definition:\n" + error
            getLogger(GUI_LOG_NAME).debug(self.err_msg)
            QMessageBox().critical(self, self.tr("Error"), self.err_msg)

        else:  # No error => modification accepted
            self.accept()
