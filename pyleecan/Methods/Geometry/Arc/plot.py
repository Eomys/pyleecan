from numpy import array
from ....Functions.init_fig import init_fig
from ....Functions.Plot import TEXT_BOX


def plot(
    self,
    fig=None,
    ax=None,
    linestyle="solid",
    linewidth=1,
    color="black",
    label=None,
    offset_label=0,
    fontsize=12,
):
    """Plot the Arc

    Parameters
    ----------
    self : Arc
        An Arc object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
    linestyle : str
        Line of the line (solid, dotted...)
    linewidth : int
        Line Width
    color : str
        Color of the line
    label : str
        To add a label at the middle of the line
    offset_label : complex
        Complex value to shift the label from the middle
    fontsize : int
        Size of the font for the label (if any)

    Returns
    -------
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """

    # Init fig
    (fig, ax, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")

    # Plot the line
    points = self.discretize(nb_point=10000)
    ax.plot(
        points.real, points.imag, linestyle=linestyle, linewidth=linewidth, color=color
    )

    # Add the label (if needed)
    if label is not None:
        Zmid = self.get_middle()
        ax.text(
            Zmid.real + offset_label.real,
            Zmid.imag + offset_label.imag,
            label,
            fontsize=fontsize,
            bbox=TEXT_BOX,
        )

    return fig, ax
