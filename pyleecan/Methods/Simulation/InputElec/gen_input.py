# -*- coding: utf-8 -*-

from ....Classes.OutElec import OutElec
from ....Classes.Simulation import Simulation
from ....Methods.Simulation.Input import InputError
from numpy import ndarray, pi, linspace


def gen_input(self):
    """Generate the input for the magnetic module (electrical output)

    Parameters
    ----------
    self : InputCurrent
        An InputCurrent object
    """

    output = OutElec()

    # Get the phase number for verifications
    if self.parent is None:
        raise InputError(
            "ERROR: InputCurrent object should be inside a Simulation object"
        )
    # get the simulation
    if isinstance(self.parent, Simulation):
        simu = self.parent
    elif isinstance(self.parent.parent, Simulation):
        simu = self.parent.parent
    else:
        raise InputError("Cannot find InputElec simulation.")

    output.N0 = self.N0
    output.felec = self.comp_felec()

    # Load/define time
    if self.time is None:
        if self.Nrev is None or self.Nt_tot is None or self.N0 is None:
            raise InputError("ERROR: InputCurrent.time missing")
        output.time = self.comp_time(self.N0)
    else:  # Enfore time vector
        output.time = self.time.get_data()
    # Check time
    if not isinstance(output.time, ndarray) or len(output.time.shape) != 1:
        # time should be a vector
        raise InputError(
            "ERROR: InputCurrent.time should be a vector, "
            + str(output.time.shape)
            + " shape found"
        )
    self.Nt_tot = len(output.time)

    # Load/define angle
    if self.angle is None:
        if self.Na_tot is None:
            raise InputError("ERROR: InputCurrent.angle missing")
        output.angle = linspace(0, 2 * pi, self.Na_tot)
    else:  # Enfore angle vector
        output.angle = self.angle.get_data()
    # Check angle
    if not isinstance(output.angle, ndarray) or len(output.angle.shape) != 1:
        # angle should be a vector
        raise InputError(
            "ERROR: InputCurrent.angle should be a vector, "
            + str(output.angle.shape)
            + " shape found"
        )
    self.Na_tot = len(output.angle)

    # Initialize output at None
    output.Id_ref = None
    output.Iq_ref = None
    output.Ud_ref = None
    output.Uq_ref = None
    output.Is = None
    output.Ir = None

    # Load and check voltage and currents
    if self.Ud_ref is not None and self.Uq_ref is not None:
        output.Ud_ref = self.Ud_ref
        output.Uq_ref = self.Uq_ref
        simu.elec.eec.parameters["Ud"] = self.Ud_ref
        simu.elec.eec.parameters["Uq"] = self.Uq_ref
        if self.Id_ref is not None and self.Iq_ref is not None:
            output.Id_ref = self.Id_ref
            output.Iq_ref = self.Iq_ref
        else:
            output.Id_ref = 1
            output.Iq_ref = 1
    elif self.Id_ref is not None and self.Iq_ref is not None:
        output.Id_ref = self.Id_ref
        output.Iq_ref = self.Iq_ref
    else:
        raise InputError("ERROR: Id/Iq or Ud/Uq missing")

    # Load and check rot_dir
    if self.rot_dir is None or self.rot_dir not in [-1, 1]:
        # Enforce default rotation direction
        output.rot_dir = -1
    else:
        output.rot_dir = self.rot_dir

    if simu.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )

    # Save the Output in the correct place
    simu.parent.elec = output
