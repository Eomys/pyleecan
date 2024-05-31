# -*- coding: utf-8 -*-
"""File generated according to PHoleM52R/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM52R.Ui_PHoleM52R import (
    Ui_PHoleM52R,
)


class Gen_PHoleM52R(Ui_PHoleM52R):
    def setupUi(self, PHoleM52R):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PHoleM52R.setupUi(self, PHoleM52R)
        # Setup of in_W0
        txt = self.tr("""Magnet width""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr("""Magnet width""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_W1
        txt = self.tr("""Void width""")
        self.in_W1.setWhatsThis(txt)
        self.in_W1.setToolTip(txt)

        # Setup of lf_W1
        self.lf_W1.validator().setBottom(0)
        txt = self.tr("""Void width""")
        self.lf_W1.setWhatsThis(txt)
        self.lf_W1.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr("""Slot depth""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr("""Slot depth""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)

        # Setup of in_H1
        txt = self.tr("""Magnet height""")
        self.in_H1.setWhatsThis(txt)
        self.in_H1.setToolTip(txt)

        # Setup of lf_H1
        self.lf_H1.validator().setBottom(0)
        txt = self.tr("""Magnet height""")
        self.lf_H1.setWhatsThis(txt)
        self.lf_H1.setToolTip(txt)

        # Setup of in_H2
        txt = self.tr("""Additional depth for the magnet""")
        self.in_H2.setWhatsThis(txt)
        self.in_H2.setToolTip(txt)

        # Setup of lf_H2
        self.lf_H2.validator().setBottom(0)
        txt = self.tr("""Additional depth for the magnet""")
        self.lf_H2.setWhatsThis(txt)
        self.lf_H2.setToolTip(txt)

        # Setup of in_R0
        txt = self.tr("""Void corner radius""")
        self.in_R0.setWhatsThis(txt)
        self.in_R0.setToolTip(txt)

        # Setup of lf_R0
        self.lf_R0.validator().setBottom(0)
        txt = self.tr("""Void corner radius""")
        self.lf_R0.setWhatsThis(txt)
        self.lf_R0.setToolTip(txt)
