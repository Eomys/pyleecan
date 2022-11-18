# -*- coding: utf-8 -*-
"""File generated according to SSimu/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SSimu.Ui_SSimu import Ui_SSimu


class Gen_SSimu(Ui_SSimu):
    def setupUi(self, SSimu):
        """Abstract class to update the widget according to the csv doc"""
        Ui_SSimu.setupUi(self, SSimu)
        # Setup of in_N0
        txt = self.tr(u"""Rotor speed""")
        self.in_N0.setWhatsThis(txt)
        self.in_N0.setToolTip(txt)

        # Setup of lf_N0
        txt = self.tr(u"""Rotor speed""")
        self.lf_N0.setWhatsThis(txt)
        self.lf_N0.setToolTip(txt)

        # Setup of unit_N0
        txt = self.tr(u"""Rotor speed""")
        self.unit_N0.setWhatsThis(txt)
        self.unit_N0.setToolTip(txt)

        # Setup of in_I3
        txt = self.tr(u"""DC rotor current""")
        self.in_I3.setWhatsThis(txt)
        self.in_I3.setToolTip(txt)

        # Setup of lf_I3
        txt = self.tr(u"""DC rotor current""")
        self.lf_I3.setWhatsThis(txt)
        self.lf_I3.setToolTip(txt)

        # Setup of unit_I3
        txt = self.tr(u"""DC rotor current""")
        self.unit_I3.setWhatsThis(txt)
        self.unit_I3.setToolTip(txt)

        # Setup of in_T_mag
        txt = self.tr(
            u"""Permanent magnet temperature to adapt magnet remanent flux density"""
        )
        self.in_T_mag.setWhatsThis(txt)
        self.in_T_mag.setToolTip(txt)

        # Setup of lf_T_mag
        txt = self.tr(
            u"""Permanent magnet temperature to adapt magnet remanent flux density"""
        )
        self.lf_T_mag.setWhatsThis(txt)
        self.lf_T_mag.setToolTip(txt)

        # Setup of unit_T_mag
        txt = self.tr(
            u"""Permanent magnet temperature to adapt magnet remanent flux density"""
        )
        self.unit_T_mag.setWhatsThis(txt)
        self.unit_T_mag.setToolTip(txt)

        # Setup of in_Na_tot
        txt = self.tr(u"""Angular discretization""")
        self.in_Na_tot.setWhatsThis(txt)
        self.in_Na_tot.setToolTip(txt)

        # Setup of si_Na_tot
        self.si_Na_tot.setMinimum(1)
        self.si_Na_tot.setMaximum(999999)
        txt = self.tr(u"""Angular discretization""")
        self.si_Na_tot.setWhatsThis(txt)
        self.si_Na_tot.setToolTip(txt)

        # Setup of is_per_a
        txt = self.tr(
            u"""True to compute only on one angle periodicity (use periodicities defined in axes_dict[angle])"""
        )
        self.is_per_a.setWhatsThis(txt)
        self.is_per_a.setToolTip(txt)

        # Setup of in_Nt_tot
        txt = self.tr(u"""Time discretization""")
        self.in_Nt_tot.setWhatsThis(txt)
        self.in_Nt_tot.setToolTip(txt)

        # Setup of si_Nt_tot
        self.si_Nt_tot.setMinimum(1)
        self.si_Nt_tot.setMaximum(999999)
        txt = self.tr(u"""Time discretization""")
        self.si_Nt_tot.setWhatsThis(txt)
        self.si_Nt_tot.setToolTip(txt)

        # Setup of is_per_t
        txt = self.tr(
            u"""True to compute only on one time periodicity (use periodicities defined in axes_dict[time])"""
        )
        self.is_per_t.setWhatsThis(txt)
        self.is_per_t.setToolTip(txt)

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
