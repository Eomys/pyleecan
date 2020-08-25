# -*- coding: utf-8 -*-


def comp_surface_magnet_id(self, index):
    """Compute the surface of the hole magnet of the corresponding index

    Parameters
    ----------
    self : HoleUD
        A HoleUD object
    index : int
        Index of the magnet to compute the surface

    Returns
    -------
    Smag: float
        Surface of the Magnet [m**2]
    """

    label = "magnet_" + str(index)
    if label in self.magnet_dict:
        if self.magnet_dict[label] is None:  # Magnet disabled
            return 0
        else:
            # Find the corresponding surface
            mag_id = 0
            for surf in self.surf_list:
                if "HoleMagnet" in surf.label and mag_id == index:
                    return surf.comp_surface()
                elif "HoleMagnet" in surf.label:
                    mag_id += 1
            return 0
