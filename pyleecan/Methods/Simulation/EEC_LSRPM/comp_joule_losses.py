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
    I_ds = output.elec.Ids_ref
    I_qs = output.elec.Iqs_ref
    I_da = output.elec.Ida_ref
    I_qa = output.elec.Iqa_ref

    R_s = self.parameters["R_s"]
    R_a = self.parameters["R_a"]

    # Id and Iq are in RMS
    Pj_losses = qs * (R_s * (I_ds**2 + I_qs**2) + R_a * (I_da**2 + I_qa**2))

    output.elec.Pj_losses = Pj_losses
