# -*- coding: utf-8 -*-


def clean(self, clean_level=1):
    """Clean MagFEMM outputs depending on cleaning level

    Parameters
    ----------
    self : OutMagFEMM
        the OutMagFEMM object to update
    clean_level : int
        Value to indicate which fields to clean in OutMagFEMM (default=1/min=0/max=4)

    """

    # if clean_level = 0:
    # keep all internal outputs

    if clean_level > 0:
        # clean FEMM_dict
        self.FEMM_dict = None
