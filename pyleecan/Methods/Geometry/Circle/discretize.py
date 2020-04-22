# -*- coding: utf-8 -*-


def discretize(self):
    """Return the discretize version of the Circle.

    Parameters
    ----------
    self : Circle
        A Circle Object

    nb_point : int
        Number of point on the circle

    Returns
    -------
    point_list : list
        List of complex coordinate of the points

    """

    # check if the Circle is correct
    self.check()

    # getting Arc which delimit the Circle
    lines = self.get_lines()
    point_list = list()
    for line in lines:
        point_list.extend(line.discretize())
        point_list.pop()
    return point_list
