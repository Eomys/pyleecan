from numpy import pi

from ....Classes.LamSlotWind import LamSlotWind


def comp_length(self):
    """Compute the end winding conductor length on one side for a half-turn
    excluding the straight conductor length outside of the lamination (winding.Lewout).

    Parameters
    ----------
    self: EndWindingRect
        A EndWindingRect object

    Returns
    -------
    end_wind_length : float
        End-winding length on one side for a half-turn [m].
    """

    # check that Endwinding is in Winding of a Lamination with slots
    if (
        self.parent is None
        or self.parent.parent is None
        or not isinstance(self.parent.parent, LamSlotWind)
        or self.parent.parent.slot is None
    ):
        self.get_logger.warning(
            "EndWindingRect.comp_length(): "
            + "EndWindingRect has to be in a lamination with slot winding to calculate "
            + "the end winding length. Returning zero lenght."
        )
        return 0

    Rmid = self.parent.parent.slot.comp_radius_mid_active()
    Zs = self.parent.parent.slot.Zs
    p = self.parent.p

    # get the coil pitch (with some fall backs), first from the user definition
    # TODO utilize swat_em coil pitch calc.
    coil_pitch = self.coil_pitch
    if coil_pitch is None:
        # try to get coil_pitch of winding
        coil_pitch = getattr(self.parent, "coil_pitch", None)
        if coil_pitch is None:
            coil_pitch = Zs / p / 2
            self.get_logger().warning(
                "EndWindingCirc.comp_lenght_endwinding():"
                + "Using a coil pitch of one pole pitch for EW length calculation."
            )

    # end winding length is half the distance between two slots separated by the coil pitch
    end_wind_length = coil_pitch * pi / Zs * Rmid

    return end_wind_length
