# -*- coding: utf-8 -*-

from numpy import pi, sin, arcsin


def comp_surface_active(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]
    """

    R0 = self._comp_R0()
    alpha = float(2 * arcsin(self.W0 / (2 * R0)))
    # Area of the full circle
    S1 = pi * (R0**2)
    # Area of the top Arc
    S2 = (R0**2.0) / 2.0 * (alpha - sin(alpha))
    # Arc of the bore
    alpha_op = self.comp_angle_opening()
    S3 = (self.get_Rbo() ** 2.0) / 2.0 * (alpha_op - sin(alpha_op))

    if self.H0 < self.W0 / 2:
        # Center is in airgap
        if self.is_outwards():
            return S2 - S3
        else:
            return S2 + S3
    else:  # Center is in the Lamination
        if self.is_outwards():
            return S1 - S2 - S3
        else:
            return S1 - S2 + S3
