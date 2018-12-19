# -*- coding: utf-8 -*-
def get_lines(self):
    """The list returned contains all the Line of the SurfLine

    Parameters
    ----------
    self : SurfLine
        A SurfLine object


    Returns
    -------
    line_list : list
        list of lines delimiting the surface

    """
    # Check if the surface is correct
    self.check()
    return self.line_list
