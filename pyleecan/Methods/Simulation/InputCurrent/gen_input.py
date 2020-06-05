# -*- coding: utf-8 -*-

from ....Classes.OutElec import OutElec
from ....Methods.Simulation.Input import InputError
from numpy import ndarray


def gen_input(self):
    """Generate the input for the magnetic module (electrical output)

    Parameters
    ----------
    self : InputCurrent
        An InputCurrent object
    """

    output = OutElec()
    # Load and check time
    if self.time is None:
        raise InputError("ERROR: InputCurrent.time missing")
    output.time = self.time.get_data()

    if not isinstance(output.time, ndarray) or len(output.time.shape) != 1:
        # time should be a vector
        raise InputError(
            "ERROR: InputCurrent.time should be a vector, "
            + str(output.time.shape)
            + " shape found"
        )
    Nt_tot = len(output.time)

    # Load and check angle
    if self.angle is None:
        raise InputError("ERROR: InputCurrent.angle missing")
    output.angle = self.angle.get_data()
    if not isinstance(output.angle, ndarray) or len(output.angle.shape) != 1:
        # angle should be a vector
        raise InputError(
            "ERROR: InputCurrent.angle should be a vector, "
            + str(output.angle.shape)
            + " shape found"
        )

    # Get the phase number for verifications
    if self.parent is None:
        raise InputError(
            "ERROR: InputCurrent object should be inside a Simulation object"
        )
    simu = self.parent
    # Number of winding phases for stator/rotor
    qs = len(simu.machine.stator.get_name_phase())
    qr = len(simu.machine.rotor.get_name_phase())

    # Load and check Is
    if qs > 0:
        if self.Is is None:
            raise InputError("ERROR: InputCurrent.Is missing")
        output.Is = self.Is.get_data()
        if not isinstance(output.Is, ndarray) or output.Is.shape != (Nt_tot, qs):
            raise InputError(
                "ERROR: InputCurrent.Is must be a matrix with the shape "
                + str((Nt_tot, qs))
                + " (len(time), stator phase number), "
                + str(output.Is.shape)
                + " returned"
            )

    # Load and check Ir is needed
    if qr > 0:
        if self.Ir is None:
            raise InputError("ERROR: InputCurrent.Ir missing")
        output.Ir = self.Ir.get_data()
        if not isinstance(output.Ir, ndarray) or output.Ir.shape != (Nt_tot, qr):
            raise InputError(
                "ERROR: InputCurrent.Ir must be a matrix with the shape "
                + str((Nt_tot, qr))
                + " (len(time), rotor phase number), "
                + str(output.Ir.shape)
                + " returned"
            )

    # Load and check alpha_rotor and Nr
    if self.angle_rotor is None and self.Nr is None:
        raise InputError(
            "ERROR: InputCurrent.angle_rotor and InputCurrent.Nr can't be None at the same time"
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
                "ERROR: InputCurrent.angle_rotor should be a vector of the same length as time, "
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
                "ERROR: InputCurrent.Nr should be a vector of the same length as time, "
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
    # Save the Output in the correct place
    self.parent.parent.elec = output
