from numpy import pi

from SciDataTool import Data1D, DataLinspace, Norm_ref

from ....Methods.Simulation.Input import InputError


def comp_axis_time(self, output, p, per_t, is_antiper_t, Time_in=None):
    """Compute time axis, with or without periodicities and including normalizations

    Parameters
    ----------
    self : Input
        an Input object
    output: Output
        An output object to calculate angle_rotor normalization
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
    # Get electrical fundamental frequency
    f_elec = self.comp_felec()

    # Get magnetic field rotation direction
    rot_dir = output.get_rot_dir()

    # Setup normalizations for time and angle axes
    norm_time = {
        "elec_order": Norm_ref(ref=f_elec),
        "mech_order": Norm_ref(ref=f_elec / p),
        "angle_elec": Norm_ref(ref=rot_dir / (2 * pi * f_elec)),
    }

    if Time_in is not None:
        # Compute Time axis based on the one stored in OutElec
        Time = Time_in.get_axis_periodic(Nper=per_t, is_aper=is_antiper_t)
        Time.normalizations = norm_time

    # Create time axis
    elif self.time is None:
        # Create time axis as a DataLinspace
        if self.Nrev is not None:
            if self.N0 is not None:
                t_final = 60 / self.N0 * self.Nrev
            else:
                raise InputError("time and N0 can't be both None")
        else:
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
        else:
            sym_t["period"] = per_t
        Time.symmetries = sym_t
        Time = Time.to_linspace()

    # Compute angle_rotor (added to time normalizations)
    output.comp_angle_rotor(Time)

    return Time
