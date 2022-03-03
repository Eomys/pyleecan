from numpy import sqrt, where


def solve(self, eec_param):
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
    eec_param: dict
        dictionnary containing EEC parameters

    Returns
    ----------
    out_dict: dict
        Output dict containing EEC values
    """

    Phi_m = eec_param["Phi_m"]
    I_m = eec_param["I_m"]

    # solving elementary system, initial start with unsaturated inductance
    i_start = where(I_m > 0)[0][0]
    eec_param["Lm"] = Phi_m[i_start] / I_m[i_start]
    eec_param, delta_Lm = self.solve_elementary(eec_param)
    if Phi_m.size > 1:
        # iteration until convergence is reached, and max number of iterations on EEC
        delta_Lm_max = 1e-6
        Nmax = 20
        niter_Lm = 1
        while abs(delta_Lm) > delta_Lm_max and niter_Lm < Nmax:
            eec_param, delta_Lm = self.solve_elementary(eec_param)
            niter_Lm = niter_Lm + 1

    out_dict = dict()

    # remove Phi_m and I_m
    del eec_param["Phi_m"]
    del eec_param["I_m"]

    out_dict["eec_param"] = eec_param
    out_dict["Ud"] = eec_param["U1"].real
    out_dict["Uq"] = eec_param["U1"].imag
    out_dict["Id"] = eec_param["I1"].real
    out_dict["Iq"] = eec_param["I1"].imag
    out_dict["Ir"] = eec_param["I2"] * eec_param["K21I"] * sqrt(2)

    return out_dict
