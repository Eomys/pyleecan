# -*- coding: utf-8 -*-


def comp_joule_losses(self, output):
    """Compute the electrical Joule losses

    Parameters
    ----------
    self : Electrical
        an Electrical object
    output : Output
        an Output object
    """
    # TODO include rotor losses
    # TODO use of output Id Iq may be wrong ???

    qs = output.simu.machine.stator.winding.qs
    Id = output.elec.Id_ref
    Iq = output.elec.Iq_ref
    R = self.parameters["Rs"]

    Pj_losses = qs * R * (Id ** 2 + Iq ** 2) / 2

    output.elec.Pj_losses = Pj_losses
