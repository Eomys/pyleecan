# -*- coding: utf-8 -*-
"""File generated according to SWindPat/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWindPat.Ui_SWindPat import Ui_SWindPat


class Gen_SWindPat(Ui_SWindPat):
    def setupUi(self, SWindPat):
        """Abstract class to update the widget according to the csv doc
        """
        Ui_SWindPat.setupUi(self, SWindPat)
        # Setup of in_qs
        txt = self.tr(u"""number of phases """)
        self.in_qs.setWhatsThis(txt)
        self.in_qs.setToolTip(txt)

        # Setup of si_qs
        self.si_qs.setMinimum(1)
        self.si_qs.setMaximum(100)
        txt = self.tr(u"""number of phases """)
        self.si_qs.setWhatsThis(txt)
        self.si_qs.setToolTip(txt)

        # Setup of is_reverse
        txt = self.tr(
            u"""1 to reverse the default winding algorithm along the airgap (c, b, a instead of a, b, c along the trigonometric direction)"""
        )
        self.is_reverse.setWhatsThis(txt)
        self.is_reverse.setToolTip(txt)

        # Setup of in_Nslot
        txt = self.tr(
            u"""0 not to change the stator winding connection matrix built by pyleecan number of slots to shift the coils obtained with pyleecan winding algorithm (a, b, c becomes b, c, a with Nslot_shift_wind1=1)"""
        )
        self.in_Nslot.setWhatsThis(txt)
        self.in_Nslot.setToolTip(txt)

        # Setup of si_Nslot
        self.si_Nslot.setMinimum(-999999)
        self.si_Nslot.setMaximum(999999)
        txt = self.tr(
            u"""0 not to change the stator winding connection matrix built by pyleecan number of slots to shift the coils obtained with pyleecan winding algorithm (a, b, c becomes b, c, a with Nslot_shift_wind1=1)"""
        )
        self.si_Nslot.setWhatsThis(txt)
        self.si_Nslot.setToolTip(txt)
