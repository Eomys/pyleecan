# -*- coding: utf-8 -*-


def comp_surface_active(self):
    """Compute the Slot active inner surface (by analytical computation)

    Parameters
    ----------
    self : SlotM12
        A SlotM12 object

    Returns
    -------
    Swind: float
        Slot active inner surface [m**2]

    """

    S1 = self.Hmag * self.Wmag
    S2 = 0  # TODO Top arc
    return S1 + S2
