from ....Classes.DataKeeper import DataKeeper


def get_mag_datakeeper(self, symbol_list):
    """
    Generate DataKeepers to store by default results from magnetic module

    Parameters
    ----------
    self: VarLoad
        A VarLoad object
    symbol_list : list
        List of the existing datakeeper (to avoid duplicate)

    Returns
    -------
    dk_list: list
        list of DataKeeper
    """
    dk_list = []
    error_nan = "lambda simu: np.nan"
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

    return dk_list
