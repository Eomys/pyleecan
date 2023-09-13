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
        txt = self.tr(
            """<qt><nobr>Number of Hole around the circumference</nobr></qt>"""
        )
        self.in_Zh.setWhatsThis(txt)
        self.in_Zh.setToolTip(txt)

        # Setup of si_Zh
        self.si_Zh.setMinimum(0)
        self.si_Zh.setMaximum(999999)
        txt = self.tr(
            """<qt><nobr>Number of Hole around the circumference</nobr></qt>"""
        )
        self.si_Zh.setWhatsThis(txt)
        self.si_Zh.setToolTip(txt)

        # Setup of in_D0
        txt = self.tr("""<qt><nobr>Hole height</nobr></qt>""")
        self.in_D0.setWhatsThis(txt)
        self.in_D0.setToolTip(txt)

        # Setup of lf_D0
        self.lf_D0.validator().setBottom(0)
        txt = self.tr("""<qt><nobr>Hole height</nobr></qt>""")
        self.lf_D0.setWhatsThis(txt)
        self.lf_D0.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr("""<qt><nobr>Radius of the hole bottom</nobr></qt>""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr("""<qt><nobr>Radius of the hole bottom</nobr></qt>""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)

        # Setup of in_W1
        txt = self.tr("""<qt><nobr>Hole small basis</nobr></qt>""")
        self.in_W1.setWhatsThis(txt)
        self.in_W1.setToolTip(txt)

        # Setup of lf_W1
        self.lf_W1.validator().setBottom(0)
        txt = self.tr("""<qt><nobr>Hole small basis</nobr></qt>""")
        self.lf_W1.setWhatsThis(txt)
        self.lf_W1.setToolTip(txt)

        # Setup of in_W2
        txt = self.tr("""<qt><nobr>Hole large basis</nobr></qt>""")
        self.in_W2.setWhatsThis(txt)
        self.in_W2.setToolTip(txt)

        # Setup of lf_W2
        self.lf_W2.validator().setBottom(0)
        txt = self.tr("""<qt><nobr>Hole large basis</nobr></qt>""")
        self.lf_W2.setWhatsThis(txt)
        self.lf_W2.setToolTip(txt)
