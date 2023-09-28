def comp_axes(self, output):
    """Compute the axes required in any Magnetics module

    Parameters
    ----------
    self : Magnetic
        a Magnetic object
    output : Output
        an Output object (to update)

    Returns
    -------
    axes_dict: {Data}
        Dict containing Time and Angle axes including (anti-)periodicties used in any Magnetics module

    """

    # Get geometry output
    outgeo = output.geo

    # Get axis dict from OutGeo
    axes_dict_geo = outgeo.axes_dict

    # Add periodicities to time and angle axes
    axes_dict = output.simu.input.comp_axes(
        axes_list=["time", "angle"],
        axes_dict_in=axes_dict_geo,
        is_periodicity_a=self.is_periodicity_a,
        is_periodicity_t=self.is_periodicity_t,
        is_periodicity_rotor=self.is_periodicity_rotor,
    )

    # Check Time periodicities regarding Magnetics model input
    per_t0, is_antiper_t0 = axes_dict["time"].get_periodicity()
    is_periodicity_t0 = per_t0 > 1 or is_antiper_t0
    if not is_periodicity_t0 and self.is_periodicity_t:
        # Remove time periodicity in Magnetic model
        self.is_periodicity_t = False
        if outgeo.per_t_S != 1:
            Nt_tot = axes_dict["time"].get_length(is_oneperiod=False)
            self.get_logger().warning(
                "In Magnetic model, Nt_tot="
                + str(Nt_tot)
                + " is not divisible by the machine time periodicity ("
                + str(outgeo.per_t_S)
                + "). Time periodicity removed"
            )

    # Check Angle periodicities regarding Magnetics model input
    per_a0, is_antiper_a0 = axes_dict["angle"].get_periodicity()
    is_periodicity_a0 = per_a0 > 1 or is_antiper_a0
    if not is_periodicity_a0 and self.is_periodicity_a:
        # Remove time periodicity in Magnetic model
        self.is_periodicity_a = False
        if outgeo.per_a != 1:
            Na_tot = axes_dict["angle"].get_length(is_oneperiod=False)
            self.get_logger().warning(
                "In Magnetic model, Na_tot="
                + str(Na_tot)
                + " is not divisible by the machine angular periodicity ("
                + str(outgeo.per_a)
                + "). Angular periodicity removed"
            )

    # Compute slice axis
    Slice = self.Slice_enforced.get_data()

    # Add slice axis
    axes_dict["z"] = Slice

    # Add Time axis on which to calculate torque
    # Copy from standard Time axis
    Time_Tem = axes_dict["time"].copy()

    # Remove anti-periodicity if any
    if "antiperiod" in Time_Tem.symmetries:
        Time_Tem.symmetries["period"] = Time_Tem.symmetries.pop("antiperiod")

    # Store in axis dict
    axes_dict["time_Tem"] = Time_Tem

    return axes_dict
