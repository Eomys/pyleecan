# -*- coding: utf-8 -*-
from ....Methods.Machine.Winding import WindingError


def comp_Ntsp(self, Zs=None):
    """Compute the number of turns in series per phase

    Parameters
    ----------
    self : Winding
        A Winding object
    Zs : int
        Number of slot

    Returns
    -------
    Ntspc: float
        Number of turns in series per phase

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

    # effective number of turns in series per phase from connection matrix
    Ntspc_eff_ = (
        abs(self.get_connection_mat(Zs).sum(axis=(0, 1))).sum(axis=0) / self.Npcp / 2
    )
    if Ntspc_eff_.std() != 0:
        self.get_logger().warning(
            "Winding.comp_Ntsp: "
            "Uneven number of turns in series per phase. "
            + "Mean number of turns will be used."
        )

    Ntspc_eff = Ntspc_eff_.mean()

    return Ntspc_eff
