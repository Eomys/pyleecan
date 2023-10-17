# -*- coding: utf-8 -*-
"""File generated according to PMSlot13/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot13.Ui_PMSlot13 import Ui_PMSlot13


class Gen_PMSlot13(Ui_PMSlot13):
    def setupUi(self, PMSlot13):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PMSlot13.setupUi(self, PMSlot13)
        # Setup of in_W0
        txt = self.tr(u"""Slot isthmus width.""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr(u"""Slot isthmus width.""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_W1
        txt = self.tr(u"""Magnet width""")
        self.in_W1.setWhatsThis(txt)
        self.in_W1.setToolTip(txt)

        # Setup of lf_W1
        self.lf_W1.validator().setBottom(0)
        txt = self.tr(u"""Magnet width""")
        self.lf_W1.setWhatsThis(txt)
        self.lf_W1.setToolTip(txt)

        # Setup of in_Rtopm
        txt = self.tr(u"""Radius of the magnet top""")
        self.in_Rtopm.setWhatsThis(txt)
        self.in_Rtopm.setToolTip(txt)

        # Setup of lf_Rtopm
        self.lf_Rtopm.validator().setBottom(0)
        txt = self.tr(u"""Radius of the magnet top""")
        self.lf_Rtopm.setWhatsThis(txt)
        self.lf_Rtopm.setToolTip(txt)

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
        txt = self.tr(u"""Magnet Height""")
        self.in_H1.setWhatsThis(txt)
        self.in_H1.setToolTip(txt)

        # Setup of lf_H1
        self.lf_H1.validator().setBottom(0)
        txt = self.tr(u"""Magnet Height""")
        self.lf_H1.setWhatsThis(txt)
        self.lf_H1.setToolTip(txt)
