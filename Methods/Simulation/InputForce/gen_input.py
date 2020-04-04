# -*- coding: utf-8 -*-
"""
@date Created on Thu Mar 07 14:05:30 2019
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Classes.OutStruct import OutStruct
from pyleecan.Methods.Simulation.Input import InputError
from numpy import ndarray


def gen_input(self):
    """Generate the input for the structural module (skip force computation)

    Parameters
    ----------
    self : InputForce
        An InputForce object
    """

    output = OutStruct()
    # Load and check time
    if self.time is None:
        raise InputError("ERROR: InputForce.time missing")
    output.time = self.time.get_data()

    if not isinstance(output.time, ndarray) or len(output.time.shape) != 1:
        # time should be a vector
        raise InputError(
            "ERROR: InputForce.time should be a vector, "
            + str(output.time.shape)
            + " shape found"
        )
    Nt_tot = len(output.time)

    # Load and check angle
    if self.angle is None:
        raise InputError("ERROR: InputForce.angle missing")
    output.angle = self.angle.get_data()
    if not isinstance(output.angle, ndarray) or len(output.angle.shape) != 1:
        # angle should be a vector
        raise InputError(
            "ERROR: InputForce.angle should be a vector, "
            + str(output.angle.shape)
            + " shape found"
        )
    Na_tot = len(output.angle)

    if self.Prad is None:
        raise InputError("ERROR: InputForce.Prad missing")
    output.Prad = self.Prad.get_data()
    if not isinstance(output.Prad, ndarray) or output.Prad.shape != (Nt_tot, Na_tot):
        raise InputError(
            "ERROR: InputForce.Prad must be a matrix with the shape "
            + str((Nt_tot, Na_tot))
            + " (len(time), stator phase number), "
            + str(output.Prad.shape)
            + " returned"
        )

    if self.Ptan is not None:
        output.Ptan = self.Ptan.get_data()
        if not isinstance(output.Ptan, ndarray) or output.Ptan.shape != (
            Nt_tot,
            Na_tot,
        ):
            raise InputError(
                "ERROR: InputForce.Ptan must be a matrix with the shape "
                + str((Nt_tot, Na_tot))
                + " (len(time), rotor phase number), "
                + str(output.Ptan.shape)
                + " returned"
            )
    else:
        output.Ptan = None

    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )
    # Save the Output in the correct place
    self.parent.parent.struct = output
