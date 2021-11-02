from numpy import isscalar


def comp_parameters(self, machine, OP, Tsta=None, Trot=None):
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
    # TODO maybe set currents to small value if I is 0 to compute inductance

    # OPdq = N0, felec, Id, Iq, Ud, Uq, Tem, Pem
    # OPslip = N0, felec, U0, slip, I0, Phi0, Tem, Pem

    PAR = self.parameters
    Cond = machine.stator.winding.conductor

    I_dict = OP.get_Id_Iq()
    Id_ref, Iq_ref = I_dict["Id"], I_dict["Iq"]

    U_dict = OP.get_Ud_Uq()
    Ud_ref, Uq_ref = U_dict["Ud"], U_dict["Uq"]

    # Update frequency with current OP and store frequency in EEC
    self.freq0 = OP.get_felec()
    felec = self.freq0

    # compute skin_effect
    Xkr_skinS, Xke_skinS = Cond.comp_skin_effect(T=Tsta, freq=felec)

    # Stator resistance
    if "R20" not in PAR:
        R20 = machine.stator.comp_resistance_wind()
        PAR["R20"] = R20 * Xkr_skinS

    # Stator flux linkage
    if "phi" not in PAR and Ud_ref is not None and Uq_ref is not None:
        PAR["phi"] = self.fluxlink.comp_fluxlinkage(machine)

    # Parameters which may vary for each simulation
    is_comp_ind = False
    # check for complete parameter set
    # (there may be some redundancy here but it seems simplier to implement)
    if (
        Ud_ref is not None
        and Uq_ref is not None
        and not all(k in PAR for k in ("Phid", "Phiq", "Ld", "Lq"))
    ):
        is_comp_ind = True

    # check for d- and q-current (change)
    if "Id" not in PAR or (isscalar(PAR["Id"]) and PAR["Id"] != Id_ref):
        PAR["Id"] = Id_ref
        is_comp_ind = True

    if "Iq" not in PAR or (isscalar(PAR["Iq"]) and PAR["Iq"] != Iq_ref):
        PAR["Iq"] = Iq_ref
        is_comp_ind = True

    # check for d- and q-voltage (change)
    if Ud_ref is not None and (
        "Ud" not in PAR or (isscalar(PAR["Ud"]) and PAR["Ud"] != Ud_ref)
    ):
        PAR["Ud"] = Ud_ref

    if Uq_ref is not None and (
        "Uq" not in PAR or (isscalar(PAR["Uq"]) and PAR["Uq"] != Uq_ref)
    ):
        PAR["Uq"] = Uq_ref

    # compute inductance if necessary
    if is_comp_ind:
        (phid, phiq) = self.indmag.comp_inductance(machine=machine, OP_ref=OP)
        PAR["Phid"] = phid * Xke_skinS
        PAR["Phiq"] = phiq * Xke_skinS

        if PAR["Id"] != 0 and "phi" in PAR and Ud_ref is not None:
            PAR["Ld"] = (PAR["Phid"] - PAR["phi"]) / PAR["Id"]
        else:
            PAR["Ld"] = None  # to have the parameters complete though

        if PAR["Iq"] != 0 and Uq_ref is not None:
            PAR["Lq"] = PAR["Phiq"] / PAR["Iq"]
        else:
            PAR["Lq"] = None  # to have the parameters complete though
