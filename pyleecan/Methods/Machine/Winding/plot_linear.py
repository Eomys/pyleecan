from numpy import ones, real, imag, conjugate, array, delete, insert, round
from swat_em import datamodel
from swat_em.config import config
from matplotlib.patches import Rectangle, Patch, FancyArrowPatch
import matplotlib.pyplot as plt

from ....Functions.init_fig import init_fig
from ....Functions.Geometry.inter_line_line import inter_line_line
from ....Functions.Winding.gen_phase_list import gen_name
from ....definitions import config_dict

PHASE_COLORS = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]
ROTOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["ROTOR_COLOR"]
STATOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["STATOR_COLOR"]


def plot_linear(
    self,
    fig=None,
    ax=None,
    is_max_sym=True,
    is_show_fig=True,
    save_path=None,
    win_title=None,
    is_legend=True,
):
    """Plots the winding linear pattern. Method based on plot_overhang method of swat-em module

    Parameters
    ----------
    self : Winding
        A Winding object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    is_max_sym : bool
        To only plot the linear pattern on the maximum symetry of the machine
    is_show_fig : bool
        To call show at the end of the method
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    win_title : str
        Title for the window
    is_legend : bool
        True to add the legend
    """

    # Recovering the colors of the phases
    if (
        not isinstance(config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"][0], str)
        and len(config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"][0]) == 4
    ):  # convert rgba to hex
        config["plt"]["phase_colors"] = [
            "#{:02x}{:02x}{:02x}".format(
                int(color[0] * 255 * (1 - color[3]) + 255 * color[3]),
                int(color[1] * 255 * (1 - color[3]) + 255 * color[3]),
                int(color[2] * 255 * (1 - color[3]) + 255 * color[3]),
            )
            for color in config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]
        ]
    else:
        config["plt"]["phase_colors"] = config_dict["PLOT"]["COLOR_DICT"][
            "PHASE_COLORS"
        ]

    # Step 1 : Generate a datamodel for the winding
    Zs = self.parent.get_Zs()
    p = self.parent.get_pole_pair_number()

    # Generating the winding from inputs and recovering its attributes
    wdg = datamodel()
    wdg.genwdg(
        Q=Zs,
        P=2 * p,
        m=self.qs,
        layers=self.Nlayer,
        turns=self.Ntcoil,
        w=self.coil_pitch,
    )

    # Detecting the direction of the layer (tangential or radial)
    # If Nlayer > 1 then we have to precise if the direction is tangential or radial to draw the coil at the right location in the slot
    Nrad, Ntan = self.get_dim_wind()
    if Nrad < Ntan:
        is_tangential_layer = True
    else:
        is_tangential_layer = False

    # Input used to build the coils that we will display
    bz = 0.5  # tooth width
    hz = 0.5  # slot height
    h1 = 0.6  # height of the coil side
    h2 = 0.5 + self.coil_pitch / 6  # height of the winding overhang
    db1 = (
        0 if self.Nlayer == 1 or not is_tangential_layer else 0.1
    )  # distance between coil side and slot center

    # Only plotting the machine for a period (if antiperiod given using the full period)
    # This done by only taking into account Zs for a period
    if is_max_sym:
        per, is_antiper = self.comp_periodicity()
        Zs_per = Zs // (per // 2) if is_antiper else Zs // per
    else:
        Zs_per = Zs

    # Step 2: Creating a list of patches and lines that will be plotted
    patches = list()
    lines_dict = dict()

    # Step 2-1: Adding slot surface as rectangural patches
    xy = [(k - 0.5 - bz / 2, -hz / 2) for k in range(Zs_per + 1)]
    width = ones([Zs_per + 1]) * bz
    height = hz

    # First tooth is cut in half so we have two surfaces instead of 1
    xy[0] = (-0.5, -hz / 2)
    width[0] = bz / 2
    width[-1] = bz / 2

    for idx_slot in range(Zs_per + 1):
        point = xy[idx_slot]
        width_patch = width[idx_slot]
        patch = Rectangle(
            xy=point,
            width=width_patch,
            height=height,
            color=STATOR_COLOR if self.parent.is_stator else ROTOR_COLOR,
            linewidth=0,
        )
        patches.append(patch)

    # Step 2-2: Adding coil pattern as line between six points
    head = wdg.get_wdg_overhang(optimize_overhang=False)

    # Taking into account slot shifting transformation
    if self.Nslot_shift_wind not in [0, None]:
        Nslot_shift_wind = self.Nslot_shift_wind
    else:
        Nslot_shift_wind = 0

    # Permuting B and C if asked
    if self.is_permute_B_C:
        head_2 = head.copy()
        head_2[1] = head[2]
        head_2[2] = head[1]
        head = head_2

    for idx_phase, phase in enumerate(head):
        coils = list()  # list of points that constitutes the coils of a phase
        for coil in phase:

            # Step 2-2-1: Building 6 points to have the following coil pattern
            #        P1
            #       /  \
            #      /    \
            #     P0    P2
            #     |      |
            #     |      |
            #     |      |
            #     P5     P3
            #      \    /
            #       \  /
            #        P4

            P0 = db1 + 1j * h1
            P1 = coil[1] / 2 + 1j * h2
            P2 = coil[1] - db1 + 1j * h1
            P3 = coil[1] - db1 - 1j * h1
            P4 = coil[1] / 2 - 1j * h2
            P5 = db1 - 1j * h1

            point_list = [P0, P1, P2, P3, P4, P5]
            x_, y_ = real(point_list), imag(point_list)

            # Step 2-2-2: Shifting the coil pattern to the right slot according to the direction of the winding and the potential winding transformation
            direct = coil[2]
            if self.is_reverse_wind:
                if direct < 0:
                    slot_shift = Zs - coil[0][0]
                else:
                    slot_shift = Zs - coil[0][1]
            else:
                if direct > 0:
                    slot_shift = coil[0][0] - 1
                else:
                    slot_shift = coil[0][1] - 1

            x_ += slot_shift + Nslot_shift_wind

            point_list_updated = x_ + 1j * y_

            # Step 2-2-3: If a coil cross the right border then it must be splitted in 2,
            # if the coil is completely out of bounds then we do not plot it at all
            idx_point_too_far = [i for i in range(len(x_)) if x_[i] > Zs_per - 0.5]
            # if the coil is on the left border, not plotting it (overlap with coil splitted on right border)
            idx_point_too_low = [i for i in range(len(x_)) if x_[i] < -0.5]
            if (
                idx_point_too_far != list()
                and len(idx_point_too_far) != len(x_)
                and idx_point_too_low == list()
            ):
                wrong_points = x_[idx_point_too_far] + 1j * y_[idx_point_too_far]

                # Correcting first point so that it is on the right border (new P2 point) and getting P3 as the conjugate of P2
                # if there more than two points that are incorrect we have to remove them as we only need the first and the last one
                idx_point_to_remove = (
                    idx_point_too_far[1:-1] if len(idx_point_too_far) > 2 else list()
                )
                idx_point_too_far = [idx_point_too_far[0], idx_point_too_far[-1]]

                # For the point that we have to correct, we have to find the intersection
                # between the segments that are too far and a vertical line on Y= Zs_per-0.5
                wrong_point = x_[idx_point_too_far[0]] + 1j * y_[idx_point_too_far[0]]
                previous_point = (
                    x_[idx_point_too_far[0] - 1] + 1j * y_[idx_point_too_far[0] - 1]
                )

                lim_axis_y_point_A = Zs_per - 0.5 + 1j * h2
                lim_axis_y_point_B = Zs_per - 0.5 - 1j * h2

                point_correct = inter_line_line(
                    previous_point,
                    wrong_point,
                    lim_axis_y_point_A,
                    lim_axis_y_point_B,
                )

                # Listing the point corrected and its conjugate
                point_corrected = list()
                point_corrected.append(point_correct[0])
                point_corrected.append(conjugate(point_correct[0]))

                # Putting the corrected point on the left border to complete the coil
                point_to_add = array(point_corrected) - Zs_per
                point_to_add = insert(point_to_add, 1, wrong_points - Zs_per)

                # Replacing the incorrect point by the new P2 and P3
                for idx_point, _ in enumerate(idx_point_too_far):
                    point_list_updated[idx_point_too_far[idx_point]] = point_corrected[
                        idx_point
                    ]

                # Removing point that are not necessary (when more that 2 point are out of bounds)
                if idx_point_to_remove != list():
                    point_list_updated = delete(point_list_updated, idx_point_to_remove)

                coils.append(point_list_updated)
                coils.append(point_to_add)
            elif len(idx_point_too_far) != len(x_) and idx_point_too_low == list():
                coils.append(point_list_updated)

            # If we apply the reverse winding transformation then we must invert the the signe of the coil
            if self.is_reverse_wind:
                direct *= -1

            # Step 2-2-4: Adding arrow patch for each coil between P2<->P3 and P5<->P0 (direction depending on winding direction)
            if len(idx_point_too_far) != len(x_) and idx_point_too_low == list():
                if idx_point_too_far != list():
                    # If the coil is splitted, then the point of the arrow are different compared with other case
                    if direct > 0:
                        # Winding direction from left to right
                        start_point_1 = point_list_updated[-1]
                        start_point_2 = point_to_add[len(point_to_add) // 2 - 1]

                    else:
                        # Winding direction from right to left
                        start_point_1 = point_list_updated[0]
                        start_point_2 = point_to_add[len(point_to_add) // 2]
                else:
                    if direct > 0:
                        # Winding direction from left to right
                        start_point_1 = point_list_updated[5]
                        start_point_2 = point_list_updated[2]

                    else:
                        # Winding direction from right to left
                        start_point_1 = point_list_updated[0]
                        start_point_2 = point_list_updated[3]

                arrow_1 = FancyArrowPatch(
                    (start_point_1.real, start_point_1.imag),
                    (start_point_1.real, 0),
                    facecolor=PHASE_COLORS[idx_phase],
                    linewidth=0,
                    arrowstyle="Simple, tail_width=0, head_width=8, head_length=12",
                )
                arrow_2 = FancyArrowPatch(
                    (start_point_2.real, start_point_2.imag),
                    (start_point_2.real, 0),
                    facecolor=PHASE_COLORS[idx_phase],
                    linewidth=0,
                    arrowstyle="Simple, tail_width=0, head_width=8, head_length=12",
                )

                patches.append(arrow_1)
                patches.append(arrow_2)

        # Step 2-2-4: Keeping the coils of each phase inside a dict
        lines_dict["Phase " + str(idx_phase + 1)] = coils

    # Step 3: plotting the line and patches that we computed before
    # Step 3-1: Initializing the figure
    (fig, ax, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")

    # Step 3-2: Drawing the coils
    for idx_phase, phase in enumerate(lines_dict):
        for coil in lines_dict[phase]:
            for idx_coil in range(len(coil)):
                # If the line begin at P5 then it ends at P0
                if idx_coil == len(coil) - 1:
                    begin = coil[idx_coil]
                    end = coil[0]
                # Drawing the line betwe PN and PN+1
                else:
                    begin = coil[idx_coil]
                    end = coil[idx_coil + 1]

                # Adding condition to make sure that we do not draw lines between two point on the left or  the right border
                if (
                    round(real(begin), decimals=1) != -0.5
                    or round(real(end), decimals=1) != -0.5
                ) and (
                    round(real(begin), decimals=1) != Zs_per - 0.5
                    or round(real(end), decimals=1) != Zs_per - 0.5
                ):
                    points = array([begin, end])
                    ax.plot(
                        points.real,
                        points.imag,
                        color=PHASE_COLORS[idx_phase],
                    )

    # Step 3-3: Adding stator tooth patches to the figure
    for patch in patches:
        ax.add_patch(patch)

    # Step 3-4: Adding plot slot number between each tooth
    for slot_nb in range(Zs_per):
        ax.annotate(
            xy=(slot_nb, -hz / 2),
            text=str(slot_nb + 1),
            family=config_dict["PLOT"]["FONT_NAME"],
            horizontalalignment="center",
            color="k",
        )

    # Step 3-5: Setting limits of the figure and removing axes
    ax.set_xlim(-0.5, Zs_per - 0.5)
    ax.set_ylim(-h2 * 1.2, h2 * 1.2)
    ax.set_axis_off()

    # Step 3-6: Setting the title of the window and of the figure
    if self.parent.is_stator:
        title = "Stator winding linear pattern"
        prefix = "Stator "
    else:
        title = "Rotor winding linear pattern"
        prefix = "Rotor "
    # Add machine name if available
    if self.parent.parent is not None and self.parent.parent.name not in ["", None]:
        win_title = self.parent.parent.name + " " + title
    else:
        win_title = title
    manager = plt.get_current_fig_manager()
    if manager is not None:
        manager.set_window_title(win_title)
    ax.set_title(win_title)

    # Step 3-7: Setting the legend of the figure
    # Adding lamination name in the lamination
    if self.parent.is_stator and "Stator" not in label_leg:
        patch_leg.append(Patch(color=STATOR_COLOR))
        label_leg.append("Stator")
    elif not self.parent.is_stator and "Rotor" not in label_leg:
        patch_leg.append(Patch(color=ROTOR_COLOR))
        label_leg.append("Rotor")

    # Adding each Phase name in the lamination
    phase_name = [prefix + n for n in gen_name(self.qs, is_add_phase=True)]
    for idx_phase_nb in range(self.qs):
        # Avoid adding twice the same label
        if not phase_name[idx_phase_nb] in label_leg:
            index = idx_phase_nb % len(PHASE_COLORS)
            patch_leg.append(Patch(color=PHASE_COLORS[index]))
            label_leg.append(phase_name[idx_phase_nb])

    # Adding the legend if necessary
    if is_legend:
        ax.legend(patch_leg, label_leg, bbox_to_anchor=(1, 1))

    fig.tight_layout()

    # Saving the figure if necessary
    if save_path is not None:
        fig.savefig(save_path)
        plt.close(fig=fig)

    # Displaying the figure if necessary
    if is_show_fig:
        fig.show()

    return fig, ax
