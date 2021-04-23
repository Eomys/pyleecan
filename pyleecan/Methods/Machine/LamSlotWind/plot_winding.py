# -*- coding: utf-8 -*-

from matplotlib.lines import Line2D
from matplotlib.pyplot import axis, legend, plot, subplots, title
from numpy import array, linspace, meshgrid

from ....Functions.Winding.comp_wind_periodicity import comp_wind_periodicity
from ....Functions.Winding.gen_phase_list import gen_color, gen_name


def plot_winding(self, wind_mat=None, all_slot=False, is_show_fig=True):
    """Plot the Winding in a matplotlib fig

    Parameters
    ----------
    self : LamSlotWind
        A: LamSlotWind object
    wind_mat : numpy.ndarray
        Winding Matrix, if None will call comp_connection_mat (Default value = None)
    all_slot : bool
        True if we plot all slot and false when plotting only needed one(sym)
    is_show_fig : bool
        To call show at the end of the method
    Returns
    -------
    None
    """

    # We compute the wind_mat only if needed
    if wind_mat is None:
        wind_mat = self.winding.comp_connection_mat(self.slot.Zs)

    # Number of point on rad and tan direction
    Nrad, Ntan = self.winding.get_dim_wind()
    Zs = self.slot.Zs  # Number of slot

    # Number of Slot to plot
    if all_slot:  # Every Slot
        Nplot = Zs
    else:  # Only the needed one (sym)
        Nperw = comp_wind_periodicity(wind_mat)[0]  # Symmetry of the winding
        Nplot = Zs // Nperw

    qs = wind_mat.shape[3]  # Number of phase

    # Symbole for pole
    qs_color = gen_color(self.winding.qs)
    qs_name = gen_name(self.winding.qs)

    # Schematic slot without ratio
    Wt = 0.5
    W0 = 0.5
    H = 1

    # Coordinate of the First Slot   (center on 0)
    Slot_tan = array(
        [-Wt / 2 - W0 / 2, -W0 / 2, -W0 / 2, W0 / 2, W0 / 2, W0 / 2 + Wt / 2]
    )
    Slot_rad = [0, 0, H, H, 0, 0]

    # Duplicate the Slot along tan direction (angular abscissa )
    x = list()
    y = list()
    for i in range(0, Nplot):
        x.extend((Slot_tan + (Wt + W0) * i).tolist())
        y.extend(Slot_rad)

    # Plot the Schematics Slots
    fig, ax = subplots()
    plot(x, y, "r-")

    # First Winding Grid (Coordinate of the winding mark)
    range_x = linspace(-W0 / 2, W0 / 2, Ntan + 1, endpoint=False)
    range_y = linspace(0, H, Nrad + 1, endpoint=False)
    # We don't want the first and last point of the linespace
    Grid_x, Grid_y = meshgrid(range_x[1:], range_y[1:])

    # Plot the Winding Grid point by point by reading wind_mat
    for Zs in range(0, Nplot):  # For "every" Slot
        for q in range(0, qs):  # For every phase
            for r in range(0, Nrad):  # For every rad layer
                for theta in range(0, Ntan):  # For every tan layer
                    if wind_mat[r, theta, Zs, q] != 0:
                        # Add the correct mark at the correct coordinates
                        if wind_mat[r, theta, Zs, q] > 0:
                            plot(
                                Grid_x[r][theta] + Zs * (Wt + W0),
                                Grid_y[r][theta],
                                color=qs_color[q],
                                linewidth=0,
                                marker="+",
                                markeredgewidth=3,
                                markersize=20,
                            )
                        else:
                            plot(
                                Grid_x[r][theta] + Zs * (Wt + W0),
                                Grid_y[r][theta],
                                color=qs_color[q],
                                linewidth=0,
                                marker="x",
                                markeredgewidth=3,
                                markersize=20,
                            )
    if self.is_stator:
        Lam_Name = "Stator"
    else:
        Lam_Name = "Rotor"
    if all_slot or Nperw == 1:
        title(Lam_Name + "'s Winding (every slot)")
    else:
        title(Lam_Name + "'s Winding (periodicity 1/" + str(Nperw) + ")")

    axis("equal")
    ax.get_yaxis().set_visible(False)

    # Legend qs
    sym_leg = list()  # Symbol
    label_leg = list()  # Text
    for q in range(0, qs):  # Positive mark
        sym_leg.append(
            Line2D(
                [],
                [],
                color=qs_color[q],
                linewidth=0,
                marker="+",
                markeredgewidth=3,
                markersize=20,
            )
        )
        label_leg.append(qs_name[q] + "+")
    for q in range(0, qs):  # Negative mark
        sym_leg.append(
            Line2D(
                [],
                [],
                color=qs_color[q],
                linewidth=0,
                marker="x",
                markeredgewidth=3,
                markersize=20,
            )
        )
        label_leg.append(qs_name[q] + "-")

    legend(sym_leg, label_leg, ncol=2)

    if is_show_fig:
        fig.show()
