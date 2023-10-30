# -*- coding: utf-8 -*-
"""File generated according to PMSlot18/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot18.Ui_PMSlot18 import Ui_PMSlot18


class Gen_PMSlot18(Ui_PMSlot18):
    def setupUi(self, PMSlot18):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PMSlot18.setupUi(self, PMSlot18)
        # Setup of in_H0
        txt = self.tr(u"""Magnet Height""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr(u"""Magnet Height""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)
