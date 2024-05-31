from numpy import pi


def comp_inductance(self):
    """Compute the end winding inductance based on permeance coefficient stored in EndWindingRect object
    from "Design of Rotating Electrical Machines", J. Pyrhonen, second edition

    Parameters
    ----------
    self: EndWindingRect
        A EndWindingRect object

    Returns
    -------
    Lew : float
        end winding inductance [H].
    """

    if self.parent is not None:
        winding = self.parent
    else:
        return 0

    p = winding.p
    Ntcoil = winding.Ntcoil

    mu0 = 4 * pi * 1e-7

    if winding.Lewout is not None:
        l_ew = winding.Lewout
    else:
        l_ew = 0

    # Calculate width of end winding
    w_ew = 2 * self.comp_length()

    # Calculate Eq(4.100)
    l_lambda = 2 * l_ew * self.lambda_length + w_ew * self.lambda_width

    # Calculate end-winding inductance from Eq (4.98) p.261
    Lw = 2 / p * Ntcoil**2 * mu0 * l_lambda

    return Lw
