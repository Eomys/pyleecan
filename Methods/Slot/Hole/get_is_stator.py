
from pyleecan.Methods import ParentMissingError


def get_is_stator(self):
    """Return True if the parent lamination is stator and False if is a rotor

    Parameters
    ----------
    self : Hole
        A Hole object

    Returns
    -------
    is_stator: bool
        True if the Lamination is a stator and False if not
    """

    if self.parent is not None:
        return self.parent.is_stator
    else:
        raise ParentMissingError("Error: The hole is not inside a Lamination")
