def get_min(self):
    """Return the minimum value of the ParamExplorer

    Parameters
    ----------
    self : ParamExplorerInterval
        A ParamExplorerInterval object

    Returns
    -------
    min_value: float
        Minimum value of the ParamExplorer
    """

    if self.type_value == 0:  # float
        return self.min_value
    else:
        return int(self.min_value)
