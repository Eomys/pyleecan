# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlotWind.plot
Lamination with Winding plot method
@date Created on Wed Dec 10 10:35:39 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from matplotlib.patches import Patch
from matplotlib.pyplot import axis, legend

from pyleecan.Functions.Winding.find_wind_phase_color import find_wind_phase_color
from pyleecan.Functions.init_fig import init_fig
from pyleecan.Methods.Machine import PHASE_COLOR, PHASE_NAME, ROTOR_COLOR, STATOR_COLOR
from pyleecan.Classes.WindingSC import WindingSC


def plot(self, fig=None, plot_winding=True, sym=1, alpha=0, delta=0):
    """Plot the Lamination in a matplotlib fig

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object
    fig :
        if None, open a new fig and plot, else add to the current
        one (Default value = None)
    plot_winding : bool
        If True, plot the winding area (Default value = True)
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation

    Returns
    -------
    None
    """
    if self.is_stator:
        color_lam = STATOR_COLOR
    else:
        color_lam = ROTOR_COLOR

    Zs = self.slot.Zs
    # Get the LamSlot surface(s)
    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)

    patches = list()
    # getting the matrix  wind_mat [Nrad,Ntan,Zs,qs] representing the winding
    if type(self.winding) is WindingSC:
        wind_mat = None
    else:
        try:
            wind_mat = self.winding.comp_connection_mat(Zs)
            (Nrad, Ntan, Zs, qs) = wind_mat.shape
        except Exception:
            wind_mat = None
    if wind_mat is None:
        qs = 1  # getting number of surface in winding Zone in the Slot
    for surf in surf_list:
        if surf.label is not None and "Ext" in surf.label:
            patches.append(surf.get_patch(color_lam))
        elif ("Wind" in surf.label or "Bare" in surf.label) and plot_winding:
            color = find_wind_phase_color(wind_mat=wind_mat, label=surf.label)
            patches.append(surf.get_patch(color=color))
        else:
            patches.append(surf.get_patch())

    # Display the result
    (fig, axes, patch_leg, label_leg) = init_fig(fig)
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    for patch in patches:
        axes.add_patch(patch)
    # Axis Setup
    axis("equal")

    # The Lamination is centered in the figure
    Lim = self.Rext * 1.5
    axes.set_xlim(-Lim, Lim)
    axes.set_ylim(-Lim, Lim)

    # Add the legend
    if self.is_stator:
        patch_leg.append(Patch(color=STATOR_COLOR))
        label_leg.append("Stator")
        axes.set_title("Stator with Winding")
    else:
        patch_leg.append(Patch(color=ROTOR_COLOR))
        label_leg.append("Rotor")
        axes.set_title("Rotor with Winding")
    for ii in range(qs):
        if not ("Phase " + PHASE_NAME[ii] in label_leg):
            # Avoid adding twice the same label
            index = ii % len(PHASE_COLOR)
            patch_leg.append(Patch(color=PHASE_COLOR[index]))
            label_leg.append("Phase " + PHASE_NAME[ii])
    legend(patch_leg, label_leg)
    fig.show()
