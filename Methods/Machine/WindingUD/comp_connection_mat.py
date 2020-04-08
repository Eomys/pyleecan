# -*- coding: utf-8 -*-

from pyleecan.Methods.Machine.Winding import WindingError


def comp_connection_mat(self, Zs=None):
    """Compute the Winding Matrix (for winding type 0)
    Type 0 : User defined

    Parameters
    ----------
    self : Winding
        A: Winding object
    Zs : int
        Number of Slot (Integer >0)

    Returns
    -------
    wind_mat: numpy.ndarray
        Winding Matrix (Nlay_rad, Nlay_tan, Zs, qs)

    Raises
    ------
    WindingT0DefSumError
        the sum of the element in user_wind_mat
        must be null
    WindingT0DefShapeError
        user_wind_mat shape must be (Nlay_rad,
        Nlay_tan,Zs,qs)

    """
    if Zs is None:
        if self.parent is None:
            raise WindingError(
                "ERROR: The Winding object must be in a Lamination object."
            )

        if self.parent.slot is None:
            raise WindingError(
                "ERROR: The Winding object must be in a Lamination object with Slot."
            )

        Zs = self.parent.slot.Zs

    assert Zs > 0, "Zs must be >0"
    assert Zs % 1 == 0, "Zs must be an integer"

    wind_mat = self.user_wind_mat

    shape = wind_mat.shape
    if shape[2] != Zs:
        raise WindingT0DefShapeError(
            "wrong winding definition, wrong "
            "user_wind_mat shape, must be (Nlay_rad, "
            "Nlay_tan, Zs,qs), Zs = " + str(Zs) + " but " + str(shape) + " given !"
        )
    elif shape[3] != self.qs:
        raise WindingT0DefShapeError(
            "wrong winding definition, wrong "
            "user_wind_mat shape, must be (Nlay_rad, "
            "Nlay_tan, Zs,qs), qs = " + str(self.qs) + " but " + str(shape) + " given !"
        )

    if wind_mat.sum() != 0:
        raise WindingT0DefSumError(
            "wrong winding definition, the sum of the "
            "element in user_wind_mat isn't null !"
        )

    # Apply the transformations
    if self.is_reverse_wind:
        wind_mat = reverse_wind_mat(wind_mat)
    if self.Nslot_shift_wind > 0:
        wind_mat = shift_wind_mat(wind_mat, self.Nslot_shift_wind)

    return wind_mat


class WindingT0DefShapeError(WindingError):
    """ """

    pass


class WindingT0DefSumError(WindingError):
    """ """

    pass
