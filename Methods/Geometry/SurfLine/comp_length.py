# -*- coding: utf-8 -*-
def comp_length(self):
    """Compute the length of the SurfLine object

    Parameters
    ----------
    self : SurfLine
        A SurfLine object

    Returns
    -------
    length: float
        Length of the surface [m]


    """
    # check if the SurfLine is correct
    self.check()
    length = 0
    for line in self.line_list:
        length += line.comp_length()

    return length
