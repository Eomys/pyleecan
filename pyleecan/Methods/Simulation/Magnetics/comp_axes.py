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
            per_t_S = outgeo.per_t_S
            if outgeo.is_antiper_t_S:
                per_t_S *= 2
            self.get_logger().warning(
                "In Magnetic model, Nt_tot="
                + str(Nt_tot)
                + " is not divisible by the machine time periodicity ("
                + str(per_t_S)
                + "). Time periodicity removed"
            )

    # Change Time periodicity in case meshsolution is requested
    # and rotor time periodicity is not the same as stator time periodicity
    if self.is_get_meshsolution:

        Time = axes_dict["time"]

        # Adjust time periodicity if it is requested but stator and rotor time periodicities don't match
        if self.is_periodicity_t:

            Time_S = Time.copy()  # Time axis in stator frame
            Time_R = Time.copy()  # Time axis in rotor frame
            # Get time periodicity in stator and rotor frames
            pert_S, is_apert_S, pert_R, _ = output.simu.machine.comp_periodicity_time()

            # If there is the same time periodicity for stator and rotor, anti-periodicity in stator frame and anti-periodicity in Time axis
            if pert_S == pert_R and is_apert_S and "antiperiod" in Time.symmetries:
                # Anti-periodicity in stator frame become periodicity in rotor frame (there is no anti-periodicity in rotor frame)
                Time_R.symmetries = {"period": Time.symmetries["antiperiod"]}
            else:
                # Change stator to rotor periodicity
                Time_R = Time_S.get_axis_periodic(Nper=pert_R, is_aper=False)
                Time = Time_R.copy()
                self.get_logger().debug(
                    f"""In {self.__class__.__name__ }, calculating magnetic mesh quantities in stator and rotor frames (is_get_meshsolution=True) : 
            setting time periodicity from stator frame (period={pert_S}, is_antiper={str(is_apert_S)}) to rotor frame (period={pert_R}, is_antiper=False)"""
                )

            # Store time axes for both stator and rotor frame
            axes_dict["time"] = Time
            axes_dict["time_S"] = Time_S
            axes_dict["time_R"] = Time_R

    # Check Angle periodicities regarding Magnetics model input
    per_a0, is_antiper_a0 = axes_dict["angle"].get_periodicity()
    is_periodicity_a0 = per_a0 > 1 or is_antiper_a0
    if not is_periodicity_a0 and self.is_periodicity_a:
        # Remove time periodicity in Magnetic model
        self.is_periodicity_a = False
        if outgeo.per_a != 1:
            Na_tot = axes_dict["angle"].get_length(is_oneperiod=False)
            per_a = outgeo.per_a
            if outgeo.is_antiper_a:
                per_a *= 2
            self.get_logger().warning(
                "In Magnetic model, Na_tot="
                + str(Na_tot)
                + " is not divisible by the machine angular periodicity ("
                + str(per_a)
                + "). Angular periodicity removed"
            )

    # Compute slice axis
    Slice = self.Slice_enforced.get_data()

    # Add slice axis
    axes_dict["z"] = Slice

    # Add Time axis on which to calculate torque
    if self.is_get_meshsolution and self.is_periodicity_t:
        # Copy from stator referential Time axis
        Time_Tem = axes_dict["time_S"].copy()
    else:
        # Copy from standard Time axis
        Time_Tem = axes_dict["time"].copy()

    # Remove anti-periodicity if any
    if "antiperiod" in Time_Tem.symmetries:
        Time_Tem.symmetries["period"] = Time_Tem.symmetries.pop("antiperiod")

    # Store in axis dict
    axes_dict["time_Tem"] = Time_Tem

    return axes_dict
