# -*- coding: utf-8 -*-
from os.path import join

from ....Classes.Magnetics import Magnetics


def store_output(self, output, out_dict, axes_dict):
    """Store the additional outputs of MagFEMM that are temporarily in out_dict into OutMag

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

    # Store MeshSolution object and save it as .h5 file if requested
    if "meshsolution" in out_dict:

        # Store meshsolution in OutMag
        output.mag.meshsolution = out_dict.pop("meshsolution")

        # Save meshsolution as .h5 on disk if requested
        if self.is_save_FEA:
            save_path = self.get_path_save(output)
            save_path_fea = join(save_path, "MeshSolutionFEMM.h5")
            output.mag.meshsolution.save(save_path_fea)
