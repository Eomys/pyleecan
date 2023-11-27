# -*- coding: utf-8 -*-
"""File generated according to PWSlot30/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot30.Ui_PWSlot30 import Ui_PWSlot30


class Gen_PWSlot30(Ui_PWSlot30):
    def setupUi(self, PWSlot30):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PWSlot30.setupUi(self, PWSlot30)
        # Setup of in_W0
        txt = self.tr(u"""Slot isthmus width.""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr(u"""Slot isthmus width.""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_W3
        txt = self.tr(u"""Tooth width""")
        self.in_W3.setWhatsThis(txt)
        self.in_W3.setToolTip(txt)

        # Setup of lf_W3
        self.lf_W3.validator().setBottom(0)
        txt = self.tr(u"""Tooth width""")
        self.lf_W3.setWhatsThis(txt)
        self.lf_W3.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr(u"""Slot isthmus height.""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr(u"""Slot isthmus height.""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)

        # Setup of in_H1
        txt = self.tr(u"""Slot active height.""")
        self.in_H1.setWhatsThis(txt)
        self.in_H1.setToolTip(txt)

        # Setup of lf_H1
        self.lf_H1.validator().setBottom(0)
        txt = self.tr(u"""Slot active height.""")
        self.lf_H1.setWhatsThis(txt)
        self.lf_H1.setToolTip(txt)

        # Setup of in_R1
        txt = self.tr(u"""Top radius""")
        self.in_R1.setWhatsThis(txt)
        self.in_R1.setToolTip(txt)

        # Setup of lf_R1
        self.lf_R1.validator().setBottom(0)
        txt = self.tr(u"""Top radius""")
        self.lf_R1.setWhatsThis(txt)
        self.lf_R1.setToolTip(txt)

        # Setup of in_R2
        txt = self.tr(u"""Bottom radius""")
        self.in_R2.setWhatsThis(txt)
        self.in_R2.setToolTip(txt)

        # Setup of lf_R2
        self.lf_R2.validator().setBottom(0)
        txt = self.tr(u"""Bottom radius""")
        self.lf_R2.setWhatsThis(txt)
        self.lf_R2.setToolTip(txt)
