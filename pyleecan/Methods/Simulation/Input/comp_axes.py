def comp_axes(
    self,
    axes_list,
    machine=None,
    axes_dict_in=None,
    is_periodicity_a=None,
    is_periodicity_t=None,
    per_a=None,
    is_antiper_a=None,
    per_t=None,
    is_antiper_t=None,
    is_periodicity_rotor=False,
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
    is_periodicity_rotor: bool
        True to consider rotor periodicity over time instead of stator

    Returns
    -------
    axes_dict: {Data}
        dict of axes containing requested axes

    """
    if len(axes_list) == 0:
        raise Exception("axes_list should not be empty")

    if self.parent is not None:
        simu = self.parent
    else:
        simu = None

    if hasattr(simu, "parent") and simu.parent is not None:
        output = simu.parent
    else:
        output = None

    if (axes_list is None or len(axes_list) == 0) and (
        axes_dict_in is None or len(axes_dict_in) == 0
    ):
        raise Exception(
            "Cannot calculate axes if both axes list and axes dict are None"
        )

    if machine is None:
        # Fetch machine from input
        if hasattr(simu, "machine") and simu.machine is not None:
            machine = simu.machine
        else:
            raise Exception("Cannot calculate axes if simu.machine is None")

    # Get machine pole pair number
    p = machine.get_pole_pair_number()

    # Fill periodicity parameters that are None
    if (is_periodicity_a is not False or is_periodicity_t is not False) and (
        per_a is None or is_antiper_a is None or per_t is None or is_antiper_t is None
    ):
        if output is not None:
            # Get time and space (anti-)periodicities from the output
            (
                per_a_0,
                is_antiper_a_0,
                per_t_0,
                is_antiper_t_0,
            ) = output.get_machine_periodicity(is_rotor_ref=is_periodicity_rotor)
        else:
            # Compute time and space (anti-)periodicities from the machine
            per_a_0, is_antiper_a_0 = machine.comp_periodicity_spatial()
            if is_periodicity_rotor:
                _, _, per_t_0, is_antiper_t_0 = machine.comp_periodicity_time()
            else:
                per_t_0, is_antiper_t_0, _, _ = machine.comp_periodicity_time()

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

    # Init axes_dict
    axes_dict = dict()

    # Get time axis
    if "time" in axes_list:
        # Check if Time is already in input dict of axes
        if axes_dict_in is not None and "time" in axes_dict_in:
            Time_in = axes_dict_in["time"]
        else:
            Time_in = None

        # Calculate time axis
        Time = self.comp_axis_time(p, per_t, is_antiper_t, Time_in)

        # Store time axis in dict
        axes_dict["time"] = Time

    # Get angle axis
    if "angle" in axes_list:
        # Airgap radius
        try:
            Rag = machine.comp_Rgap_mec()
        except (
            Exception
        ):  # Case where rotor is not defined yet (Rag is only used for angle axis normalization)
            Rag = 1

        # Check if Angle is already in input dict of axes
        if axes_dict_in is not None and "angle" in axes_dict_in:
            Angle_in = axes_dict_in["angle"]
        else:
            Angle_in = None

        # Calculate angle axis
        Angle = self.comp_axis_angle(p, Rag, per_a, is_antiper_a, Angle_in)

        # Store angle axis in dict
        axes_dict["angle"] = Angle

    if "phase_S" in axes_list:
        # Check if Phase is already in input dict of axes
        stator_label = "phase_" + machine.stator.get_label()
        if axes_dict_in is not None and stator_label in axes_dict_in:
            Phase_in = axes_dict_in[stator_label]
        else:
            Phase_in = None

        # Calculate stator phase axis
        Phase = self.comp_axis_phase(machine.stator, Phase_in)

        if Phase is not None:
            # Store phase axis in dict
            axes_dict[stator_label] = Phase

    if "phase_R" in axes_list:
        # Check if Phase is already in input dict of axes
        rotor_label = "phase_" + machine.rotor.get_label()
        if axes_dict_in is not None and rotor_label in axes_dict_in:
            Phase_in = axes_dict_in[rotor_label]
        else:
            Phase_in = None

        # Calculate rotor phase axis
        Phase = self.comp_axis_phase(machine.rotor, per_a, is_antiper_a, Phase_in)

        if Phase is not None:
            # Store phase axis in dict
            axes_dict[rotor_label] = Phase

    return axes_dict
