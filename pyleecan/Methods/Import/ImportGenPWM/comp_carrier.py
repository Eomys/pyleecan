import numpy as np

from scipy import signal


def comp_carrier(self, time):
    """Function to compute the carrier

    Parameters
    ----------
    time : array
        Time vector

    Returns
    -------
    Y: ndarray
        carrier

    """

    fswi = self.fswi
    type_carrier = self.type_carrier

    T = 1 / fswi
    time = time % T

    if type_carrier == 1:  # forward toothsaw carrier
        Y = (
            20
            * (
                np.where(time <= 0.5 * T, time, 0) * time
                + np.where(time > 0.5 * T, time, 0) * (time - T)
            )
            / (0.5 * T)
        )
    elif type_carrier == 2:  # backwards toothsaw carrier
        Y = (
            20
            * -(
                np.where(time <= 0.5 * T, time, 0) * time
                + np.where(time > 0.5 * T, time, 0) * (time - T)
            )
            / (0.5 * T)
        )
    elif type_carrier == 3:  # toothsaw carrier
        t1 = (1 + type_carrier) * T / 4
        t2 = T - t1
        Y = (
            np.where(time <= t1, 1, 0) * time / t1
            + np.where(time > t1, 1, 0)
            * np.where(time < t2, 1, 0)
            * (-time + 0.5 * T)
            / (-t1 + 0.5 * T)
            + np.where(time >= t2, 1, 0) * (time - T) / (T - t2)
        )
    else:
        wswiT = 2 * np.pi * time * fswi
        Y = signal.sawtooth(wswiT, 0.5)

    return Y
