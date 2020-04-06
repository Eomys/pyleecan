# -*-- coding: utf-8 -*
def discretize(self, Npoint=-1):
    """Returns the discretize version of the SurfRing

    Parameters
    ----------
    self: SurfRing
        A SurfRing object
    Npoint : int
        Number of point on each line (Default value = -1 => use the line default discretization)

    Returns
    -------
    point_list : list
        List of complex coordinates
    """
    # check if the SurfRing is correct
    self.check()
    # getting lines that delimit the SurfLine

    point_list = self.out_surf.discretize(Npoint=Npoint)
    point_list.extend(self.in_surf.discretize(Npoint=Npoint))
    return point_list
