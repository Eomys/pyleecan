from numpy import exp


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

    Returns
    ----------
    eec_param: dict
        dictionnary containing EEC parameters
    """

    eec_param = dict()

    if self.parameters is not None:
        eec_param.update(self.parameters)

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
    eec_param["K21Z"] = K21Z
    eec_param["K21I"] = K21I

    # Store electrical frequency in parameters
    eec_param["felec"] = felec

    # Store slip in parameters
    eec_param["slip"] = slip

    # compute temperature effect on stator side
    if LUT is not None:
        T1_ref = LUT.T1_ref
    else:
        T1_ref = Tsta
    Tfact1 = CondS.comp_temperature_effect(T_op=Tsta, T_ref=T1_ref)
    if self.type_skin_effect:
        # compute skin_effect on stator side
        Xkr_skinS, Xke_skinS = CondS.comp_skin_effect(freq=felec, Tfact=Tfact1)
    else:
        Xkr_skinS, Xke_skinS = 1, 1

    # compute temperature effect on rotor side
    if LUT is not None:
        T2_ref = LUT.T2_ref
    else:
        T2_ref = Trot
    Tfact2 = CondR.comp_temperature_effect(T_op=Trot, T_ref=T2_ref)
    if self.type_skin_effect and felec * eec_param["slip"] > 0:
        # compute skin_effect on rotor side
        Xkr_skinR, Xke_skinR = CondR.comp_skin_effect(
            freq=felec * eec_param["slip"], Tfact=Tfact2
        )
    else:
        Xkr_skinR, Xke_skinR = 1, 1

    # check that parameters are in ELUT, otherwise compute missing ones
    if (
        "U0_ref" not in eec_param or eec_param["U0_ref"] is None
    ) and OP.U0_ref is not None:
        UPhi0_ref = 0 if OP.UPhi0_ref is None else OP.UPhi0_ref
        eec_param["U0_ref"] = OP.U0_ref * exp(1j * UPhi0_ref)

    elif (
        "I0_ref" not in eec_param or eec_param["I0_ref"] is None
    ) and OP.I0_ref is not None:
        IPhi0_ref = 0 if OP.IPhi0_ref is None else OP.IPhi0_ref
        eec_param["I0_ref"] = OP.I0_ref * exp(1j * IPhi0_ref)

    if "R1" not in eec_param or eec_param["R1"] is None:
        if is_LUT and LUT.R1 is not None:
            R10 = LUT.R1
        else:
            # get resistance calculated analytically at simulation temperature
            R10 = machine.stator.comp_resistance_wind(T=Tsta)

        # update resistance value including skin effect
        eec_param["R1"] = R10 * Tfact1 * Xkr_skinS

    if "L1" not in eec_param or eec_param["L1"] is None:
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

        eec_param["L1"] = L10 * Xke_skinS

    if "Rfe" not in eec_param:
        eec_param["Rfe"] = 1e12  # TODO calculate (or estimate at least)

    if "R2" not in eec_param or eec_param["R2"] is None:
        if is_LUT and LUT.R2 is not None:
            R20 = LUT.R2
        else:
            # get resistance calculated analytically at simulation temperature
            Rr = machine.rotor.comp_resistance_wind(T=Trot, qs=3)
            # putting resistance on stator side in EEC
            R20 = K21Z * Rr

        # update resistance value including skin effect
        eec_param["R2"] = R20 * Tfact2 * Xkr_skinR

    if "L2" not in eec_param or eec_param["L2"] is None:
        if is_LUT and LUT.L2 is not None:
            L20 = LUT.L2
            T2_ref = LUT.T2_ref
        elif type_comp_Lr == 1:
            # analytic calculation
            # L10 = machine.stator.slot.comp_inductance_leakage_ANL() #TODO
            pass
        else:
            # FEA calculation
            # L1 = machine.rotor.slot.comp_inductance_leakage_FEA() #TODO
            pass

        # add temperature and skin effects
        eec_param["L1"] = L10 * Xke_skinS

    if "Rfe" not in eec_param:
        eec_param["Rfe"] = 1e12  # TODO calculate (or estimate at least)

    if "R2" not in eec_param or eec_param["R2"] is None:
        if is_LUT and LUT.R2 is not None:
            R20 = LUT.R2
        else:
            # get resistance calculated analytically at simulation temperature
            Rr = machine.rotor.comp_resistance_wind(T=Trot, qs=3)
            # putting resistance on stator side in EEC
            R20 = K21Z * Rr

        # add temperature and skin effects
        eec_param["R2"] = R20 * Tfact2 * Xkr_skinR

    if "L2" not in eec_param or eec_param["L2"] is None:
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
        eec_param["L2"] = L20 * Xke_skinR

    # check if inductances have to be calculated
    if "Phi_m" not in eec_param or eec_param["Phi_m"] is None:
        if is_LUT and LUT.Phi_m is not None:
            eec_param["Phi_m"] = LUT.Phi_m
            eec_param["I_m"] = LUT.I_m
        elif type_comp_Lm == 1:
            # analytic calculation
            # Phi_m, I_m = machine.comp_inductance_magnetization_ANL() #TODO
            eec_param["Phi_m"] = None
            eec_param["I_m"] = None

        else:
            # FEA calculation
            # Lm, Im =comp_Lm_FEA(self) #TODO
            eec_param["Phi_m"] = None
            eec_param["I_m"] = None

    return eec_param
