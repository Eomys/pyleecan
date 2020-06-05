# -*- coding: utf-8 -*-


def get_length(self):
    """Return the length of the Frame

    Parameters
    ----------
    self : Frame
        A Frame object

    Returns
    -------
    length: float
        Length of the frame

    """

    if self.comp_height_eq() > 0:
        return self.Lfra
    else:
        return 0
