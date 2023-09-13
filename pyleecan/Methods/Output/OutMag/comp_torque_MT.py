from numpy import pi

from SciDataTool.Functions.derivation_integration import integrate


def comp_torque_MT(self):
    """Compute the rotor electromagnetic torque from Maxwell Stress Tensor.

    Parameters
    ----------
    self : OutMag
        an OutMag object

    Returns
    -------
    Tem_slice : ndarray
        Rotor electromagnetic torque per slice [N]

    """
    Tem_slice = None
    B = self.B

    if (
        B is not None
        and "radial" in B.components.keys()
        and "tangential" in B.components.keys()
    ):
        machine = self.parent.simu.machine

        # Load airgap Maxwell Stress Tensor
        Brphiz = B.get_rphiz_along(
            "time[smallestperiod]",
            "angle[smallestperiod]",
            "z[smallestpattern]",
            is_squeeze=False,
        )

        Br = Brphiz["radial"]
        Bt = Brphiz["tangential"]

        if self.Rag is None:
            R = machine.comp_Rgap_mec()
        else:
            R = self.Rag

        # Magnetic void permeability
        mu_0 = 4 * pi * 1e-7

        # Integrate over angle to get the electromagnetic torque per slice
        Nper, _ = B.get_axes()[1].get_periodicity()
        Tem_slice = (
            R**2
            / mu_0
            * integrate(
                values=Br * Bt,
                ax_val=Brphiz["angle"],
                index=1,
                Nper=Nper,
                is_aper=False,
                is_phys=True,
            )[:, 0, :]
        )

        if Tem_slice.ndim == 1:
            Tem_slice = Tem_slice[:, None]

    return Tem_slice
