from numpy import sqrt


def get_Jrms_max(self):
    """Return the stator current density rms maximum value

    Parameters
    ----------
    self : OutElec
        an OutElec object

    Returns
    -------
    Jrms_max: float
        stator current density rms maximum value [A/m^2]
    """

    if self.Jrms_max is None:

        output = self.parent
        machine = output.simu.machine

        # Calculate maximum current function of current density
        Swire = machine.stator.winding.conductor.comp_surface_active()
        Npcp = machine.stator.winding.Npcp

        Idq_dict = self.OP.get_Id_Iq()

        self.Jrms_max = sqrt(Idq_dict["Id"] ** 2 + Idq_dict["Iq"] ** 2) / (Swire * Npcp)

    return self.Jrms_max
