from numpy import log, pi, sqrt

from ....Classes.LamSlotWind import LamSlotWind


def comp_inductance(self):
    """Compute the end winding inductance from "Design of Brushless Permanent-Magnet Machines", J.R Henderson, 2010

    Parameters
    ----------
    self: EndWinding
        A EndWinding object

    Returns
    -------
    Lew : float
        end winding inductance [H].
    """

    # ckeck that Endwinding is in Winding of a Lamination with slots
    if (
        self.parent is None
        or self.parent.parent is None
        or not isinstance(self.parent.parent, LamSlotWind)
        or self.parent.parent.slot is None
    ):
        self.get_logger.warning(
            "EndWindingCirc.comp_inductance(): "
            + "EndWindingCirc has to be in a lamination with slot winding to calculate "
            + "the end winding inductance. Returning zero inductance."
        )
        return 0

    # get the middle radius of the slots active area
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
                "EndWindingCirc.comp_inductance():"
                + "Using a coil pitch of one pole pitch for EW inductance calculation."
            )

    # End winding is a circle whose radius is half the coil pitch distance
    Re = pi / Zs * Rmid * coil_pitch

    # Eq(5.49) p.234
    Scond = self.parent.conductor.comp_surface()
    R = 0.4394 * sqrt(Scond)

    # Eq (5.48) p 233
    Ntcoil = self.parent.Ntcoil
    mu0 = 4 * pi * 1e-7
    Lw = mu0 * Re * Ntcoil**2 * (log(8 * Re / R) - 2)

    return Lw
