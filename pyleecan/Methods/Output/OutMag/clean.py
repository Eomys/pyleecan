# -*- coding: utf-8 -*-


def clean(self, clean_level=1):
    """Clean Magnetics standard outputs depending on cleaning level

    Parameters
    ----------
    self : OutMag
        the OutMag object to update
    clean_level : int
        Value to indicate which fields to clean in OutMag (default=1/min=0/max=4/5=LUT)

    """

    # if clean_level = 0:
    # keep all outputs

    if clean_level == 5:  # LUT
        self.meshsolution = None
        self.Phi_wind_stator = None  # Use Phi_wind
        self.emf = None
        self.internal = None
        self.axes_dict = None
        return

    if clean_level > 0:
        # clean meshsolution
        self.meshsolution = None

    if clean_level > 1:
        # clean airgap flux density
        self.B = None

    if clean_level > 2:
        # clean airgap flux density
        self.Tem = None
        self.Phi_wind_stator = None
        self.Phi_wind = None
        self.emf = None

    if clean_level > 3:
        # clean all internal outputs
        self.internal = None
        self.axes_dict = None

    else:
        # clean internal depending on log_level
        self.internal.clean(clean_level)
