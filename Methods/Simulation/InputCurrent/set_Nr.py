from numpy import ones
from ....Classes.ImportMatrixVal import ImportMatrixVal


def set_Nr(self, value):
    """Set Nr with a constant value

    Parameters
    ----------
    self : InputCurrent
        An InputCurrent object
    value: float
        Nr value to enforce
    """

    if self.time is None:
        raise Exception('You must define "time" property before calling set_Nr')

    self.Nr = ImportMatrixVal()
    self.Nr.value = value * ones(self.time.get_data().size)
