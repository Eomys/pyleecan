from ....Methods import ParentMissingError


def is_yoke(self):
    """Return if the Shape is for the Bore or Yoke radius

    Parameters
    ----------
    self : Bore
        A Bore object

    Returns
    -------
    is_yoke : bool
        True if the shape is on the yoke
    """

    if self.parent is not None:
        return self is self.parent.yoke
    else:
        raise ParentMissingError("Error: The Bore object is not inside a Lamination")
