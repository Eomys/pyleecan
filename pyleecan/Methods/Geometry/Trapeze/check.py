# -*-- coding: utf-8 -*


def check(self):
    """Check if the Trapeze object is correct

    Parameters
    ----------
    self : Trapeze
        a Trapeze Object


    Returns
    -------
    None

    Raises
    ------
    TrapezeError
        the W1 base of Trapeze must be greater than 0
    TrapezeError
        the W2 base of Trapeze must be greater than 0

    """
    if self.W1 <= 0:
        raise TrapezeError("the W1 base of Trapeze must be greater than 0")

    if self.W2 <= 0:
        raise TrapezeError("the W2 base of Trapeze must be greater than 0")


class TrapezeError(Exception):
    """ """

    pass
