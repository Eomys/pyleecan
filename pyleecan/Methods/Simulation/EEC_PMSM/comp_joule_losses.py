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

    qs = output.simu.machine.stator.winding.qs
    I_dict = self.OP.get_Id_Iq()
    Id, Iq = I_dict["Id"], I_dict["Iq"]
    R = self.parameters["R20"]

    # Id and Iq are in RMS
    Pj_losses = qs * R * (Id ** 2 + Iq ** 2)

    output.elec.Pj_losses = Pj_losses
