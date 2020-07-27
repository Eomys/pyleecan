# -*- coding: utf-8 -*-
from numpy import pi
from SciDataTool import Data1D, DataLinspace, DataTime
from ....Functions.Winding.gen_phase_list import gen_name
from ....Functions.Plot.plot_A_space import plot_A_space
from ....definitions import config_dict


def plot_mmf_unit(self, Na=2048, fig=None):
    """Plot the winding unit mmf as a function of space
    Parameters
    ----------
    self : LamSlotWind
        an LamSlotWind object
    Na : int
        Space discretization
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    """

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
    Br = DataTime(
        name="WF", unit="p.u.", symbol="Magnitude", axes=[Phase, Angle], values=wf
    )

    color_list = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"][: qs + 1]
    plot_A_space(
        Br,
        is_fft=True,
        index_list=[0, 1, 2],
        data_list=[mmf_u],
        fig=fig,
        color_list=color_list,
    )
