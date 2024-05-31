# -*- coding: utf-8 -*-
"""File generated according to PVentCirc/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.DAVDuct.PVentCirc.Ui_PVentCirc import (
    Ui_PVentCirc,
)


class Gen_PVentCirc(Ui_PVentCirc):
    def setupUi(self, PVentCirc):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PVentCirc.setupUi(self, PVentCirc)
        # Setup of in_Zh
        txt = self.tr("""Number of Hole around the circumference""")
        self.in_Zh.setWhatsThis(txt)
        self.in_Zh.setToolTip(txt)

        # Setup of si_Zh
        self.si_Zh.setMinimum(0)
        self.si_Zh.setMaximum(999999)
        txt = self.tr("""Number of Hole around the circumference""")
        self.si_Zh.setWhatsThis(txt)
        self.si_Zh.setToolTip(txt)

        # Setup of in_D0
        txt = self.tr("""Hole diameters""")
        self.in_D0.setWhatsThis(txt)
        self.in_D0.setToolTip(txt)

        # Setup of lf_D0
        self.lf_D0.validator().setBottom(0)
        txt = self.tr("""Hole diameters""")
        self.lf_D0.setWhatsThis(txt)
        self.lf_D0.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr("""Radius of the hole centers""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr("""Radius of the hole centers""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)
