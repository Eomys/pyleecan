from SciDataTool.Functions import AxisError


def create_from_axis(axis_in, per, is_aper, is_include_per, is_remove_aper=False):
    """
    Create axis input axis accounting for (anti-)periodicity changes imposed
    by physics and model inputs

    Parameters
    ----------
    axis_in : Data
        The input axis coming from previous output (a Data object such as Data1D or DataLinspace)
    per: int
        machine periodicity along current axis
    is_aper: bool
        True if the machine is anti-periodic along current axis
    is_include_per: bool
        True if the model requires to include periodicity
    is_remove_aper: bool
        True if the model requires to remove anti-periodicity

    Returns
    -------
    axis_out : Data
        The output axis (a Data object such as Data1D or DataLinspace)
    is_include_per : bool
        Returns is_include_per in case periodicity is activated in the model but cannot be applied

    """

    # Getting the computation axes (with or without periodicity)
    if is_include_per:
        try:
            # Reduce axis to the machine periodicity
            per = per * 2 if is_aper else per
            axis_out = axis_in.get_axis_periodic(per, is_aper and not is_remove_aper)

        except AxisError:
            # Periodicity cannot be applied, return full axis
            axis_out = axis_in.copy()
            is_include_per = False

    else:
        # Return full axis
        axis_out = axis_in.copy()

    return axis_out, is_include_per
