# -*- coding: utf-8 -*-


def comp_surface_magnet_id(self, index):
    """Compute the surface of the hole magnet of the corresponding index

    Parameters
    ----------
    self : HoleM63
        A HoleM63 object
    index : int
        Index of the magnet to compute the surface

    Returns
    -------
    Smag: float
        Surface of the Magnet [m**2]
    """

    if index != 0:
        raise Exception("Only one magnet for HoleM63")
    if self.magnet_0 is not None:
        return self.comp_surface()  # Full magnet, no air
    return 0
