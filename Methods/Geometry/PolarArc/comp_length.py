# -*-- coding: utf-8 -*
def comp_length(self):
    """Returns the length of the PolarArc

    Parameters
    ----------
    self : PolarArc
        a PolarArc object


    Returns
    -------
    length : float
        length of the PolarArc [m]
    """
    # check if the PolarArc is correct
    self.check()

    lines = self.get_lines()
    length = 0
    for line in lines:
        length += line.comp_length()
    return length
