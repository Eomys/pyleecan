# -*-- coding: utf-8 -*
def discretize(self, Npoint=-1):
    """Returns the discretize version of the SurfLine

    Parameters
    ----------
    self: SurfLine
        A SurfLine object
    Npoint : int
        Number of point on each line (Default value = -1 => use the line default discretization)

    Returns
    -------
    point_list : list
        List of complex coordinates
    """
    # check if the SurfLine is correct
    self.check()
    # getting lines that delimit the SurfLine
    lines = self.get_lines()
    if lines[0].get_begin() == lines[-1].get_end():
        closed = True
    else:
        closed = False

    point_list = list()
    for line in lines:
        if Npoint == -1:
            point_list.extend(line.discretize())
        else:
            point_list.extend(line.discretize(Npoint))
        if line != lines[-1]:
            point_list.pop()
        else:
            if closed:  # if the SurfLine is closed
                point_list.pop()
    return point_list
