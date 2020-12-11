# -*- coding: utf-8 -*-


def remove_magnet(self):
    """Remove the magnet (set to None) of the Hole

    Parameters
    ----------
    self : HoleUD
        a HoleUD object
    """

    for key in self.magnet_dict.keys():
        self.magnet_dict[key] = None
