def get_simu(self, index):
    """
    Generate a simulation according to index
    
    Parameters
    ----------
    index: int
        simulation index
    
    Returns
    -------
    simu : Simulation
        simulation generated
    """

    # Get reference simulation
    ref_simu = self.simu

    # Construct the simulation
    simu = ref_simu.copy()
    simu.var_simu = None

    # Run setters
    for paramexplorer in self.paramexplorer_list:
        paramexplorer.setter(simu, paramexplorer.value[index])

    return simu
