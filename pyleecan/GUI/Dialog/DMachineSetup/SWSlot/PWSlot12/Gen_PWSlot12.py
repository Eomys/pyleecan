# -*- coding: utf-8 -*-
"""File generated according to PWSlot12/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot12.Ui_PWSlot12 import Ui_PWSlot12


class Gen_PWSlot12(Ui_PWSlot12):
    def setupUi(self, PWSlot12):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PWSlot12.setupUi(self, PWSlot12)
        # Setup of in_R1
        txt = self.tr("""Wedges radius""")
        self.in_R1.setWhatsThis(txt)
        self.in_R1.setToolTip(txt)

        # Setup of lf_R1
        self.lf_R1.validator().setBottom(0)
        txt = self.tr("""Wedges radius""")
        self.lf_R1.setWhatsThis(txt)
        self.lf_R1.setToolTip(txt)

        # Setup of in_R2
        txt = self.tr("""Slot bottom radius""")
        self.in_R2.setWhatsThis(txt)
        self.in_R2.setToolTip(txt)

        # Setup of lf_R2
        self.lf_R2.validator().setBottom(0)
        txt = self.tr("""Slot bottom radius""")
        self.lf_R2.setWhatsThis(txt)
        self.lf_R2.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr("""Slot isthmus height.""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr("""Slot isthmus height.""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)

        # Setup of in_H1
        txt = self.tr("""Slot middle height""")
        self.in_H1.setWhatsThis(txt)
        self.in_H1.setToolTip(txt)

        # Setup of lf_H1
        self.lf_H1.validator().setBottom(0)
        txt = self.tr("""Slot middle height""")
        self.lf_H1.setWhatsThis(txt)
        self.lf_H1.setToolTip(txt)
