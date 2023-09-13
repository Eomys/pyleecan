# -*- coding: utf-8 -*-
"""File generated according to PWSlot26/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot26.Ui_PWSlot26 import Ui_PWSlot26


class Gen_PWSlot26(Ui_PWSlot26):
    def setupUi(self, PWSlot26):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PWSlot26.setupUi(self, PWSlot26)
        # Setup of in_W0
        txt = self.tr("""Slot isthmus width.""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr("""Slot isthmus width.""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

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
        txt = self.tr("""Slot depth """)
        self.in_H1.setWhatsThis(txt)
        self.in_H1.setToolTip(txt)

        # Setup of lf_H1
        self.lf_H1.validator().setBottom(0)
        txt = self.tr("""Slot depth """)
        self.lf_H1.setWhatsThis(txt)
        self.lf_H1.setToolTip(txt)

        # Setup of in_R1
        txt = self.tr("""Slot edge radius""")
        self.in_R1.setWhatsThis(txt)
        self.in_R1.setToolTip(txt)

        # Setup of lf_R1
        self.lf_R1.validator().setBottom(0)
        txt = self.tr("""Slot edge radius""")
        self.lf_R1.setWhatsThis(txt)
        self.lf_R1.setToolTip(txt)

        # Setup of in_R2
        txt = self.tr("""Slot top radius""")
        self.in_R2.setWhatsThis(txt)
        self.in_R2.setToolTip(txt)

        # Setup of lf_R2
        self.lf_R2.validator().setBottom(0)
        txt = self.tr("""Slot top radius""")
        self.lf_R2.setWhatsThis(txt)
        self.lf_R2.setToolTip(txt)
