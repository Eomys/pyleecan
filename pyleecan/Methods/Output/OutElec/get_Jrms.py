from numpy import sqrt


def get_Jrms(self):
    """Return the stator current density rms value

    Parameters
    ----------
    self : OutElec
        an OutElec object

    Returns
    -------
    Jrms: float
        stator current density rms value [A/m^2]
    """

    if self.Jrms is None:
        output = self.parent
        machine = output.simu.machine

        Swire = machine.stator.winding.conductor.comp_surface_active()
        Npcp = machine.stator.winding.Npcp

        Idq_dict = self.OP.get_Id_Iq()

        self.Jrms = sqrt(Idq_dict["Id"] ** 2 + Idq_dict["Iq"] ** 2) / (Swire * Npcp)

    return self.Jrms
