# -*- coding: utf-8 -*-
def get_lines(self):
    """The list returned contains all the Line of the SurRing

    Parameters
    ----------
    self : SurfRing
        A SurfRing object


    Returns
    -------
    line_list : list
        list of lines delimiting the surface

    """
    line_list = list()
    line_list.extend(self.out_surf.get_lines())
    line_list.extend(self.in_surf.get_lines())
    return line_list
