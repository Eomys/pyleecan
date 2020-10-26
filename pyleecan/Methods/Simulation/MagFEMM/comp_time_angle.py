# -*- coding: utf-8 -*-
from ....Classes.Magnetics import Magnetics


def comp_time_angle(self, output):
    """Compute the time and space discretization of the MagFEMM module

    Parameters
    ----------
    self : Magnetic
        a Magnetic object
    output : Output
        an Output object (to update)

    Returns
    -------
    axes_dict: {Data}
        Dict containing Time axis used in MagFEMM to store torque result
    """
    # Calculate and store Time and Angle axes for airgap flux
    axes_dict = Magnetics.comp_time_angle(self, output)

    # Add Time axis on which to calculate torque
    Time_Tem = axes_dict["Time"].copy()
    if "antiperiod" in Time_Tem.symmetries:
        Time_Tem.symmetries["period"] = Time_Tem.symmetries.pop("antiperiod")

    axes_dict["Time_Tem"] = Time_Tem

    return axes_dict
