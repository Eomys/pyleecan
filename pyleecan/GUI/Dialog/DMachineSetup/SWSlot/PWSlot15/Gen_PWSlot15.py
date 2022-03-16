# -*- coding: utf-8 -*-
"""File generated according to PWSlot15/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot15.Ui_PWSlot15 import Ui_PWSlot15


class Gen_PWSlot15(Ui_PWSlot15):
    def setupUi(self, PWSlot15):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PWSlot15.setupUi(self, PWSlot15)
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

        # Setup of in_H1
        txt = self.tr("""Slot intermediate height.""")
        self.in_H1.setWhatsThis(txt)
        self.in_H1.setToolTip(txt)

        # Setup of lf_H1
        self.lf_H1.validator().setBottom(0)
        txt = self.tr("""Slot intermediate height.""")
        self.lf_H1.setWhatsThis(txt)
        self.lf_H1.setToolTip(txt)

        # Setup of unit_H1
        txt = self.tr("""Slot intermediate height.""")
        self.unit_H1.setWhatsThis(txt)
        self.unit_H1.setToolTip(txt)

        # Setup of in_H2
        txt = self.tr("""Slot height""")
        self.in_H2.setWhatsThis(txt)
        self.in_H2.setToolTip(txt)

        # Setup of lf_H2
        self.lf_H2.validator().setBottom(0)
        txt = self.tr("""Slot height""")
        self.lf_H2.setWhatsThis(txt)
        self.lf_H2.setToolTip(txt)

        # Setup of unit_H2
        txt = self.tr("""Slot height""")
        self.unit_H2.setWhatsThis(txt)
        self.unit_H2.setToolTip(txt)

        # Setup of in_R1
        txt = self.tr("""Top radius""")
        self.in_R1.setWhatsThis(txt)
        self.in_R1.setToolTip(txt)

        # Setup of lf_R1
        self.lf_R1.validator().setBottom(0)
        txt = self.tr("""Top radius""")
        self.lf_R1.setWhatsThis(txt)
        self.lf_R1.setToolTip(txt)

        # Setup of unit_R1
        txt = self.tr("""Top radius""")
        self.unit_R1.setWhatsThis(txt)
        self.unit_R1.setToolTip(txt)

        # Setup of in_R2
        txt = self.tr("""Bottom radius""")
        self.in_R2.setWhatsThis(txt)
        self.in_R2.setToolTip(txt)

        # Setup of lf_R2
        self.lf_R2.validator().setBottom(0)
        txt = self.tr("""Bottom radius""")
        self.lf_R2.setWhatsThis(txt)
        self.lf_R2.setToolTip(txt)

        # Setup of unit_R2
        txt = self.tr("""Bottom radius""")
        self.unit_R2.setWhatsThis(txt)
        self.unit_R2.setToolTip(txt)
