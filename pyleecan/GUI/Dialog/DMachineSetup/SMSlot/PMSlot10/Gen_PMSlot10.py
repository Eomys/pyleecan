# -*- coding: utf-8 -*-
"""File generated according to PMSlot10/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.Ui_PMSlot10 import Ui_PMSlot10


class Gen_PMSlot10(Ui_PMSlot10):
    def setupUi(self, PMSlot10):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PMSlot10.setupUi(self, PMSlot10)
        # Setup of in_W0
        txt = self.tr("""Slot isthmus width.""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr("""Slot isthmus width.""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_W1
        txt = self.tr("""Magnet width""")
        self.in_W1.setWhatsThis(txt)
        self.in_W1.setToolTip(txt)

        # Setup of lf_W1
        self.lf_W1.validator().setBottom(0)
        txt = self.tr("""Magnet width""")
        self.lf_W1.setWhatsThis(txt)
        self.lf_W1.setToolTip(txt)

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
        txt = self.tr("""Magnet Height""")
        self.in_H1.setWhatsThis(txt)
        self.in_H1.setToolTip(txt)

        # Setup of lf_H1
        self.lf_H1.validator().setBottom(0)
        txt = self.tr("""Magnet Height""")
        self.lf_H1.setWhatsThis(txt)
        self.lf_H1.setToolTip(txt)
