# -*- coding: utf-8 -*-


def get_m2(self, value):
    """Convert the value the correct m² unit (to display in GUI)

    Parameters
    ----------
    self : Unit
        A Unit object
    value : float
        Value to convert

    Returns
    -------
    value : float
        Value in the current unit
    """
    if value is None:
        return None
    if self.unit_m2 == 1:  # Convert to mm^2
        return value * 1000000
    else:
        return value
