# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from ......GUI.Dialog.DMachineSetup.SPreview.WMachineTable.Ui_WMachineTable import (
    Ui_WMachineTable,
)
import matplotlib.pyplot as plt


class WMachineTable(Ui_WMachineTable, QWidget):
    """Table to display the main paramaters of the machine
    """

    def __init__(self, parent=None):
        """Initialize the GUI

        Parameters
        ----------
        self : SWindCond
            A SWindCond widget
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.machine = None

        # Connect the widget
        self.b_mmf.clicked.connect(self.plot_mmf)

    def update_tab(self, machine):
        """Update the table to match the machine

        Parameters
        ----------
        self : WMachineTable
            A WMachineTable object
        """

        self.machine = machine
        desc_dict = self.machine.comp_desc_dict()

        self.tab_param.clear()
        # Set header
        self.tab_param.setColumnCount(2)
        item = QTableWidgetItem("Name")
        self.tab_param.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem("Value")
        self.tab_param.setHorizontalHeaderItem(1, item)
        # Set containt
        for ii, desc in enumerate(desc_dict):
            if desc["value"] is not None:
                self.tab_param.insertRow(ii)
                self.tab_param.setItem(ii, 0, QTableWidgetItem(desc["verbose"]))
                if desc["type"] is float:
                    txt = format(desc["value"], ".4g")
                else:
                    txt = str(desc["value"])
                if desc["unit"] not in ["", None]:
                    txt += " " + desc["unit"]
                self.tab_param.setItem(ii, 1, QTableWidgetItem(txt))

    def plot_mmf(self):
        """Plot the unit mmf of the stator
        """
        if self.machine is not None:
            fig, axes = plt.subplots()
            axes.set_visible(False)
            self.machine.stator.plot_mmf_unit(fig=fig)
            fig.show()
