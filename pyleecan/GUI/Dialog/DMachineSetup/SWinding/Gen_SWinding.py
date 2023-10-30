# -*- coding: utf-8 -*-
"""File generated according to SWinding/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWinding.Ui_SWinding import Ui_SWinding


class Gen_SWinding(Ui_SWinding):
    def setupUi(self, SWinding):
        """Abstract class to update the widget according to the csv doc"""
        Ui_SWinding.setupUi(self, SWinding)
        # Setup of in_qs
        txt = self.tr(u"""number of phases """)
        self.in_qs.setWhatsThis(txt)
        self.in_qs.setToolTip(txt)

        # Setup of si_qs
        self.si_qs.setMinimum(0)
        self.si_qs.setMaximum(999999)
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
            u"""Number of slots to shift the coils obtained with pyleecan winding algorithm (a, b, c becomes b, c, a with Nslot_shift_wind=1)"""
        )
        self.in_Nslot.setWhatsThis(txt)
        self.in_Nslot.setToolTip(txt)

        # Setup of si_Nslot
        self.si_Nslot.setMinimum(-999999)
        self.si_Nslot.setMaximum(999999)
        txt = self.tr(
            u"""Number of slots to shift the coils obtained with pyleecan winding algorithm (a, b, c becomes b, c, a with Nslot_shift_wind=1)"""
        )
        self.si_Nslot.setWhatsThis(txt)
        self.si_Nslot.setToolTip(txt)

        # Setup of in_coil_pitch
        txt = self.tr(
            u"""Distance (in slot) between a conductor of a certain phase and the corresponding return conductor"""
        )
        self.in_coil_pitch.setWhatsThis(txt)
        self.in_coil_pitch.setToolTip(txt)

        # Setup of si_coil_pitch
        self.si_coil_pitch.setMinimum(-999999)
        self.si_coil_pitch.setMaximum(999999)
        txt = self.tr(
            u"""Distance (in slot) between a conductor of a certain phase and the corresponding return conductor"""
        )
        self.si_coil_pitch.setWhatsThis(txt)
        self.si_coil_pitch.setToolTip(txt)

        # Setup of in_Ntcoil
        txt = self.tr(u"""number of turns per coil""")
        self.in_Ntcoil.setWhatsThis(txt)
        self.in_Ntcoil.setToolTip(txt)

        # Setup of si_Ntcoil
        self.si_Ntcoil.setMinimum(1)
        self.si_Ntcoil.setMaximum(999999)
        txt = self.tr(u"""number of turns per coil""")
        self.si_Ntcoil.setWhatsThis(txt)
        self.si_Ntcoil.setToolTip(txt)

        # Setup of in_Npcp
        txt = self.tr(u"""number of parallel circuits per phase""")
        self.in_Npcp.setWhatsThis(txt)
        self.in_Npcp.setToolTip(txt)

        # Setup of si_Npcp
        self.si_Npcp.setMinimum(1)
        self.si_Npcp.setMaximum(999999)
        txt = self.tr(u"""number of parallel circuits per phase""")
        self.si_Npcp.setWhatsThis(txt)
        self.si_Npcp.setToolTip(txt)
