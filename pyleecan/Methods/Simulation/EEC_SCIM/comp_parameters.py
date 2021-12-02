from numpy import zeros, sqrt, pi, tile, isnan
from multiprocessing import cpu_count

from ....Functions.Electrical.dqh_transformation import n2abc, abc2n
from ....Functions.labels import STATOR_LAB, ROTOR_LAB
from ....Functions.load import import_class


def comp_parameters(self, machine, OP, Tsta, Trot):
    """Compute the parameters dict for the equivalent electrical circuit:
    resistance, inductance
    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    machine : Machine
        a Machine object
    OP : OP
        an OP object
    Tsta : float
        Average stator temperature
    Trot : float
        Average rotor temperature
    """

    if self.parameters is None:
        self.parameters = dict()
    par = self.parameters

    # get some machine parameters
    Zsr = machine.rotor.slot.Zs
    qsr = machine.rotor.winding.qs
    qs = machine.stator.winding.qs
    CondS = machine.stator.winding.conductor
    CondR = machine.rotor.winding.conductor
    felec = OP.get_felec()
    slip = OP.get_slip()

    LUT = self.LUT_enforced
    is_LUT = self.LUT_enforced is not None

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
    par["K21Z"] = K21Z
    par["K21I"] = K21I

    # Store electrical frequency in parameters
    par["felec"] = felec

    # check that parameters are in ELUT, otherwise compute missing ones
    if "U0_ref" not in par or par["U0_ref"] is None:
        par["U0_ref"] = OP.U0_ref

    if "slip" not in par or par["slip"] is None:
        par["slip"] = slip

    if "R1" not in par or par["R1"] is None:
        if is_LUT and LUT.R1 is not None:
            R10 = LUT.R1
            T1_ref = LUT.T1_ref
        else:
            # get resistance calculated analytically at simulation temperature
            R10 = machine.stator.comp_resistance_wind(T=Tsta)

        # compute skin_effect on stator side
        Tfact1 = CondS.comp_temperature_effect(T_op=Tsta, T_ref=T1_ref)
        Xkr_skinS, _ = CondS.comp_skin_effect(freq=felec, Tfact=Tfact1)
        # update resistance value including skin effect
        par["R1"] = R10 * Tfact1 * Xkr_skinS

    if "L1" not in par or par["L1"] is None:
        if is_LUT and LUT.L1 is not None:
            L10 = LUT.L1
            T1_ref = LUT.T1_ref
        elif type_comp_Ls == 1:
            # analytic calculation
            # L10 = machine.stator.slot.comp_inductance_leakage_ANL() #TODO
            pass
        else:
            # FEA calculation
            # L1 = machine.rotor.slot.comp_inductance_leakage_FEA() #TODO
            pass

        Tfact1 = CondS.comp_temperature_effect(T_op=Tsta, T_ref=T1_ref)
        _, Xke_skinS = CondS.comp_skin_effect(freq=felec, Tfact=Tfact1)
        par["L1"] = L10 * Xke_skinS

    if "Rfe" not in par:
        par["Rfe"] = 1e12  # TODO calculate (or estimate at least)

    if "R2" not in par or par["R2"] is None:
        if is_LUT and LUT.R2 is not None:
            R20 = LUT.R2
            T2_ref = LUT.T2_ref
        else:
            # get resistance calculated analytically at simulation temperature
            Rr = machine.rotor.comp_resistance_wind(T=Trot, qs=3)
            # putting resistance on stator side in EEC
            R20 = K21Z * Rr

        # compute skin_effect on rotor side
        Tfact2 = CondR.comp_temperature_effect(T_op=Trot, T_ref=T2_ref)
        Xkr_skinR, _ = CondR.comp_skin_effect(freq=felec * par["slip"], Tfact=Tfact2)
        # update resistance value including skin effect
        par["R2"] = R20 * Tfact2 * Xkr_skinR

    if "L2" not in par or par["L2"] is None:
        if is_LUT and LUT.L2 is not None:
            L20 = LUT.L2
            T2_ref = LUT.T2_ref
        elif type_comp_Lr == 1:
            # analytic calculation
            # L2 = machine.rotor.slot.comp_inductance_leakage_ANL() #TODO
            pass
        else:
            # FEA calculation
            # L2 = machine.rotor.slot.comp_inductance_leakage_FEA() #TODO
            pass

        Tfact2 = CondR.comp_temperature_effect(T_op=Trot, T_ref=T2_ref)
        _, Xke_skinR = CondR.comp_skin_effect(freq=felec * par["slip"], Tfact=Tfact2)
        par["L2"] = L20 * Xke_skinR

    # check if inductances have to be calculated
    if "Phi_m" not in par or par["Phi_m"] is None:
        if is_LUT and LUT.Phi_m is not None:
            par["Phi_m"] = LUT.Phi_m
            par["I_m"] = LUT.I_m
        elif type_comp_Lm == 1:
            # analytic calculation
            # Phi_m, I_m = machine.comp_inductance_magnetization_ANL() #TODO
            par["Phi_m"] = None
            par["I_m"] = None

        else:
            # FEA calculation
            # Lm, Im =comp_Lm_FEA(self) #TODO
            par["Phi_m"] = None
            par["I_m"] = None

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

    par["Lm"] = (Phi_r * K21Z * Zsr / 3) / self.I
    L1 = (Phi_s - (Phi_r * K21Z * Zsr / 3)) / self.I
    par["L1"] = L1 * Xke_skinS
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
    K21Z = par["K21Z"]
    I_m = self.I
    Lm = Phi_s / I_m
    L2 = ((Phi_r * K21Z * Zsr / 3) - Phi_s) / self.I

    return Phi_s, I_m
