# -*- coding: utf-8 -*-

from ....Functions.Plot.plot_A_2D import plot_A_2D
from numpy import pi, linspace, floor, finfo, concatenate, flip, unique
from scipy.interpolate import interp1d


def plot(self):
    """Plots skew angle 
    
    Parameters
    ----------
    self : Skew
        a Skew object

    """

    plot_A_2D(
        linspace(0, self.Nslices, self.Nslices),
        [self.angle_list],
        xlabel="Slice",
        ylabel="Skew angle [rad]",
    )
