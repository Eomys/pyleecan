from ....Methods.Simulation.Input import InputError
from ....Classes.OutStruct import OutStruct


def comp_axes(self, output):
    """Compute axes used for the Structural module

    Parameters
    ----------
    self : Structural
        a Structural object
    output : Output
        an Output object (to update)
    """
    if self.parent is None:
        raise InputError("The Structural object must be in a Simulation object to run")
    if self.parent.parent is None:
        raise InputError("The Simulation object must be in an Output object to run")

    # setup OutStruct if None
    if self.parent.parent.struct is None:
        self.parent.parent.struct = OutStruct()

    output.struct.axes_dict = dict()

    for key, val in output.geo.axes_dict.items():
        output.struct.axes_dict[key] = val
