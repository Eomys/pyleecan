# -*- coding: utf-8 -*-
"""File generated according to PVentUD/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.DAVDuct.PVentUD.Ui_PVentUD import Ui_PVentUD


class Gen_PVentUD(Ui_PVentUD):
    def setupUi(self, PVentUD):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PVentUD.setupUi(self, PVentUD)
        # Setup of in_Zh
        txt = self.tr(u"""Number of Hole around the circumference""")
        self.in_Zh.setWhatsThis(txt)
        self.in_Zh.setToolTip(txt)

        # Setup of si_Zh
        self.si_Zh.setMinimum(0)
        self.si_Zh.setMaximum(999999)
        txt = self.tr(u"""Number of Hole around the circumference""")
        self.si_Zh.setWhatsThis(txt)
        self.si_Zh.setToolTip(txt)
