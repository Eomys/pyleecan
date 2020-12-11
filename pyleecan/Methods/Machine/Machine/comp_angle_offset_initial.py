# -*- coding: utf-8 -*-


def comp_angle_offset_initial(self):
    """Compute initial angle between the d-axis of the rotor and stator

    Parameters
    ----------
    self : Machine
        A: Machine object

    Returns
    -------
    angle_offset_initial: float
        initial angle between the d-axis of the rotor and stator [rad]

    Raises
    ------


    """
    return self.stator.comp_angle_d_axis() - self.rotor.comp_angle_d_axis()
