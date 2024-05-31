# -*- coding: utf-8 -*-

from numpy import arctan, exp, sqrt, tan


def comp_flower_arc(alpha, Rarc, Rext):
    """Compute the angle and end of a "flower arc".

    Parameters
    ----------
    alpha : float
        Angular width of the arc (angle(z_top_feft)=alpha/2)
    Rarc : float
        The radius of the arc to draw [m]
    Rext : float
        The radius of the external arc ((Rext,0) is on the
        flower arc) [m]

    Returns
    -------
    (alpha_lim,z_top_left,z_top_right) : (float, complex, complex)
        alpha_lim: angle of the arc [ard]
        z_top_left: first point of the arc
        z_top_right: second point fo the arc

    """
    # For readibility
    R = Rarc
    T = tan(alpha / 2)

    # Computation of the angle of the Arc (analitical solution for
    # equation : tan(alpha_mag/2) = Rsin(alpha)/(Rext-R(1-cos(alpha))
    alpha_lim1 = -2 * arctan(
        (R + sqrt(R**2 + 2 * R * Rext * T**2 - Rext**2 * T**2)) / (T * (2 * (R - Rext)))
    )
    alpha_lim2 = -2 * arctan(
        (R - sqrt(R**2 + 2 * R * Rext * T**2 - Rext**2 * T**2)) / (T * (2 * R - Rext))
    )
    alpha_lim = min(abs(alpha_lim1), abs(alpha_lim2))

    z_top_left = R * exp(+1j * alpha_lim) + (Rext - R)
    z_top_right = R * exp(-1j * alpha_lim) + (Rext - R)

    return (alpha_lim, z_top_left, z_top_right)
