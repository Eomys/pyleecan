# -*- coding: utf-8 -*-

from pyleecan.Methods.Output.Output.getter import GetOutError


def get_BH_rotor(self):
    """Return the B(H) curve of the rotor material

    Parameters
    ----------
    self : Output
        an Output object

    Returns
    -------
    BH: numpy.ndarray
        B(H) values (two colums matrix: H and B(H))

    """

    # Already available => Return
    if self.geo.rotor.BH_curve is not None:
        return self.geo.rotor.BH_curve

    # Check if possible to get the BH curve
    if (
        self.simu is None
        or self.simu.machine is None
        or self.simu.machine.rotor is None
        or self.simu.machine.rotor.mat_type is None
    ):
        raise GetOutError(
            "Output.simu.machine.rotor.mat_type is not Set, can't get the B(H) curve"
        )
    mat_type = self.simu.machine.rotor.mat_type
    if mat_type.mag is None:
        raise GetOutError("rotor materials magnetic property is not set")

    # Compute and store the BH curve
    BH = mat_type.mag.get_BH()
    self.geo.rotor.BH_curve = BH

    return BH


class BHShapeError(Exception):
    """Raised when the BH curve has not the expected shape
    """

    pass
