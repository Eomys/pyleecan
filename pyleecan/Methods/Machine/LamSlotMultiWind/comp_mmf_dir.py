from ....Functions.Load.import_class import import_class


def comp_mmf_dir(self, current_dir=None, phase_dir=None, is_plot=False):
    """Compute the rotation direction of the fundamental magnetomotive force induced by the winding

    Parameters
    ----------
    self : LamSlotMultiWind
        A LamSlotMultiWind object
    felec : float
        Stator current frequency to consider
    current_dir: int
        Stator current rotation direction +/-1
    phase_dir: int
        Stator winding phasor rotation direction +/-1
    is_plot: bool
        True to plot fft2 of stator MMF

    Returns
    -------
    mmf_dir : int
        -1 or +1
    """

    # Call method of LamSlotWind
    LamSlotWind = import_class("pyleecan.Classes", "LamSlotWind")

    rot_dir = LamSlotWind.comp_mmf_dir(self, current_dir, phase_dir, is_plot)

    return rot_dir
