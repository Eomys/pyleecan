from numpy import sqrt, where


def solve(self):
    """Solve the equivalent electrical circuit of SCIM

                  --->                     ---->
     -----Rs------XsIs---- --- -----Rr'----XrIr----
    |                     |   |                       |
    |                     Rfe Xm                      Rr*(s-1)/s
    |                     |   |                       |
     ---------Is---------- --- ---------Ir------------

             --->
              Us

    Parameters
    ----------
    self : EEC_SCIM
        an EEC_SCIM object

    Returns
    ----------
    out_dict: dict
        Output dict containing EEC values
    """

    Lm_table = self.Lm_table
    Im_table = self.Im_table

    # solving elementary system, initial start with unsaturated inductance
    i_start = where(Im_table > 0)[0][0]
    self.Lm = Lm_table[i_start]
    delta_Lm = self.solve_elementary()
    if Lm_table.size > 1:
        # iteration until convergence is reached, and max number of iterations on EEC
        delta_Lm_max = 1e-6
        Nmax = 20
        niter_Lm = 1
        while abs(delta_Lm) > delta_Lm_max and niter_Lm < Nmax:
            delta_Lm = self.solve_elementary()
            niter_Lm = niter_Lm + 1

    out_dict = dict()

    # remove Lm and Im (still in simulation.elec.eec)
    self.Lm_table = None
    self.Im_table = None

    out_dict["Ud"] = self.U1.real
    out_dict["Uq"] = self.U1.imag
    out_dict["Id"] = self.I1.real
    out_dict["Iq"] = self.I1.imag
    out_dict["Ir"] = self.I2 * self.K21I * sqrt(2)

    return out_dict
