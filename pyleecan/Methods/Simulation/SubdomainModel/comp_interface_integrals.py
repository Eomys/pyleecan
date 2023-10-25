from numpy import pi, sin, cos, abs as np_abs, where


def comp_interface_integrals(self):
    """Abstract method used to define all the integral functions

    Parameters
    ----------
    self: SubdomainModel
        a SubdomainModel object

    Returns
    ----------
    var: type
        var description
    """

    return


def I_cni(a, ni, theta_in, per_a=1, is_antiper_a=False):
    val = 2 * sin(a * ni / 2) * cos(theta_in * ni) / ni

    if is_antiper_a:
        val_a = val - I_cni(a, ni, theta_in + pi / per_a)
        return val, val_a

    else:
        return val, val


def I_sni(a, ni, theta_in, per_a=1, is_antiper_a=False):
    val = 2 * sin(a * ni / 2) * sin(theta_in * ni) / ni

    if is_antiper_a:
        val_a = val - I_sni(a, ni, theta_in + pi / per_a)
        return val, val_a

    else:
        return val, val


def I_ckni(a, nik, kni, theta_ikn, per_a=1, is_antiper_a=False):
    val = (
        a**2
        * nik
        * (
            (-1) ** kni * sin(nik * (a + 2 * theta_ikn) / 2)
            + sin(nik * (a - 2 * theta_ikn) / 2)
        )
        / (a**2 * nik**2 - pi**2 * kni**2)
    )

    ind0 = where((np_abs(nik - kni * pi / a) < 1e-5))[0]

    if ind0.size > 0:
        niv1 = nik[ind0]
        theta_ikn1 = theta_ikn[ind0]

        val[ind0] = (
            2 * a * niv1 * cos(a * niv1 / 2 - niv1 * theta_ikn1)
            + sin(niv1 * (a / 2 - theta_ikn1))
            + sin(3 * a * niv1 / 2 + niv1 * theta_ikn1)
        ) / (4 * niv1)

    if is_antiper_a:
        val_a = val - I_ckni(a, nik, kni, theta_ikn + pi / per_a)
        return val, val_a

    else:
        return val, val


def I_skni(a, nik, kni, theta_ikn, per_a=1, is_antiper_a=False):
    val = (
        a**2
        * nik
        * (
            -((-1) ** kni) * cos(nik * (a + 2 * theta_ikn) / 2)
            + cos(nik * (a - 2 * theta_ikn) / 2)
        )
        / (a**2 * nik**2 - pi**2 * kni**2)
    )

    ind0 = where((np_abs(nik - kni * pi / a) < 1e-5))[0]

    if ind0.size > 0:
        niv1 = nik[ind0]
        theta_ikn1 = theta_ikn[ind0]

        val[ind0] = (
            -2 * a * niv1 * sin(a * niv1 / 2 - niv1 * theta_ikn1)
            + cos(niv1 * (a / 2 - theta_ikn1))
            - cos(3 * a * niv1 / 2 + niv1 * theta_ikn1)
        ) / (4 * niv1)

    if is_antiper_a:
        val_a = val - I_skni(a, nik, kni, theta_ikn + pi / per_a)
        return val, val_a

    else:
        return val, val
