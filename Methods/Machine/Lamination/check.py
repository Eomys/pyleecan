# -*- coding: utf-8 -*-

from pyleecan.Methods.Machine import MachineCheckError


def check(self):
    """Check that the Lamination object is correct

    Parameters
    ----------
    self :
        A Lamination object

    Returns
    -------
    None

    Raises
    _______
    LC_VentYokeIn
        The ventilation ducts cross the yoke internal radius
    LC_VentYokeOut
        The ventilation ducts cross the yoke external radius
    LC_RadiusError
        The internal radius is greater than the external one


    """

    if self.Rint > self.Rext:
        raise LC_RadiusError("The internal radius is greater than the " "external one")

    for vent in self.axial_vent:
        vent.check()

        # The ventilation duct must be on the yoke
        if vent.Zh > 0:
            if self.is_internal:
                Rin = self.Rint
                Rout = self.Rint + self.comp_height_yoke()
            else:
                Rin = self.Rint + self.comp_height_yoke()
                Rout = self.Rext

            (Rmin, Rmax) = vent.comp_radius()

            if Rmin < Rin:
                raise LC_VentYokeIn(
                    "The ventilation ducts cross the yoke " "internal radius"
                )
            if Rmax > Rout:
                raise LC_VentYokeOut(
                    "The ventilation ducts cross the yoke " "external radius"
                )


class LaminationCheckError(MachineCheckError):
    """ """

    pass


class LC_RadiusError(LaminationCheckError):
    """  """

    pass


class LC_VentYokeOut(LaminationCheckError):
    """ """

    pass


class LC_VentYokeIn(LaminationCheckError):
    """ """

    pass
