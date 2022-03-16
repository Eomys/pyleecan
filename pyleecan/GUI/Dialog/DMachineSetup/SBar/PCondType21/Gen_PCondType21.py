# -*- coding: utf-8 -*-
"""File generated according to PCondType21/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SBar.PCondType21.Ui_PCondType21 import (
    Ui_PCondType21,
)


class Gen_PCondType21(Ui_PCondType21):
    def setupUi(self, PCondType21):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PCondType21.setupUi(self, PCondType21)
        # Setup of w_mat
        txt = self.tr("""Material of the conductor""")
        self.w_mat.setWhatsThis(txt)
        self.w_mat.setToolTip(txt)

        # Setup of lf_Hbar
        self.lf_Hbar.validator().setBottom(0)
        txt = self.tr("""Bar height""")
        self.lf_Hbar.setWhatsThis(txt)
        self.lf_Hbar.setToolTip(txt)

        # Setup of in_Hbar
        txt = self.tr("""Bar height""")
        self.in_Hbar.setWhatsThis(txt)
        self.in_Hbar.setToolTip(txt)

        # Setup of in_Wbar
        txt = self.tr("""Bar width""")
        self.in_Wbar.setWhatsThis(txt)
        self.in_Wbar.setToolTip(txt)

        # Setup of lf_Wbar
        self.lf_Wbar.validator().setBottom(0)
        txt = self.tr("""Bar width""")
        self.lf_Wbar.setWhatsThis(txt)
        self.lf_Wbar.setToolTip(txt)
