# -*- coding: utf-8 -*-

from matplotlib.patches import Patch
from matplotlib.pyplot import axis, legend

from ....Functions.Winding.find_wind_phase_color import find_wind_phase_color
from ....Functions.Winding.gen_phase_list import gen_name
from ....Functions.init_fig import init_fig
from ....definitions import config_dict
from ....Classes.WindingSC import WindingSC

PHASE_COLORS = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]
ROTOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["ROTOR_COLOR"]
STATOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["STATOR_COLOR"]


def plot(
    self,
    fig=None,
    is_lam_only=False,
    sym=1,
    alpha=0,
    delta=0,
    is_edge_only=False,
    is_display=True,
    is_show=True,
):
    """Plot the Lamination in a matplotlib fig

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object
    fig :
        if None, open a new fig and plot, else add to the current
        one (Default value = None)
    is_lam_only : bool
        True to plot only the lamination (remove the Winding)
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_edge_only: bool
        To plot transparent Patches
    is_display : bool
        False to return the patches
    is_show : bool
        To call show at the end of the method
    Returns
    -------
    patches : list
        List of Patches
    """
    if self.is_stator:
        color_lam = STATOR_COLOR
    else:
        color_lam = ROTOR_COLOR

    # Get the LamSlot surface(s)
    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)

    patches = list()
    # getting the number of phases and winding connection matrix
    if self.winding is not None:
        if isinstance(self.winding, WindingSC):  # plot only one phase for WindingSC
            wind_mat = None
            qs = 1
        else:
            Zs = self.get_Zs()
            wind_mat = self.winding.comp_connection_mat(Zs)
            qs = self.winding.qs

    for surf in surf_list:
        if surf.label is not None and "Lamination" in surf.label:
            patches.extend(surf.get_patches(color_lam, is_edge_only=is_edge_only))
        elif "Wind" in surf.label or "Bar" in surf.label:
            if not is_lam_only:
                color = find_wind_phase_color(wind_mat=wind_mat, label=surf.label)
                patches.extend(surf.get_patches(color=color, is_edge_only=is_edge_only))
        else:
            patches.extend(surf.get_patches(is_edge_only=is_edge_only))

    if is_display:
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
        if not is_edge_only:
            if self.is_stator and "Stator" not in label_leg:
                patch_leg.append(Patch(color=STATOR_COLOR))
                label_leg.append("Stator")
                axes.set_title("Stator with Winding")
            elif not self.is_stator and "Rotor" not in label_leg:
                patch_leg.append(Patch(color=ROTOR_COLOR))
                label_leg.append("Rotor")
                axes.set_title("Rotor with Winding")
            # Add the winding legend only if needed
            if not is_lam_only:
                if self.is_stator:
                    prefix = "Stator "
                else:
                    prefix = "Rotor "
                if isinstance(self.winding, WindingSC):
                    patch_leg.append(Patch(color=PHASE_COLORS[0]))
                    label_leg.append(prefix + "Bar")
                else:
                    phase_name = [prefix + n for n in gen_name(qs, is_add_phase=True)]
                    for ii in range(qs):
                        if not phase_name[ii] in label_leg:
                            # Avoid adding twice the same label
                            index = ii % len(PHASE_COLORS)
                            patch_leg.append(Patch(color=PHASE_COLORS[index]))
                            label_leg.append(phase_name[ii])
            legend(patch_leg, label_leg)
        if is_show:
            fig.show()
    else:
        return patches
