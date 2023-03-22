from numpy import real, imag

from ....Functions.init_fig import init_fig


def plot_lines(self, fig=None, ax=None):
    """Plot the SurfRing-Contour in a matplotlib fig
    (For plotting unclosed contour, for Polygon use plot method from Surface object)

    Parameters
    ----------
    self : SurfRing
        A SurfRing object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data

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

    points = self.out_surf.discretize(10)
    for idx in range(len(points) - 1):
        z1 = points[idx]
        z2 = points[idx + 1]
        x1 = real(z1)
        y1 = imag(z1)
        x2 = real(z2)
        y2 = imag(z2)
        ax.plot([x1, x2], [y1, y2], "k")

    points = self.in_surf.discretize(10)
    for idx in range(len(points) - 1):
        z1 = points[idx]
        z2 = points[idx + 1]
        x1 = real(z1)
        y1 = imag(z1)
        x2 = real(z2)
        y2 = imag(z2)
        ax.plot([x1, x2], [y1, y2], "k")

    # Axis Setup
    ax.axis("equal")

    fig.show()
    return fig, ax
