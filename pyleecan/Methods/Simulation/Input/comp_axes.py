from numpy import pi

from SciDataTool import Data1D, DataLinspace, Norm_ref

from ....Methods.Simulation.Input import InputError

from ....Functions.Winding.gen_phase_list import gen_name


def comp_axes(
    self,
    axes_list,
    machine=None,
    axes_dict=None,
    is_periodicity_a=None,
    is_periodicity_t=None,
    per_a=None,
    is_antiper_a=None,
    per_t=None,
    is_antiper_t=None,
):
    """Compute simulation axes such as time / angle / phase axes, with or without periodicities
    and including normalizations

    Parameters
    ----------
    self : Input
        an Input object
    machine : Machine
        a Machine object
    axes_list: list
        List of axes name to return in axes dict
    axes_dict: {Data}
        dict of axes containing time and angle axes (with or without (anti-)periodicity)
    is_periodicity_a: bool
        True if spatial periodicity is requested
    is_periodicity_t: bool
        True if time periodicity is requested
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
        dict of axes containing requested axes

    """

    if self.parent is not None:
        simu = self.parent
    else:
        raise Exception("Cannot calculate axes if parent simu is None")

    if hasattr(self.parent, "parent") and self.parent.parent is not None:
        output = simu.parent
    else:
        raise Exception("Cannot calculate axes if parent output is None")

    if (axes_list is None or len(axes_list) == 0) and (
        axes_dict is None or len(axes_dict) == 0
    ):
        raise Exception(
            "Cannot calculate axes if both axes list and axes dict are None"
        )

    if len(axes_list) == 0:
        raise Exception("axes_list should not be empty")

    if axes_dict is not None:
        # Get list of axes name from dict of axes
        axes_dict_list = list(axes_dict.keys())
        for ax in axes_list:
            if ax not in axes_dict_list:
                raise Exception("Axis " + ax + " is requested but is not in axes_dict")

    if axes_dict is None or len(axes_dict) == 0:
        # Init axes_dict
        axes_dict = dict()

    if machine is None:
        # Fetch machine from input
        if hasattr(simu, "machine") and simu.machine is not None:
            machine = simu.machine
        else:
            raise Exception("Cannot calculate axes if simu.machine is None")

    # Get machine pole pair number
    p = machine.get_pole_pair_number()

    # Fill periodicity parameters that are None
    if per_a is None or is_antiper_a is None or per_t is None or is_antiper_t is None:
        # Get time and space (anti-)periodicities of the machine
        (
            per_a_0,
            is_antiper_a_0,
            per_t_0,
            is_antiper_t_0,
        ) = output.get_machine_periodicity()

    if "time" in axes_list:

        if is_periodicity_t is None or is_periodicity_t:
            # Enforce None values to machine time periodicity
            per_t = per_t_0 if per_t is None else per_t
            is_antiper_t = is_antiper_t_0 if is_antiper_t is None else is_antiper_t
            if is_periodicity_t is None:
                # Check time periodicity is included
                is_periodicity_t = per_t > 1 or is_antiper_t
        elif not is_periodicity_t:
            # Remove time periodicity
            per_t = 1
            is_antiper_t = False

        # Get electrical fundamental frequency
        f_elec = self.comp_felec()

        # Setup normalizations for time and angle axes
        norm_time = {
            "elec_order": Norm_ref(ref=f_elec),
            "mech_order": Norm_ref(ref=f_elec / p),
        }

        if "time" in axes_dict:
            # Compute Time axis based on the one stored in OutElec
            Time = axes_dict["time"].get_axis_periodic(Nper=per_t, is_aper=is_antiper_t)
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
            self.Nt_tot = len(time)
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

        # Store time axis in dict
        axes_dict["time"] = Time

    if "angle" in axes_list:

        if is_periodicity_a is None or is_periodicity_a:
            # Enforce None values to machine periodicity
            per_a = per_a_0 if per_a is None else per_a
            is_antiper_a = is_antiper_a_0 if is_antiper_a is None else is_antiper_a
            if is_periodicity_a is None:
                # Enforce requested angle periodicity
                is_periodicity_a = per_a > 1 or is_antiper_a
        elif not is_periodicity_a:
            # Remove angle periodicity
            per_a = 1
            is_antiper_a = False

        # Airgap radius
        Rag = machine.comp_Rgap_mec()

        norm_angle = {"space_order": Norm_ref(ref=p), "distance": Norm_ref(ref=1 / Rag)}

        if "angle" in axes_dict:
            # Compute Angle axis based on the one stored in OutElec
            Angle = axes_dict["angle"].get_axis_periodic(
                Nper=per_a, is_aper=is_antiper_a
            )

        # Create angle axis
        elif self.angle is None:

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
            Angle = Angle.to_linspace()

        # Store angle axis in dict
        axes_dict["angle"] = Angle

    if "phase" in axes_list:

        qs = machine.stator.winding.qs

        # Creating the data object
        Phase = Data1D(
            name="phase",
            unit="",
            values=gen_name(qs),
            is_components=True,
        )

        # Store phase axis in dict
        axes_dict["phase"] = Phase

    return axes_dict
