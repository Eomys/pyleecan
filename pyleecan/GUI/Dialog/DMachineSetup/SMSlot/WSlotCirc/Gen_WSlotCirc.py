# -*- coding: utf-8 -*-
"""File generated according to WSlotCirc/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.WSlotCirc.Ui_WSlotCirc import Ui_WSlotCirc


class Gen_WSlotCirc(Ui_WSlotCirc):
    def setupUi(self, WSlotCirc):
        """Abstract class to update the widget according to the csv doc"""
        Ui_WSlotCirc.setupUi(self, WSlotCirc)
        # Setup of in_W0
        txt = self.tr(u"""Slot isthmus width.""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr(u"""Slot isthmus width.""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr(u"""Slot height""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr(u"""Slot height""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)
