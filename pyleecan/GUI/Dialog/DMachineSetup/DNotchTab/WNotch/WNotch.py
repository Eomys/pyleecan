from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget, QMessageBox
from numpy import pi
from logging import getLogger

from ......loggers import GUI_LOG_NAME

from ......Classes.LamSlot import LamSlot

from ......GUI.Dialog.DMachineSetup.SWSlot.PWSlotUD.PWSlotUD import PWSlotUD
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.PMSlot10 import PMSlot10
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot11.PMSlot11 import PMSlot11
from ......GUI.Dialog.DMachineSetup.SMSlot.WSlotCirc.WSlotCirc import WSlotCirc
from ......GUI.Dialog.DMachineSetup.DNotchTab.WNotch.Ui_WNotch import Ui_WNotch


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

        # Adding tooltip + setting the min and max value for si_Zn
        txt = self.tr("""notch number""")
        self.in_Zn.setWhatsThis(txt)
        self.in_Zn.setToolTip(txt)
        self.si_Zn.setWhatsThis(txt)
        self.si_Zn.setToolTip(txt)
        self.si_Zn.setMinimum(0)
        self.si_Zn.setMaximum(999999)

        if self.obj.is_stator:
            txt = self.tr(
                """angular position of the first notch (0 is middle of first tooth)"""
            )
        else:
            txt = self.tr("""angular position of the first notch""")
        self.in_alpha.setWhatsThis(txt)
        self.in_alpha.setToolTip(txt)
        self.lf_alpha.setWhatsThis(txt)
        self.lf_alpha.setToolTip(txt)

        # String storing the last error message (used in test)
        self.err_msg = None

        # Adapt the GUI to the current machine
        self.wid_list = [PMSlot10, PMSlot11, WSlotCirc, PWSlotUD]

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
        self.si_Zn.setValue(self.lam_notch.slot.Zs)

        # Regenerate the pages with the new values
        self.w_notch.setParent(None)
        self.w_notch = self.wid_list[self.c_notch_type.currentIndex()](
            lamination=self.lam_notch,
            is_notch=True,
        )
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_notch)
        self.main_layout.insertWidget(1, self.w_notch)

        # Connect the slot
        self.c_notch_type.currentIndexChanged.connect(self.set_notch_type)
        self.si_Zn.editingFinished.connect(self.set_Zn)
        self.lf_alpha.editingFinished.connect(self.set_alpha)
        self.c_alpha_unit.currentIndexChanged.connect(self.set_alpha_unit)
        self.b_plot.clicked.connect(self.preview_notch)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def preview_notch(self):
        """Preview the notch on the lamination"""
        self.err_msg = None
        error = self.check()
        if error:  # Error => Display it
            self.err_msg = "Unable to generate a preview:\n" + error
            getLogger(GUI_LOG_NAME).debug(self.err_msg)
            QMessageBox().critical(self, self.tr("Error"), self.err_msg)
        else:
            # No error in the definition of the notche => the preview should be generated
            self.obj.plot_preview_notch(index=self.index)

    def set_alpha(self):
        """Set alpha value according to widgets"""
        if self.lf_alpha.value() == None:
            self.lf_alpha.setValue(0)
        if self.c_alpha_unit.currentIndex() == 0:  # rad
            self.obj.notch[self.index].alpha = self.lf_alpha.value()
        else:  # deg
            self.obj.notch[self.index].alpha = self.lf_alpha.value() * pi / 180
        if isinstance(self.w_notch, PWSlotUD):
            self.w_notch.update_graph()

    def set_Zn(self):
        """Set the value of Zn"""
        self.lam_notch.slot.Zs = self.si_Zn.value()
        if isinstance(self.w_notch, PWSlotUD):
            self.w_notch.update_graph()

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
            self.lam_notch.slot._set_None()  # Clear default value
        else:  # Load the previous notch of this type
            self.lam_notch.slot = self.previous_notch[self.type_list[c_index]]
        self.lam_notch.slot.is_bore = True  # Default value
        self.set_alpha()
        self.set_Zn()
        self.obj.notch[self.index].notch_shape = self.lam_notch.slot

        # Update the GUI
        self.w_notch.setParent(None)
        self.w_notch = self.wid_list[c_index](
            lamination=self.lam_notch,
            is_notch=True,
        )
        self.w_notch.saveNeeded.connect(self.emit_save)
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_notch)
        self.main_layout.insertWidget(1, self.w_notch)
        # Update Zs for PWSlotUD
        if isinstance(self.w_notch, PWSlotUD):
            self.w_notch.ZsChanged.connect(self.set_Zs_UD)
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Zs_UD(self):
        self.si_Zn.blockSignals(True)
        self.si_Zn.setValue(self.w_notch.slot.Zs)
        self.si_Zn.blockSignals(False)

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

        if not isinstance(self.w_notch, PWSlotUD):
            # Check that the user did not define a notch a dimension equal to 0
            if self.w_notch.lf_W0.value() is None:
                return "You must set W0 !"
            elif self.w_notch.lf_W0.value() <= 0:
                return "W0 must be higher than 0"
            if self.w_notch.lf_H0.value() is None:
                return "You must set H0 !"
            if self.w_notch.lf_H0.value() <= 0:
                return "H0 must be higher than 0"

        return self.w_notch.check(self.lam_notch)
