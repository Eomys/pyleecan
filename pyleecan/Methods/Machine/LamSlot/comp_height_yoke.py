# -*- coding: utf-8 -*-


def comp_height_yoke(self):
    """Compute the yoke height

    Parameters
    ----------
    self : LamSlot
        A LamSlot object

    Returns
    -------
    Hy: float
        yoke height [m]

    """
    if self.slot is not None and self.slot.Zs > 0:
        return self.Rext - self.Rint - self.slot.comp_height()
    else:
        return self.Rext - self.Rint
