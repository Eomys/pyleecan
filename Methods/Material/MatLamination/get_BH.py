# -*- coding: utf-8 -*-


def get_BH(self):
    """Return the B(H) curve of the material according to the Import object

    Parameters
    ----------
    self : MatLamination
        a MatLamination object

    Returns
    -------
    BH: numpy.ndarray
        B(H) values (two colums matrix: H and B(H))

    """

    BH = self.BH_curve.get_data()

    if len(BH.shape) != 2:
        raise BHShapeError(
            "BH must be a two colums matrix: H and B(H). Return shape: " + str(BH.shape)
        )
    if BH.shape[1] != 2:
        raise BHShapeError(
            "BH must be a two colums matrix: H and B(H). Return shape: " + str(BH.shape)
        )
    return BH


class BHShapeError(Exception):
    """Raised when the BH curve has not the expected shape
    """

    pass
