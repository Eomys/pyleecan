# -*- coding: utf-8 -*-

from numpy import linspace, sin, pi


def get_data(self):
    """Generate the sinus vector

    Parameters
    ----------
    self : ImportGenVectSin
        An ImportGenVectSin object

    Returns
    -------
    vect: ndarray
        The generated sinus vector

    """

    time = linspace(start=0, stop=self.Tf, num=self.N, endpoint=False)

    vect = self.A * sin(2 * pi * self.f * time + self.Phi)
    return self.edit_matrix(vect)
