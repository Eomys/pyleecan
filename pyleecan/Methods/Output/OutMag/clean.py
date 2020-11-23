# -*- coding: utf-8 -*-


def clean(self):
    """Clean Magnetics standard outputs depending on simulation cleaning level

    Parameters
    ----------
    self : OutMag
        the OutMag object to update
    """

    clean_level = self.parent.simu.clean_level

    # TODO
