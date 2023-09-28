def comp_emf(self):
    """Compute the Electromotive force [V]

    Parameters
    ----------
    self : OutMag
        an OutMag object

    """

    # Get stator winding flux
    Phi_wind = self.Phi_wind[self.parent.simu.machine.stator.get_label()]

    EMF = Phi_wind.get_data_along("time=derivate", "phase")

    EMF.name = "Stator Winding Electromotive Force"
    EMF.unit = "V"
    EMF.symbol = "EMF"

    self.emf = EMF
