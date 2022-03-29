from ....Functions.init_fig import init_fig


def plot_BH(self, fig=None, grid=True, color="r", is_show_fig=True):
    """Plot the curve B(H) at the specified frequency

    Parameters
    ----------
    self : MatMagnetics
        a MatMagnetics object
    fig :
        if None, open a new fig and plot, else add to the gcf (Default value = None)

    Returns
    -------
    None
    """
    (fig, axes, patch_leg, label_leg) = init_fig(fig)

    BH = self.get_BH()

    if BH is not None:
        axes.plot(BH[:, 0], BH[:, 1], color=color)
        axes.grid(b=True)
        axes.set_xlabel("H [A/m]")
        axes.set_ylabel("B [T]")
        axes.set_title("B(H) curve")
        if is_show_fig:
            fig.show()

    return fig
