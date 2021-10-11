def comp_axes(self, output):
    """Compute the axes required in any Force module

    Parameters
    ----------
    self : Force
        a Force object
    output : Output
        an Output object (to update)

    Returns
    -------
    axes_dict: {Data}
        Dict containing Time and Angle axes including (anti-)periodicties used in any Force module
    """

    # Get geometry output
    outgeo = output.geo

    # Get axis dict from OutMag
    axes_dict_mag = output.mag.axes_dict

    # Add periodicities to time and angle axes
    axes_dict = output.simu.input.comp_axes(
        axes_list=["time", "angle"],
        axes_dict_in=axes_dict_mag,
        is_periodicity_a=self.is_periodicity_a,
        is_periodicity_t=self.is_periodicity_t,
    )

    # Remove time anti-periodicity if any
    if "antiperiod" in axes_dict["time"].symmetries:
        axes_dict["time"].symmetries["period"] = axes_dict["time"].symmetries.pop(
            "antiperiod"
        )

    # Check Time periodicities regarding Force model input
    per_t0, is_antiper_t0 = axes_dict["time"].get_periodicity()
    is_periodicity_t0 = per_t0 > 1 or is_antiper_t0
    is_periodic_machine_t = outgeo.per_t_S > 1 or outgeo.is_antiper_t_S
    if is_periodicity_t0 != self.is_periodicity_t and is_periodic_machine_t:
        # Remove time periodicity in Force model
        self.is_periodicity_t = False
        Nt_tot = axes_dict["time"].get_length(is_oneperiod=False)
        self.get_logger().warning(
            "In Force model, Nt_tot="
            + str(Nt_tot)
            + " is not divisible by the machine time periodicity ("
            + str(outgeo.per_t_S)
            + "). Time periodicity removed"
        )

    # Remove angular anti-periodicity if any
    if "antiperiod" in axes_dict["angle"].symmetries:
        axes_dict["angle"].symmetries["period"] = axes_dict["angle"].symmetries.pop(
            "antiperiod"
        )

    # Check Angle periodicities regarding Force model input
    per_a0, is_antiper_a0 = axes_dict["angle"].get_periodicity()
    is_periodicity_a0 = per_a0 > 1 or is_antiper_a0
    is_periodic_machine_a = outgeo.per_a > 1 or outgeo.is_antiper_a
    if is_periodicity_a0 != self.is_periodicity_a and is_periodic_machine_a:
        # Remove time periodicity in Magnetic model
        self.is_periodicity_a = False
        Na_tot = axes_dict["angle"].get_length(is_oneperiod=False)
        self.get_logger().warning(
            "In Force model, Na_tot="
            + str(Na_tot)
            + " is not divisible by the machine angular periodicity ("
            + str(outgeo.per_a)
            + "). Angular periodicity removed"
        )

    return axes_dict
