from ....Functions.Load.import_class import import_class


def comp_angle_d_axis(self, is_plot=False):
    """Compute the angle between the X axis and the first d+ axis
    By convention a "Tooth" is centered on the X axis

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object
    is_plot : bool
        True to plot d axis position regarding unit mmf

    Returns
    -------
    d_angle : float
        angle between the X axis and the first d+ axis
    """

    # Call method of LamSlotWind
    LamSlotWind = import_class("pyleecan.Classes", "LamSlotWind")

    d_angle = LamSlotWind.comp_angle_d_axis(self, is_plot=is_plot)

    return d_angle
