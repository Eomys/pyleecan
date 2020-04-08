# -*- coding: utf-8 -*-


def comp_width_airgap_mag(self):
    """Compute the magnetic airgap (distance beetween the two Lamination)

    Parameters
    ----------
    self: Machine
        A Machine object
    Returns
    -------
    mag_gap: float
        The magnetic airgap [m]

    """

    if self.rotor.is_internal:
        return self.stator.Rint - self.rotor.Rext
    else:
        return self.rotor.Rint - self.stator.Rext
