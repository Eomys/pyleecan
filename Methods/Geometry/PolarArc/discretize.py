# -*-- coding: utf-8 -*
def discretize(self, nb_point):
    """Returns the discretize version of the PolarArc

    Parameters
    ----------
    nb_point : int
        number of points wanted per line

    Returns
    -------
    point_list : list
        List of complex coordinate of the points

    """
    # check if the PolarArc is correct
    self.check()

    if not isinstance(nb_point, int):
        raise NbPointPolarArcError("Discretize : the nb_point must be an integer")
    if nb_point < 0:
        raise NbPointPolarArcError("Discretize: nb_point must be >= 0")

    # getting lines that delimit the PolarArc
    lines = self.get_lines()
    point_list = list()
    for line in lines:
        point_list.extend(line.discretize(nb_point))
        # The begin of the next line is the end of the current one
        point_list.pop()
    return point_list


class NbPointPolarArcError(Exception):
    """ """

    pass
