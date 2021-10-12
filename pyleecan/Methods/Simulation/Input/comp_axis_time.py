from numpy import pi

from SciDataTool import Data1D, DataLinspace, Norm_ref


def comp_axis_time(self, p, per_t, is_antiper_t, Time_in=None, output=None):
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
    output: Output
        An output object to calculate angle_rotor normalization

    Returns
    -------
    Time: Data
        Requested Time axis
    """

    logger = self.get_logger()

    # Get electrical fundamental frequency
    f_elec = self.comp_felec(p=p)

    # Get magnetic field rotation direction
    if output is not None:
        rot_dir = output.get_rot_dir()
    else:
        if self.rot_dir not in [-1, 1]:
            self.rot_dir = -1
            logger.debug("Enforcing input.rot_dir=-1")
        rot_dir = self.rot_dir

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
            # Set final time depending on rotor speed and number of revolutions
            t_final = 60 / self.N0 * self.Nrev
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

    if output is not None:
        # Compute angle_rotor (added to time normalizations)
        output.comp_angle_rotor(Time)
    else:
        # Add default normalization
        Time.normalizations["angle_rotor"] = Norm_ref(ref=rot_dir * self.N0 * 360 / 60)
        logger.debug("Enforcing default angle_rotor normalization to time axis")

    return Time
