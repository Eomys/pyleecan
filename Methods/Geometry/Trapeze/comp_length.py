# -*-- coding: utf-8 -*
def comp_length(self):
    """Returns the length of the Trapeze

    Parameters
    ----------
    self : Trapeze
        a Trapeze object


    Returns
    -------
    length: float
        Length of the surface [m]

    """
    # check if the Trapeze is correct
    self.check()
    lines = self.get_lines()
    length = 0
    for line in lines:
        length += line.comp_length()
    return length
