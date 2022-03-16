# -*- coding: utf-8 -*-
"""File generated according to PWSlot25/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot25.Ui_PWSlot25 import Ui_PWSlot25


class Gen_PWSlot25(Ui_PWSlot25):
    def setupUi(self, PWSlot25):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PWSlot25.setupUi(self, PWSlot25)
        # Setup of in_W3
        txt = self.tr("""Teeth bottom width""")
        self.in_W3.setWhatsThis(txt)
        self.in_W3.setToolTip(txt)

        # Setup of lf_W3
        self.lf_W3.validator().setBottom(0)
        txt = self.tr("""Teeth bottom width""")
        self.lf_W3.setWhatsThis(txt)
        self.lf_W3.setToolTip(txt)

        # Setup of in_W4
        txt = self.tr("""Teeth top width""")
        self.in_W4.setWhatsThis(txt)
        self.in_W4.setToolTip(txt)

        # Setup of lf_W4
        self.lf_W4.validator().setBottom(0)
        txt = self.tr("""Teeth top width""")
        self.lf_W4.setWhatsThis(txt)
        self.lf_W4.setToolTip(txt)

        # Setup of in_H1
        txt = self.tr("""Slot top height""")
        self.in_H1.setWhatsThis(txt)
        self.in_H1.setToolTip(txt)

        # Setup of lf_H1
        self.lf_H1.validator().setBottom(0)
        txt = self.tr("""Slot top height""")
        self.lf_H1.setWhatsThis(txt)
        self.lf_H1.setToolTip(txt)

        # Setup of in_H2
        txt = self.tr("""Slot bottom height""")
        self.in_H2.setWhatsThis(txt)
        self.in_H2.setToolTip(txt)

        # Setup of lf_H2
        self.lf_H2.validator().setBottom(0)
        txt = self.tr("""Slot bottom height""")
        self.lf_H2.setWhatsThis(txt)
        self.lf_H2.setToolTip(txt)
