from ....Functions.Geometry.inter_circle_circle import inter_circle_circle

# import matplotlib.pyplot as plt


def intersect_obj(self, other, is_on_line=True):
    """Find the intersection points between this line
    and another line object

    Parameters
    ----------
    self : Arc
        An Arc object
    other : Line
        The other line object to intersect
    is_on_line : bool
        True to return only points that are on both Line objects

    Returns
    -------
    Z_list: list
        Complex coordinates of the intersection (if any)
    """

    if other.is_arc():
        inter_list = inter_circle_circle(
            Zc1=self.get_center(),
            Zc2=other.get_center(),
            R1=abs(self.comp_radius()),
            R2=abs(other.comp_radius()),
        )
    else:
        inter_list = self.intersect_line(Z1=other.get_begin(), Z2=other.get_end())

    if not is_on_line:
        return inter_list

    # Plot for debug
    # fig, ax = self.plot(color="r")
    # other.plot(fig=fig, ax=ax, color="b")
    # for ii, Z in enumerate(inter_list):
    #     ax.plot(Z.real, Z.imag, "rx", zorder=0)
    #     ax.text(Z.real, Z.imag, str(ii))
    # ax.plot(0, 0, "kx", zorder=0)
    # ax.text(0, 0, "O")
    # plt.show()

    # Keep only points on both lines
    Z_list = list()
    for Z in inter_list:
        if self.is_on_line(Z) and other.is_on_line(Z):
            Z_list.append(Z)

    return Z_list
