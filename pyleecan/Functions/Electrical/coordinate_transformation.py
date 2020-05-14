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
SQRT3 = sqrt(3)


def ab2n(Z_ab, n=3):
    """
    2 phase equivalent to n phase coordinate transformation, i.e. Clarke transformation

    Parameters
    ----------
    Z_ab : numpy array
        matrix (N x 2) of 2 phase equivalent values
    n : int
        number of phases

    Outputs
    -------
    Z_n : numpy array
        transformed matrix (N x n) of n phase values

    """
    ii = linspace(0, n - 1, n)
    alpha = 2 * ii * pi / n

    # Transformation matrix
    ab_2_n = vstack((cos(alpha).round(decimals=EPS), -sin(alpha).round(decimals=EPS)))

    Z_n = matmul(Z_ab, ab_2_n)

    return Z_n


def n2ab(Z_n, n=3):
    """n phase to 2 phase equivalent coordinate transformation, i.e. Clarke transformation

    Parameters
    ----------
    Z_n : numpy array 
        matrix (N x n) of n phase values

    Outputs
    -------
    Z_ab : numpy array
        transformed matrix (N x 2) of 2 phase equivalent values

    """
    ii = linspace(0, n - 1, n)
    alpha = 2 * ii * pi / n

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
    Z_ab : numpy array
        matrix (N x 2) of alpha-beta - reference frame values

    theta : numpy array
        angle of the rotor coordinate system

    Outputs
    -------
    Z_dq : numpy array
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
    Z_dq : numpy array
        matrix (N x 2) of dq - reference frame values

    theta : numpy array
        angle of the rotor coordinate system

    Outputs
    -------
    Z_ab : numpy array
        transformed array

    """
    if len(Z_dq.shape) == 1:
        Z_dq = Z_dq[newaxis, :]

    sin_theta = sin(theta).round(decimals=EPS)
    cos_theta = cos(theta).round(decimals=EPS)

    Z_a = Z_dq[:, 0] * cos_theta - Z_dq[:, 1] * sin_theta
    Z_b = Z_dq[:, 0] * sin_theta + Z_dq[:, 1] * cos_theta

    return reshape([Z_a, Z_b], (2, -1)).transpose()


def n2dq(Z_n, theta, n=3):
    """n phase to dq equivalent coordinate transformation

    Parameters
    ----------
    Z_n : numpy array 
        matrix (N x n) of n phase values

    Outputs
    -------
    Z_dq : numpy array
        transformed matrix (N x 2) of dq equivalent values

    """
    return ab2dq(n2ab(Z_n, n=n), theta)


def dq2n(Z_dq, theta, n=3):
    """n phase to dq equivalent coordinate transformation

    Parameters
    ----------
    Z_dq : numpy array 
        matrix (N x 2) of dq phase values

    Outputs
    -------
    Z_n : numpy array
        transformed matrix (N x n) of n phase values

    """
    return ab2n(dq2ab(Z_dq, theta), n=n)
