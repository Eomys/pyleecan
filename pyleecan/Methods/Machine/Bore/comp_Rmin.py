import numpy as np


def comp_Rmin(self):
    """Compute the minimum radius of the Bore shape

    Parameters
    ----------
    self : Bore
        A Bore object

    Returns
    -------
    Rmin : float
        Minimum radius of the Bore shape
    """

    line_list = self.get_bore_line()
    point_list = list()

    for line in line_list:
        point_list.extend(line.discretize(100))

    return np.min(np.abs(np.array(point_list)))
