# -*- coding: utf-8 -*-
"""File generated according to SSimu/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SSimu.Ui_SSimu import Ui_SSimu


class Gen_SSimu(Ui_SSimu):
    def setupUi(self, SSimu):
        """Abstract class to update the widget according to the csv doc"""
        Ui_SSimu.setupUi(self, SSimu)
        # Setup of in_Kmesh
        txt = self.tr(
            u"""global coefficient to adjust mesh fineness in FEMM (1 : default , > 1 : finner , < 1 : less fine)"""
        )
        self.in_Kmesh.setWhatsThis(txt)
        self.in_Kmesh.setToolTip(txt)

        # Setup of lf_Kmesh
        txt = self.tr(
            u"""global coefficient to adjust mesh fineness in FEMM (1 : default , > 1 : finner , < 1 : less fine)"""
        )
        self.lf_Kmesh.setWhatsThis(txt)
        self.lf_Kmesh.setToolTip(txt)

        # Setup of in_nb_worker
        txt = self.tr(
            u"""To run FEMM in parallel (the parallelization is on the time loop)"""
        )
        self.in_nb_worker.setWhatsThis(txt)
        self.in_nb_worker.setToolTip(txt)

        # Setup of si_nb_worker
        self.si_nb_worker.setMinimum(-999999)
        self.si_nb_worker.setMaximum(999999)
        txt = self.tr(
            u"""To run FEMM in parallel (the parallelization is on the time loop)"""
        )
        self.si_nb_worker.setWhatsThis(txt)
        self.si_nb_worker.setToolTip(txt)
