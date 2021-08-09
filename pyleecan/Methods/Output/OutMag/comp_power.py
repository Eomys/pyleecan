from numpy import pi


def comp_power(self):
    """Compute the Ouput power

    Parameter
    --------
    self : OutMag
        An OutMag object
    """

    if (
        self.parent is not None
        and self.parent.elec is not None
        and self.parent.elec.N0 is not None
        and self.Tem_av is not None
    ):
        self.P = 2 * pi * self.parent.elec.N0 / 60 * self.Tem_av
    else:
        self.P = None
