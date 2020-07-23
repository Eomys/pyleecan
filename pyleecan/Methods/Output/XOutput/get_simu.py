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

    assert len(index) == len(self.shape), Exception(
        "Index must have {} dimensions".format(len(self.shape))
    )

    # Get reference simulation
    ref_simu = self.simu

    # Construct the simulation
    simu = ref_simu.copy()
    simu.var_simu = None

    # Run setters
    for paramexplorer in self.paramexplorer_list:
        paramexplorer.setter(simu, paramexplorer.value[index])

    return simu
