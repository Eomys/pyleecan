# -*- coding: utf-8 -*-
"""File generated according to SlotCirc/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.SlotCirc.Ui_SlotCirc import Ui_SlotCirc


class Gen_SlotCirc(Ui_SlotCirc):
    def setupUi(self, SlotCirc):
        """Abstract class to update the widget according to the csv doc"""
        Ui_SlotCirc.setupUi(self, SlotCirc)
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
