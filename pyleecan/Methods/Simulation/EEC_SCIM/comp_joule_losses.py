# -*- coding: utf-8 -*-
from numpy import mean, zeros
from ....Functions.Electrical.coordinate_transformation import n2ab


def comp_joule_losses(self, output):
    """Compute the electrical Joule losses

    Parameters
    ----------
    self : Electrical
        an Electrical object
    output : Output
        an Output object
    """
    # TODO utilize loss models instead here
    # compute stator joule losses
    qs = output.simu.machine.stator.winding.qs
    Id = output.elec.Id_ref
    Iq = output.elec.Iq_ref
    Rs = self.parameters["Rs"]

    P_joule_s = qs * Rs * (Id ** 2 + Iq ** 2)

    # compute rotor joule losses
    qr = output.simu.machine.rotor.winding.qs
    sym = output.simu.machine.comp_periodicity()[0]
    Rr = self.parameters["Rr_norm"] / self.parameters["norm"] ** 2

    # get the bar currents
    Ir = output.elec.Ir.get_along("time", "phase")["Ir"].T

    # transform rotor current to 2 phase equivalent
    qr_eff = qr // sym
    Ir_2ph = zeros([Ir.shape[0], 2])
    for ii in range(sym):
        id0 = qr_eff * ii
        id1 = qr_eff * (ii + 1)
        Ir_2ph += n2ab(Ir[:, id0:id1], n=qr_eff) / sym

    Ir_mag = abs(Ir_2ph[:, 0] + 1j * Ir_2ph[:, 1])

    P_joule_r = 3 * Rr * mean(Ir_mag ** 2) / 2

    output.elec.Pj_losses = P_joule_s + P_joule_r
