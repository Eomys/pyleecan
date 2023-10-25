from numpy import log

from ..Subdomain.comp_polynoms import E, P


def comp_magnet_solution(self, r):
    """Method description

    Parameters
    ----------
    self: Subdomain_MagnetSurface
        a Subdomain_MagnetSurface object

    Returns
    ----------
    var: type
        var description
    """

    Ry = self.Ryoke
    Rag = self.Rbore

    n = self.k

    f_n_Rag = f(n, Rag)
    df_n_Ry = df(n, Ry)
    E_n_r_Rag = E(n, r, Rag)
    P_n_Ry_Rag = P(n, Ry, Rag)
    P_n_r_Rag = P(n, r, Rag)

    # Resolution in potential
    X_n_r = (Ry * df_n_Ry * E_n_r_Rag + n * f_n_Rag * P(n, Ry, r)) / P_n_Ry_Rag - n * f(
        n, r
    )

    Y_n_r = (X_n_r + Ry * E_n_r_Rag / P_n_Ry_Rag) / n

    dX_n_r = n * (Ry * df_n_Ry * P_n_r_Rag - n * f_n_Rag * E(n, Ry, r)) / (
        r * P_n_Ry_Rag
    ) - n * df(n, r)

    dY_n_r = dX_n_r / n + Ry * P_n_r_Rag / (r * P_n_Ry_Rag)

    return X_n_r, Y_n_r, dX_n_r, dY_n_r


def f(n, r):
    result = r / (n**2 - 1)

    is_n1 = n == 1

    if isinstance(r, float):
        result[is_n1] = -r * log(r) / 2
    else:
        result[is_n1] = -r[is_n1] * log(r[is_n1]) / 2

    return result


def df(n, r):
    result = 1 / (n**2 - 1)

    is_n1 = n == 1

    if isinstance(r, float):
        result[is_n1] = -(log(r) + 1) / 2
    else:
        result[is_n1] = -(log(r[is_n1]) + 1) / 2

    return result
