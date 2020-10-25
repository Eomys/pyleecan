from SciDataTool.Functions import AxisError


def get_axes(self, output, is_remove_apera=False, is_remove_apert=False):
    """
    Parameters
    ----------
    self : Force
        a Force object
    output: Output
        an Output object
    is_remove_apera: bool
        True to remove anti-periodicity from angular axis if any
    is_remove_apert: bool
        True to remove anti-periodicity from time axis if any

    Returns
    -------
    Time : Data
        a Data object such as Data1D or DataLinspace
    Angle : Data
        a Data object such as Data1D or DataLinspace

    """

    # Periodicity optimization
    (
        per_a,
        is_antiper_a,
        per_t,
        is_antiper_t,
    ) = self.parent.parent.get_machine_periodicity()

    # Getting the computation axes (with or without periodicity)
    if self.is_periodicity_a:
        try:
            # Reduce angle axis to the machine periodicity
            per_a = per_a * 2 if is_antiper_a else per_a
            Angle = output.mag.Angle.get_axis_periodic(
                per_a, is_antiper_a and not is_remove_apera
            )

        except AxisError:
            Angle = output.mag.Angle
            self.is_periodicity_a = False
            Na_tot = Angle.get_length(is_oneperiod=False)
            self.get_logger().warning(
                "WARNING: In Force model, Na_tot="
                + str(Na_tot)
                + " is not divisible by the machine angular periodicity ("
                + str(per_a)
                + "). Angular periodicity removed"
            )
    else:
        # Return full axis
        Angle = output.mag.Angle

    if self.is_periodicity_t:
        try:
            # Reduce time axis to the machine periodicity
            per_t = per_t * 2 if is_antiper_t else per_t
            Time = output.mag.Time.get_axis_periodic(
                per_t, is_antiper_t and not is_remove_apert
            )

        except AxisError:
            # Disable periodicity
            Time = output.mag.Time
            self.is_periodicity_t = False
            Nt_tot = Time.get_length(is_oneperiod=False)
            self.get_logger().warning(
                "WARNING: In Force model, Nt_tot="
                + str(Nt_tot)
                + " is not divisible by the machine time periodicity ("
                + str(per_t)
                + "). Time periodicity removed"
            )
    else:
        # Return full axis
        Time = output.mag.Time

    return Angle, Time
