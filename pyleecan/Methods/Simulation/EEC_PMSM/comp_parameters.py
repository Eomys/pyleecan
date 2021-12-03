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
    """

    if self.parameters is None:
        self.parameters = dict()
    par = self.parameters

    is_LUT = self.LUT_enforced is not None
    LUT = self.LUT_enforced

    # Store electrical frequency in parameters
    par["felec"] = OP.get_felec()

    # Store dqh voltages
    par.update(OP.get_Ud_Uq())

    if Id_array is None and Iq_array is None:
        # Store dqh currents
        par.update(OP.get_Id_Iq())
    else:
        # Store arrays of Id / Iq
        par["Id"] = Id_array
        par["Iq"] = Iq_array

    # Get stator conductor
    CondS = machine.stator.winding.conductor

    # compute temperature effect on stator side
    if LUT is not None:
        T1_ref = LUT.T1_ref
    else:
        T1_ref = Tsta
    Tfact1 = CondS.comp_temperature_effect(T_op=Tsta, T_ref=T1_ref)
    # compute skin_effect on stator side
    Xkr_skinS, Xke_skinS = CondS.comp_skin_effect(freq=par["felec"], Tfact=Tfact1)

    # Stator resistance
    if "R1" not in par:
        if is_LUT and LUT.R1 is not None:
            R10 = LUT.R1
        else:
            R10 = machine.stator.comp_resistance_wind()
        par["R1"] = R10 * Tfact1 * Xkr_skinS

    # Stator flux linkage only due to permanent magnets
    if "Phid_mag" not in par or "Phiq_mag" not in par:
        if is_LUT:
            Phi_dqh_mag_mean = LUT.get_Phidqh_mag_mean()
        else:
            Phi_dqh_mag_mean = self.fluxlink.comp_fluxlinkage(machine)
        par["Phid_mag"] = float(Phi_dqh_mag_mean[0])
        par["Phiq_mag"] = float(Phi_dqh_mag_mean[1])

    # Stator winding flux
    if (
        par["Id"] is not None
        and par["Iq"] is not None
        and ("Phid" not in par or "Phiq" not in par)
    ):
        if is_LUT:
            # Get dqh flux function of current
            Phi_dqh_mean = LUT.interp_Phi_dqh(Id=par["Id"], Iq=par["Iq"])
        else:
            Phi_dqh_mean = self.indmag.comp_inductance(machine=machine, OP_ref=OP)

        par["Phid"] = Phi_dqh_mean[0]  # * Xke_skinS
        par["Phiq"] = Phi_dqh_mean[1]  # * Xke_skinS
        if par["Phid"].size == 1:
            par["Phid"] = float(par["Phid"])
            par["Phiq"] = float(par["Phiq"])

    # compute inductance if necessary
    if "Ld" not in par or "Lq" not in par:

        if (
            isscalar(par["Id"])
            and par["Id"] != 0
            and isscalar(par["Iq"])
            and par["Iq"] != 0
        ):

            par["Ld"] = (par["Phid"] - par["Phid_mag"]) / par["Id"]
            par["Lq"] = (par["Phiq"] - par["Phiq_mag"]) / par["Iq"]

        else:
            par["Ld"] = None
            par["Lq"] = None
