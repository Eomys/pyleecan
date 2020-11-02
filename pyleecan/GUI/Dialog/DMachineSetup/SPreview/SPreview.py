# -*- coding: utf-8 -*-


from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMessageBox, QWidget


from .....GUI.Dialog.DMachineSetup.SPreview.Ui_SPreview import Ui_SPreview


class SPreview(Ui_SPreview, QWidget):
    """Step to define the winding conductor"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for DMachineSetup nav
    step_name = "Machine Summary"

    def __init__(self, machine, matlib, is_stator=False):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SPreview
            A SPreview widget
        machine : Machine
            current machine to edit
        matlib : MatLib
            Material Library
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.machine = machine
        # Update the preview
        self.tab_machine.update_tab(self.machine)

        self.machine.plot(
            fig=self.w_plot.fig,
            ax=self.w_plot.axes,
            sym=1,
            alpha=0,
            delta=0,
            is_show_fig=False,
        )
        self.w_plot.axes.set_axis_off()
        if self.w_plot.axes.get_legend() is not None:
            self.w_plot.axes.get_legend().remove()
        self.w_plot.draw()

    # def resizeEvent(self, event):
    #     W_main = self.width() - self.tab_machine.width()
    #     H_main = self.tab_machine.height()
    #     Size = max(min(W_main, H_main), 300)
    #     self.w_plot.resize(Size, Size)
    #     return super(SPreview, self).resizeEvent(event)
