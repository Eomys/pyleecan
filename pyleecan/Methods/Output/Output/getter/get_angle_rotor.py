from numpy import pi


def get_angle_rotor(self, Time=None):
    """
    Return the angular position of the rotor as a function of time
    and set the Output.elec.angle_rotor attribute if it is None

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
            logger = self.get_logger()
            logger.error("No time axis, cannot compute rotor angle")

    if "angle_rotor" in Time.normalizations:
        # angle rotor is stored in degrees as normalization of Time axis
        angle_rotor = Time.get_values(normalization="angle_rotor") * pi / 180
    else:
        # compute angle rotor from time axis
        angle_rotor = self.comp_angle_rotor(Time)

    return angle_rotor
