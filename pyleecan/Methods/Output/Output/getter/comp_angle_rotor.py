from numpy import pi, cumsum, roll, array, unique

from SciDataTool import Norm_vector, Norm_affine


def comp_angle_rotor(self, Time):
    """Computes the angular position of the rotor as a function of time and set it as normalization
    (should not happen since angle_rotor is already added in Time normalizations in Input.comp_axis_time)

    Parameters
    ----------
    self : Output
        an Output object
    Time : Data
        a time axis (SciDataTool Data object)
    rot_dir: int
        Rotor rotating direction (by default -1: clockwise)

    Returns
    -------
    angle_rotor: ndarray
        angular position of the rotor as a function of time (vector) [rad]

    """

    # Get rotor rotating direction
    rot_dir = self.geo.rot_dir

    # Compute according to the speed
    Nr = self.elec.get_Nr(Time=Time)

    # Compute rotor initial angle (for synchronous machines, to align rotor d-axis and stator alpha-axis)
    A0 = self.get_angle_rotor_initial()

    # Case where normalization is a constant
    if unique(Nr).size == 1:
        # Define affine normalization between time and rotor angle
        Time.normalizations["angle_rotor"] = Norm_affine(
            slope=rot_dir * Nr[0] * 360 / 60, offset=A0 * 180 / pi
        )
        # Compute rotor angle array from normalization
        angle_rotor = Time.get_values(normalization="angle_rotor") * pi / 180

    else:
        # Calculate rotor angle from spee
        time = Time.get_values(is_smallestperiod=True)
        if time.size == 1:
            # Only one time step, no need to compute the position
            angle_rotor = array([A0])
        else:
            deltaT = time[1] - time[0]
            # Convert Nr from [rpm] to [rad/s] (time in [s] and angle_rotor in [rad])
            Ar = cumsum(rot_dir * deltaT * Nr * 2 * pi / 60)
            # Enforce first position to 0
            Ar = roll(Ar, 1)
            Ar[0] = 0
            angle_rotor = Ar + A0
        # Define vector normalization between time and rotor angle
        Time.normalizations["angle_rotor"] = Norm_vector(vector=angle_rotor)

    return angle_rotor
