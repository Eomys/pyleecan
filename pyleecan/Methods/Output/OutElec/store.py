# -*- coding: utf-8 -*-
from numpy import insert

from SciDataTool import DataFreq

from pyleecan.Functions.Electrical.dqh_transformation import dqh2n_DataTime


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
        # Add f=0Hz
        out_dict_harm["axes_list"][0].initial = 0
        out_dict_harm["axes_list"][0].number += 1
        values = insert(out_dict_harm["Is_harm"], 0, 0, axis=0)
        Is_dqh = DataFreq(
            name="Harmonic stator current",
            unit="A",
            symbol="I_s^{harm}",
            axes=out_dict_harm["axes_list"],
            values=values,
        )
        # ifft
        Is_dqh_time = Is_dqh.freq_to_time()
        qs = self.parent.simu.machine.stator.winding.qs
        # back to ABC
        Is_abc = dqh2n_DataTime(Is_dqh_time, qs, is_n_rms=True, phase=self.phase_dir)
        self.Is_harm = Is_abc.time_to_freq()
