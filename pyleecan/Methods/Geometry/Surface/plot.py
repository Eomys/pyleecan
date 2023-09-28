from ....Functions.init_fig import init_fig
from ....definitions import config_dict

PATCH_EDGE = config_dict["PLOT"]["COLOR_DICT"]["PATCH_EDGE"]
PATCH_COLOR = config_dict["PLOT"]["COLOR_DICT"]["PATCH_COLOR"]


def plot(
    self,
    fig=None,
    ax=None,
    color=PATCH_COLOR,
    edgecolor=PATCH_EDGE,
    is_edge_only=False,
    linestyle=None,
    is_disp_point_ref=False,
    is_disp_line_index=False,
    is_show_fig=True,
):
    """Plot the Surface patch in a matplotlib fig

    Parameters
    ----------
    self : Surface
        A Surface object
    fig :
        if None, open a new fig and plot, else add to the
        current one (Default value = None)
    color :
        the color of the patch (Default value = PATCH_COLOR)
    edgecolor :
        the edge color of the patch (Default value = PATCH_EDGE)
    is_edge_only: bool
        To set the transparancy of the face color to 0 and 1 for the edge color
    linestyle : str
        Line style of the edge {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
    is_disp_point_ref : bool
        True to add the point_ref
    is_disp_line_index : bool
        True to add the index of the lines
    is_show_fig : bool
        To call show at the end of the methods

    Returns
    -------
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """

    (fig, ax, patch_leg, label_leg) = init_fig(fig, ax)
    ax.set_xlabel("[m]")
    ax.set_ylabel("[m]")

    patches = self.get_patches(
        color=color, edgecolor=edgecolor, is_edge_only=is_edge_only, linestyle=linestyle
    )
    for patch in patches:
        ax.add_patch(patch)

    if is_disp_point_ref:
        ax.plot(self.point_ref.real, self.point_ref.imag, "kx")

    if is_disp_line_index:
        for ii, line in enumerate(self.get_lines()):
            mid = line.get_middle()
            ax.text(mid.real, mid.imag, str(ii))
    # Axis Setup
    ax.axis("equal")

    if is_show_fig:
        fig.show()
    return fig, ax
