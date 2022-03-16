# -*- coding: utf-8 -*-
"""File generated according to PHoleM51/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM51.Ui_PHoleM51 import Ui_PHoleM51


class Gen_PHoleM51(Ui_PHoleM51):
    def setupUi(self, PHoleM51):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PHoleM51.setupUi(self, PHoleM51)
        # Setup of in_W0
        txt = self.tr("""Hole bottom width""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr("""Hole bottom width""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_W1
        txt = self.tr("""Hole angular width""")
        self.in_W1.setWhatsThis(txt)
        self.in_W1.setToolTip(txt)

        # Setup of lf_W1
        self.lf_W1.validator().setBottom(0)
        txt = self.tr("""Hole angular width""")
        self.lf_W1.setWhatsThis(txt)
        self.lf_W1.setToolTip(txt)

        # Setup of in_W3
        txt = self.tr("""magnet_1 width""")
        self.in_W3.setWhatsThis(txt)
        self.in_W3.setToolTip(txt)

        # Setup of lf_W3
        self.lf_W3.validator().setBottom(0)
        txt = self.tr("""magnet_1 width""")
        self.lf_W3.setWhatsThis(txt)
        self.lf_W3.setToolTip(txt)

        # Setup of in_W4
        txt = self.tr("""magnet_2 position""")
        self.in_W4.setWhatsThis(txt)
        self.in_W4.setToolTip(txt)

        # Setup of lf_W4
        self.lf_W4.validator().setBottom(0)
        txt = self.tr("""magnet_2 position""")
        self.lf_W4.setWhatsThis(txt)
        self.lf_W4.setToolTip(txt)

        # Setup of in_W5
        txt = self.tr("""magnet_2 width""")
        self.in_W5.setWhatsThis(txt)
        self.in_W5.setToolTip(txt)

        # Setup of lf_W5
        self.lf_W5.validator().setBottom(0)
        txt = self.tr("""magnet_2 width""")
        self.lf_W5.setWhatsThis(txt)
        self.lf_W5.setToolTip(txt)

        # Setup of in_W6
        txt = self.tr("""magnet_0 position""")
        self.in_W6.setWhatsThis(txt)
        self.in_W6.setToolTip(txt)

        # Setup of lf_W6
        self.lf_W6.validator().setBottom(0)
        txt = self.tr("""magnet_0 position""")
        self.lf_W6.setWhatsThis(txt)
        self.lf_W6.setToolTip(txt)

        # Setup of in_W7
        txt = self.tr("""magnet_0 width""")
        self.in_W7.setWhatsThis(txt)
        self.in_W7.setToolTip(txt)

        # Setup of lf_W7
        self.lf_W7.validator().setBottom(0)
        txt = self.tr("""magnet_0 width""")
        self.lf_W7.setWhatsThis(txt)
        self.lf_W7.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr("""Hole depth""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr("""Hole depth""")
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
        txt = self.tr("""Hole width""")
        self.in_H2.setWhatsThis(txt)
        self.in_H2.setToolTip(txt)

        # Setup of lf_H2
        self.lf_H2.validator().setBottom(0)
        txt = self.tr("""Hole width""")
        self.lf_H2.setWhatsThis(txt)
        self.lf_H2.setToolTip(txt)
