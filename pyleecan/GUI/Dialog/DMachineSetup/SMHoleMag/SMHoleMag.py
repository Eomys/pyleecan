# -*- coding: utf-8 -*-


from qtpy.QtCore import Signal
from qtpy.QtWidgets import QMessageBox, QWidget, QSizePolicy
from logging import getLogger
from .....loggers import GUI_LOG_NAME
from .....Classes.HoleM50 import HoleM50
from .....Classes.Material import Material
from .....GUI.Dialog.DMachineSetup.SMHoleMag.Ui_SMHoleMag import Ui_SMHoleMag
from .....GUI.Dialog.DMachineSetup.SMHoleMag.WHoleMag.WHoleMag import WHoleMag
from .....Methods.Slot.Slot import SlotCheckError
from .....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon
from numpy import pi


class SMHoleMag(Ui_SMHoleMag, QWidget):
    """Step to set several Holes"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for DMachineSetup
    step_name = "Hole"

    def __init__(self, machine, material_dict, is_stator=False):
        """Initialize the widget according to machine

        Parameters
        ----------
        self : SMHoleMag
            A SMHoleMag widget
        machine : Machine
            current machine to edit
        material_dict: dict
            Materials dictionary (library + machine)
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        """
        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Saving arguments
        self.machine = machine
        self.material_dict = material_dict
        self.is_stator = is_stator
        self.is_test = False  # True to hide the plots
        self.test_err_msg = None  # To test the error messages

        # Get the correct object to set
        if self.is_stator:
            self.obj = machine.stator
        else:
            self.obj = machine.rotor
        if self.obj.hole is None:
            self.obj.hole = list()

        # If the hole is not set, initialize it with a HoleM50
        if len(self.obj.hole) == 0:
            self.obj.hole.append(HoleM50())
            if self.machine.type_machine == 5:  # SyRM
                self.obj.hole[0].remove_magnet()
            self.obj.hole[0]._set_None()
            self.obj.hole[0].Zh = machine.stator.winding.p * 2  # Default value
        self.set_hole_pitch(self.obj.hole[0].Zh)

        # Update all the hole tab
        # (the current hole types will be initialized)
        # print(type(self.obj.hole[0]).__name__)
        self.tab_hole.clear()
        for hole in self.obj.hole:
            self.s_add(hole)
        self.tab_hole.setCurrentIndex(0)

        # Set Help URL
        self.b_help.hide()

        # Connect the slot
        self.tab_hole.tabCloseRequested.connect(self.s_remove)
        self.b_add.clicked.connect(lambda: self.s_add(hole=None))

        self.b_plot.clicked.connect(self.s_plot)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def set_hole_pitch(self, Zh):
        """Update out_hole_pitch with the correct value

        Parameters
        ----------
        self : SMHoleMag
            A SMHoleMag object
        Zh : int
            The current value of Zh
        """
        Zh_txt = self.tr("Slot pitch: 360 / 2p = ")
        if Zh in [None, 0]:
            self.out_hole_pitch.setText(Zh_txt + "?")
        else:
            hole_pitch = 360.0 / Zh
            self.out_hole_pitch.setText(
                Zh_txt
                + "%.4g" % (hole_pitch)
                + " [°] = "
                + "%.4g" % (hole_pitch * pi / 180)
                + " [rad]"
            )

    def s_add(self, hole=None):
        """Signal to add a new hole

        Parameters
        ----------
        self : SMHoleMag
            a SMHoleMag object
        hole : HoleMag
            hole to initialize in the new page
            if None create a new empty HoleM50
        """
        # Adapt the GUI according to the machine type
        if self.machine.type_machine == 5:  # SyRM
            is_mag = False
        else:
            is_mag = True
        # Create a new hole if needed
        if hole is None:
            self.obj.hole.append(HoleM50())
            hole = self.obj.hole[-1]
            hole._set_None()
            hole_index = len(self.obj.hole) - 1
            if self.machine.type_machine == 5:
                hole.remove_magnet()
            else:
                hole.set_magnet_by_id(0, self.obj.hole[0].get_magnet_by_id(0))
            hole.Zh = self.obj.hole[0].Zh
        else:
            hole_index = self.obj.hole.index(hole)
        tab = WHoleMag(
            self, is_mag=is_mag, index=hole_index, material_dict=self.material_dict
        )
        tab.saveNeeded.connect(self.emit_save)
        self.tab_hole.addTab(tab, "Hole Set " + str(hole_index + 1))

    def s_remove(self, index):
        """Signal to remove the last hole

        Parameters
        ----------
        self : SMHoleMag
            a SMHoleMag object
        """
        if len(self.obj.hole) > 1:
            self.tab_hole.removeTab(index)
            self.obj.hole.pop(index)

            self.emit_save()
        else:
            QMessageBox().warning(
                self,
                self.tr("Warning"),
                "Impossible to remove the hole as it is the last one defined",
            )
            return

    def s_plot(self):
        """Try to plot the lamination

        Parameters
        ----------
        self : SMHoleMag
            a SMHoleMag object
        """
        # Update p
        for hole in self.obj.hole:
            hole.Zh = self.machine.stator.winding.p * 2
        self.set_hole_pitch(self.obj.hole[0].Zh)

        # We have to make sure the hole is right before trying to plot it
        error = self.check(self.obj)
        if error:  # Error => Display it
            self.test_err_msg = "Error in Hole definition:\n" + error
            getLogger(GUI_LOG_NAME).debug(self.test_err_msg)
            QMessageBox().critical(self, self.tr("Error"), self.test_err_msg)
        else:  # No error => Plot the lamination
            try:
                self.obj.plot(is_show_fig=not self.is_test)
                set_plot_gui_icon()
            except Exception as e:
                self.test_err_msg = (
                    "Error while plotting Lamination in Hole definition:\n" + str(e)
                )
                getLogger(GUI_LOG_NAME).error(self.test_err_msg)
                QMessageBox().critical(self, self.tr("Error"), self.test_err_msg)

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
        for hole in lamination.hole:
            try:
                hole.check()
            except SlotCheckError as error:
                return str(error)
