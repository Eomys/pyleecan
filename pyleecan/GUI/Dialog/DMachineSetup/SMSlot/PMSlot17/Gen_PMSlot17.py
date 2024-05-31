# -*- coding: utf-8 -*-
"""File generated according to PMSlot17/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot17.Ui_PMSlot17 import Ui_PMSlot17


class Gen_PMSlot17(Ui_PMSlot17):
    def setupUi(self, PMSlot17):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PMSlot17.setupUi(self, PMSlot17)
        # Setup of in_Lmag
        txt = self.tr("""Magnet axial length""")
        self.in_Lmag.setWhatsThis(txt)
        self.in_Lmag.setToolTip(txt)

        # Setup of lf_Lmag
        self.lf_Lmag.validator().setBottom(0)
        txt = self.tr("""Magnet axial length""")
        self.lf_Lmag.setWhatsThis(txt)
        self.lf_Lmag.setToolTip(txt)
