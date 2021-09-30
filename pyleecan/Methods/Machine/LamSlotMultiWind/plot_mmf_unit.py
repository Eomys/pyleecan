# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc
from ....Functions.Plot import dict_2D
from ....definitions import config_dict


def plot_mmf_unit(self, r_max=100, fig=None, is_show_fig=True):
    """Plot the winding unit mmf as a function of space
    Parameters
    ----------

    self : LamSlotMultiWind
        an LamSlotMultiWind object
    Na : int
        Space discretization
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    is_show_fig : bool
        To call show at the end of the method
    """

    name = ""
    if self.parent is not None and self.parent.name not in [None, ""]:
        name += self.parent.name + " "
    if self.is_stator:
        name += "Stator "
    else:
        name += "Rotor "

    # Compute the winding function and mmf
    wf = self.comp_wind_function(per_a=1)
    qs = self.winding.qs
    MMF_U, WF = self.comp_mmf_unit(Nt=1, Na=wf.shape[1])

    color_list = config_dict["PLOT"]["COLOR_DICT"]["COLOR_LIST"][:qs]

    dict_2D_0 = dict_2D.copy()
    dict_2D_0["color_list"] = color_list + ["k"]

    fig, axs = plt.subplots(2, 1, tight_layout=True, figsize=(8, 8))

    WF.plot_2D_Data(
        "angle{°}",
        "phase[]",
        data_list=[MMF_U],
        fig=fig,
        ax=axs[0],
        is_show_fig=is_show_fig,
        win_title=name + "Phase MMF over space",
        **dict_2D_0,
    )

    dict_2D_0["color_list"] = [color_list[0], "k"]

    WF.plot_2D_Data(
        "wavenumber=[0," + str(r_max) + "]",
        data_list=[MMF_U],
        fig=fig,
        ax=axs[1],
        is_show_fig=is_show_fig,
        win_title=name + "Phase MMF FFT",
        **dict_2D_0,
    )
