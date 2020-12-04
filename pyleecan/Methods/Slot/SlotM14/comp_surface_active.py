# -*- coding: utf-8 -*-


def comp_surface_active(self):
    """Compute the Slot inner active surface (by analytical computation)

    Parameters
    ----------
    self : SlotM14
        A SlotM14 object

    Returns
    -------
    Swind: float
        Slot inner active surface [m**2]

    """

    [_, _, _, _, ZM1, ZM2, _, _, _] = self._comp_point_coordinate()

    R1 = abs(ZM1)
    R2 = abs(ZM2)

    S1 = pi * R1 ** 2 * (self.Wmag / (2 * pi))
    S2 = pi * R2 ** 2 * (self.Wmag / (2 * pi))

    return abs(S1 - S2)
