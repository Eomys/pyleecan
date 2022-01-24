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

    # Store slip in parameters
    par["slip"] = slip

    # compute temperature effect on stator side
    if LUT is not None:
        T1_ref = LUT.T1_ref
    else:
        T1_ref = Tsta
    Tfact1 = CondS.comp_temperature_effect(T_op=Tsta, T_ref=T1_ref)
    # compute skin_effect on stator side
    Xkr_skinS, Xke_skinS = CondS.comp_skin_effect(freq=felec, Tfact=Tfact1)

    # compute temperature effect on rotor side
    if LUT is not None:
        T2_ref = LUT.T2_ref
    else:
        T2_ref = Trot
    Tfact2 = CondR.comp_temperature_effect(T_op=Trot, T_ref=T2_ref)
    # compute skin_effect on rotor side
    Xkr_skinR, Xke_skinR = CondR.comp_skin_effect(
        freq=felec * par["slip"], Tfact=Tfact2
    )

    # check that parameters are in ELUT, otherwise compute missing ones
    if "U0_ref" not in par or par["U0_ref"] is None:
        par["U0_ref"] = OP.U0_ref

    if "R1" not in par or par["R1"] is None:
        if is_LUT and LUT.R1 is not None:
            R10 = LUT.R1
        else:
            # get resistance calculated analytically at simulation temperature
            R10 = machine.stator.comp_resistance_wind(T=Tsta)

        # add temperature and skin effects
        par["R1"] = R10 * Tfact1 * Xkr_skinS

    if "L1" not in par or par["L1"] is None:
        if is_LUT and LUT.L1 is not None:
            L10 = LUT.L1
        elif type_comp_Ls == 1:
            # analytic calculation
            # L10 = machine.stator.slot.comp_inductance_leakage_ANL() #TODO
            pass
        else:
            # FEA calculation
            # L1 = machine.rotor.slot.comp_inductance_leakage_FEA() #TODO
            pass

        # add temperature and skin effects
        par["L1"] = L10 * Xke_skinS

    if "Rfe" not in par:
        par["Rfe"] = 1e12  # TODO calculate (or estimate at least)

    if "R2" not in par or par["R2"] is None:
        if is_LUT and LUT.R2 is not None:
            R20 = LUT.R2
        else:
            # get resistance calculated analytically at simulation temperature
            Rr = machine.rotor.comp_resistance_wind(T=Trot, qs=3)
            # putting resistance on stator side in EEC
            R20 = K21Z * Rr

        # add temperature and skin effects
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

        # add temperature and skin effects
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
