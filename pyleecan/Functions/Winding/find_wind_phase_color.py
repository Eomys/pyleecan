# -*- coding: utf-8 -*-
from ...definitions import config_dict

PHASE_COLORS = config_dict["PLOT"]["color_dict"]["PHASE_COLORS"]


def find_wind_phase_color(label, wind_mat):
    """Returns Color phase of the Winding surface

    Parameters
    ----------
    label : str
        the label of the surface

    wind_mat : numpy.ndarray
        A matrix [Nrad,Ntan,Zs,qs] representing the winding

    Returns
    -------
    color: str
        Color of the zone

    """
    st = label.split("_")
    Nrad = int(st[1][1:])
    Ntan = int(st[2][1:])
    Zs = int(st[3][1:])
    if wind_mat is not None:
        q = get_phase_id(wind_mat, Nrad, Ntan, Zs)
        if q is None:  # No phase => White
            color = "w"
        else:
            color = PHASE_COLORS[q]
    else:
        color = PHASE_COLORS[0]

    return color


def get_phase_id(wind_mat, Nrad, Ntan, Zs):
    """Return the id of the corresponding phase for the zone (Nrad,Ntan,Zs)

    Parameters
    ----------
    wind_mat : numpy.ndarray
        A matrix [Nrad,Ntan,Zs,qs] representing the winding
    Nrad : int
        Zone radial coordinate
    Ntan : int
        Zone tagential coordinate
    Zs : int
        Zone slot number coordinate

    Returns
    -------
    q_id: int
        Id of the phase

    """
    A = wind_mat[Nrad, Ntan, Zs, :]
    for zz in range(len(A)):
        if A[zz] != 0:
            return zz
    return None  # If all the phase are at 0 : the zone is empty
