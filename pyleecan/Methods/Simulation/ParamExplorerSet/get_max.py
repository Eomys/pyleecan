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

    if len(self.value) > 0 and isinstance(self.value[0], (int, float)):
        return max(self.value)
    else:
        return None
