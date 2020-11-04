# -*- coding: utf-8 -*-
from ....Classes.Magnetics import Magnetics


def comp_axes(self, output):
    """Compute the additional axes required in the MagElmer module

    Parameters
    ----------
    self : Magnetic
        a Magnetic object
    output : Output
        an Output object (to update)

    Returns
    -------
    axes_dict: {Data}
        Dict containing Time_Tem axis used in MagFEMM to store torque result
    """
    # Calculate standard axes from Magnetics model
    axes_dict = Magnetics.comp_axes(self, output)

    # Add Time axis on which to calculate torque
    # Copy from standard Time axis
    Time_Tem = axes_dict["Time"].copy()

    # Remove anti-periodicity if any
    if "antiperiod" in Time_Tem.symmetries:
        Time_Tem.symmetries["period"] = Time_Tem.symmetries.pop("antiperiod")

    # Store in axis dict
    axes_dict["Time_Tem"] = Time_Tem

    # Add other axes if requested by Elmer
    # TODO

    return axes_dict
