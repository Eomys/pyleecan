from matplotlib.patches import Patch, FancyArrowPatch
import matplotlib.pyplot as plt
from swat_em import datamodel
from numpy import sqrt

from ....Functions.labels import decode_label, WIND_LAB, BAR_LAB, LAM_LAB, WEDGE_LAB
from ....Functions.Winding.find_wind_phase_color import find_wind_phase_color
from ....Functions.Winding.gen_phase_list import gen_name
from ....Functions.init_fig import init_fig
from ....Functions.Plot import dict_2D
from ....definitions import config_dict
from ....Classes.WindingSC import WindingSC
from ....Classes.WindingUD import WindingUD

PHASE_COLORS = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]
ROTOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["ROTOR_COLOR"]
STATOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["STATOR_COLOR"]
if "WEDGE_COLOR" not in config_dict["PLOT"]["COLOR_DICT"]:
    config_dict["PLOT"]["COLOR_DICT"]["WEDGE_COLOR"] = "y"
WEDGE_COLOR = config_dict["PLOT"]["COLOR_DICT"]["WEDGE_COLOR"]
PLUS_HATCH = "++"
MINUS_HATCH = ".."


def plot(
    self,
    fig=None,
    ax=None,
    is_lam_only=False,
    sym=1,
    alpha=0,
    delta=0,
    is_edge_only=False,
    edgecolor=None,
    is_add_arrow=False,
    is_display=True,
    is_add_sign=True,
    is_show_fig=True,
    save_path=None,
    win_title=None,
    is_legend=True,
    is_clean_plot=False,
    is_winding_connection=False,
    is_winding_connection_phase_A=False,
):
    """Plot the Lamination in a matplotlib fig

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
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
    edgecolor:
        Color of the edges if is_edge_only=True
    is_display : bool
        False to return the patches
    is_add_sign : bool
        True to Add + / - on the winding
    is_show_fig : bool
        To call show at the end of the method
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    win_title : str
        Title for the window
    is_legend : bool
        True to add the legend
    is_clean_plot : bool
        True to remove title, legend, axis (only machine on plot with white background)
    is_winding_connection : bool
        True to display winding connections (plot based on plot_polar_layout method of swat-em)
    is_winding_connection : bool
        True to display winding connections on phase A only
    Returns
    -------
    patches : list
        List of Patches
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """
    # Arrow style
    head = None
    style = "Simple, tail_width=2, head_width=8, head_length=12"
    kw = dict(arrowstyle=style, linewidth=0.8, edgecolor="k")

    if self.is_stator:
        color_lam = STATOR_COLOR
    else:
        color_lam = ROTOR_COLOR

    # If the winding is user defined, we can not plot the radial pattern
    if isinstance(self.winding, WindingUD):
        is_winding_connection = False

    # Get the LamSlot surface(s)
    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)

    patches = list()
    # getting the number of phases and winding connection matrix
    if self.winding is not None:
        if isinstance(self.winding, WindingSC):  # plot only one phase for WindingSC
            wind_mat = None
            qs = 1
        else:
            try:
                wind_mat = self.winding.get_connection_mat(self.get_Zs())
                qs = self.winding.qs
                # Calling swat-em method for the winding if we want to plot the radial pattern
                if is_winding_connection:
                    # generate a datamodel for the winding
                    wdg = datamodel()
                    # generate winding from inputs
                    wdg.genwdg(
                        Q=self.get_Zs(),
                        P=2 * self.get_pole_pair_number(),
                        m=qs,
                        layers=self.winding.Nlayer,
                        turns=self.winding.Ntcoil,
                        w=self.winding.coil_pitch,
                    )
                    head = wdg.get_wdg_overhang(optimize_overhang=False)
            except:
                wind_mat = None
                qs = 1
    else:
        wind_mat = None
        qs = 1

    for surf in surf_list:
        label_dict = decode_label(surf.label)
        if LAM_LAB in label_dict["surf_type"]:
            patches = surf.get_patches(
                color_lam, is_edge_only=is_edge_only, edgecolor=edgecolor
            )
            # Add transparency to stator lamination when arrows are added
            if head is not None and self.is_stator:
                # Only adding transparency to the first surface as the second is a white circle
                patches[0]._alpha = 0.2
            patches.extend(patches)
        elif WIND_LAB in label_dict["surf_type"] or BAR_LAB in label_dict["surf_type"]:
            if not is_lam_only:
                color, sign = find_wind_phase_color(wind_mat=wind_mat, label=surf.label)
                if sign == "+" and is_add_sign:
                    hatch = PLUS_HATCH
                elif sign == "-" and is_add_sign:
                    hatch = MINUS_HATCH
                else:
                    hatch = None
                patches.extend(
                    surf.get_patches(
                        color=color,
                        is_edge_only=is_edge_only,
                        hatch=hatch,
                        edgecolor=edgecolor,
                    )
                )
        elif WEDGE_LAB in label_dict["surf_type"] and not is_lam_only:
            patches.extend(surf.get_patches(WEDGE_COLOR, is_edge_only=is_edge_only))
        else:
            patches.extend(
                surf.get_patches(is_edge_only=is_edge_only, edgecolor=edgecolor)
            )

    # Adding arrows between slots for winding radial pattern
    if head is not None:
        # Taking into account slot shifting transformation
        if self.winding.Nslot_shift_wind not in [0, None]:
            Nslot_shift_wind = self.winding.Nslot_shift_wind
        else:
            Nslot_shift_wind = 0

        # Permuting B and C if asked
        if self.winding.is_permute_B_C:
            head_2 = head.copy()
            head_2[1] = head[2]
            head_2[2] = head[1]
            head = head_2

        # Detecting the direction of the layer (tangential or radial)
        # If Nlayer > 1 then we have to precise if the direction is tangential or radial
        # If Nlayer ==1 then checking radial but value always equal to 0
        Nrad, Ntan = self.winding.get_dim_wind()
        if Nrad < Ntan:
            layer_id_name = "T_id"
        else:
            layer_id_name = "R_id"

        Zs = self.get_Zs()
        for idx_phase, phase in enumerate(head):
            # Take into account case where only want to plot one phase for readability
            if is_winding_connection_phase_A and idx_phase != 0:
                break
            for coil in phase:
                # Recovering the starting and ending slot index of the coil (applying reverse layer transformation if needed)
                if self.winding.is_reverse_wind:
                    start_slot_idx = Zs + Nslot_shift_wind + 1 - coil[0][0]
                    end_slot_idx = Zs + Nslot_shift_wind + 1 - coil[0][1]
                else:
                    start_slot_idx = coil[0][0] + Nslot_shift_wind
                    end_slot_idx = coil[0][1] + Nslot_shift_wind

                # Recovering the starting and ending slot layer index of the coil (applying reverse layer transformation if needed)
                if (
                    self.winding.is_reverse_layer
                    ^ (self.winding.is_reverse_wind and layer_id_name == "T_id")
                    ^ (
                        self.winding.is_reverse_wind
                        and layer_id_name == "R_id"
                        and self.is_internal
                    )
                ):
                    start_slot_layer_idx = coil[3][0]
                    end_slot_layer_idx = coil[3][1]
                else:
                    start_slot_layer_idx = self.winding.Nlayer - 1 - coil[3][0]
                    end_slot_layer_idx = self.winding.Nlayer - 1 - coil[3][1]

                start_slot = (start_slot_idx, start_slot_layer_idx)
                end_slot = (end_slot_idx, end_slot_layer_idx)

                # If the value is geater than Zs putting it back between 1 and Zs
                if start_slot[0] > Zs:
                    start_slot = (start_slot[0] % Zs, start_slot[1])
                if end_slot[0] > Zs:
                    end_slot = (end_slot[0] % Zs, end_slot[1])

                # Recovering the winding direction:  1-> from left to right, -1-> from right to left
                # Applying reverse winding transformation by changing the winding direction as well
                if self.winding.is_reverse_wind:
                    winding_direction = -1 * coil[2]
                else:
                    winding_direction = coil[2]

                # Recovering the surface corresponding to the starting slot and ending slot
                wind_surf_list = [
                    surf
                    for surf in surf_list
                    if WIND_LAB in decode_label(surf.label)["surf_type"]
                ]

                start_slot_surf = [
                    surf
                    for surf in wind_surf_list
                    if decode_label(surf.label)["S_id"] + 1 == start_slot[0]
                    and decode_label(surf.label)[layer_id_name] == start_slot[1]
                ]

                end_slot_surf = [
                    surf
                    for surf in wind_surf_list
                    if decode_label(surf.label)["S_id"] + 1 == end_slot[0]
                    and decode_label(surf.label)[layer_id_name] == end_slot[1]
                ]

                # Making sure that only one surface was selected for each slot
                if len(start_slot_surf) != 1 or len(end_slot_surf) != 1:
                    raise Exception(
                        "Could not find the surface of the starting or ending slot of the winding"
                    )
                else:
                    start_slot_surf = start_slot_surf[0]
                    end_slot_surf = end_slot_surf[0]

                # Recovering the start point and ending point of the arrow as the center of each slot
                start_point = [
                    start_slot_surf.comp_point_ref().real,
                    start_slot_surf.comp_point_ref().imag,
                ]

                end_point = [
                    end_slot_surf.comp_point_ref().real,
                    end_slot_surf.comp_point_ref().imag,
                ]

                # Computing the angle of the arc and its sign
                dist_AB = sqrt(
                    (end_point[0] - start_point[0]) ** 2
                    + (end_point[1] - start_point[1]) ** 2
                )

                # Changing arrow size depending on type of rotor (inner or outer)
                arrow_size = -0.5 if self.is_internal else 1.5
                angle = winding_direction * (arrow_size * self.Rext) / dist_AB

                # Adding the arrow as a Patch
                line = FancyArrowPatch(
                    start_point,
                    end_point,
                    connectionstyle="arc3,rad=" + str(angle),
                    facecolor=PHASE_COLORS[idx_phase],
                    **kw
                )
                patches.append(line)

    if is_display:
        # Display the result
        (fig, ax, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")

        ax.set_xlabel("[m]")
        ax.set_ylabel("[m]")
        for patch in patches:
            ax.add_patch(patch)
        # Axis Setup
        ax.axis("equal")

        # Window title
        if is_winding_connection:
            if self.is_stator:
                prefix = "Stator winding radial pattern "
            else:
                prefix = "Rotor winding radial pattern "
        else:
            if self.is_stator:
                prefix = "Stator "
            else:
                prefix = "Rotor "
        if (
            win_title is None
            and self.parent is not None
            and self.parent.name not in [None, ""]
        ):
            win_title = self.parent.name + " " + prefix[:-1]
        elif win_title is None:
            win_title = prefix[:-1]
        manager = plt.get_current_fig_manager()
        if manager is not None:
            manager.set_window_title(win_title)

        # The Lamination is centered in the figure
        Lim = self.Rext * 1.5
        ax.set_xlim(-Lim, Lim)
        ax.set_ylim(-Lim, Lim)

        title = None

        # Add the legend
        if not is_edge_only:
            if is_winding_connection:
                if self.is_stator and "Stator" not in label_leg:
                    patch_leg.append(Patch(color=STATOR_COLOR))
                    label_leg.append("Stator")
                    title = "Stator winding radial pattern"
                elif not self.is_stator and "Rotor" not in label_leg:
                    patch_leg.append(Patch(color=ROTOR_COLOR))
                    label_leg.append("Rotor")
                    title = "Rotor winding radial pattern"
            elif is_lam_only:
                if self.is_stator and "Stator" not in label_leg:
                    patch_leg.append(Patch(color=STATOR_COLOR))
                    label_leg.append("Stator")
                    title = "Stator Lamination"
                elif not self.is_stator and "Rotor" not in label_leg:
                    patch_leg.append(Patch(color=ROTOR_COLOR))
                    label_leg.append("Rotor")
                    title = "Rotor Lamination"
            else:
                if self.is_stator and "Stator" not in label_leg:
                    patch_leg.append(Patch(color=STATOR_COLOR))
                    label_leg.append("Stator")
                    title = "Stator with winding"
                elif not self.is_stator and "Rotor" not in label_leg:
                    patch_leg.append(Patch(color=ROTOR_COLOR))
                    label_leg.append("Rotor")
                    title = "Rotor with winding"

            ax.set_title(title)
            # Add the wedges legend only if needed
            if (
                self.slot is not None
                and self.slot.wedge_mat is not None
                and not is_lam_only
            ):
                patch_leg.append(Patch(color=WEDGE_COLOR))
                label_leg.append("Wedge")
            # Add the winding legend only if needed
            if not is_lam_only:
                if isinstance(self.winding, WindingSC):
                    patch_leg.append(Patch(color=PHASE_COLORS[0]))
                    label_leg.append(prefix + "Bar")
                elif self.winding is not None:
                    if is_add_sign:
                        if "Phase +" not in label_leg:
                            # Adding + and - in the legend as separate patch
                            patch_leg.append(Patch(color="w", hatch=PLUS_HATCH))
                            patch_leg[-1].set_edgecolor("k")
                            label_leg.append("Phase +")

                        if "Phase -" not in label_leg:
                            # Adding + and - legend
                            patch_leg.append(Patch(color="w", hatch=MINUS_HATCH))
                            patch_leg[-1].set_edgecolor("k")
                            label_leg.append("Phase -")

                    phase_name = [prefix + n for n in gen_name(qs, is_add_phase=True)]
                    for ii in range(qs):
                        if not phase_name[ii] in label_leg:
                            # Avoid adding twice the same label
                            index = ii % len(PHASE_COLORS)
                            patch_leg.append(Patch(color=PHASE_COLORS[index]))
                            label_leg.append(phase_name[ii])

            if is_legend:
                ax.legend(
                    patch_leg,
                    label_leg,
                    prop={
                        "family": dict_2D["font_name"],
                        "size": dict_2D["font_size_legend"],
                    },
                )

            for item in (
                [ax.xaxis.label, ax.yaxis.label]
                + ax.get_xticklabels()
                + ax.get_yticklabels()
            ):
                item.set_fontname(dict_2D["font_name"])
                item.set_fontsize(dict_2D["font_size_label"])
            ax.title.set_fontname(dict_2D["font_name"])
            ax.title.set_fontsize(dict_2D["font_size_title"])

        if save_path is not None:
            fig.savefig(save_path)
            plt.close(fig=fig)
        # Clean figure
        if is_clean_plot:
            ax.set_axis_off()
            ax.axis("equal")
            if ax.get_legend() is not None:
                ax.get_legend().remove()
            ax.set_title("")

        if is_show_fig:
            fig.show()
        return fig, ax
    else:
        return patches
