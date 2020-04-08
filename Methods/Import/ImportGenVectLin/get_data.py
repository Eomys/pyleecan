# -*- coding: utf-8 -*-

from numpy import linspace


def get_data(self):
    """Generate the linspace vector

    Parameters
    ----------
    self : ImportGenVectLin
        An ImportGenVectLin object

    Returns
    -------
    vect: ndarray
        The generated linspace vector

    """

    vect = linspace(
        start=self.start, stop=self.stop, num=int(self.num), endpoint=self.endpoint
    )

    return self.edit_matrix(vect)
