# -*- coding: utf-8 -*-

from pyleecan.Methods.Output.Output.getter import GetOutError


def get_BH_stator(self):
    """Return the B(H) curve of the stator material

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
    if self.geo.stator.BH_curve is not None:
        return self.geo.stator.BH_curve

    # Check if possible to get the BH curve
    if (
        self.simu is None
        or self.simu.machine is None
        or self.simu.machine.stator is None
        or self.simu.machine.stator.mat_type is None
    ):
        raise GetOutError(
            "Output.simu.machine.stator.mat_type is not Set, can't get the B(H) curve"
        )
    mat_type = self.simu.machine.stator.mat_type
    if mat_type.mag is None:
        raise GetOutError("stator materials magnetic property is not set")

    # Compute and store the BH curve
    BH = mat_type.mag.get_BH()
    self.geo.stator.BH_curve = BH

    return BH


class BHShapeError(Exception):
    """Raised when the BH curve has not the expected shape
    """

    pass
