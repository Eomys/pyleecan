# -*- coding: utf-8 -*-
"""File generated according to PCondType22/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SBar.PCondType22.Ui_PCondType22 import (
    Ui_PCondType22,
)


class Gen_PCondType22(Ui_PCondType22):
    def setupUi(self, PCondType22):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PCondType22.setupUi(self, PCondType22)
        # Setup of w_mat
        txt = self.tr("""Material of the conductor""")
        self.w_mat.setWhatsThis(txt)
        self.w_mat.setToolTip(txt)
