# -*- coding: utf-8 -*-
def check(self):
    """assert the Surface is correct

    Parameters
    ----------
    self : SurfLine
        A SurfLine object

    Returns
    -------
    None
    """
    if self.line_list != []:
        for line in self.line_list:
            line.check()
