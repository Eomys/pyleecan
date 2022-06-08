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

        # Setup of in_Zn
        txt = self.tr(u"""slot number""")
        self.in_Zn.setWhatsThis(txt)
        self.in_Zn.setToolTip(txt)

        # Setup of si_Zn
        self.si_Zn.setMinimum(0)
        self.si_Zn.setMaximum(999999)
        txt = self.tr(u"""slot number""")
        self.si_Zn.setWhatsThis(txt)
        self.si_Zn.setToolTip(txt)
