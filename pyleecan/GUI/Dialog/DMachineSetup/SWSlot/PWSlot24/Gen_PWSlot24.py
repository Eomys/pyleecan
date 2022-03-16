# -*- coding: utf-8 -*-
"""File generated according to PWSlot24/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot24.Ui_PWSlot24 import Ui_PWSlot24


class Gen_PWSlot24(Ui_PWSlot24):
    def setupUi(self, PWSlot24):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PWSlot24.setupUi(self, PWSlot24)
        # Setup of in_W3
        txt = self.tr("""Teeth width""")
        self.in_W3.setWhatsThis(txt)
        self.in_W3.setToolTip(txt)

        # Setup of lf_W3
        self.lf_W3.validator().setBottom(0)
        txt = self.tr("""Teeth width""")
        self.lf_W3.setWhatsThis(txt)
        self.lf_W3.setToolTip(txt)

        # Setup of in_H2
        txt = self.tr("""Slot height""")
        self.in_H2.setWhatsThis(txt)
        self.in_H2.setToolTip(txt)

        # Setup of lf_H2
        self.lf_H2.validator().setBottom(0)
        txt = self.tr("""Slot height""")
        self.lf_H2.setWhatsThis(txt)
        self.lf_H2.setToolTip(txt)
