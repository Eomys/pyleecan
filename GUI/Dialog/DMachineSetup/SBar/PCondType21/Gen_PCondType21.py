# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from pyleecan.GUI.Dialog.DMachineSetup.SBar.PCondType21.Ui_PCondType21 import (
    Ui_PCondType21,
)


class Gen_PCondType21(Ui_PCondType21):
    def setupUi(self, PCondType21):
        Ui_PCondType21.setupUi(self, PCondType21)
        # Setup of w_mat
        txt = self.tr(u"""Material of the conductor""")
        self.w_mat.setWhatsThis(txt)
        self.w_mat.setToolTip(txt)

        # Setup of lf_Hbar
        self.lf_Hbar.validator().setBottom(0)
        txt = self.tr(u"""Bar height""")
        self.lf_Hbar.setWhatsThis(txt)
        self.lf_Hbar.setToolTip(txt)

        # Setup of in_Hbar
        txt = self.tr(u"""Bar height""")
        self.in_Hbar.setWhatsThis(txt)
        self.in_Hbar.setToolTip(txt)

        # Setup of in_Wbar
        txt = self.tr(u"""Bar width""")
        self.in_Wbar.setWhatsThis(txt)
        self.in_Wbar.setToolTip(txt)

        # Setup of lf_Wbar
        self.lf_Wbar.validator().setBottom(0)
        txt = self.tr(u"""Bar width""")
        self.lf_Wbar.setWhatsThis(txt)
        self.lf_Wbar.setToolTip(txt)
