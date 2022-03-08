def get_phase_dir(self):
    """Return the Rotation direction of the stator phases

    Parameters
    ----------
    self : LUT
        A LUT object

    Returns
    -------
    phase_dir : int
        Rotation direction of the stator phase
    """

    return self.output_list[0].elec.phase_dir
