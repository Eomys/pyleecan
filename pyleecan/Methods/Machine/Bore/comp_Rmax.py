import numpy as np


def comp_Rmax(self):
    """Compute the maximum radius of the Bore shape

    Parameters
    ----------
    self : Bore
        A Bore object

    Returns
    -------
    Rmax : float
        Maximum radius of the Bore shape [m]
    """

    line_list = self.get_bore_line()
    point_list = list()

    for line in line_list:
        point_list.extend(line.discretize(100))

    return np.max(np.abs(np.array(point_list)))
