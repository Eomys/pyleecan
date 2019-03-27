# -*- coding: utf-8 -*-
"""
@date Created on Thu Mar 07 14:05:30 2019
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Classes.OutElec import OutElec
from pyleecan.Methods.Simulation.Input import InputError


def gen_input(self):
    """Generate the input for the magnetic module (electrical output)

    Parameters
    ----------
    self : InCurrent
        An InCurrent object
    """

    output = OutElec()
    # Load and check time
    if self.time is None:
        raise InputError("ERROR: InCurrent.time missing")
    output.time = self.time.get_data()

    if len(output.time.shape) != 1:
        # time should be a vector
        raise InputError(
            "ERROR: InCurrent.time should be a vector, "
            + str(output.time.shape)
            + " shape found"
        )
    Nt_tot = len(output.time)

    # Load and check angle
    if self.angle is None:
        raise InputError("ERROR: InCurrent.angle missing")
    output.angle = self.angle.get_data()
    if len(output.angle.shape) != 1:
        # angle should be a vector
        raise InputError(
            "ERROR: InCurrent.angle should be a vector, "
            + str(output.angle.shape)
            + " shape found"
        )

    # Get the phase number for verifications
    if self.parent is None:
        raise InputError("ERROR: InCurrent object should be inside a Simulation object")
    simu = self.parent
    # Number of winding phases for stator/rotor
    qs = len(simu.machine.stator.get_name_phase())
    qr = len(simu.machine.rotor.get_name_phase())

    # Load and check Is
    if qs > 0:
        if self.Is is None:
            raise InputError("ERROR: InCurrent.Is missing")
        output.Is = self.Is.get_data()
        if output.Is.shape != (Nt_tot, qs):
            raise InputError(
                "ERROR: InCurrent.Is must have the shape "
                + str((Nt_tot, qs))
                + " (len(time), stator phase number), "
                + str(output.Is.shape)
                + " returned"
            )

    # Load and check Ir is needed
    if qr > 0:
        if self.Ir is None:
            raise InputError("ERROR: InCurrent.Ir missing")
        output.Ir = self.Ir.get_data()
        if output.Ir.shape != (Nt_tot, qr):
            raise InputError(
                "ERROR: InCurrent.Ir must have the shape "
                + str((Nt_tot, qr))
                + " (len(time), rotor phase number), "
                + str(output.Ir.shape)
                + " returned"
            )

    # Load and check alpha_rotor and Nr
    if self.angle_rotor is None and self.Nr is None:
        raise InputError(
            "ERROR: InCurrent.angle_rotor and InCurrent.Nr can't be None at the same time"
        )
    if self.angle_rotor is not None:
        output.angle_rotor = self.angle_rotor.get_data()
        if len(output.angle_rotor.shape) != 1 or output.angle_rotor.size != Nt_tot:
            # angle_rotor should be a vector of same length as time
            raise InputError(
                "ERROR: InCurrent.angle_rotor should be a vector of the same length as time, "
                + str(output.angle_rotor.shape)
                + " shape found, "
                + str(output.time.shape)
                + " expected"
            )
    if self.Nr is not None:
        output.Nr = self.Nr.get_data()
        if len(output.Nr.shape) != 1 or output.Nr.size != Nt_tot:
            # angle_rotor should be a vector of same length as time
            raise InputError(
                "ERROR: InCurrent.Nr should be a vector of the same length as time, "
                + str(output.Nr.shape)
                + " shape found, "
                + str(output.time.shape)
                + " expected"
            )

    if self.rot_dir is None or self.rot_dir not in [-1, 1]:
        # Enforce default rotation direction
        output.rot_dir = -1
    else:
        output.rot_dir = self.rot_dir

    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )
    # Save the Output in the correct place
    self.parent.parent.elec = output
