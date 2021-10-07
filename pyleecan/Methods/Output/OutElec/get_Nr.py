from numpy import ones


def get_Nr(self, Time=None):
    """Create speed in function of time vector Nr

    Parameters
    ----------
    self : OutElec
        An OutElec object
    Time : Data
        a time axis (SciDataTool Data object)

    Returns
    -------
    Nr: ndarray
        speed in function of time
    """

    if Time is None:
        if self.axes_dict is not None and "time" in self.axes_dict:
            Time = self.axes_dict["time"]
        else:
            raise Exception('You must define "time" property before calling get_Nr')

    if self.N0 is None:
        raise Exception('You must define "N0" before calling get_Nr')

    # Same speed for every timestep
    Nr = self.N0 * ones(Time.get_length(is_smallestperiod=True))

    return Nr
