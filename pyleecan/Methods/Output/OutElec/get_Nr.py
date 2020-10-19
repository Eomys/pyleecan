from numpy import ones
from ....Classes.ImportMatrixVal import ImportMatrixVal


class OutElecError(Exception):
    pass


def get_Nr(self):
    """Create speed in function of time vector Nr

    Parameters
    ----------
    self : OutElec
        An OutElec object

    Returns
    -------
    Nr: ndarray
        speed in function of time
    """
    if self.time is None:
        raise OutElecError('You must define "time" property before calling get_Nr')
    if self.N0 is None:
        raise OutElecError('You must define "N0" before calling get_Nr.')

    # Same speed for every timestep
    Nr = self.N0 * ones(self.time.get_length(is_oneperiod=False))
    return Nr
