# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from ....Functions.init_fig import init_fig


def plot(
    self,
    fig=None,
    ax=None,
    sym=1,
    alpha=0,
    delta=0,
    is_edge_only=False,
    comp_machine=None,
    is_show_fig=True,
    save_path=None,
    win_title=None,
    is_max_sym=False,
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
    comp_machine : Machine
        A machine to plot in transparency on top of the self machine
    is_show_fig : bool
        To call show at the end of the method
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    win_title : str
        Name of the Window (default machine name)
    is_max_sym : bool
        True: overwrite sym parameter with max periodicity of the machine
    """
    # Get maximum symetry for plot
    if is_max_sym:
        pera, is_apera = self.comp_periodicity_spatial()
        sym = 2 * pera if is_apera else pera

    (fig, ax, _, _) = init_fig(fig=fig, ax=ax, shape="rectangle")

    # Call each plot method to properly set the legend
    if self.frame is not None:
        self.frame.plot(
            fig=fig,
            ax=ax,
            sym=sym,
            alpha=alpha,
            delta=delta,
            is_edge_only=is_edge_only,
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
            is_show_fig=False,
        )

    if lam_list[0].Rint > 0 and self.shaft is not None:
        self.shaft.plot(
            fig=fig,
            ax=ax,
            sym=sym,
            alpha=alpha,
            delta=delta,
            is_edge_only=is_edge_only,
            is_show_fig=False,
        )

    Lim = (Rext + Wfra) * 1.5  # Axes limit for plot

    if comp_machine is not None:
        comp_machine.rotor.plot(
            fig,
            ax,
            sym=sym,
            alpha=alpha,
            delta=delta,
            is_edge_only=True,
            is_show_fig=is_show_fig,
        )
        comp_machine.stator.plot(
            fig,
            ax,
            sym=sym,
            alpha=alpha,
            delta=delta,
            is_edge_only=True,
            is_show_fig=is_show_fig,
        )

    ax.set_xlabel("(m)")
    ax.set_ylabel("(m)")
    ax.set_title(self.name)

    # Axis Setup
    plt.axis("equal")

    # The Lamination is centered in the figure
    ax.set_xlim(-Lim, Lim)
    ax.set_ylim(-Lim, Lim)

    # Set Windows title
    if self.name not in ["", None] and win_title is None:
        win_title = self.name + " plot machine"

    if save_path is not None:
        fig.savefig(save_path)
        plt.close()

    if is_show_fig:
        fig.show()

    if win_title:
        manager = plt.get_current_fig_manager()
        if manager is not None:
            manager.set_window_title(win_title)
