from numpy import zeros, sqrt, pi, tile, isnan
from multiprocessing import cpu_count

from ....Functions.Electrical.coordinate_transformation import n2abc, abc2n
from ....Functions.labels import STATOR_LAB, ROTOR_LAB
from ....Functions.load import import_class


def comp_parameters(self, machine, OP, Tsta, Trot):
    """Compute the parameters dict for the equivalent electrical circuit:
    resistance, inductance
    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    output : Output
        an Output object
    """

    # get some machine parameters
    Zsr = machine.rotor.slot.Zs
    qsr = machine.rotor.winding.qs
    qs = machine.stator.winding.qs
    p = machine.rotor.winding.p
    N0 = OP.get_N0()
    felec = OP.get_felec()

    # simulation type for magnetizing inductance when missing (0: FEA, 1: Analytical)
    type_comp_Lm = 0
    # simulation type for rotor slot leakage inductance when missing (0: FEA, 1: Analytical)
    type_comp_Lr = 0
    # simulation type for stator slot leakage inductance when missing (0: FEA, 1: Analytical)
    type_comp_Ls = 0

    # change from rotor frame to stator frame
    xi = machine.stator.winding.comp_winding_factor()
    Ntspc = machine.stator.winding.comp_Ntsp()

    # winding transformation ratios
    K21 = (xi[0] * Ntspc) / (1 * 0.5)  # (xi1[0] * Ntspc1) / (xi2[0] * Ntspc2)  for DFIM
    # transformation ratio from secondary (2, rotor) to primary (1, stator) for impedance in SCIM case
    K21I = (qs / Zsr) * K21
    # transformation ratio from secondary (2, rotor) to primary (1, stator) for current  in SCIM case
    K21Z = (qs / Zsr) * K21 ** 2
    self.parameters["K21Z"] = K21Z
    self.parameters["K21I"] = K21I

    # check that parameters are in ELUT, otherwise compute missing ones -> to be put in check_ELUT method?
    if "slip" not in self.parameters or self.parameters["slip"] is None:
        Nr = N0
        Ns = felec / p * 60
        slip = (Ns - Nr) / Ns
        self.parameters["slip"] = slip

    if "R1" not in self.parameters or self.parameters["R1"] is None:
        CondS = machine.stator.winding.conductor
        # get resistance calculated analytically at simulation temperature
        R1 = machine.stator.comp_resistance_wind(T=Tsta)
        # compute skin_effect on stator side
        Xkr_skinS, Xke_skinS = CondS.comp_skin_effect(freq=felec, T=Tsta)
        # update resistance value including skin effect
        self.parameters["R1"] = R1 * Xkr_skinS

    if "R2" not in self.parameters or self.parameters["R2"] is None:
        # get resistance calculated analytically at simulation temperature
        Rr = machine.rotor.comp_resistance_wind(T=Trot, qs=3)
        # putting resistance on stator side in EEC
        R2 = K21Z * Rr

        # compute skin_effect on rotor side
        if Xkr_skinR is None:
            CondR = machine.rotor.winding.conductor
            Xkr_skinR, Xke_skinR = CondR.comp_skin_effect(
                freq=felec * (self.parameters["slip"]), T=Trot
            )

        # update resistance value including skin effect
        self.parameters["R2"] = Rr * Xkr_skinR

    if "Rfe" not in self.parameters:
        self.parameters["Rfe"] = 1e12  # TODO calculate (or estimate at least)

    if "L2" not in self.parameters or self.parameters["L2"] is None:
        if type_comp_Lr == 1:
            # analytic calculation
            # L2 = machine.rotor.slot.comp_inductance_leakage_ANL() #TODO
            L20 = 0
            if Xke_skinR is None:
                CondR = machine.rotor.winding.conductor
                Xkr_skinR, Xke_skinR = CondR.comp_skin_effect(
                    freq=felec * (self.parameters["slip"]), T=Trot
                )
                L2 = L20 * Xke_skinR
        else:
            # FEA calculation
            # L2 = machine.rotor.slot.comp_inductance_leakage_FEA() #TODO
            L2 = 0

        self.parameters["L2"] = L2

    if "L1" not in self.parameters or self.parameters["L1"] is None:
        if type_comp_Ls == 1:
            # analytic calculation
            # L10 = machine.stator.slot.comp_inductance_leakage_ANL() #TODO
            L10 = 0
            if Xke_skinS is None:
                CondS = machine.stator.winding.conductor
                Xkr_skinS, Xke_skinS = CondS.comp_skin_effect(freq=felec, T=Tsta)
                L1 = L10 * Xke_skinS
        else:
            # FEA calculation
            # L1 = machine.rotor.slot.comp_inductance_leakage_FEA() #TODO
            L1 = 0

        self.parameters["L1"] = L1

    # alphasw = self.cond_mat.elec.alpha
    # # stator winding phase resistance, skin effect correction
    # if felec is None:
    #     Rs_freq = self.Rs
    # else:
    #     Rs_dc = self.Rs  # DC resistance at Tsta_ref
    #     K_RSE_sta = self.K_RSE_sta  # skin effect factor for resistance
    #     Rs_freq = Rs_dc * interp(K_RSE_sta[0, :], K_RSE_sta[1, :], felec)

    # # stator winding phase resistance, temperature correction
    # if Tsta is not None:
    #     Rs_freq_temp = Rs_freq
    # else:
    #     Tsta_ref = self.Tsta_ref  # ref temperature
    #     Rs_freq_temp = Rs_freq * (1 + alphasw * (Tsta - Tsta_ref))

    # # stator winding phase leakage inductance, skin effect correction
    # if felec is None:
    #     Ls_freq = self.Ls
    # else:
    #     Ls_dc = self.Ls  # DC resistance
    #     K_ISE_sta = self.K_ISE_sta  # skin effect factor for leakage inductance
    #     Ls_freq = Ls_dc * interp(K_ISE_sta[0, :], K_ISE_sta[1, :], felec)

    # check if inductances have to be calculated
    if "Phi_m" not in self.parameters or self.parameters["Phi_m"] is None:
        if type_comp_Lm == 1:
            # analytic calculation
            # Phi_m, I_m = machine.comp_inductance_magnetization_ANL() #TODO
            Phi_m = None
            I_m = None

        else:
            # FEA calculation
            # Lm, Im =comp_Lm_FEA(self) #TODO
            Phi_m = None
            I_m = None

        self.parameters["Phi_m"] = Phi_m
        self.parameters["I_m"] = I_m


def _comp_flux_mean(self, out):
    # TODO add fix for single time value
    # TODO add option to calculate RMS instead of mean fluxlinkage

    # some readability
    logger = self.get_logger()
    machine = out.simu.machine
    p = machine.rotor.winding.p
    qsr = machine.rotor.winding.qs
    sym, is_anti_per = machine.comp_periodicity_spatial()

    # get the fluxlinkages
    Phi = out.mag.Phi_wind[ROTOR_LAB + "-0"].get_along("time", "phase")["Phi_{wind}"]

    # reconstruct fluxlinkage in case of (anti) periodicity
    if out.simu.mag.is_periodicity_a:
        # reconstruct anti periodicity
        if is_anti_per:
            qsr_eff = qsr // (sym * (1 + is_anti_per))
            for ii in range(qsr_eff):
                if not all(isnan(Phi[:, ii + qsr_eff]).tolist()):
                    logger.warning(
                        f"{type(self).__name__}: "
                        + f"Rotor fluxlinkage of bar {ii + qsr_eff} will be overridden."
                    )
                Phi[:, ii + qsr_eff] = -Phi[:, ii]
        # reconstruct periodicity
        if sym != 1:
            qsr_eff = qsr // sym
            if not all(isnan(Phi[:, qsr_eff:]).tolist()):
                logger.warning(
                    f"{type(self).__name__}: "
                    + f"Rotor fluxlinkage of bar "
                    + "starting with {qsr_eff} will be overridden."
                )
            for ii in range(sym - 1):
                id0 = qsr_eff * (ii + 1)
                id1 = qsr_eff * (ii + 2)
                Phi[:, id0:id1] = Phi[:, :qsr_eff]

        # rescale
        Phi = Phi / (sym * (1 + is_anti_per))

    # compute mean value of periodic bar flux linkage
    Phi_ab = zeros([Phi.shape[0], 2])
    if (qsr % p) == 0:
        qsr_per_pole = qsr // p
        for ii in range(p):
            id0 = qsr_per_pole * ii
            id1 = qsr_per_pole * (ii + 1)
            Phi_ab += n2abc(Phi[:, id0:id1], n=qsr_per_pole) / p
    else:
        logger.warning(f"{type(self).__name__}: " + "Not Implemented Yet")

    # compute rotor and stator flux linkage
    Phi_r = abs(Phi_ab[:, 0] + 1j * Phi_ab[:, 1]).mean() / sqrt(2)
    Phi_ab = n2abc(
        out.mag.Phi_wind[STATOR_LAB + "-0"].get_along("time", "phase")["Phi_{wind}"]
    )
    Phi_s = abs(Phi_ab[:, 0] + 1j * Phi_ab[:, 1]).mean() / sqrt(2)

    return Phi_s, Phi_r


def _comp_Lm_FEA(self):

    # setup a MagFEMM simulation to get the parameters
    # TODO maybe use IndMagFEMM or FluxlinkageFEMM
    #      but for now they are not suitable so I utilize 'normal' MagFEMM simu
    from ....Classes.Simu1 import Simu1
    from ....Classes.InputCurrent import InputCurrent
    from ....Classes.MagFEMM import MagFEMM
    from ....Classes.Output import Output
    from ....Classes.ImportGenVectLin import ImportGenVectLin
    from ....Classes.ImportMatrixVal import ImportMatrixVal

    # set frequency, time and number of revolutions
    # TODO what will be the best settings to get a good average with min. samples
    if self.N0 is None and self.felec is None:
        N0 = 50 * 60 / p
        felec = 50
    elif self.N0 is None and self.felec is not None:
        N0 = self.felec * 60 / p
    elif self.N0 is not None and self.felec is None:
        N0 = self.N0
        felec = N0 / 60 * p
    else:
        N0 = self.N0
        felec = self.felec

    Nrev = self.Nrev

    T = Nrev / (N0 / 60)
    Ir = ImportMatrixVal(value=zeros((self.Nt_tot, qsr)))
    time = ImportGenVectLin(start=0, stop=T, num=self.Nt_tot, endpoint=False)

    # TODO estimate magnetizing current if self.I == None
    # TODO compute magnetizing curve as function of I

    # setup the simu object
    simu = Simu1(name="EEC_comp_parameter", machine=machine.copy())
    # Definition of the enforced output of the electrical module
    simu.input = InputCurrent(
        Is=None,
        Id_ref=self.I,
        Iq_ref=0,
        Ir=Ir,  # zero current for the rotor
        N0=N0,
        angle_rotor=None,  # Will be computed
        time=time,
        felec=felec,
    )

    # Definition of the magnetic simulation (no symmetry)
    nb_worker = self.nb_worker if self.nb_worker else cpu_count()

    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=self.is_periodicity_a,
        is_periodicity_t=False,
        Kgeo_fineness=0.5,
        Kmesh_fineness=0.5,
        nb_worker=nb_worker,
    )
    simu.force = None
    simu.struct = None

    # --- compute the main inductance and stator stray inductance ---
    # set output and run first simulation
    out = Output(simu=simu)
    out.simu.run()

    # compute average rotor and stator fluxlinkage
    # TODO check wind_mat that the i-th bars is in the i-th slots
    Phi_s, Phi_r = _comp_flux_mean(self, out)

    self.parameters["Lm"] = (Phi_r * K21Z * Zsr / 3) / self.I
    L1 = (Phi_s - (Phi_r * K21Z * Zsr / 3)) / self.I
    self.parameters["L1"] = L1 * Xke_skinS
    # --- compute the main inductance and rotor stray inductance ---
    # set new output
    out = Output(simu=simu)

    # set current values
    Ir_ = zeros([self.Nt_tot, 2])
    Ir_[:, 0] = self.I * K21Z * sqrt(2)
    Ir = abc2n(Ir_, n=qsr // p)  # TODO no rotation for now

    Ir = ImportMatrixVal(value=tile(Ir, (1, p)))

    simu.input.Is = None
    simu.input.Id_ref = 0
    simu.input.Iq_ref = 0
    simu.input.Ir = Ir

    out.simu.run()

    # compute average rotor and stator fluxlinkage
    # TODO check wind_mat that the i-th bars is in the i-th slots
    Phi_s, Phi_r = _comp_flux_mean(self, out)
    K21Z = self.parameters["K21Z"]
    I_m = self.I
    Lm = Phi_s / I_m
    L2 = ((Phi_r * K21Z * Zsr / 3) - Phi_s) / self.I

    return Phi_s, I_m
