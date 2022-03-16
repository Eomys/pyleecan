# -*- coding: utf-8 -*-
"""File generated according to PWSlot22/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot22.Ui_PWSlot22 import Ui_PWSlot22


class Gen_PWSlot22(Ui_PWSlot22):
    def setupUi(self, PWSlot22):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PWSlot22.setupUi(self, PWSlot22)
        # Setup of in_W0
        txt = self.tr("""Slot isthmus orthoradial angular width.""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr("""Slot isthmus orthoradial angular width.""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_W2
        txt = self.tr("""Angle between slot edges""")
        self.in_W2.setWhatsThis(txt)
        self.in_W2.setToolTip(txt)

        # Setup of lf_W2
        self.lf_W2.validator().setBottom(0)
        txt = self.tr("""Angle between slot edges""")
        self.lf_W2.setWhatsThis(txt)
        self.lf_W2.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr("""Slot isthmus radial height.""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr("""Slot isthmus radial height.""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)

        # Setup of in_H2
        txt = self.tr("""Slot radial height below wedge """)
        self.in_H2.setWhatsThis(txt)
        self.in_H2.setToolTip(txt)

        # Setup of lf_H2
        self.lf_H2.validator().setBottom(0)
        txt = self.tr("""Slot radial height below wedge """)
        self.lf_H2.setWhatsThis(txt)
        self.lf_H2.setToolTip(txt)
