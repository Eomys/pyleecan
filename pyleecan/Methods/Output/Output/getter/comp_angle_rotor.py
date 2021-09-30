from numpy import pi, cumsum, roll, ones, unique


def comp_angle_rotor(self, Time):
    """
    Computes the angular position of the rotor as a function of time
    and set the Output.elec.angle_rotor attribute if it is None

    Parameters
    ----------
    self : Output
        an Output object
    Time : Data
        a time axis (SciDataTool Data object)

    Returns
    -------
    alpha_rotor: numpy.ndarray
        angular position of the rotor as a function of time (vector) [rad]

    """

    # Compute according to the speed
    Nr = self.elec.get_Nr(Time=Time)

    # Get rotor rotating direction
    # rotor rotating is the opposite of rot_dir which is fundamental field rotation direction
    # so that rotor moves in positive angles
    rot_dir = -self.get_rot_dir()

    # Compute rotor initial angle (for synchronous machines, to align rotor d-axis and stator alpha-axis)
    A0 = self.get_angle_offset_initial()

    # Case where normalization is a constant
    if A0 == 0 and unique(Nr).size == 1:
        angle_rotor = rot_dir * Nr[0] * 2 * pi / 60

    else:

        time = Time.get_values(is_oneperiod=False)
        if time.size == 1:
            # Only one time step, no need to compute the position
            angle_rotor = ones(1) * A0
        else:
            deltaT = time[1] - time[0]
            # Convert Nr from [rpm] to [rad/s] (time in [s] and angle_rotor in [rad])
            Ar = cumsum(rot_dir * deltaT * Nr * 2 * pi / 60)
            # Enforce first position to 0
            Ar = roll(Ar, 1)
            Ar[0] = 0
            angle_rotor = Ar + A0

    # Store in time axis normalizations
    Time.normalizations["angle_rotor"] = angle_rotor

    return angle_rotor
