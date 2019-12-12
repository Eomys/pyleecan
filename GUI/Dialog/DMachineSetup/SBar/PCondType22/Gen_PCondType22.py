# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from pyleecan.GUI.Dialog.DMachineSetup.SBar.PCondType22.Ui_PCondType22 import (
    Ui_PCondType22,
)


class Gen_PCondType22(Ui_PCondType22):
    def setupUi(self, PCondType22):
        Ui_PCondType22.setupUi(self, PCondType22)
        # Setup of w_mat
        txt = self.tr(u"""Material of the conductor""")
        self.w_mat.setWhatsThis(txt)
        self.w_mat.setToolTip(txt)
