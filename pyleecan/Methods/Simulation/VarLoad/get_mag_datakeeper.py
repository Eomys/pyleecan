from ....Classes.DataKeeper import DataKeeper
from math import nan


def get_mag_datakeeper(self):
    """
    Generate DataKeepers to store by default results from magnetic module

    Parameters
    ----------
    self: VarLoadFlux object

    Returns
    -------
    dk_list: list
        list of DataKeeper
    """
    error_nan = lambda simu: nan
    # Average torque Datakeeper
    T_d = DataKeeper(
        name="Average Torque",
        symbol="Tem_av",
        unit="N.m",
        keeper=lambda out: out.mag.Tem_av,
        error_keeper=error_nan,
    )
    # Peak to Peak Torque ripple
    Tpp_d = DataKeeper(
        name="Peak to Peak Torque ripple",
        symbol="Tem_rip_pp",
        unit="N.m",
        keeper=lambda out: out.mag.Tem_rip_pp,
        error_keeper=error_nan,
    )
    # Peak to Peak Torque ripple normalized
    Tppn_d = DataKeeper(
        name="Peak to Peak Torque ripple normalized",
        symbol="Tem_rip_norm",
        unit="N.m",
        keeper=lambda out: out.mag.Tem_rip_norm,
        error_keeper=error_nan,
    )

    return [T_d, Tpp_d, Tppn_d]
