# -*- coding: utf-8 -*-
"""@package Methods.Machine.VentilationCirc.plot

@date Created on Wed Jan 14 14:27:38 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from matplotlib.patches import Circle, Patch
from matplotlib.pyplot import axis, legend
from numpy import exp, pi

from pyleecan.Functions.init_fig import init_fig


def plot(self, fig=None):
    """Plot the Ventilation in a matplotlib fig

    Parameters
    ----------
    self : VentilationCirc
        A VentilationCirc object
    fig :
        if None, open a new fig and plot, else add to the current
        one (Default value = None)

    Returns
    -------
    None
    """
    self.check()

    patches = list()

    if fig is None:
        color = "k"  # Only the vents are plot
    else:
        color = "w"  # Vents are "air" on a Lamination

    for ii in range(self.Zh.size):  # For every ventilation group
        for jj in range(int(self.Zh[ii])):
            # For every ventilation in one group
            # Computation of center coordinates
            Zc = self.H0[ii] * exp(1j * (jj * 2 * pi / self.Zh[ii] + self.Alpha0[ii]))
            # Creation of the Circle
            patches.append(Circle((Zc.real, Zc.imag), self.D0[ii] / 2.0, color=color))

    # Display the result
    (fig, axes, patch_leg, label_leg) = init_fig(fig)
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    axes.set_title("Axial Ventilation Ducts")

    # Add the magnet to the fig
    for patch in patches:
        axes.add_patch(patch)

    # Axis Setup
    axis("equal")
    Lim = self.comp_radius()[1] * 1.2
    axes.set_xlim(-Lim, Lim)
    axes.set_ylim(-Lim, Lim)

    # Legend setup
    if color != "w":
        patch_leg.append(Patch(color="k"))
        label_leg.append("Ventilations")

        legend(patch_leg, label_leg)
    fig.show()
