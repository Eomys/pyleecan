from numpy import pi

from SciDataTool import Data1D, DataLinspace, Norm_ref, Norm_affine


def comp_axis_time(self, p, per_t, is_antiper_t, Time_in=None):
    """Compute time axis, with or without periodicities and including normalizations

    Parameters
    ----------
    self : Input
        an Input object
    p: int
        Number of pole pairs
    per_t : int
        time periodicity
    is_antiper_t : bool
        if the time axis is antiperiodic
    Time_in: Data
        Input time axis

    Returns
    -------
    Time: Data
        Requested Time axis
    """

    f_elec = self.OP.get_felec(p=p)
    N0 = self.OP.get_N0(p=p)
    A0 = self.angle_rotor_initial

    # Setup normalizations for time and angle axes
    norm_time = {
        "elec_order": Norm_ref(ref=f_elec),
        "mech_order": Norm_ref(ref=N0 / 60),
        "angle_elec": Norm_ref(ref=self.current_dir / (2 * pi * f_elec)),
        "angle_rotor": Norm_affine(
            slope=self.rot_dir * N0 * 360 / 60, offset=A0 * 180 / pi
        ),
    }

    if Time_in is not None:
        # Compute Time axis based on the one stored in OutElec
        Time = Time_in.get_axis_periodic(Nper=per_t, is_aper=is_antiper_t)
        Time.normalizations = norm_time

    # Create time axis
    elif self.time is None:
        # Create time axis as a DataLinspace
        if self.Nrev is not None:
            # Set final time depending on rotor speed and number of revolutions
            t_final = 60 / self.OP.N0 * self.Nrev
        else:
            # Set final time to p times the number of electrical periods
            t_final = p / f_elec
        # Create time axis as a DataLinspace
        Time = DataLinspace(
            name="time",
            unit="s",
            initial=0,
            final=t_final,
            number=self.Nt_tot,
            include_endpoint=False,
            normalizations=norm_time,
        )
        # Add time (anti-)periodicity
        if per_t > 1 or is_antiper_t:
            Time = Time.get_axis_periodic(per_t, is_antiper_t)
    else:
        # Load time data
        time = self.time.get_data()
        self.Nt_tot = time.size
        Time = Data1D(name="time", unit="s", values=time, normalizations=norm_time)
        # Add time (anti-)periodicity
        sym_t = dict()
        if is_antiper_t:
            sym_t["antiperiod"] = per_t
        elif per_t > 1:
            sym_t["period"] = per_t
        Time.symmetries = sym_t
        Time = Time.to_linspace()

    return Time
