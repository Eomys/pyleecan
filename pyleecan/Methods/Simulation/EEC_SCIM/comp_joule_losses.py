# -*- coding: utf-8 -*-
from numpy import mean, zeros
from ....Functions.Electrical.dqh_transformation import n2abc


def comp_joule_losses(self, out_dict, machine):
    """Compute the electrical Joule losses

    Parameters
    ----------
    self : Electrical
        an Electrical object
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in comp_parameters of EEC
    machine : Machine
        a Machine object
    """
    # TODO utilize loss models instead here
    # compute stator joule losses
    qs = machine.stator.winding.qs
    I_dict = self.OP.get_Id_Iq()
    Id, Iq = I_dict["Id"], I_dict["Iq"]
    Rs = self.parameters["Rs"]

    P_joule_s = qs * Rs * (Id ** 2 + Iq ** 2)

    # compute rotor joule losses
    qr = machine.rotor.winding.qs
    p = machine.rotor.winding.p
    Rr = self.parameters["Rr_norm"] / self.parameters["norm"] ** 2

    # get the bar currents
    Ir = machine.parent.parent.elec.Ir.get_along("time", "phase")["Ir"].T

    # transform rotor current to 2 phase equivalent
    qr_eff = qr // p
    Ir_2ph = zeros([Ir.shape[0], 2])
    for ii in range(p):
        id0 = qr_eff * ii
        id1 = qr_eff * (ii + 1)
        Ir_2ph += n2abc(Ir[:, id0:id1], n=qr_eff) / p

    Ir_mag = abs(Ir_2ph[:, 0] + 1j * Ir_2ph[:, 1])

    P_joule_r = 3 * Rr * mean(Ir_mag ** 2) / 2

    out_dict["Pj_losses"] = P_joule_s + P_joule_r

    return out_dict
