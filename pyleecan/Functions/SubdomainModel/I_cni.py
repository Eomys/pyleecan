from numpy import pi, sin, cos


def I_cni(a, ni, theta_in, per_a=1, is_antiper_a=False):
    val = 2 * sin(a * ni / 2) * cos(theta_in * ni) / ni

    if is_antiper_a:
        val_a = val - I_cni(a, ni, theta_in + pi / per_a)
        return val, val_a.T

    else:
        return val, val.T
