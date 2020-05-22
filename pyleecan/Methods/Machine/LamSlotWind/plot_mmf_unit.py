# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from numpy import pi, linspace, zeros, sqrt, dot, array, squeeze
from SciDataTool import Data1D, DataLinspace, DataTime
from ....Functions.Electrical.coordinate_transformation import dq2n
from ....Functions.Winding.gen_phase_list import gen_name


def plot_mmf_unit(self, Na=2048):
    """Plot the winding unit mmf as a function of space
    Parameters
    ----------
    self : LamSlotWind
        an LamSlotWind object
    Na : int
        Space discretization
    """

    # Create an empty Output object to use the generic plot methods
    module = __import__("pyleecan.Classes.Output", fromlist=["Output"])
    Output = getattr(module, "Output")
    out = Output()

    # Compute the winding function and mmf
    wf = self.comp_wind_function(Na=Na)
    qs = self.winding.qs
    mmf_u = self.comp_mmf_unit(Na=Na)

    # Create a Data object
    Phase = Data1D(
        name="phase",
        unit="",
        values=gen_name(qs, is_add_phase=True),
        is_components=True,
    )
    Angle = DataLinspace(
        name="angle",
        unit="rad",
        symmetries={},
        initial=0,
        final=2 * pi,
        number=Na,
        include_endpoint=False,
    )
    out.mag.Br = DataTime(
        name="WF", unit="p.u.", symbol="Magnitude", axes=[Phase, Angle], values=wf
    )

    out.plot_A_space("mag.Br", is_fft=True, index_list=[0, 1, 2], data_list=[mmf_u])
