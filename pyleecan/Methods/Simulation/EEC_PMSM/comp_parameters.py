from numpy import isscalar


def comp_parameters(
    self, machine, OP, Tsta=None, Trot=None, Id_array=None, Iq_array=None
):
    """Compute the parameters dict for the equivalent electrical circuit:
    resistance, inductance and back electromotive force

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
    Id_array : ndarray
        Array of Id currents for vectorized calculation
    Iq_array : ndarray
        Array of Iq currents for vectorized calculation

    Returns
    ----------
    eec_param: dict
        dictionnary containing EEC parameters

    """

    eec_param = dict()

    if self.parameters is not None:
        eec_param.update(self.parameters)

    is_LUT = self.LUT_enforced is not None
    LUT = self.LUT_enforced

    # Store electrical frequency in parameters
    eec_param["felec"] = OP.get_felec()

    # Store dqh voltages
    eec_param.update(OP.get_Ud_Uq())

    if Id_array is None and Iq_array is None:
        # Store dqh currents
        eec_param.update(OP.get_Id_Iq())
    else:
        # Store arrays of Id / Iq
        eec_param["Id"] = Id_array
        eec_param["Iq"] = Iq_array

    # Get stator conductor
    CondS = machine.stator.winding.conductor

    # compute temperature effect on stator side
    if LUT is not None:
        T1_ref = LUT.T1_ref
    else:
        T1_ref = Tsta
    Tfact1 = CondS.comp_temperature_effect(T_op=Tsta, T_ref=T1_ref)
    if self.type_skin_effect:
        # compute skin_effect on stator side
        Xkr_skinS, Xke_skinS = CondS.comp_skin_effect(
            freq=eec_param["felec"], Tfact=Tfact1
        )
    else:
        Xkr_skinS, Xke_skinS = 1, 1

    # Stator resistance
    if "R1" not in eec_param:
        if is_LUT and LUT.R1 is not None:
            R10 = LUT.R1
        else:
            R10 = machine.stator.comp_resistance_wind()
        eec_param["R1"] = R10 * Tfact1 * Xkr_skinS

    # Stator flux linkage only due to permanent magnets
    if "Phid_mag" not in eec_param or "Phiq_mag" not in eec_param:
        if is_LUT:
            Phi_dqh_mag_mean = LUT.get_Phidqh_mag_mean(
                is_skew=machine.rotor.skew is not None
            )
        else:
            Phi_dqh_mag_mean = self.fluxlink.comp_fluxlinkage(machine)
        eec_param["Phid_mag"] = float(Phi_dqh_mag_mean[0])
        eec_param["Phiq_mag"] = float(Phi_dqh_mag_mean[1])

    # Stator winding flux
    if (
        eec_param["Id"] is not None
        and eec_param["Iq"] is not None
        and ("Phid" not in eec_param or "Phiq" not in eec_param)
    ):
        if is_LUT:
            # Get dqh flux function of current
            Phi_dqh_mean = LUT.interp_Phi_dqh(Id=eec_param["Id"], Iq=eec_param["Iq"])
        else:
            Phi_dqh_mean = self.indmag.comp_inductance(machine=machine, OP_ref=OP)

        eec_param["Phid"] = Phi_dqh_mean[0]  # * Xke_skinS
        eec_param["Phiq"] = Phi_dqh_mean[1]  # * Xke_skinS
        if eec_param["Phid"].size == 1:
            eec_param["Phid"] = float(eec_param["Phid"])
            eec_param["Phiq"] = float(eec_param["Phiq"])

    # compute inductance if necessary
    if "Ld" not in eec_param or "Lq" not in eec_param:

        if (
            isscalar(eec_param["Id"])
            and eec_param["Id"] != 0
            and isscalar(eec_param["Iq"])
            and eec_param["Iq"] != 0
        ):

            eec_param["Ld"] = (eec_param["Phid"] - eec_param["Phid_mag"]) / eec_param[
                "Id"
            ]
            eec_param["Lq"] = (eec_param["Phiq"] - eec_param["Phiq_mag"]) / eec_param[
                "Iq"
            ]

        else:
            eec_param["Ld"] = None
            eec_param["Lq"] = None

    return eec_param
