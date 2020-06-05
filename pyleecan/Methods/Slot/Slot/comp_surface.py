# -*- coding: utf-8 -*-


def comp_surface(self):
    """Compute the Slot total surface (by numerical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    surf = self.get_surface()
    return surf.comp_surface()
