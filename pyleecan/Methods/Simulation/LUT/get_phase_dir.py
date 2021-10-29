from ....Functions.Electrical.dqh_transformation import get_phase_dir_DataTime


def get_phase_dir(self):
    """Get the phase rotating direction of stator flux stored in LUT

    Parameters
    ----------
    self : LUT
        a LUT object

    Returns
    ----------
    phase_dir : int
        rotating direction of phases +/-1
    """

    if self.phase_dir not in [-1, 1]:
        # recalculate phase_dir from Phi_wind
        self.phase_dir = get_phase_dir_DataTime(self.Phi_wind[0])

    return self.phase_dir
