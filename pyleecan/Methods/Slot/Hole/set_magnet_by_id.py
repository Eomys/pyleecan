from . import MagnetIndexError


def set_magnet_by_id(self, index, magnet):
    """Set the magnet at the corresponding index
    Raise error if the hole doesn't have a magnet for the corresponding index

    Parameters
    ----------
    self : Hole
        A Hole object
    index : int
        Index of the magnet to return
    magnet : Magnet
        Magnet object to set (or None)
    """

    label = "magnet_" + str(index)
    if hasattr(self, label):
        setattr(self, label, magnet)
    elif hasattr(self, "magnet_dict") and label in self.magnet_dict:
        self.magnet_dict[label] = magnet
    else:
        raise MagnetIndexError(
            "Hole of type " + str(type(self)) + " has no magnet " + label
        )
