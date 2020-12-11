# -*- coding: utf-8 -*-

from numpy import linspace, where, sin, pi


def get_data(self):
    """Generate the toothsaw vector

    Parameters
    ----------
    self : ImportGenToothSaw
        An ImportGenToothSaw object

    Returns
    -------
    vect: ndarray
        The generated toothsaw vector

    """

    time = linspace(start=0, stop=self.Tf, num=self.N, endpoint=False)

    T = 1 / self.f
    time = (time + self.Dt) % T

    if self.type_signal == 0:  # forward toothsaw carrier
        Y = (
            where(time <= 0.5 * T, 1, 0) * time
            + where(time > 0.5 * T, 1, 0) * (time - T)
        ) / (0.5 * T)
    elif self.type_signal == 1:  # backwards toothsaw carrier
        Y = -(
            where(time <= 0.5 * T, 1, 0) * time
            + where(time > 0.5 * T, 1, 0) * (time - T)
        ) / (0.5 * T)
    elif self.type_signal == 2:  # symmetrical toothsaw carrier
        t1 = T / 4
        t2 = T - t1
        Y = (
            where(time <= t1, 1, 0) * time / t1
            + where(time > t1, 1, 0)
            * where(time < t2, 1, 0)
            * (-time + 0.5 * T)
            / (-t1 + 0.5 * T)
            + where(time >= t2, 1, 0) * (time - T) / (T - t2)
        )

    return self.edit_matrix(self.A * Y)
