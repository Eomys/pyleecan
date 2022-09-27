# -*- coding: utf-8 -*-
"""File generated according to PBoreFlower/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.DBore.PBoreFlower.Ui_PBoreFlower import (
    Ui_PBoreFlower,
)


class Gen_PBoreFlower(Ui_PBoreFlower):
    def setupUi(self, PBoreFlower):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PBoreFlower.setupUi(self, PBoreFlower)
        # Setup of in_Rarc
        txt = self.tr(u"""Radius of the flower arc""")
        self.in_Rarc.setWhatsThis(txt)
        self.in_Rarc.setToolTip(txt)

        # Setup of lf_Rarc
        self.lf_Rarc.validator().setBottom(0)
        txt = self.tr(u"""Radius of the flower arc""")
        self.lf_Rarc.setWhatsThis(txt)
        self.lf_Rarc.setToolTip(txt)

        # Setup of in_alpha
        txt = self.tr(u"""Angular offset for the arc""")
        self.in_alpha.setWhatsThis(txt)
        self.in_alpha.setToolTip(txt)

        # Setup of lf_alpha
        txt = self.tr(u"""Angular offset for the arc""")
        self.lf_alpha.setWhatsThis(txt)
        self.lf_alpha.setToolTip(txt)
