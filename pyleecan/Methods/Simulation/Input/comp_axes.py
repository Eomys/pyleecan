from numpy import pi
from SciDataTool import Data1D, DataLinspace
from ....Methods.Simulation.Input import InputError


def comp_axes(
    self,
    machine=None,
    per_a=1,
    is_antiper_a=False,
    per_t=1,
    is_antiper_t=False,
):
    """Compute simulation axes, i.e. space DataObject including (anti)-periodicity
    and time DataObject including (anti)-periodicity and accounting for rotating speed
    and number of revolutions

    Parameters
    ----------
    self : Input
        an Input object
    machine : Machine
        a Machine object
    per_a : int
        angle periodicity
    is_antiper_a : bool
        if the angle axis is antiperiodic
    per_t : int
        time periodicity
    is_antiper_t : bool
        if the time axis is antiperiodic

    Returns
    -------
    axes_dict: {Data}
        dict of axes containing time and angle axes (with or without (anti-)periodicity)

    """

    N0 = self.N0

    if self.time is None and N0 is None:
        raise InputError("time and N0 can't be both None")

    if machine is None:
        # Fetch machine from input
        if (
            self.parent is not None
            and hasattr(self.parent, "machine")
            and self.parent.machine is not None
        ):
            machine = self.parent.machine

    # Get machine pole pair number
    p = machine.get_pole_pair_number()

    # Get electrical fundamental frequency
    f_elec = self.comp_felec()

    # Airgap radius
    Rag = machine.comp_Rgap_mec()

    # Setup normalizations for time and angle axes
    norm_time = {
        "elec_order": f_elec,
        "mech_order": f_elec / p,
    }

    norm_angle = {"space_order": p, "distance": 1 / Rag}

    # Create time axis
    if self.time is None:
        # Create time axis as a DataLinspace
        if self.Nrev is not None:
            t_final = 60 / N0 * self.Nrev
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
        self.Nt_tot = len(time)
        Time = Data1D(name="time", unit="s", values=time, normalizations=norm_time)
        # Add time (anti-)periodicity
        sym_t = dict()
        if is_antiper_t:
            sym_t["antiperiod"] = per_t
        else:
            sym_t["period"] = per_t
        Time.symmetries = sym_t

    # Create angle axis
    if self.angle is None:
        # Create angle axis as a DataLinspace
        Angle = DataLinspace(
            name="angle",
            unit="rad",
            initial=0,
            final=2 * pi,
            number=self.Na_tot,
            include_endpoint=False,
            normalizations=norm_angle,
        )
        # Add angle (anti-)periodicity
        if per_a > 1 or is_antiper_a:
            Angle = Angle.get_axis_periodic(per_a, is_antiper_a)

    else:
        # Load angle data
        angle = self.angle.get_data()
        self.Na_tot = len(angle)
        Angle = Data1D(
            name="angle", unit="rad", values=angle, normalizations=norm_angle
        )
        # Add angle (anti-)periodicity
        sym_a = dict()
        if is_antiper_a:
            sym_a["antiperiod"] = per_a
        else:
            sym_a["period"] = per_a
        Angle.symmetries = sym_a

    # Compute angle_rotor (added to time normalizations)
    self.parent.parent.comp_angle_rotor(Time)

    axes_dict = {"time": Time, "angle": Angle}

    return axes_dict
