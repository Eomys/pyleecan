# -*- coding: utf-8 -*-

from .....Methods.Output.Output.getter import GetOutError
from numpy import pi, cumsum, roll, size, ones


def get_angle_rotor(self):
    """
    Return the angular position of the rotor as a function of time
    and set the Output.elec.angle_rotor attribute if it is None

    Parameters
    ----------
    self : Output
        an Output object

    Returns
    -------
    alpha_rotor: numpy.ndarray
        angular position of the rotor as a function of time (vector) [rad]

    """

    # Already available => Return
    if self.elec.angle_rotor is not None and self.elec.angle_rotor.size > 0:
        return self.elec.angle_rotor
    else:  # Compute according to the speed
        Nr = self.elec.get_Nr()
        if self.elec.rot_dir is None or self.elec.rot_dir not in [-1, 1]:
            rot_dir = -1
        else:
            rot_dir = self.elec.rot_dir
        if self.elec.angle_rotor_initial is None:
            A0 = 0
        else:
            A0 = self.elec.angle_rotor_initial

        if self.elec.time.size == 1:
            # Only one time step, no need to compute the position
            return ones(1) * A0
        else:
            deltaT = self.elec.time[1] - self.elec.time[0]
            # Convert Nr from [rpm] to [rad/s] (time in [s] and angle_rotor in [rad])
            Ar = cumsum(rot_dir * deltaT * Nr * 2 * pi / 60)
            # Enforce first position to 0
            Ar = roll(Ar, 1)
            Ar[0] = 0
            self.elec.angle_rotor = Ar + A0
            return self.elec.angle_rotor
