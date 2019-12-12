# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from pyleecan.GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.PVentCirc.Ui_PVentCirc import (
    Ui_PVentCirc,
)


class Gen_PVentCirc(Ui_PVentCirc):
    def setupUi(self, PVentCirc):
        Ui_PVentCirc.setupUi(self, PVentCirc)
        # Setup of in_Alpha0
        txt = self.tr(u"""Shift angle of the holes around circumference""")
        self.in_Alpha0.setWhatsThis(txt)
        self.in_Alpha0.setToolTip(txt)

        # Setup of lf_Alpha0
        self.lf_Alpha0.validator().setBottom(0)
        self.lf_Alpha0.validator().setTop(6.29)
        txt = self.tr(u"""Shift angle of the holes around circumference""")
        self.lf_Alpha0.setWhatsThis(txt)
        self.lf_Alpha0.setToolTip(txt)

        # Setup of in_D0
        txt = self.tr(u"""Hole diameters""")
        self.in_D0.setWhatsThis(txt)
        self.in_D0.setToolTip(txt)

        # Setup of lf_D0
        self.lf_D0.validator().setBottom(0)
        txt = self.tr(u"""Hole diameters""")
        self.lf_D0.setWhatsThis(txt)
        self.lf_D0.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr(u"""Diameter of the hole centers""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr(u"""Diameter of the hole centers""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)
