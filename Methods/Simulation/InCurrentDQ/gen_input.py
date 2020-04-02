# -*- coding: utf-8 -*-
"""
@date Created on Thu Mar 07 14:05:30 2019
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Classes.MachineSync import MachineSync
from pyleecan.Classes.OutElec import OutElec
from pyleecan.Methods.Simulation.Input import InputError
from pyleecan.Functions.Electrical.coordinate_transformation import dq2ab, ab2uvw
from numpy import ndarray


def gen_input(self):
    """set the electrical output (i.e. input for the magnetic module)

    Parameters
    ----------
    self : InCurrentDQ
        An InCurrentDQ object
    """

    output = OutElec()
    # Load and check time
    if self.time is None:
        raise InputError("ERROR: InCurrentDQ.time missing")
    output.time = self.time.get_data()

    if not isinstance(output.time, ndarray) or len(output.time.shape) != 1:
        # time should be a vector
        raise InputError(
            "ERROR: InCurrentDQ.time should be a vector, "
            + str(output.time.shape)
            + " shape found"
        )
    Nt_tot = len(output.time)

    # Load and check angle
    if self.angle is None:
        raise InputError("ERROR: InCurrentDQ.angle missing")
    output.angle = self.angle.get_data()
    if not isinstance(output.angle, ndarray) or len(output.angle.shape) != 1:
        # angle should be a vector
        raise InputError(
            "ERROR: InCurrentDQ.angle should be a vector, "
            + str(output.angle.shape)
            + " shape found"
        )

    # Get the phase number for verifications
    if self.parent is None:
        raise InputError(
            "ERROR: InCurrentDQ object should be inside a Simulation object"
        )
    simu = self.parent
    # Number of winding phases for stator/rotor
    qs = len(simu.machine.stator.get_name_phase())
    qr = len(simu.machine.rotor.get_name_phase())

    # stator angle to align coordinate systems
    if not hasattr(simu.machine, "comp_initial_angle"):
        raise InputError("ERROR: 'comp_initial_angle' method not implemented")
    init_angle = simu.machine.comp_initial_angle()

    # Load and check Is
    if qs > 0:
        if self.Is is None:
            raise InputError("ERROR: InCurrentDQ.Is missing")
        IsDQ = self.Is.get_data()
        if not isinstance(IsDQ, ndarray) or IsDQ.shape != (Nt_tot, 2):
            raise InputError(
                "ERROR: InCurrentDQ.Is must be a matrix with the shape "
                + str((Nt_tot, 2))
                + " (len(time), stator phase number), "
                + str(IsDQ.shape)
                + " returned"
            )

    # Load and check Ir is needed
    if qr > 0:
        if self.Ir is None:
            raise InputError("ERROR: InCurrentDQ.Ir missing")
        output.Ir = self.Ir.get_data()
        if not isinstance(output.Ir, ndarray) or output.Ir.shape != (Nt_tot, qr):
            raise InputError(
                "ERROR: InCurrentDQ.Ir must be a matrix with the shape "
                + str((Nt_tot, qr))
                + " (len(time), rotor phase number), "
                + str(output.Ir.shape)
                + " returned"
            )

    # Load and check alpha_rotor and Nr
    if self.angle_rotor is None and self.Nr is None:
        raise InputError(
            "ERROR: InCurrentDQ.angle_rotor and InCurrentDQ.Nr can't be None at the same time"
        )
    if self.angle_rotor is not None:
        output.angle_rotor = self.angle_rotor.get_data()
        if (
            not isinstance(output.angle_rotor, ndarray)
            or len(output.angle_rotor.shape) != 1
            or output.angle_rotor.size != Nt_tot
        ):
            # angle_rotor should be a vector of same length as time
            raise InputError(
                "ERROR: InCurrentDQ.angle_rotor should be a vector of the same length as time, "
                + str(output.angle_rotor.shape)
                + " shape found, "
                + str(output.time.shape)
                + " expected"
            )
    if self.Nr is not None:
        output.Nr = self.Nr.get_data()
        if (
            not isinstance(output.Nr, ndarray)
            or len(output.Nr.shape) != 1
            or output.Nr.size != Nt_tot
        ):
            # angle_rotor should be a vector of same length as time
            raise InputError(
                "ERROR: InCurrentDQ.Nr should be a vector of the same length as time, "
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

    if self.angle_rotor_initial is None:
        # Enforce default initial position
        output.angle_rotor_initial = 0
    else:
        output.angle_rotor_initial = self.angle_rotor_initial

    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )

    if qs != 3:
        if self.Is is None:
            raise InputError(
                "ERROR: InCurrentDQ: only 3 phase stator currents implemented yet"
            )

    # save the Output in the correct place
    self.parent.parent.elec = output

    # calculate/get rotor angle and calculate phase currents
    angle_rotor = self.parent.parent.get_angle_rotor()
    angle = angle_rotor - init_angle
    zp = simu.machine.stator.get_pole_pair_number()

    # add stator current
    output.Is = ab2uvw(dq2ab(IsDQ, angle * zp))
