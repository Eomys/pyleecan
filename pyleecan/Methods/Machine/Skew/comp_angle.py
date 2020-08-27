# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError
from numpy import pi, linspace, concatenate, flip, array
from logging import Logger, FileHandler, Formatter, INFO, NOTSET


def comp_angle(self, z_list=None, angle_list=None):
    """Compute skew angles  
    
    Parameters
    ----------
    self : Skew
        a Skew object
    z_list : list
        slice positions

    Returns
    -------
    angle_list : list
        list of skew angles
    z_list : list
        list of slice positions
    """

    logger = self.get_logger()

    if self.parent is None:
        raise InputError("ERROR: The Skew object must be in a Lamination object to run")

    L = self.parent.comp_length()

    if z_list is None:
        if angle_list is not None:  # User-defined skew
            Nslices = len(angle_list)
        else:
            logger.warning(
                "WARNING: Skew slices positions have not been specified, using default slicing: linspace(-L/2, L/2, 5)"
            )
            Nslices = 5  # Default value
        z_list = linspace(-L / 2, L / 2, 5).tolist()
    else:
        z_list = [z * L for z in z_list]

    if self.is_step:
        z_list = [(z_list[i] + z_list[i + 1]) / 2 for i in range(len(z_list) - 1)]

    if angle_list is not None:  # User-defined skew
        if len(angle_list) != len(z_list):
            raise InputError(
                "angle_list and z_list must have the same length for user-defined skew"
            )
        else:
            self.angle_list = angle_list
            self.z_list = z_list

    else:

        Nslices = len(z_list)
        rate = self.rate
        Z = self.parent.get_Zs()

        if self.type == "linear":
            angle_list = [z * rate * 2 * pi / (L * Z) for z in z_list]
        elif self.type == "vshape":
            if self.type == "vshape" and Nslices % 2 == 0:
                logger.warning(
                    "WARNING: Nslices should be odd for v-shape skew, adding one slice."
                )
                Nslices = Nslices + 1
                z_list = sorted(z_list + [0])
                # z_list = linspace(z_list[0], z_list[-1], Nslices).tolist()
            angles = [
                (rate * pi / Z) * (4 * z / L + 1)
                for z in z_list[: int((Nslices + 1) / 2)]
            ]
            angle_list = angles[:-1] + list(reversed(angles))
        elif self.type == "function":
            try:
                angle_list = self.function(array(z_list)).tolist()
            except InputError as error:
                error("Error in skew function definition")
        elif self.type == "user-defined":
            raise InputError("angle_list not provided for user-defined skew")
        else:
            raise InputError("Unknown skew type: " + self.type)

        self.angle_list = angle_list
        self.z_list = z_list
