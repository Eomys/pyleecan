from ....Classes.VarLoad import VarLoad


def get_var_load(self):
    """Return the VarLoad object from var_simu or var_simu.var_simu

    Parameters
    ----------
    self : Simulation
        A Simulation object
    """

    if self.var_simu is None:
        return None
    if isinstance(self.var_simu, VarLoad):
        return self.var_simu
    if isinstance(self.var_simu.var_simu, VarLoad):
        return self.var_simu.var_simu
    return None
