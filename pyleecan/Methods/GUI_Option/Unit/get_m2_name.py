# -*- coding: utf-8 -*-


def get_m2_name(self):
    """Return the name of the current area unit

    Parameters
    ----------
    self : Unit
        A Unit object

    Returns
    -------
    unit_name : str
        Name of the current unit
    """
    if self.unit_m2 == 1:
        return "mm²"
    else:
        return "m²"
