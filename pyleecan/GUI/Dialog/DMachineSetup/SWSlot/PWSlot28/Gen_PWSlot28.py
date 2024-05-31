# -*- coding: utf-8 -*-
"""File generated according to PWSlot28/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot28.Ui_PWSlot28 import Ui_PWSlot28


class Gen_PWSlot28(Ui_PWSlot28):
    def setupUi(self, PWSlot28):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PWSlot28.setupUi(self, PWSlot28)
        # Setup of in_W0
        txt = self.tr("""Slot isthmus width.""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr("""Slot isthmus width.""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of unit_W0
        txt = self.tr("""Slot isthmus width.""")
        self.unit_W0.setWhatsThis(txt)
        self.unit_W0.setToolTip(txt)

        # Setup of in_W3
        txt = self.tr("""Tooth width""")
        self.in_W3.setWhatsThis(txt)
        self.in_W3.setToolTip(txt)

        # Setup of lf_W3
        self.lf_W3.validator().setBottom(0)
        txt = self.tr("""Tooth width""")
        self.lf_W3.setWhatsThis(txt)
        self.lf_W3.setToolTip(txt)

        # Setup of unit_W3
        txt = self.tr("""Tooth width""")
        self.unit_W3.setWhatsThis(txt)
        self.unit_W3.setToolTip(txt)

        # Setup of in_R1
        txt = self.tr("""Slot edge radius""")
        self.in_R1.setWhatsThis(txt)
        self.in_R1.setToolTip(txt)

        # Setup of lf_R1
        self.lf_R1.validator().setBottom(0)
        txt = self.tr("""Slot edge radius""")
        self.lf_R1.setWhatsThis(txt)
        self.lf_R1.setToolTip(txt)

        # Setup of unit_R1
        txt = self.tr("""Slot edge radius""")
        self.unit_R1.setWhatsThis(txt)
        self.unit_R1.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr("""Slot isthmus height.""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr("""Slot isthmus height.""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)

        # Setup of unit_H0
        txt = self.tr("""Slot isthmus height.""")
        self.unit_H0.setWhatsThis(txt)
        self.unit_H0.setToolTip(txt)

        # Setup of in_H3
        txt = self.tr("""Tooth height""")
        self.in_H3.setWhatsThis(txt)
        self.in_H3.setToolTip(txt)

        # Setup of lf_H3
        self.lf_H3.validator().setBottom(0)
        txt = self.tr("""Tooth height""")
        self.lf_H3.setWhatsThis(txt)
        self.lf_H3.setToolTip(txt)

        # Setup of unit_H3
        txt = self.tr("""Tooth height""")
        self.unit_H3.setWhatsThis(txt)
        self.unit_H3.setToolTip(txt)
