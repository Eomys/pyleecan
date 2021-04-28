# -*- coding: utf-8 -*-
"""File generated according to SWindParam/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWindParam.Ui_SWindParam import Ui_SWindParam


class Gen_SWindParam(Ui_SWindParam):
    def setupUi(self, SWindParam):
        """Abstract class to update the widget according to the csv doc"""
        Ui_SWindParam.setupUi(self, SWindParam)
        # Setup of in_Ntcoil
        txt = self.tr(u"""number of turns per coil""")
        self.in_Ntcoil.setWhatsThis(txt)
        self.in_Ntcoil.setToolTip(txt)

        # Setup of si_Ntcoil
        self.si_Ntcoil.setMinimum(1)
        self.si_Ntcoil.setMaximum(1000)
        txt = self.tr(u"""number of turns per coil""")
        self.si_Ntcoil.setWhatsThis(txt)
        self.si_Ntcoil.setToolTip(txt)

        # Setup of in_Npcp
        txt = self.tr(u"""number of parallel circuits per phase (maximum 2p)""")
        self.in_Npcp.setWhatsThis(txt)
        self.in_Npcp.setToolTip(txt)

        # Setup of si_Npcp
        self.si_Npcp.setMinimum(1)
        self.si_Npcp.setMaximum(1000)
        txt = self.tr(u"""number of parallel circuits per phase (maximum 2p)""")
        self.si_Npcp.setWhatsThis(txt)
        self.si_Npcp.setToolTip(txt)
