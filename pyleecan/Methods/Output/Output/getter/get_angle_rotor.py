# -*- coding: utf-8 -*-

from .....Methods.Output.Output.getter import GetOutError
from numpy import pi, cumsum, roll, size, ones


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
    alpha_rotor: numpy.ndarray
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

    # TODO: debug with normalizations as array
    if False:  # "angle_rotor" in Time.normalizations:
        # angle rotor is stored as normalization of Time axis
        angle_rotor = Time.normalizations["angle_rotor"]
    else:
        # compute angle rotor from time axis
        angle_rotor = self.comp_angle_rotor(Time)

    return angle_rotor
