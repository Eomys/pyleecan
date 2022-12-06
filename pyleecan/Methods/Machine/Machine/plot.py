import matplotlib.pyplot as plt
from ....Functions.init_fig import init_fig
from matplotlib.patches import Patch
from ....definitions import config_dict

REF_EDGE_COLOR = "k"
COMP_EDGE_COLOR = "r--"
PATCH_COLOR_ALPHA = config_dict["PLOT"]["COLOR_DICT"]["PATCH_COLOR_ALPHA"]


def plot(
    self,
    fig=None,
    ax=None,
    sym=1,
    alpha=0,
    delta=0,
    is_edge_only=False,
    edgecolor=None,
    is_add_arrow=False,
    comp_machine=None,
    comp_legend=None,
    is_show_fig=True,
    save_path=None,
    win_title=None,
    fig_title=None,
    is_max_sym=False,
    is_clean_plot=False,
):
    """Plot the Machine in a matplotlib fig

    Parameters
    ----------
    self : Machine
        A Machine object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
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
    comp_machine : Machine
        A machine to plot in transparency on top of the self machine
    comp_legend : str
        Name of the compare machine to set in the legeng (comp_machine != None)
    is_show_fig : bool
        To call show at the end of the method
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    win_title : str
        Name of the Window (default machine name)
    fig_title : str
        Name of the figure (default machine name)
    is_max_sym : bool
        True: overwrite sym parameter with max periodicity of the machine
    is_clean_plot : bool
        True to remove title, legend, axis (only machine on plot with white background)

    Returns
    -------
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """

    # Get maximum symetry for plot
    if is_max_sym:
        pera, is_apera = self.comp_periodicity_spatial()
        sym = 2 * pera if is_apera else pera

    if edgecolor is None:
        edgecolor = "k"  # Default is black
    (fig, ax, _, _) = init_fig(fig=fig, ax=ax, shape="square")

    # Call each plot method to properly set the legend
    if self.frame is not None:
        self.frame.plot(
            fig=fig,
            ax=ax,
            sym=sym,
            alpha=alpha,
            delta=delta,
            is_edge_only=is_edge_only,
            edgecolor=edgecolor,
            is_show_fig=False,
        )
        Wfra = self.frame.comp_height_eq()
    else:
        Wfra = 0

    # Determin order of plotting parts
    lam_list = self.get_lam_list(is_int_to_ext=True)

    Rext = lam_list[-1].Rext
    for lam in lam_list[::-1]:
        lam.plot(
            fig=fig,
            ax=ax,
            sym=sym,
            alpha=alpha,
            delta=delta,
            is_edge_only=is_edge_only,
            edgecolor=edgecolor,
            is_add_arrow=is_add_arrow,
            is_show_fig=False,
        )

    if lam_list[0].Rint > 0 and self.shaft is not None and self.shaft.Drsh is not None:
        self.shaft.plot(
            fig=fig,
            ax=ax,
            sym=sym,
            alpha=alpha,
            delta=delta,
            is_edge_only=is_edge_only,
            edgecolor=edgecolor,
            is_show_fig=False,
        )

    if comp_machine is not None:
        comp_machine.rotor.plot(
            fig,
            ax,
            sym=sym,
            alpha=alpha,
            delta=delta,
            is_edge_only=True,
            edgecolor=COMP_EDGE_COLOR,
            is_add_arrow=is_add_arrow,
            is_show_fig=is_show_fig,
        )
        comp_machine.stator.plot(
            fig,
            ax,
            sym=sym,
            alpha=alpha,
            delta=delta,
            is_edge_only=True,
            edgecolor=COMP_EDGE_COLOR,
            is_add_arrow=is_add_arrow,
            is_show_fig=is_show_fig,
        )
        patch_leg = [
            Patch(facecolor=PATCH_COLOR_ALPHA, edgecolor="k"),
            Patch(facecolor=PATCH_COLOR_ALPHA, edgecolor="r", linestyle="--"),
        ]
        if comp_legend is None:
            comp_legend = "Compared machine"
        label_leg = ["Reference", comp_legend]
        ax.set_axis_off()
        ax.legend(patch_leg, label_leg)

    ax.set_xlabel("Position along x-axis [m]")
    ax.set_ylabel("Position along y-axis [m]")
    if fig_title is None:
        fig_title = self.name
    ax.set_title(fig_title)

    # Axis Setup
    ax.axis("equal")

    # The Lamination is centered in the figure
    Lim = (Rext + Wfra) * 1.5  # Axes limit for plot
    if sym > 2:
        ax.set_xlim(-Lim * 0.1, Lim)
        ax.set_ylim(-Lim * 0.1, Lim)
    elif sym == 2:
        ax.set_xlim(-Lim, Lim)
        ax.set_ylim(-Lim * 0.1, Lim)
    else:
        ax.set_xlim(-Lim, Lim)
        ax.set_ylim(-Lim, Lim)

    # Set Windows title
    if self.name not in ["", None] and win_title is None:
        win_title = self.name + " plot machine"

    # Clean figure
    if is_clean_plot:
        ax.set_axis_off()
        ax.axis("equal")
        if ax.get_legend() is not None:
            ax.get_legend().remove()
        ax.set_title("")

    if save_path is not None:
        fig.savefig(save_path)
        plt.close(fig=fig)

    if is_show_fig:
        fig.show()

    if win_title:
        manager = plt.get_current_fig_manager()
        if manager is not None:
            manager.set_window_title(win_title)
    return fig, ax
