# -*- coding: utf-8 -*-


def comp_width_opening(self):
    """Compute the average opening width of the Slot

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    W0: float
        Average opening width of the slot [m]
    """

    line_list = self.build_geometry()
    Z1 = line_list[0].get_begin()
    Z2 = line_list[-1].get_end()

    return abs(Z2 - Z1)
