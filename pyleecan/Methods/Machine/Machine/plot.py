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
):
    """Plot the Machine in a matplotlib fig

    Parameters
    ----------
    self : Machine
        A Machine object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        ax on which to plot the data
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
    """

    # Set figure if needed
    if fig is None and ax is None:
        (fig, ax, _, _) = init_fig(fig=None, shape="rectangle")

    # Get the patches to display from corresponding plot
    # The order in the list matters (largest to smallest)
    if self.frame is not None:
        plot_frame = self.frame.plot
        Wfra = self.frame.comp_height_eq()
    else:
        plot_frame = None
        Wfra = 0

    # Determin order of plotting parts
    plot_int, plot_ext, plot_shaft = None, None, None
    Rext = 0

    if self.rotor is not None:
        if self.rotor.is_internal:
            plot_int = self.rotor.plot
            if self.rotor.Rint > 0 and self.shaft is not None:
                plot_shaft = self.shaft.plot
        else:
            plot_ext = self.rotor.plot
        Rext = self.rotor.Rext  # will be reset by stator in case

    if self.stator is not None:
        if self.stator.is_internal:
            plot_int = self.stator.plot
        else:
            plot_ext = self.stator.plot
        if self.stator.Rext > Rext:
            Rext = self.stator.Rext

    Lim = (Rext + Wfra) * 1.5  # Axes limit for plot

    # Plot
    plot_args = {
        "sym": sym,
        "alpha": alpha,
        "delta": delta,
        "is_edge_only": is_edge_only,
        "is_show_fig": is_show_fig,
    }

    _plot(plot_frame, fig, plot_args)
    _plot(plot_ext, fig, plot_args)
    _plot(plot_int, fig, plot_args)
    _plot(plot_shaft, fig, plot_args)

    if comp_machine is not None:
        comp_machine.rotor.plot(
            fig,
            sym=sym,
            alpha=alpha,
            delta=delta,
            is_edge_only=True,
            is_show_fig=is_show_fig,
        )
        comp_machine.stator.plot(
            fig,
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

    if save_path is not None:
        fig.savefig(save_path)
        plt.close()

    if is_show_fig:
        fig.show()


def _plot(plt_fcn, fig, plot_args):
    if plt_fcn is not None:
        try:
            plt_fcn(fig, **plot_args)
        except Exception:
            pass
