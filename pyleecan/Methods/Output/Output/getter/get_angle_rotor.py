from numpy import pi


def get_angle_rotor(self, Time=None):
    """Return the angular position of the rotor as a function of time from Time normalizations
    and or calculate angle_rotor and add it to Time normalization

    Parameters
    ----------
    self : Output
        an Output object
    Time: Data
        a time axis (SciDataTool Data object)

    Returns
    -------
    angle_rotor: ndarray
        angular position of the rotor as a function of time (vector) [rad]

    """

    # time axis is not provided -> use elec or mag time axis
    if Time is None:
        if self.elec.axes_dict is not None and "time" in self.elec.axes_dict:
            Time = self.elec.axes_dict["time"]
        elif self.mag.axes_dict is not None and "time" in self.mag.axes_dict:
            Time = self.mag.axes_dict["time"]
        else:
            raise Exception("No time axis given, cannot compute rotor angle")

    if "angle_rotor" in Time.normalizations:
        # angle rotor is stored in degrees as normalization of Time axis
        angle_rotor = Time.get_values(normalization="angle_rotor") * pi / 180
    else:
        # Recalculate rotor angular position over time (should not happen)
        self.get_logger().warning(
            "angle_rotor not in time normalizations, recalculate rotor angular position over time and add it to normalizations"
        )
        angle_rotor = self.comp_angle_rotor(Time)

    return angle_rotor
