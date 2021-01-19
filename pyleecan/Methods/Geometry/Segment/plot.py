from numpy import array
from ....Functions.init_fig import init_fig
from ....Functions.Plot import TEXT_BOX


def plot(
    self,
    fig=None,
    ax=None,
    is_arrow=False,
    linestyle="solid",
    linewidth=1,
    color="black",
    label=None,
    fontsize=12,
):
    """Plot the segment

    Parameters
    ----------
    self : Segment
        A Segment object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
    is_arrow : bool
        True to draw a double headed arrow instead of a line
    linestyle : str
        Line of the line (solid, dotted...)
    linewidth : int
        Line Width
    color : str
        Color of the line
    label : str
        To add a label at the middle of the line
    fontsize : int
        Size of the font for the label (if any)
    """
    begin = self.get_begin()
    end = self.get_end()

    # Init fig
    (fig, axes, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")

    if is_arrow:  # Plot as double headed arrow
        axes.annotate(
            text="",
            xy=(end.real, end.imag),
            xytext=(begin.real, begin.imag),
            arrowprops=dict(arrowstyle="<->", linewidth=linewidth, color=color),
        )
    else:  # Plot as a line
        points = array([begin, end])
        axes.plot(
            points.real,
            points.imag,
            linestyle=linestyle,
            linewidth=linewidth,
            color=color,
        )

    # Add the Label
    if label is not None:
        Zmid = self.get_middle()
        axes.text(
            Zmid.real,
            Zmid.imag,
            label,
            fontsize=fontsize,
            bbox=TEXT_BOX,
        )
