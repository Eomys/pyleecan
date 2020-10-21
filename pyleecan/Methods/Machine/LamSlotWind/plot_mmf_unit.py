# -*- coding: utf-8 -*-
from numpy import pi
from SciDataTool import Data1D, DataLinspace, DataTime
from ....Functions.Winding.gen_phase_list import gen_name
from ....Functions.Plot.plot_A_space import plot_A_space
from ....definitions import config_dict


def plot_mmf_unit(self, fig=None):
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
    wf = self.comp_wind_function()
    qs = self.winding.qs
    mmf_u = self.comp_mmf_unit(Nt=1, Na=wf.shape[1])

    if len(mmf_u.values.shape) == 1:
        mmf_u.values = mmf_u.values[None, :]  # TODO: correct bug in SciDataTool

    # Create a Data object
    Phase = Data1D(
        name="phase",
        unit="",
        values=gen_name(qs),
        is_components=True,
    )
    Angle = mmf_u.axes[1]
    WF = DataTime(
        name="WF",
        unit="p.u.",
        symbol="Magnitude",
        axes=[Phase, Angle],
        values=wf,
        symmetries=mmf_u.symmetries,
    )

    color_list = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"][: qs + 1]
    plot_A_space(
        WF,
        is_fft=True,
        index_list=[0, 1, 2],
        data_list=[mmf_u],
        fig=fig,
        color_list=color_list,
    )
