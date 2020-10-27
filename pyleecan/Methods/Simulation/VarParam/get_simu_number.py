def get_simu_number(self):
    """Return the number of simulation defined by the Param Explorer

    Parameters
    ----------
    self : VarParam
        A VarParam object

    Returns
    -------
    nb_simu : int
        number of simulation
    """

    nb_simu = 1
    for paramexplorer in self.paramexplorer_list:
        nb_simu *= len(paramexplorer.value)

    return nb_simu
