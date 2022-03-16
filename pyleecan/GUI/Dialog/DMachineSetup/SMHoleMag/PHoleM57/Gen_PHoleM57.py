# -*- coding: utf-8 -*-
"""File generated according to PHoleM57/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM57.Ui_PHoleM57 import Ui_PHoleM57


class Gen_PHoleM57(Ui_PHoleM57):
    def setupUi(self, PHoleM57):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PHoleM57.setupUi(self, PHoleM57)
        # Setup of in_W0
        txt = self.tr("""V angle""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        self.lf_W0.validator().setTop(3.15)
        txt = self.tr("""V angle""")
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
        txt = self.tr("""Distance Magnet to top of the V""")
        self.in_W2.setWhatsThis(txt)
        self.in_W2.setToolTip(txt)

        # Setup of lf_W2
        self.lf_W2.validator().setBottom(0)
        txt = self.tr("""Distance Magnet to top of the V""")
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
        txt = self.tr("""Magnet height""")
        self.in_H2.setWhatsThis(txt)
        self.in_H2.setToolTip(txt)

        # Setup of lf_H2
        self.lf_H2.validator().setBottom(0)
        txt = self.tr("""Magnet height""")
        self.lf_H2.setWhatsThis(txt)
        self.lf_H2.setToolTip(txt)
