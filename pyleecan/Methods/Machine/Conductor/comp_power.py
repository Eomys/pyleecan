# -*- coding: utf-8 -*-


def comp_power(self, output):
    """Compute the electrical average power

    Parameters
    ----------
    self : Electrical
        an Electrical object
    output : Output
        an Output object
    """

    qs = output.simu.machine.stator.winding.qs
    I_dict = output.elec.OP.get_Id_Iq()
    Id, Iq = I_dict["Id"], I_dict["Iq"]

    U_dict = output.elec.OP.get_Ud_Uq()
    Ud, Uq = U_dict["Ud"], U_dict["Uq"]

    # All quantities are in RMS
    Pem_av_ref = qs * (Ud * Id + Uq * Iq)

    output.elec.OP.Pem_av_ref = Pem_av_ref
