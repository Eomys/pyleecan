# -*- coding: utf-8 -*-


from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMessageBox, QWidget
from logging import getLogger
from .....loggers import GUI_LOG_NAME
from .....GUI.Dialog.DMachineSetup.SPreview.Ui_SPreview import Ui_SPreview


class SPreview(Ui_SPreview, QWidget):
    """Step to define the winding conductor"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for DMachineSetup nav
    step_name = "Machine Summary"

    def __init__(self, machine, material_dict, is_stator=False):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SPreview
            A SPreview widget
        machine : Machine
            current machine to edit
        material_dict: dict
            Materials dictionary (library + machine)
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor  (unused)
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.machine = machine
        # Update the preview
        self.tab_machine.update_tab(self.machine)

        try:
            self.machine.plot(
                fig=self.w_plot.fig,
                ax=self.w_plot.axes,
                sym=1,
                alpha=0,
                delta=0,
                is_show_fig=False,
                is_max_sym=True,
            )
        except Exception as e:
            err_msg = "Error while plotting machine in Machine Summary:\n" + str(e)
            getLogger(GUI_LOG_NAME).error(err_msg)
            QMessageBox().critical(
                self,
                self.tr("Error"),
                err_msg,
            )
        self.w_plot.axes.set_axis_off()
        self.w_plot.axes.axis("equal")
        if self.w_plot.axes.get_legend() is not None:
            self.w_plot.axes.get_legend().remove()
        self.w_plot.draw()

    @staticmethod
    def check(machine):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        machine : Machine
            Machine to check

        Returns
        -------
        error : str
            Error message (return None if no error)

        """
        return None  # Nothing to check here

    # def resizeEvent(self, event):
    #     W_main = self.width() - self.tab_machine.width()
    #     H_main = self.tab_machine.height()
    #     Size = max(min(W_main, H_main), 300)
    #     self.w_plot.resize(Size, Size)
    #     return super(SPreview, self).resizeEvent(event)
