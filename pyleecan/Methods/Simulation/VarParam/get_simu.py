def get_simu(self, *index):
    """
    Generate a simulation according to index
    
    Parameters
    ----------
    index: tuple
        simulation index
    
    Returns
    -------
    simu : Simulation
        simulation generated
    """

    if isinstance(index, int):
        index = (index,)

    assert len(index) == len(self.paramsetter_list), Exception(
        "Index must have {} dimensions".format(len(self.paramsetter_list))
    )

    # Get reference simulation
    ref_simu = self.parent

    # Construct the simulation
    simu = ref_simu.copy()
    simu.var_simu = None

    # Run setters
    for idx, param_setter in zip(index, self.paramsetter_list):
        param_setter.setter(simu, param_setter.value_list[idx])

    return simu
