from numpy import pi
from SciDataTool import Data1D, DataLinspace, Norm_ref
from ....Methods.Simulation.Input import InputError


def comp_axes(
    self,
    axes_values,
    machine=None,
    N0=None,
    per_a=1,
    is_antiper_a=False,
    per_t=1,
    is_antiper_t=False,
):
    """Compute simulation axes, i.e. space DataObject including (anti)-periodicity
    and time DataObject including (anti)-periodicity and accounting for rotating speed
    and number of revolutions -> overrides Input comp_axes method

    Parameters
    ----------
    self : InputFlux
        an InputFlux object
    axes_values : {ndarray}
        dict of axe values
    machine : Machine
        a Machine object
    N0 : float
        rotating speed [rpm]
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
    axes_dict : {Data}
        dict of Data objects for each axis

    """

    norm_time = {}
    norm_angle = {}

    if machine is not None:
        # Get machine pole pair number
        p = machine.get_pole_pair_number()

        # Get electrical fundamental frequency
        f_elec = self.comp_felec()

        # Airgap radius
        Rag = machine.comp_Rgap_mec()

        # Setup normalizations for time and angle axes
        norm_time["elec_order"] = Norm_ref(ref=f_elec)
        norm_time["mech_order"] = Norm_ref(ref=f_elec / p)
        if N0 is not None:
            norm_time["angle_rotor"] = Norm_ref(ref=1 / (360 * N0 / 60))

        norm_angle["space_order"] = Norm_ref(ref=p)
        norm_angle["distance"] = Norm_ref(ref=1 / Rag)

    sym_t = {}
    if is_antiper_t:
        sym_t["antiperiod"] = per_t
    else:
        sym_t["period"] = per_t

    if self.time is not None:
        Time = Data1D(
            name="time",
            unit="s",
            values=self.time.get_data(),
            normalizations=norm_time,
            symmetries=sym_t,
        )
    elif "time" in axes_values:
        Time = Data1D(
            name="time",
            unit="s",
            values=axes_values["time"],
            normalizations=norm_time,
            symmetries=sym_t,
        )
    elif N0 is None:
        raise InputError("ERROR: time and N0 can't be both None")
    else:
        # Create time axis as a DataLinspace
        Time = DataLinspace(
            name="time",
            unit="s",
            initial=0,
            final=60 / N0 * self.Nrev,
            number=self.Nt_tot,
            include_endpoint=False,
            normalizations=norm_time,
            symmetries=sym_t,
        )

    sym_a = {}
    if is_antiper_a:
        sym_a["antiperiod"] = per_a
    else:
        sym_a["period"] = per_a

    if self.angle is not None:
        Angle = Data1D(
            name="angle",
            unit="rad",
            values=self.angle.get_data(),
            normalizations=norm_angle,
            symmetries=sym_a,
        )
    elif "angle" in axes_values:
        Angle = Data1D(
            name="angle",
            unit="rad",
            values=axes_values["angle"],
            normalizations=norm_angle,
            symmetries=sym_a,
        )
    else:
        # Create angle axis as a DataLinspace
        Angle = DataLinspace(
            name="angle",
            unit="rad",
            initial=0,
            final=2 * pi,
            number=self.Na_tot,
            include_endpoint=False,
            normalizations=norm_angle,
            symmetries=sym_a,
        )

    # Store in axes_dict
    axes_dict = {"Time": Time, "Angle": Angle}

    return axes_dict
