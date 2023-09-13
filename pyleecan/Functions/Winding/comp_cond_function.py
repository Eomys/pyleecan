from numpy import mod, pi


def comp_cond_function(alpha_cond, W0, alpha_rad):
    """Single conductor winding function for magnetomotive force calculation

    Parameters
    ----------
    alpha_cond : float
        angular position of the conductor [rad]
    W0 : float
        slot opening angular width (for linear rise of the mmf) [rad]
    alpha_rad : ndarray
        Position vector to compute the conductor winding function

    Returns
    -------
    wf: ndarray
        The conductor winding function

    """

    alpha_rad = mod(alpha_rad + pi - alpha_cond, 2 * pi)

    thi = 0
    thf = 2 * pi
    if W0 == 0:
        A = (alpha_rad < pi) * 1
        B = (alpha_rad > pi) * 1

        return B * ((alpha_rad - thf) / (pi - thf)) - A * (
            (alpha_rad - thi) / (pi - thi)
        )

    else:
        x1 = pi - W0 / 2.0
        x2 = pi + W0 / 2.0

        A = (alpha_rad < x1) * 1
        B = (alpha_rad > x2) * 1

        C = 1 - A - B
        return (
            C * (alpha_rad - pi) / (W0 / 2.0)
            + B * ((alpha_rad - thf) / (x2 - thf))
            - A * ((alpha_rad - thi) / (x1 - thi))
        )
