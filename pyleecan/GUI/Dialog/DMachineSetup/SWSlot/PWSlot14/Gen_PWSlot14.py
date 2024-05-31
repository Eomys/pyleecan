# -*- coding: utf-8 -*-
"""File generated according to PWSlot14/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot14.Ui_PWSlot14 import Ui_PWSlot14


class Gen_PWSlot14(Ui_PWSlot14):
    def setupUi(self, PWSlot14):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PWSlot14.setupUi(self, PWSlot14)
        # Setup of in_W0
        txt = self.tr("""Slot isthmus width.""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr("""Slot isthmus width.""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_W3
        txt = self.tr("""Tooth width""")
        self.in_W3.setWhatsThis(txt)
        self.in_W3.setToolTip(txt)

        # Setup of lf_W3
        self.lf_W3.validator().setBottom(0)
        txt = self.tr("""Tooth width""")
        self.lf_W3.setWhatsThis(txt)
        self.lf_W3.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr("""Slot isthmus height.""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr("""Slot isthmus height.""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)

        # Setup of in_H1
        txt = self.tr("""height or angle  (See Schematics)""")
        self.in_H1.setWhatsThis(txt)
        self.in_H1.setToolTip(txt)

        # Setup of lf_H1
        self.lf_H1.validator().setBottom(0)
        txt = self.tr("""height or angle  (See Schematics)""")
        self.lf_H1.setWhatsThis(txt)
        self.lf_H1.setToolTip(txt)

        # Setup of in_H3
        txt = self.tr("""Tooth height""")
        self.in_H3.setWhatsThis(txt)
        self.in_H3.setToolTip(txt)

        # Setup of lf_H3
        self.lf_H3.validator().setBottom(0)
        txt = self.tr("""Tooth height""")
        self.lf_H3.setWhatsThis(txt)
        self.lf_H3.setToolTip(txt)
