# -*- coding: utf-8 -*-
from numpy import mean, max as np_max, min as np_min

from SciDataTool import DataTime, VectorField, Data1D

from ....Functions.Winding.gen_phase_list import gen_name


def store(self, out_dict, axes_dict):
    """Store the standard outputs of Electrical that are temporarily in out_dict as arrays into OutElec as Data object

    Parameters
    ----------
    self : OutElec
        the OutElec object to update
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in comp_parameters of EEC
    axes_dict: {Data}
        Dict of axes used for electrical calculation

    """

    self.Pj_losses = out_dict["Pj_losses"]
    self.Tem_av_ref = out_dict["Tem_av_ref"]
    self.Pem_av_ref = out_dict["Pem_av_ref"]
