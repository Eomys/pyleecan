# -*-- coding: utf-8 -*
def discretize(self):
    """It returns the discretize version of the Trapeze

    Parameters
    ----------
    self : Trapeze
        a Trapeze object

    Returns
    -------
    point_list : list
        list of complex coordinate of the points
    """

    # check if the Trapeze is correct
    self.check()
    # getting lines that delimit the Trapeze
    lines = self.get_lines()
    point_list = list()
    for line in lines:
        point_list.extend(line.discretize())
        point_list.pop()
    return point_list
