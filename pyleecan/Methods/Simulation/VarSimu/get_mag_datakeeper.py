from ....Classes.DataKeeper import DataKeeper


def get_mag_datakeeper(self, symbol_list, is_multi=False):
    """
    Generate DataKeepers to store by default results from magnetic module

    Parameters
    ----------
    self: VarLoad
        A VarLoad object
    symbol_list : list
        List of the existing datakeeper (to avoid duplicate)
    is_multi : bool
        True for multi-simulation of multi-simulation

    Returns
    -------
    dk_list: list
        list of DataKeeper
    """
    dk_list = []
    error_nan = "lambda simu: np.nan"
    if is_multi:
        # Max Average torque Datakeeper
        if "Max_Tem_av" not in symbol_list:
            dk_list.append(
                DataKeeper(
                    name="Max Average Torque",
                    symbol="Max_Tem_av",
                    unit="N.m",
                    keeper="lambda output: max(output.xoutput_dict['Tem_av'].result)",
                    error_keeper=error_nan,
                )
            )
        # Max Peak to Peak Torque ripple
        if "Max_Tem_rip_pp" not in symbol_list:
            dk_list.append(
                DataKeeper(
                    name="Max Peak to Peak Torque ripple",
                    symbol="Max_Tem_rip_pp",
                    unit="N.m",
                    keeper="lambda output: max(output.xoutput_dict['Tem_rip_pp'].result)",
                    error_keeper=error_nan,
                )
            )
        # Max Peak to Peak Torque ripple normalized
        if "Max_Tem_rip_norm" not in symbol_list:
            dk_list.append(
                DataKeeper(
                    name="Max Peak to Peak Torque ripple normalized",
                    symbol="Max_Tem_rip_norm",
                    unit="-",
                    keeper="lambda output: max(output.xoutput_dict['Tem_rip_norm'].result)",
                    error_keeper=error_nan,
                )
            )
    else:
        # Average torque Datakeeper
        if "Tem_av" not in symbol_list:
            dk_list.append(
                DataKeeper(
                    name="Average Torque",
                    symbol="Tem_av",
                    unit="N.m",
                    keeper="lambda out: out.mag.Tem_av",
                    error_keeper=error_nan,
                )
            )
        # Peak to Peak Torque ripple
        if "Tem_rip_pp" not in symbol_list:
            dk_list.append(
                DataKeeper(
                    name="Peak to Peak Torque ripple",
                    symbol="Tem_rip_pp",
                    unit="N.m",
                    keeper="lambda out: out.mag.Tem_rip_pp",
                    error_keeper=error_nan,
                )
            )
        # Peak to Peak Torque ripple normalized
        if "Tem_rip_norm" not in symbol_list:
            dk_list.append(
                DataKeeper(
                    name="Peak to Peak Torque ripple normalized",
                    symbol="Tem_rip_norm",
                    unit="-",
                    keeper="lambda out: out.mag.Tem_rip_norm",
                    error_keeper=error_nan,
                )
            )
        # Output Power Datakeeper
        if "P" not in symbol_list:
            dk_list.append(
                DataKeeper(
                    name="Output Power",
                    symbol="P",
                    unit="W",
                    keeper="lambda out: out.mag.P",
                    error_keeper=error_nan,
                )
            )
    return dk_list
