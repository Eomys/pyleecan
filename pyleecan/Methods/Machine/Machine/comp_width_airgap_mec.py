# -*- coding: utf-8 -*-


def comp_width_airgap_mec(self):
    """Compute the mechanical airgap (mag_airgap - magnet or ring)

    Parameters
    ----------
    self: Machine
        Machine object
    Returns
    -------
    mec_gap: float
        The mechanical airgap [m]

    """

    if self.rotor.is_internal:
        return self.stator.comp_radius_mec() - self.rotor.comp_radius_mec()
    else:
        return self.rotor.comp_radius_mec() - self.stator.comp_radius_mec()
