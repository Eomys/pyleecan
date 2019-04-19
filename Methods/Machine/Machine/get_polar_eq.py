# -*- coding: utf-8 -*-


def get_polar_eq(self):
    """Returns a polar equivalent of the machine

    Parameters
    ----------
    self : Machine
        Machine object

    Returns
    -------
    polar_eq: Machine
        The polar equivalent of the machine
    """

    # Copy the machine
    polar_eq = type(self)(init_dict=self.as_dict())

    polar_eq.rotor = polar_eq.rotor.get_polar_eq()
    polar_eq.stator = polar_eq.stator.get_polar_eq()
    # TODO: polar frame
    return polar_eq
