# -*- coding: utf-8 -*-


def comp_length_endwinding(self):
    """Compute the end winding conductor length on one side for a half-turn
    excluding the straight conductor length outside of the lamination (winding.Lewout).
    Since this is the abstract class method the actual length returned will be zero.

    Parameters
    ----------
    self: EndWinding
        A EndWinding object
    Returns
    -------
    end_wind_length : float
        End-winding length on one side for a half-turn [m].
    """

    return 0
