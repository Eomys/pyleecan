from numpy import mean, pi

from ....Functions.Electrical.coordinate_transformation import n2dq


def comp_Phi_dq(self):
    """Compute the stator flux linkage along dq axes

    Parameters
    ----------
    self : OutMag
        an OutMag object

    Returns
    -------
    Phi_dqh : ndarray
        Stator flux linkage along dq axes [Wb]

    """

    output = self.parent

    qs = output.simu.machine.stator.winding.qs
    felec = output.elec.felec

    # Get rotation direction of the fundamental magnetic field created by the winding
    rot_dir = output.get_rot_dir()

    result = self.Phi_wind_stator.get_along("time[oneperiod]", "phase")

    Phi = result["Phi_{wind}"]

    time = result["time"]

    # Get stator current function of time
    Phi_dq_time = n2dq(
        Phi, 2 * pi * felec * time, n=qs, rot_dir=rot_dir, is_dq_rms=True
    )

    Phi_dq = mean(Phi_dq_time, axis=0)

    return Phi_dq
