# -*- coding: utf-8 -*-
from pyleecan.Methods.Machine.Winding import WindingError


def comp_Ncspc(self, Zs=None):
    """Compute the number of coils in series per parallel circuit

    Parameters
    ----------
    self : Winding
        A Winding object
    Zs : int
        number of slot

    Returns
    -------
    Ncspc: float
        Number of coils in series per parallel circuit

    """
    if Zs is None:
        if self.parent is None:
            raise WindingError(
                "ERROR: The Winding object must be in a Lamination object."
            )

        if self.parent.slot is None:
            raise WindingError(
                "ERROR: The Winding object must be in a Lamination object with Slot."
            )

        Zs = self.parent.slot.Zs

    (Nrad, Ntan) = self.get_dim_wind()
    Ncspc = Zs * Nrad * Ntan / (2.0 * self.qs * self.Npcpp)

    return Ncspc
