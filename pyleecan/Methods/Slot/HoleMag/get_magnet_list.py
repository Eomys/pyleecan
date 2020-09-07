# -*- coding: utf-8 -*-


def get_magnet_list(self):
    """Return the list of magnet (including None)

    Parameters
    ----------
    self : HoleMag
        A HoleMag object

    Returns
    -------
    magnet_list : list
        List of Magnet

    """

    magnet_list = list()
    if hasattr(self, "magnet_dict"):
        for value in self.magnet_dict.values():
            magnet_list.append(value)
    else:
        mag_id = 0
        while hasattr(self, "magnet_" + str(mag_id)):
            magnet_list.append(getattr(self, "magnet_" + str(mag_id)))
            mag_id += 1
    return magnet_list
