# -*- coding: utf-8 -*-
"""@package Methods.Geometry.SurfLine.plot_lines
Surface Contour Line plot method
@date Created on Wed Dec 10 10:35:39 2014
@author sebastian_g
"""

from matplotlib.pyplot import axis, legend
from numpy import real, imag

from pyleecan.Functions.init_fig import init_fig


def plot_lines(self, fig=None):
    """Plot the SurfLine-Contour in a matplotlib fig

    Parameters
    ----------
    self : SurfLine
        A SurfLine object
    fig :
        if None, open a new fig and plot, else add to the
        current one (Default value = None)
   
    Returns
    -------
    None
    """

    (fig, axes, patch_leg, label_leg) = init_fig(fig)
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")

    points = self.discretize(10)

    for idx in range(len(points) - 1):
        z1 = points[idx]
        z2 = points[idx+1]
        x1 = real(z1)
        y1 = imag(z1)
        x2 = real(z2)
        y2 = imag(z2)
        axes.plot([x1, x2], [y1, y2],'k')

    # Axis Setup
    axis("equal")

    fig.show()
