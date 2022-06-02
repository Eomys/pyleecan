from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget
from numpy import pi
from ......Classes.LamSlot import LamSlot

from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.PMSlot10 import PMSlot10
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot11.PMSlot11 import PMSlot11
from ......GUI.Dialog.DMachineSetup.DNotch.WNotch.Ui_WNotch import Ui_WNotch


class WNotch(Ui_WNotch, QWidget):
    """Widget to Setup a single notch in a list"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()

    def __init__(self, parent, index):
        """Initialize the GUI according to lamination

        Parameters
        ----------
        self : WNotch
            A WNotch object
        parent :
            A parent object containing the lamination to edit
        index : int
            Index of the notch to edit
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.is_stator = False
        # Lamination to edit
        self.obj = parent.obj
        self.lam_notch = LamSlot(
            is_stator=self.obj.is_stator,
            is_internal=self.obj.is_internal,
            Rint=self.obj.Rint,
            Rext=self.obj.Rext,
        )
        self.lam_notch.slot = self.obj.notch[index].notch_shape
        self.index = index
        self.parent = parent

        # Adapt the GUI to the current machine
        self.wid_list = [PMSlot10, PMSlot11]

        self.type_list = [wid.slot_type for wid in self.wid_list]
        self.name_list = [wid.notch_name for wid in self.wid_list]

        # Avoid erase all the parameters when navigating though the notchs
        self.previous_notch = dict()
        for notch_type in self.type_list:
            self.previous_notch[notch_type] = None

        # Fill the combobox with the available notch
        self.c_notch_type.clear()
        for notch in self.name_list:
            self.c_notch_type.addItem(notch)
        self.c_notch_type.setCurrentIndex(
            self.type_list.index(type(self.obj.notch[index].notch_shape))
        )

        self.set_alpha_unit()
        self.si_Zs.setValue(self.lam_notch.slot.Zs)

        # Regenerate the pages with the new values
        self.w_notch.setParent(None)
        self.w_notch = self.wid_list[self.c_notch_type.currentIndex()](
            lamination=self.lam_notch, is_notch=True,
        )
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_notch)
        self.main_layout.insertWidget(1, self.w_notch)

        # Connect the slot
        self.c_notch_type.currentIndexChanged.connect(self.set_notch_type)
        self.si_Zs.editingFinished.connect(self.set_Zs)
        self.lf_alpha.editingFinished.connect(self.set_alpha)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def set_alpha(self):
        """Set alpha value according to widgets"""
        if self.c_alpha_unit.currentIndex() == 0:  # rad
            self.obj.notch[self.index].alpha = self.lf_alpha.value()
        else:  # deg
            self.obj.notch[self.index].alpha = self.lf_alpha.value() * 180 / pi

    def set_Zs(self):
        """Set the value of Zs"""
        self.lam_notch.slot.Zs = self.si_Zs.value()

    def set_alpha_unit(self):
        """Change the current unit of alpha"""
        self.lf_alpha.blockSignals(True)
        if self.c_alpha_unit.currentIndex() == 0:  # rad
            self.lf_alpha.setValue(self.obj.notch[self.index].alpha)
        else:
            self.lf_alpha.setValue(self.obj.notch[self.index].alpha * 180 / pi)
        self.lf_alpha.blockSignals(False)

    def set_notch_type(self, c_index):
        """Initialize self.obj with the notch corresponding to index

        Parameters
        ----------
        self : WNotch
            A WNotch object
        c_index : int
            Index of the selected notch type in the combobox
        """

        # Save the notch
        notch = self.lam_notch.slot
        self.previous_notch[type(notch)] = notch

        # Call the corresponding constructor
        if self.previous_notch[self.type_list[c_index]] is None:
            # No previous notch of this type
            self.lam_notch.slot = self.type_list[c_index]()
            self.lam_notch.slot._set_None()  # No default value
        else:  # Load the previous notch of this type
            self.lam_notch.slot = self.previous_notch[self.type_list[c_index]]
        self.set_alpha()
        self.set_Zs()

        # Update the GUI
        self.w_notch.setParent(None)
        self.w_notch = self.wid_list[c_index](lamination=self.lam_notch, is_notch=True,)
        self.w_notch.saveNeeded.connect(self.emit_save)
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_notch)
        self.main_layout.insertWidget(1, self.w_notch)

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : WnotchMag
            A WnotchMag widget

        Returns
        -------
        error : str
            Error message (return None if no error)
        """

        return self.w_notch.check()
