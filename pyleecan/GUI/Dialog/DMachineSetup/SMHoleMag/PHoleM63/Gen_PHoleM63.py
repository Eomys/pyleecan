# -*- coding: utf-8 -*-
"""File generated according to PHoleM63/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM63.Ui_PHoleM63 import Ui_PHoleM63


class Gen_PHoleM63(Ui_PHoleM63):
    def setupUi(self, PHoleM63):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PHoleM63.setupUi(self, PHoleM63)
        # Setup of in_W0
        txt = self.tr("""Length or Angle Opening""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr("""Length or Angle Opening""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr("""Distance from the lamination bore""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr("""Distance from the lamination bore""")
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
