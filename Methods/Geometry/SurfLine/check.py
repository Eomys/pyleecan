# -*- coding: utf-8 -*-
def check(self):
    """assert the Surface is correct (the radius > 0)

    Parameters
    ----------
    self : Surface
        A Surface object

    Returns
    -------
    None
    """
    if self.line_list != []:
        for line in self.line_list:
            line.check()
