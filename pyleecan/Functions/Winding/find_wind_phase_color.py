# -*- coding: utf-8 -*-
from ...definitions import config_dict
from ...Functions.labels import decode_label

PHASE_COLORS = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]


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
    label_dict = decode_label(label)
    Nrad = label_dict["R_id"]
    Ntan = label_dict["T_id"]
    Zs_id = label_dict["S_id"]
    if wind_mat is not None:
        q_id = get_phase_id(wind_mat, Nrad, Ntan, Zs_id)
        if q_id is None:  # No phase => White
            color = "w"
            sign = None
        else:
            # Looping colors when there are more than 8 phases
            color = PHASE_COLORS[q_id % len(PHASE_COLORS)]
            if wind_mat[Nrad, Ntan, Zs_id, q_id] > 0:
                sign = "+"
            elif wind_mat[Nrad, Ntan, Zs_id, q_id] < 0:
                sign = "-"
            else:
                sign = None
    else:
        color = PHASE_COLORS[0]
        sign = None

    return color, sign


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
