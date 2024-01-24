from numpy import pi, log

from ..Subdomain.comp_polynoms import E, P


def comp_current_solution(self, r):
    """Method description

    Parameters
    ----------
    self: Subdomain_Slot
        a Subdomain_Slot object
    r : float/ndarray
        Radius at which solution is calculated

    Returns
    ----------
    var: type
        var description
    """

    mu0 = 4 * pi * 1e-7
    Ry = self.Ryoke

    # constant particular function
    X_r = mu0 * (-(r ** 2) / 2 + Ry ** 2 * log(r)) / 2
    # derivative of the constant particular function
    dX_r = mu0 * (-(r ** 2) + Ry ** 2) / (2 * r)

    if self.Jik is None:
        return X_r, dX_r, None, None
    else:
        Rbo = self.Rbore
        e_v = pi * self.k / self.slot_width
        P_v_Rbo_Ry = P(e_v, Rbo, Ry)
        f_v_Rbo = f(e_v, Rbo)
        df_v_Ry = df(e_v, Ry)

        # harmonic particular function
        Xv_r = mu0 * (
            Ry * df_v_Ry * E(e_v, Rbo, r) / (e_v * P_v_Rbo_Ry)
            - f_v_Rbo * P(e_v, r, Ry) / P_v_Rbo_Ry
            + f(e_v, r)
        )

        # derivative of the harmonic particular function
        dXv_r = mu0 * (
            -Ry * df_v_Ry * P(e_v, Rbo, r) / (r * P_v_Rbo_Ry)
            - e_v * f_v_Rbo * E(e_v, r, Ry) / (r * P_v_Rbo_Ry)
            + df(e_v, r)
        )

        return X_r, dX_r, Xv_r, dXv_r


def f(v, r):
    result = r ** 2 / (v ** 2 - 4)

    is_v2 = v == 2

    if isinstance(r, float):
        result[is_v2] = -(r ** 2) * (-log(r) + 1 / 4) / 4
    else:
        result[is_v2] = -r[is_v2] ** 2 * (-log(r[is_v2]) + 1 / 4) / 4

    return result


def df(v, r):
    result = 2 * r / (v ** 2 - 4)

    is_v2 = v == 2

    if isinstance(r, float):
        result[is_v2] = r * (-log(r) + 1 / 4) / 2 - r / 4
    else:
        result[is_v2] = r[is_v2] * (-log(r[is_v2]) + 1 / 4) / 2 - r[is_v2] / 4

    return result
