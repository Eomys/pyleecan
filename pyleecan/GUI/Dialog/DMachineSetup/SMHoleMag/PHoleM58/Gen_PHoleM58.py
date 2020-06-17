# -*- coding: utf-8 -*-
"""File generated according to PHoleM58/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM58.Ui_PHoleM58 import Ui_PHoleM58


class Gen_PHoleM58(Ui_PHoleM58):
    def setupUi(self, PHoleM58):
        """Abstract class to update the widget according to the csv doc
        """
        Ui_PHoleM58.setupUi(self, PHoleM58)
        # Setup of in_W0
        txt = self.tr(u"""Slot width""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr(u"""Slot width""")
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

        # Setup of in_W2
        txt = self.tr(u"""Distance Magnet to side of the notch""")
        self.in_W2.setWhatsThis(txt)
        self.in_W2.setToolTip(txt)

        # Setup of lf_W2
        self.lf_W2.validator().setBottom(0)
        txt = self.tr(u"""Distance Magnet to side of the notch""")
        self.lf_W2.setWhatsThis(txt)
        self.lf_W2.setToolTip(txt)

        # Setup of in_W3
        txt = self.tr(u"""Tooth angular opening width""")
        self.in_W3.setWhatsThis(txt)
        self.in_W3.setToolTip(txt)

        # Setup of lf_W3
        self.lf_W3.validator().setBottom(0)
        txt = self.tr(u"""Tooth angular opening width""")
        self.lf_W3.setWhatsThis(txt)
        self.lf_W3.setToolTip(txt)

        # Setup of in_R0
        txt = self.tr(u"""Notch radius""")
        self.in_R0.setWhatsThis(txt)
        self.in_R0.setToolTip(txt)

        # Setup of lf_R0
        self.lf_R0.validator().setBottom(0)
        txt = self.tr(u"""Notch radius""")
        self.lf_R0.setWhatsThis(txt)
        self.lf_R0.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr(u"""Slot depth""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr(u"""Slot depth""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)

        # Setup of in_H1
        txt = self.tr(u"""Distance from the lamination Bore""")
        self.in_H1.setWhatsThis(txt)
        self.in_H1.setToolTip(txt)

        # Setup of lf_H1
        self.lf_H1.validator().setBottom(0)
        txt = self.tr(u"""Distance from the lamination Bore""")
        self.lf_H1.setWhatsThis(txt)
        self.lf_H1.setToolTip(txt)

        # Setup of in_H2
        txt = self.tr(u"""Magnet Height""")
        self.in_H2.setWhatsThis(txt)
        self.in_H2.setToolTip(txt)

        # Setup of lf_H2
        self.lf_H2.validator().setBottom(0)
        txt = self.tr(u"""Magnet Height""")
        self.lf_H2.setWhatsThis(txt)
        self.lf_H2.setToolTip(txt)
