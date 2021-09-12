from numpy import (
    array,
    matmul,
    sqrt,
    cos,
    sin,
    reshape,
    newaxis,
    finfo,
    log10,
    floor,
    pi,
    linspace,
    column_stack,
    vstack,
)

EPS = int(floor(-log10(finfo(float).eps)))

# TODO: add homopolar component


def ab2n(Z_ab, n=3, rot_dir=-1):
    """
    2 phase equivalent to n phase coordinate transformation, i.e. Clarke transformation

    Parameters
    ----------
    Z_ab : ndarray
        matrix (N x 2) of 2 phase equivalent values
    n : integer
        number of phases
    rot_dir : integer
        rotation direction of the fundamental of magnetic field (rot_dir = +/- 1)

    Returns
    -------
    Z_n : ndarray
        transformed matrix (N x n) of n phase values

    """
    ii = linspace(0, n - 1, n)
    alpha = (
        rot_dir * 2 * ii * pi / n
    )  # Phasor depending on fundamental field rotation direction

    # Transformation matrix
    ab_2_n = vstack((cos(alpha).round(decimals=EPS), -sin(alpha).round(decimals=EPS)))

    Z_n = matmul(Z_ab, ab_2_n)

    return Z_n


def n2ab(Z_n, n=3, rot_dir=-1):
    """n phase to 2 phase equivalent coordinate transformation, i.e. Clarke transformation

    Parameters
    ----------
    Z_n : ndarray
        matrix (N x n) of n phase values
    n : integer
        number of phases
    rot_dir : integer
        rotation direction of the fundamental of magnetic field (rot_dir = +/- 1)

    Returns
    -------
    Z_ab : ndarray
        transformed matrix (N x 2) of 2 phase equivalent values

    """
    ii = linspace(0, n - 1, n)
    alpha = (
        rot_dir * 2 * ii * pi / n
    )  # Phasor depending on fundamental field rotation direction

    # Transformation matrix
    n_2_ab = (
        2
        / n
        * column_stack(
            (cos(alpha).round(decimals=EPS), -sin(alpha).round(decimals=EPS))
        )
    )

    Z_ab = matmul(Z_n, n_2_ab)

    return Z_ab


def ab2dq(Z_ab, theta):
    """
    alpha-beta to dq coordinate transformation
    NOTE: sin/cos values are rounded to avoid numerical errors

    Parameters
    ----------
    Z_ab : ndarray
        matrix (N x 2) of alpha-beta - reference frame values
    theta : ndarray
        angle of the rotor coordinate system

    Returns
    -------
    Z_dq : ndarray
        transformed (dq) values

    """
    if len(Z_ab.shape) == 1:
        Z_ab = Z_ab[newaxis, :]

    sin_theta = sin(theta).round(decimals=EPS)
    cos_theta = cos(theta).round(decimals=EPS)

    Z_d = Z_ab[:, 0] * cos_theta + Z_ab[:, 1] * sin_theta
    Z_q = -Z_ab[:, 0] * sin_theta + Z_ab[:, 1] * cos_theta

    return reshape([Z_d, Z_q], (2, -1)).transpose()


def dq2ab(Z_dq, theta):
    """
    dq to alpha-beta coordinate transformation
    NOTE: sin/cos values are rounded to avoid numerical errors

    Parameters
    ----------
    Z_dq : ndarray
        matrix (N x 2) of dq - reference frame values
    theta : ndarray
        angle of the rotor coordinate system

    Returns
    -------
    Z_ab : ndarray
        transformed array

    """
    if len(Z_dq.shape) == 1:
        Z_dq = Z_dq[newaxis, :]

    sin_theta = sin(theta).round(decimals=EPS)
    cos_theta = cos(theta).round(decimals=EPS)

    # Multiply by sqrt(2) to go from (Id_rms, Iq_rms) in to I_ab in amplitude
    Z_a = Z_dq[:, 0] * cos_theta - Z_dq[:, 1] * sin_theta
    Z_b = Z_dq[:, 0] * sin_theta + Z_dq[:, 1] * cos_theta

    return reshape([Z_a, Z_b], (2, -1)).transpose()


def n2dq(Z_n, theta, n=3, rot_dir=-1, is_dq_rms=True):
    """n phase to dq equivalent coordinate transformation

    Parameters
    ----------
    Z_n : ndarray
        matrix (N x n) of n phase values
    n : integer
        number of phases
    rot_dir : integer
        rotation direction of the fundamental of magnetic field (rot_dir = +/- 1)
    is_dq_rms : boolean
        True to return dq currents in rms value (Pyleecan convention), False to return peak values

    Returns
    -------
    Z_dq : ndarray
        transformed matrix (N x 2) of dq equivalent values

    """

    Z_dq = ab2dq(n2ab(Z_n, n=n, rot_dir=rot_dir), theta)

    if is_dq_rms == True:
        # Divide by sqrt(2) to go from (Id_peak, Iq_peak) to (Id_rms, Iq_rms)
        Z_dq = Z_dq / sqrt(2)

    return Z_dq


def dq2n(Z_dq, theta, n=3, rot_dir=-1, is_n_rms=False):
    """n phase to dq equivalent coordinate transformation

    Parameters
    ----------
    Z_dq : ndarray
        matrix (N x 2) of dq phase values
    n : integer
        number of phases
    rot_dir : integer
        rotation direction of the fundamental of magnetic field (rot_dir = +/- 1)
    is_n_rms : boolean
        True to return n currents in rms value, False to return peak values (Pyleecan convention)

    Returns
    -------
    Z_n : ndarray
        transformed matrix (N x n) of n phase values

    """

    Z_n = ab2n(dq2ab(Z_dq, theta), n=n, rot_dir=rot_dir)

    if is_n_rms == False:
        # Multiply by sqrt(2) to from (I_n_rms) to (I_n_peak)
        Z_n = Z_n * sqrt(2)

    return Z_n
