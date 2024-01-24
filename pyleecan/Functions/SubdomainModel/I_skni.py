from numpy import pi, sin, cos, abs as np_abs, any as np_any


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

    ind0 = np_abs(nik - kni * pi / a) < 1e-5

    if np_any(ind0):
        niv1 = nik[ind0]
        theta_ikn1 = theta_ikn[ind0]

        val[ind0] = (
            -2 * a * niv1 * sin(a * niv1 / 2 - niv1 * theta_ikn1)
            + cos(niv1 * (a / 2 - theta_ikn1))
            - cos(3 * a * niv1 / 2 + niv1 * theta_ikn1)
        ) / (4 * niv1)

    if is_antiper_a:
        val_a = val - I_skni(a, nik, kni, theta_ikn + pi / per_a)
        return val.T, val_a

    else:
        return val.T, val
