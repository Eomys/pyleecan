# -*- coding: utf-8 -*-
from ....Classes.Magnetics import Magnetics


def store_output(self, output, out_dict, axes_dict):
    """Store the additional outputs of MagElmer that are temporarily in out_dict into OutMag

    Parameters
    ----------
    self : Magnetic
        a Magnetic object
    output : Output
        an Output object (to update)
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in comp_flux_airgap
    axes_dict: {Data}
        Dict of axes used for magnetic calculation

    """

    # Call store_output method of Magnetics to store standard outputs (B, Tem, Phi_wind_stator, emf)
    Magnetics.store_output(self, output, out_dict, axes_dict)

    # Store other output if requested
    # if "output" in out_dict:      #TODO
