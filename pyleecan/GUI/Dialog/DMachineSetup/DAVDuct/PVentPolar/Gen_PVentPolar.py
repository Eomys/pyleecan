# -*- coding: utf-8 -*-
"""File generated according to PVentPolar/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.DAVDuct.PVentPolar.Ui_PVentPolar import (
    Ui_PVentPolar,
)


class Gen_PVentPolar(Ui_PVentPolar):
    def setupUi(self, PVentPolar):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PVentPolar.setupUi(self, PVentPolar)
        # Setup of in_Zh
        txt = self.tr(
            u"""<qt><nobr>Number of Hole around the circumference</nobr></qt>"""
        )
        self.in_Zh.setWhatsThis(txt)
        self.in_Zh.setToolTip(txt)

        # Setup of si_Zh
        self.si_Zh.setMinimum(0)
        self.si_Zh.setMaximum(999999)
        txt = self.tr(
            u"""<qt><nobr>Number of Hole around the circumference</nobr></qt>"""
        )
        self.si_Zh.setWhatsThis(txt)
        self.si_Zh.setToolTip(txt)

        # Setup of in_D0
        txt = self.tr(u"""<qt><nobr>Height of the hole</nobr></qt>""")
        self.in_D0.setWhatsThis(txt)
        self.in_D0.setToolTip(txt)

        # Setup of lf_D0
        self.lf_D0.validator().setBottom(0)
        txt = self.tr(u"""<qt><nobr>Height of the hole</nobr></qt>""")
        self.lf_D0.setWhatsThis(txt)
        self.lf_D0.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr(u"""<qt><nobr>Radius of the bottom of Hole</nobr></qt>""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr(u"""<qt><nobr>Radius of the bottom of Hole</nobr></qt>""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)

        # Setup of in_W1
        txt = self.tr(u"""<qt><nobr>Hole angular width</nobr></qt>""")
        self.in_W1.setWhatsThis(txt)
        self.in_W1.setToolTip(txt)

        # Setup of lf_W1
        self.lf_W1.validator().setBottom(0)
        self.lf_W1.validator().setTop(6.29)
        txt = self.tr(u"""<qt><nobr>Hole angular width</nobr></qt>""")
        self.lf_W1.setWhatsThis(txt)
        self.lf_W1.setToolTip(txt)
