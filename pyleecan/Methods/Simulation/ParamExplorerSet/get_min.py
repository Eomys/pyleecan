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

    if len(self.value) > 0 and isinstance(self.value[0], (int, float)):
        return min(self.value)
    else:
        return None
