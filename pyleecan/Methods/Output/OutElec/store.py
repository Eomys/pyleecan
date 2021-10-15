# -*- coding: utf-8 -*-
from numpy import mean, max as np_max, min as np_min

from SciDataTool import DataFreq

from ....Functions.Winding.gen_phase_list import gen_name


def store(self, out_dict, out_dict_harm):
    """Store the standard outputs of Electrical that are temporarily in out_dict as arrays into OutElec as Data object

    Parameters
    ----------
    self : OutElec
        the OutElec object to update
    out_dict : dict
        Dict containing all electrical quantities that have been calculated in EEC
    out_dict_harm : dict
        Dict containing harmonic quantities that have been calculated in EEC

    """

    # Store Id, Iq, Ud, Uq
    self.OP.Id_ref = out_dict["Id"]
    self.OP.Iq_ref = out_dict["Iq"]
    self.OP.Ud_ref = out_dict["Ud"]
    self.OP.Uq_ref = out_dict["Uq"]

    # Compute currents
    self.Is = None
    self.Is = self.get_Is()

    # Compute voltage
    self.Us = None
    self.Us = self.get_Us()

    self.Pj_losses = out_dict["Pj_losses"]
    self.Tem_av_ref = out_dict["Tem_av_ref"]
    self.Pem_av_ref = out_dict["Pem_av_ref"]

    if "Is_harm" in out_dict_harm:
        # Create Data object
        axes_list = self.Us_harm.get_axes()
        self.Is_harm = DataFreq(
            name="Harmonic stator current",
            unit="A",
            symbol="I_s^{harm}",
            axes=axes_list,
            values=out_dict_harm["Is_harm"],
        )
