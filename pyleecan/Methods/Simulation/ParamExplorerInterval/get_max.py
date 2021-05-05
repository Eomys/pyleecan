def get_max(self):
    """Return the maximum value of the ParamExplorer

    Parameters
    ----------
    self : ParamExplorerInterval
        A ParamExplorerInterval object

    Returns
    -------
    max_value: float
        Maximum value of the ParamExplorer
    """

    if self.type_value == 0:  # float
        return self.max_value
    else:
        return int(self.max_value)
