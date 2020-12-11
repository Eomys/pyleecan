# -*- coding: utf-8 -*-
from ....Functions.Plot.plot_2D_Data import plot_2D_Data
from ....definitions import config_dict


def plot_mmf_unit(self, r_max=100, fig=None, is_show_fig=True):
    """Plot the winding unit mmf as a function of space
    Parameters
    ----------
    self : LamSlotWind
        an LamSlotWind object
    Na : int
        Space discretization
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    is_show_fig : bool
        To call show at the end of the method
    """

    # Compute the winding function and mmf
    wf = self.comp_wind_function(per_a=1)
    qs = self.winding.qs
    MMF_U, WF = self.comp_mmf_unit(Nt=1, Na=wf.shape[1])

    color_list = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"][: qs + 1]
    plot_2D_Data(
        WF,
        "angle",
        "phase",
        data_list=[MMF_U],
        fig=fig,
        color_list=color_list,
        is_show_fig=is_show_fig,
    )

    plot_2D_Data(
        WF,
        "wavenumber=[0," + str(r_max) + "]",
        "phase[0]",
        data_list=[MMF_U],
        fig=fig,
        color_list=color_list,
        is_show_fig=is_show_fig,
    )
