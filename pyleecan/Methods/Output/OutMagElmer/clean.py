# -*- coding: utf-8 -*-


def clean(self, clean_level=1):
    """Clean MagElmer outputs depending on cleaning level

    Parameters
    ----------
    self : OutMagElmer
        the OutMagElmer object to update
    clean_level : int
        Value to indicate which fields to clean in OutMagElmer (default=1/min=0/max=4)

    """

    # if clean_level = 0:
    # keep all internal outputs

    if clean_level > 0:
        # clean FEA_dict
        self.FEA_dict = None
