# -*- coding: utf-8 -*-


from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMessageBox, QWidget, QDialog
from logging import getLogger


from .....loggers import GUI_LOG_NAME
from .....Methods.Slot.Slot import SlotCheckError
from .....GUI.Dialog.DMachineSetup.DNotch.WNotch.WNotch import WNotch
from .....GUI.Dialog.DMachineSetup.DNotch.Ui_DNotchTab import Ui_DNotchTab
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.PMSlot10 import PMSlot10
from .....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon
from .....Classes.NotchEvenDist import NotchEvenDist
from .....Classes.SlotM10 import SlotM10


class DNotchTab(Ui_DNotchTab, QDialog):
    """Step to set several notches"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()

    def __init__(self, machine, is_stator=False):
        """Initialize the widget according to machine

        Parameters
        ----------
        self : DNotchTab
            A DNotchTab widget
        machine : Machine
            current machine to edit
        material_dict: dict
            Materials dictionary (library + machine)
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        """
        # Build the interface according to the .ui file
        QDialog.__init__(self)
        self.setupUi(self)

        # Saving arguments
        self.machine = machine
        self.is_stator = is_stator

        # Get the correct object to set
        if self.is_stator:
            self.obj = machine.stator
        else:
            self.obj = machine.rotor
        if self.obj.notch is None:
            self.obj.notch = list()

        # Update all the notch tab
        # (the current notches types will be initialized)
        self.tab_notch.clear()
        for notch in self.obj.notch:
            self.s_add(notch)
        self.tab_notch.setCurrentIndex(0)

        # Set Help URL
        # self.b_help.hide()

        # Connect the slot
        self.b_add.clicked.connect(lambda: self.s_add())
        self.b_remove.clicked.connect(self.s_remove)
        self.b_ok.clicked.connect(self.accept)
        self.b_cancel.clicked.connect(self.reject)
        # self.b_plot.clicked.connect(self.s_plot)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def s_add(self, notch=None):
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
                NotchEvenDist(alpha=0, notch_shape=SlotM10(Zs=self.obj.get_Zs()))
            )
            notch = self.obj.notch[-1]
            notch_index = len(self.obj.notch) - 1
        else:
            notch_index = self.obj.notch.index(notch)
        tab = WNotch(self, index=notch_index)
        tab.saveNeeded.connect(self.emit_save)
        self.tab_notch.addTab(tab, "notch " + str(notch_index + 1))

    def s_remove(self):
        """Signal to remove the last notch

        Parameters
        ----------
        self : DNotchTab
            A DNotchTab widget
        """
        if len(self.obj.notch) > 1:
            self.tab_notch.removeTab(len(self.obj.notch) - 1)
            self.obj.notch.pop(-1)

    def s_plot(self):
        """Try to plot the lamination

        Parameters
        ----------
        self : DNotchTab
            A DNotchTab widget
        """
        pass

    @staticmethod
    def check(lamination):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        lamination : Lamination
            Lamination to check

        Returns
        -------
        error : str
            Error message (return None if no error)
        """

        # Check that everything is set
        for notch in lamination.notch:
            try:
                notch.check()
            except SlotCheckError as error:
                return str(error)
