# -*- coding: utf-8 -*-


from enum import unique


def comp_parameters(self, machine, OP, Tsta=None, Trot=None):
    """Compute the parameters dict for the equivalent electrical circuit:
    resistance, inductance and back electromotive force
    Parameters
    ----------
    self : EEC_ANL
        an EEC_ANL object
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

    PAR = self.parameters
    Cond = machine.stator.winding.conductor
    I_dict = OP.get_Id_Iq()
    Id_ref, Iq_ref = I_dict["Id"], I_dict["Iq"]
    U_dict = OP.get_Ud_Uq()
    Ud_ref, Uq_ref = U_dict["Ud"], U_dict["Uq"]
    self.freq0 = OP.get_felec()

    if "R20" not in PAR:
        PAR["R20"] = machine.stator.comp_resistance_wind()

    # Parameters which may vary for each simulation
    is_comp_ind = False
    # check for complete parameter set
    # (there may be some redundancy here but it seems simplier to implement)
    if not all(k in PAR for k in ("Ld", "Lq")):
        is_comp_ind = True

    # check for d- and q-current (change)
    if "Id" not in PAR or PAR["Id"] != Id_ref:
        PAR["Id"] = Id_ref
        is_comp_ind = True

    if "Iq" not in PAR or PAR["Iq"] != Iq_ref:
        PAR["Iq"] = Iq_ref
        is_comp_ind = True

    # check for d- and q-voltage (change)
    if "Ud" not in PAR or PAR["Ud"] != Ud_ref:
        PAR["Ud"] = Ud_ref

    if "Uq" not in PAR or PAR["Uq"] != Uq_ref:
        PAR["Uq"] = Uq_ref

    # compute inductance if necessary
    if is_comp_ind:
        (phid, phiq) = self.indmag.comp_inductance(
            machine=machine, Id_ref=Id_ref, Iq_ref=Iq_ref
        )
        if PAR["Id"] != 0:
            PAR["Ld"] = (phid - PAR["phi"]) / PAR["Id"]
        else:
            PAR["Ld"] = None  # to have the parameters complete though

        if PAR["Iq"] != 0:
            PAR["Lq"] = phiq / PAR["Iq"]
        else:
            PAR["Lq"] = None  # to have the parameters complete though
