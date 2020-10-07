# -*- coding: utf-8 -*-

from .....Methods.Output.Output.getter import GetOutError
from numpy import pi, cumsum, roll, size, ones


def get_angle_rotor(self):
    """Return the angular position of the rotor as a function of time

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

        # Get rotor rotating direction
        rot_dir = self.elec.rot_dir

        # Compute rotor initial angle (for synchronous machines, to align rotor d-axis and stator alpha-axis)
        A0 = self.get_angle_offset_initial()

        time = self.elec.time.get_values(is_oneperiod=False)
        if time.size == 1:
            # Only one time step, no need to compute the position
            return ones(1) * A0
        else:
            deltaT = time[1] - time[0]
            # Convert Nr from [rpm] to [rad/s] (time in [s] and angle_rotor in [rad])
            Ar = cumsum(rot_dir * deltaT * Nr * 2 * pi / 60)
            # Enforce first position to 0
            Ar = roll(Ar, 1)
            Ar[0] = 0
            self.elec.angle_rotor = Ar + A0
            return self.elec.angle_rotor
