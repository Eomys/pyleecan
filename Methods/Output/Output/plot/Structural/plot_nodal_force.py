# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from numpy import pi
import plotly.figure_factory as ff

def plot_nodal_force(self, j_t0=0, is_deg=True, out_list=[]):
    """Plot the airgap flux as a function of space

    Parameters
    ----------
    self : Output
        an Output object
    j_t0 : int
        Index of the time vector to plot
    is_deg : bool
        True to plot in degree, False in rad
    out_list : list
        List of Output object to compare
    """

    fig, ax = self.plot_permeability()
    #plt.close("all")
    fx = self.struct.nodal_forces[j_t0]['fx']
    fy = self.struct.nodal_forces[j_t0]["fy"]
    listNd = self.struct.nodal_forces[j_t0]["posf"]
    x = listNd[:, 0]
    y = listNd[:, 1]

    ax.quiver(x, y, fx, fy)

    fig.show()

    return fig
