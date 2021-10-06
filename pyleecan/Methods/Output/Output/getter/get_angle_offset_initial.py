# -*- coding: utf-8 -*-


def get_angle_offset_initial(self):
    """Return the difference between the d axis angle of the stator and the rotor

    Parameters
    ----------
    self : Output
        an Output object

    Returns
    -------
    angle_offset_initial: float
        difference between the d axis angle of the stator and the rotor [rad]

    """

    # Already available => Return
    if self.geo.angle_offset_initial is not None:
        return self.geo.angle_offset_initial
    else:  # Compute
        self.geo.angle_offset_initial = self.simu.machine.comp_angle_offset_initial()
        return self.geo.angle_offset_initial
