# -*- coding: utf-8 -*-
"""File generated according to PVentTrap/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.DAVDuct.PVentTrap.Ui_PVentTrap import (
    Ui_PVentTrap,
)


class Gen_PVentTrap(Ui_PVentTrap):
    def setupUi(self, PVentTrap):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PVentTrap.setupUi(self, PVentTrap)
        # Setup of in_Zh
        txt = self.tr(u"""Number of Hole around the circumference""")
        self.in_Zh.setWhatsThis(txt)
        self.in_Zh.setToolTip(txt)

        # Setup of si_Zh
        self.si_Zh.setMinimum(0)
        self.si_Zh.setMaximum(999999)
        txt = self.tr(u"""Number of Hole around the circumference""")
        self.si_Zh.setWhatsThis(txt)
        self.si_Zh.setToolTip(txt)

        # Setup of in_D0
        txt = self.tr(u"""Hole height""")
        self.in_D0.setWhatsThis(txt)
        self.in_D0.setToolTip(txt)

        # Setup of lf_D0
        self.lf_D0.validator().setBottom(0)
        txt = self.tr(u"""Hole height""")
        self.lf_D0.setWhatsThis(txt)
        self.lf_D0.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr(u"""Radius of the hole bottom""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr(u"""Radius of the hole bottom""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)

        # Setup of in_W1
        txt = self.tr(u"""Hole small basis""")
        self.in_W1.setWhatsThis(txt)
        self.in_W1.setToolTip(txt)

        # Setup of lf_W1
        self.lf_W1.validator().setBottom(0)
        txt = self.tr(u"""Hole small basis""")
        self.lf_W1.setWhatsThis(txt)
        self.lf_W1.setToolTip(txt)

        # Setup of in_W2
        txt = self.tr(u"""Hole large basis""")
        self.in_W2.setWhatsThis(txt)
        self.in_W2.setToolTip(txt)

        # Setup of lf_W2
        self.lf_W2.validator().setBottom(0)
        txt = self.tr(u"""Hole large basis""")
        self.lf_W2.setWhatsThis(txt)
        self.lf_W2.setToolTip(txt)
