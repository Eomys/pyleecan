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
    Rag = self.Rrbo

    n = self.k

    P_n_rmin_Rmax = P(n, Ry, Rag)

    # Resolution in potential
    X_n_r = (
        Ry * g(n, Ry) * E(n, r, Rag) + n * f(n, Rag) * P(n, Ry, r)
    ) / P_n_rmin_Rmax - n * f(n, r)
    Y_n_r = (X_n_r + Ry * E(n, r, Rag) / P(n, Ry, Rag)) / n
    dX_n_r = n * (Ry * g(n, Ry) * P(n, r, Rag) - n * f(n, Rag) * E(n, Ry, r)) / (
        r * P_n_rmin_Rmax
    ) - n * g(n, r)
    dY_n_r = dX_n_r / n + Ry * P(n, r, Rag) / (r * P(n, Ry, Rag))

    return X_n_r, Y_n_r, dX_n_r, dY_n_r


def f(n, r):
    result = r / (n**2 - 1)

    is_n1 = n == 1

    if isinstance(r, float):
        result[is_n1] = -r * log(r) / 2
    else:
        result[is_n1] = -r[is_n1] * log(r[is_n1]) / 2

    return result


def g(n, r):
    result = 1 / (n**2 - 1)

    is_n1 = n == 1

    if isinstance(r, float):
        result[is_n1] = -(log(r) + 1) / 2
    else:
        result[is_n1] = -(log(r[is_n1]) + 1) / 2

    return result
