# -*- coding: utf-8 -*-
"""File generated according to PHoleM50/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM50.Ui_PHoleM50 import Ui_PHoleM50


class Gen_PHoleM50(Ui_PHoleM50):
    def setupUi(self, PHoleM50):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PHoleM50.setupUi(self, PHoleM50)
        # Setup of in_W0
        txt = self.tr("""Slot opening""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr("""Slot opening""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_W1
        txt = self.tr("""Tooth width (at V bottom)""")
        self.in_W1.setWhatsThis(txt)
        self.in_W1.setToolTip(txt)

        # Setup of lf_W1
        self.lf_W1.validator().setBottom(0)
        txt = self.tr("""Tooth width (at V bottom)""")
        self.lf_W1.setWhatsThis(txt)
        self.lf_W1.setToolTip(txt)

        # Setup of in_W2
        txt = self.tr("""Distance Magnet to bottom of the V""")
        self.in_W2.setWhatsThis(txt)
        self.in_W2.setToolTip(txt)

        # Setup of lf_W2
        self.lf_W2.validator().setBottom(0)
        txt = self.tr("""Distance Magnet to bottom of the V""")
        self.lf_W2.setWhatsThis(txt)
        self.lf_W2.setToolTip(txt)

        # Setup of in_W3
        txt = self.tr("""Tooth width (at V top)""")
        self.in_W3.setWhatsThis(txt)
        self.in_W3.setToolTip(txt)

        # Setup of lf_W3
        self.lf_W3.validator().setBottom(0)
        txt = self.tr("""Tooth width (at V top)""")
        self.lf_W3.setWhatsThis(txt)
        self.lf_W3.setToolTip(txt)

        # Setup of in_W4
        txt = self.tr("""Magnet Width""")
        self.in_W4.setWhatsThis(txt)
        self.in_W4.setToolTip(txt)

        # Setup of lf_W4
        self.lf_W4.validator().setBottom(0)
        txt = self.tr("""Magnet Width""")
        self.lf_W4.setWhatsThis(txt)
        self.lf_W4.setToolTip(txt)

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
        txt = self.tr("""Distance from the lamination Bore""")
        self.in_H1.setWhatsThis(txt)
        self.in_H1.setToolTip(txt)

        # Setup of lf_H1
        self.lf_H1.validator().setBottom(0)
        txt = self.tr("""Distance from the lamination Bore""")
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

        # Setup of in_H3
        txt = self.tr("""Magnet Height""")
        self.in_H3.setWhatsThis(txt)
        self.in_H3.setToolTip(txt)

        # Setup of lf_H3
        self.lf_H3.validator().setBottom(0)
        txt = self.tr("""Magnet Height""")
        self.lf_H3.setWhatsThis(txt)
        self.lf_H3.setToolTip(txt)

        # Setup of in_H4
        txt = self.tr("""Slot top height""")
        self.in_H4.setWhatsThis(txt)
        self.in_H4.setToolTip(txt)

        # Setup of lf_H4
        self.lf_H4.validator().setBottom(0)
        txt = self.tr("""Slot top height""")
        self.lf_H4.setWhatsThis(txt)
        self.lf_H4.setToolTip(txt)
