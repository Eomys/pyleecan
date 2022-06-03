# -*- coding: utf-8 -*-
"""File generated according to WNotch/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.DNotchTab.WNotch.Ui_WNotch import Ui_WNotch


class Gen_WNotch(Ui_WNotch):
    def setupUi(self, WNotch):
        """Abstract class to update the widget according to the csv doc"""
        Ui_WNotch.setupUi(self, WNotch)
        # Setup of in_alpha
        txt = self.tr(
            u"""angular positon of the first notch (0 is middle of first tooth)"""
        )
        self.in_alpha.setWhatsThis(txt)
        self.in_alpha.setToolTip(txt)

        # Setup of lf_alpha
        txt = self.tr(
            u"""angular positon of the first notch (0 is middle of first tooth)"""
        )
        self.lf_alpha.setWhatsThis(txt)
        self.lf_alpha.setToolTip(txt)

        # Setup of in_Zs
        txt = self.tr(u"""slot number""")
        self.in_Zs.setWhatsThis(txt)
        self.in_Zs.setToolTip(txt)

        # Setup of si_Zs
        self.si_Zs.setMinimum(0)
        self.si_Zs.setMaximum(999999)
        txt = self.tr(u"""slot number""")
        self.si_Zs.setWhatsThis(txt)
        self.si_Zs.setToolTip(txt)
