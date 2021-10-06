from numpy import pi, array, transpose, where

from SciDataTool import Data1D, DataTime

from ....Functions.Electrical.coordinate_transformation import dq2n
from ....Functions.Winding.gen_phase_list import gen_name


def get_I_harm(self):
    """Return the stator current DataTime object

    Parameters
    ----------
    self : OutElec
        an OutElec object

    """

    # Generate current according to Id/Iq

    felec = self.felec
    I_fund_freq = self.Is.time_to_freq()

    results = I_fund_freq.get_along("freqs", "phase")

    # Remove fundamental value
    freqs = results["freqs"]
    ifund = where(freqs != self.felec)[0]

    Freqs = I_fund_freq.axes[1].copy()
    Freqs.values = results["freqs"][ifund]

    I_harm = I_fund_freq.copy()
    I_harm.axes = [I_fund_freq.axes[0], Freqs]
    I_harm.values = results["I_s"][:, ifund]

    return I_harm
