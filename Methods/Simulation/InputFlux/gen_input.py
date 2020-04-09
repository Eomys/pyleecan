# -*- coding: utf-8 -*-
"""
@date Created on Thu Mar 07 14:05:30 2019
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Classes.OutMag import OutMag
from pyleecan.Methods.Simulation.Input import InputError
from numpy import ndarray


def gen_input(self):
    """Generate the input for the structural module (magnetic output)

    Parameters
    ----------
    self : InputFlux
        An InputFlux object
    """

    output = OutMag()
    # Load and check time
    if self.time is None:
        raise InputError("ERROR: InputFlux.time missing")
    output.time = self.time.get_data()

    if not isinstance(output.time, ndarray) or len(output.time.shape) != 1:
        # time should be a vector
        raise InputError(
            "ERROR: InputFlux.time should be a vector, "
            + str(output.time.shape)
            + " shape found"
        )
    Nt_tot = len(output.time)

    # Load and check angle
    if self.angle is None:
        raise InputError("ERROR: InputFlux.angle missing")
    output.angle = self.angle.get_data()
    if not isinstance(output.angle, ndarray) or len(output.angle.shape) != 1:
        # angle should be a vector
        raise InputError(
            "ERROR: InputFlux.angle should be a vector, "
            + str(output.angle.shape)
            + " shape found"
        )
    Na_tot = len(output.angle)

    if self.Br is None:
        raise InputError("ERROR: InputFlux.Br missing")
    output.Br = self.Br.get_data()
    if not isinstance(output.Br, ndarray) or output.Br.shape != (Nt_tot, Na_tot):
        raise InputError(
            "ERROR: InputFlux.Br must be a matrix with the shape "
            + str((Nt_tot, Na_tot))
            + " (len(time), stator phase number), "
            + str(output.Br.shape)
            + " returned"
        )

    if self.Bt is not None:
        output.Bt = self.Bt.get_data()
        if not isinstance(output.Bt, ndarray) or output.Bt.shape != (Nt_tot, Na_tot):
            raise InputError(
                "ERROR: InputFlux.Bt must be a matrix with the shape "
                + str((Nt_tot, Na_tot))
                + " (len(time), rotor phase number), "
                + str(output.Bt.shape)
                + " returned"
            )
    else:
        output.Bt = None

    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )
    # Save the Output in the correct place
    self.parent.parent.mag = output
