from SciDataTool import Data1D


def comp_axes(self, output):
    """Compute the axes required in Loss module

    Parameters
    ----------
    self : LossFEA
        a LossFEA object
    output : Output
        an Output object (to update)

    Returns
    -------
    axes_dict: {Data}
        Dict containing Time (including (anti-)periodicties) and Indices axes used in any Loss module
    is_mirror : bool
        True to mirror magnetic mesh quantities calculate in stator and rotor frames to get the same Time axis
    """

    # Load axes dict from Outmag
    axes_dict_mag = output.mag.axes_dict

    # Load Time axes depending on stator and rotor periodicities
    # Check if Magnetic mesh data is calculated in rotor and stator frames with different time periodicities
    if "time_S" in axes_dict_mag and "time_R" in axes_dict_mag:

        Time_S = axes_dict_mag["time_S"].copy()
        Time_R = axes_dict_mag["time_R"].copy()

        if "antiperiod" in Time_S.symmetries:
            # There is no anti-periodicity for losses calculation since there is a constant value
            Time_S.symmetries = {"period": Time_S.symmetries["antiperiod"]}

        assert "antiperiod" not in Time_R.symmetries

        # Compare time period length between stator frame and rotor frame
        time_val_S = Time_S.get_values(is_oneperiod=True)
        time_val_R = Time_R.get_values(is_oneperiod=True)

        if time_val_S[-1] == time_val_R[-1]:
            # Same period value for both stator and rotor frames, no need to mirror any loss values
            is_mirror = False
            Time = Time_S  # Time_S and Time_R are the same
        elif time_val_S[-1] > time_val_R[-1]:
            # Stator period is longer, rotor loss values has to mirrored
            if "period" in Time_S.symmetries:
                per_t = int(Time_S.symmetries["period"])
            else:
                per_t = 1
            Time = Time_S.get_axis_periodic(Nper=per_t, is_aper=False)
            is_mirror = True
        else:
            # Rotor period is longer, stator loss values has to mirrored
            if "period" in Time_R.symmetries:
                per_t = int(Time_R.symmetries["period"])
            else:
                per_t = 1
            Time = Time_R.get_axis_periodic(Nper=per_t, is_aper=False)
            is_mirror = True

    else:
        # Same time periodicity for both stator and rotor frames
        Time = axes_dict_mag["time"].copy()
        is_mirror = False

    # Store time axes in axes_dict for time calculation
    axes_dict = {"time": Time}

    # Store frequency axis in axes_dict for frequency calculation (only average loss value is calculated by frequency model)
    axes_dict["freqs"] = Data1D(
        name="freqs", unit="Hz", values=[0.0], normalizations=Time.normalizations.copy()
    )

    # Add element indices axis for mesh calculation and plotting
    axes_dict["indice_element"] = axes_dict_mag["indice_element"].copy()

    return axes_dict, is_mirror
