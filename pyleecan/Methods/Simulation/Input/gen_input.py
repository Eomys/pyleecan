from numpy import ndarray

from ....Classes.OutElec import OutElec
from ....Methods.Simulation.Input import InputError


def gen_input(self):
    """Generate the input for the electrical module (time/space discretization)

    Parameters
    ----------
    self : Input
        An Input object
    """

    output = OutElec()
    simu = self.parent

    # Replace N0=0 by 0.1 rpm
    if self.N0 == 0:
        self.N0 = 0.1
        self.get_logger().debug("Updating N0 from 0 [rpm] to 0.1 [rpm]")
    self.comp_axes(machine=simu.machine, N0=self.N0)

    # Get the phase number for verifications
    if self.parent is None:
        raise InputError("Input object should be inside a Simulation object")

    if self.parent.parent is None:
        raise InputError(
            "Input parent error:"
            + " The Simulation object must be in an Output object to run"
        )

    # Create the correct Output object
    output = OutElec()
    self.comp_axes(machine=simu.machine)

    # Save the Output in the correct place
    self.parent.parent.elec = output
