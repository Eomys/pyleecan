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

    # Add other axes if requested by Elmer
    # TODO

    return axes_dict
