# -*- coding: utf-8 -*-
"""@package Methods.Machine.Machine.plot
Machine plot method
@date Created on Wed Dec 10 14:58:51 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""
from matplotlib.pyplot import axis, subplots
from pyleecan.Functions.init_fig import init_fig


def plot(
    self, fig=None, sym=1, alpha=0, delta=0, is_edge_only=False, comp_machine=None
):
    """Plot the Machine in a matplotlib fig

    Parameters
    ----------
    self : MachineUD
        A MachineUD object
    fig :
        if None, open a new fig and plot, else add to the gcf (Default value = None)
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

    Returns
    -------
    None

    """
    # Display
    # fig, axes = subplots()
    (fig, axes, patch_leg, label_leg) = init_fig(fig)

    plot_list = list()
    # Get the patches to display from corresponding plot
    # The order in the list matters (largest to smallest)
    if self.frame is not None:
        plot_list.append(self.frame.plot)
        Wfra = self.frame.comp_height_eq()
    else:
        Wfra = 0

    Rext = 0
    for lam in self.lam_list:
        plot_list.append(lam.plot)
        Rext = max(Rext, lam.Rext)

    Lim = (Rext + Wfra) * 1.5  # Axes limit for plot

    # Plot
    plot_args = {
        "sym": sym,
        "alpha": alpha,
        "delta": delta,
        "is_edge_only": is_edge_only,
    }

    for plot_fct in plot_list:
        _plot(plot_fct, fig, plot_args)

    if comp_machine is not None:
        raise ValueError("Comp_machine is not available for MachineUD")
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    axes.set_title("Machine")

    # Axis Setup
    axis("equal")

    # The Lamination is centered in the figure
    axes.set_xlim(-Lim, Lim)
    axes.set_ylim(-Lim, Lim)
    fig.show()


def _plot(plt_fcn, fig, plot_args):
    if plt_fcn is not None:
        try:
            plt_fcn(fig, **plot_args)
        except Exception:
            pass
