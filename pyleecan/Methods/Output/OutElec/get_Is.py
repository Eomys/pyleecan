from numpy import pi, array, transpose

from SciDataTool import Data1D, DataTime

from ....Functions.Electrical.coordinate_transformation import dq2n
from ....Functions.Winding.gen_phase_list import gen_name


def get_Is(self, Time=None, is_current_harm=False):
    """Return the stator current DataTime object

    Parameters
    ----------
    self : OutElec
        an OutElec object

    """
    # Calculate stator currents if Is is not in OutElec
    if self.Is is None or is_current_harm:
        self.Is = self.get_I_fund(Time=Time)
        
    return self.Is
