def get_desc(self, simu=None, is_print=False):
    """Generate a string description of the ParamExplorer

    Parameters
    ----------
    self : ParamExplorer
        A ParamExplorer object
    simu : Simulation
        Optional simulation object to add reference value
    is_print : bool
        True to call print on desc

    Returns
    -------
    desc: str
        Description (for instance "W0: N values from 0.001 to 0.01 (ref=0.0015) [m]")
    """

    desc = ""
    desc += self.symbol + ": "
    N = self.get_N()
    desc += str(N) + " value"
    if N > 1:
        desc += "s"

    min_value = self.get_min()
    max_value = self.get_max()
    if min_value is not None and max_value is not None and N > 1:
        desc += " from " + format(min_value, ".4g") + " to " + format(max_value, ".4g")
    if self.getter is not None and simu is not None:
        ref = self.getter(simu)
        desc += " (ref=" + format(ref, ".4g") + ")"
    if self.unit is not None:
        desc += " [" + self.unit + "]"

    if is_print:
        print(desc)
    return desc
