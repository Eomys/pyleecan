# -*- coding: utf-8 -*-

from numpy import pi
from PySide2.QtCore import Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget, QDialog
from PySide2.QtWidgets import QMessageBox
from PySide2.QtCore import Qt
from ......Functions.load import load
from ......Classes.SlotUD import SlotUD
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SWSlot.PWSlotUD.Ui_PWSlotUD import Ui_PWSlotUD
from ......GUI.Dialog.DMatLib.MatLib import MatLib
from ......Methods.Slot.Slot import SlotCheckError
from ......GUI.Dxf.DXF_Slot import DXF_Slot
from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect


class PWSlotUD(Ui_PWSlotUD, QWidget):
    """Page to set the slot from DXF"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for WslotMag
    slot_name = "Import from DXF"
    slot_type = SlotUD

    def __init__(self, lamination=None):
        """Initialize the widget according to lamination

        Parameters
        ----------
        self : PWSlotUD
            A PWSlotUD widget
        lamination : Lamination
            current lamination to edit
        """
        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Set properties
        self.lamination = lamination
        self.slot = lamination.slot
        self.u = gui_option.unit

        # Setup Path selector for Json files
        self.w_path_json.obj = None
        self.w_path_json.param_name = None
        self.w_path_json.verbose_name = "Load from json"
        self.w_path_json.extension = "JSON file (*.json)"
        self.w_path_json.update()

        # Update the GUI according to the current slot
        self.update_graph()
        self.w_out.comp_output()

        # Connect the signals
        self.b_dxf.clicked.connect(self.open_DXF_Slot)
        self.w_path_json.pathChanged.connect(self.load_slot)

    def update_graph(self):
        """Plot the lamination with/without the slot"""
        # Use a copy to avoid changing the main object
        lam = self.lamination.copy()
        try:
            self.slot.check()
            lam.slot = self.slot
        except SlotCheckError:
            # Plot only the lamination
            lam.slot = None
        # Plot the lamination in the viewer fig
        lam.plot(fig=self.w_viewer.fig, is_show_fig=False)

        # Update the Graph
        self.w_viewer.axes.set_axis_off()
        self.w_viewer.axes.axis("equal")
        if self.w_viewer.axes.get_legend() is not None:
            self.w_viewer.axes.get_legend().remove()
        self.w_viewer.draw()

    def load_slot(self):
        """Load the selected json file and display the slot"""
        # Check that the json file is correct
        try:
            slot = load(self.w_path_json.get_path())
        except Exception as e:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr("Error when loading file:\n" + str(e)),
            )
            return
        # Check that the json file contain a SlotUD
        if not isinstance(slot, SlotUD):
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr(
                    "The choosen file is not a SlotUD file (" + str(type(slot)) + ")"
                ),
            )
            return

        # Update the slot object
        Zs = self.slot.Zs
        parent = self.slot.parent
        self.slot.__init__(init_dict=slot.as_dict())  # keep pointer
        self.slot.Zs = Zs
        self.slot.parent = parent

        # Update the new GUI according to the slot
        self.update_graph()
        self.w_out.comp_output()

    def open_DXF_Slot(self):
        """Open the GUI to define the SlotUD"""
        # Init GUI with lamination parameters
        self.dxf_gui = DXF_Slot(Zs=self.slot.Zs, lam=self.lamination)
        self.dxf_gui.setWindowFlags(Qt.Window)  # To maximize the GUI
        self.dxf_gui.show()
        # Update the slot when saving
        self.dxf_gui.accepted.connect(self.set_dxf_path)

    def set_dxf_path(self):
        """Update the slot according to the file defined by DXF_Slot"""
        # Get the saving path from DXF_Slot
        self.w_path_json.set_path_txt(self.dxf_gui.save_path)
        # Update slot and GUI
        self.load_slot()
        self.dxf_gui = None

    @staticmethod
    def check(lam):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        lam: LamSlotWind
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Constraints
        try:
            lam.slot.check()
        except SlotCheckError as error:
            return str(error)

        # Output
        try:
            yoke_height = lam.comp_height_yoke()
        except Exception as error:
            return translate("Unable to compute yoke height:", "PWSlotUD") + str(error)

        if yoke_height <= 0:
            return translate(
                "The slot height is greater than the lamination !", "PWSlotUD"
            )

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()
