def get_surfaces_closing(self, sym=1):
    """Return the surfaces needed to close the radii of the Lamination

    Parameters
    ----------
    self : Lamination
        A Lamination object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)

    Returns
    -------
    surf_list : list
        List of the closing surfaces
    """

    # No notch when bore shape
    if self.bore is None:
        return self.get_notches_surf(sym=sym)
    else:
        return list()
