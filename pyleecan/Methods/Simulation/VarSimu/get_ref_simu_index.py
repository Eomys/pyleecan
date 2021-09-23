class VarSimuError(Exception):
    pass


def get_ref_simu_index(self, ref_simu, simu_dict):
    """Get the index of the reference simulation (None if must be computed)

    Parameters
    ----------
    self : VarSimu
        A VarSimu object
    ref_simu : Simulation
        A Simulation object (reference simulation)
    simu_dict : dict
        Dict of simulations

    Returns
    -------
    ref_simu_index : int
        index of the reference simulation (None if must be computed)
    """
    ref_simu_index = None
    for ii, simu in enumerate(simu_dict["simulation_list"]):
        diff_list = simu.compare(ref_simu, name="simu")
        # Remove not meaningfull differences
        if "simu.mag.file_name" in diff_list:
            diff_list.remove("simu.mag.file_name")
        if len(diff_list) == 0:
            ref_simu_index = ii
            break

    return ref_simu_index
