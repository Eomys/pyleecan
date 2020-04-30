# -*- coding: utf-8 -*-


def get_m(self, value):
    """Convert the value the correct m unit (to display in GUI)

    Parameters
    ----------
    self : Unit
        A Unit object
    value : float
        Value to convert

    Returns
    -------
    value : float
        Converted value in the current unit

    """
    if value is None:
        return None
    if self.unit_m == 1:  # Convert to mm
        return value * 1000
    else:
        return value
