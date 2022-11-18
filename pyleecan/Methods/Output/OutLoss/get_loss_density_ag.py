from numpy import pi


def get_loss_density_ag(self):
    """Get loss density in the airgap

    Parameters
    ----------
    self : OutLoss
        an OutLoss object

    Returns
    -------
    loss_density_ag : float
        airgap loss density [W/m^2]

    """

    loss = self.get_loss_overall()

    machine = self.parent.simu.machine

    Rag = machine.comp_Rgap_mec()
    Sag = 2 * pi * Rag * machine.stator.L1

    loss_density_ag = loss / Sag

    return loss_density_ag
