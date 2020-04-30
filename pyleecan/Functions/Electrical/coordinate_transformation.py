from numpy import array, matmul, sqrt, cos, sin, reshape, newaxis, finfo, log10, floor

EPS = int(floor(-log10(finfo(float).eps)))
SQRT3 = sqrt(3)


def ab2uvw(Z_ab):
    """
    2 phase equivalent to 3 phase coordinate transformation, i.e. Clarke transformation

    Parameters
    ----------
    Z_ab : numpy array
        matrix (N x 2) of 2 phase equivalent values

    Outputs
    -------
    Z_uwv : numpy array
        transformed matrix (N x 3) of 3 phase values

    """
    # Transformation matrix
    ab_2_uvw = 1 / 2 * array([[2, -1, -1], [0, SQRT3, -SQRT3]])

    Z_uvw = matmul(Z_ab, ab_2_uvw)

    return Z_uvw


def uvw2ab(Z_uvw):
    """3 phase to 2 phase equivalent coordinate transformation, i.e. Clarke transformation

    Parameters
    ----------
    Z_uvw : numpy array 
        matrix (N x 3) of 3 phase values

    Outputs
    -------
    Z_ab : numpy array
        transformed matrix (N x 2) of 2 phase equivalent values


    """
    # Transformation matrix
    uvw_2_ab = 2 / 3 * array([[1, 0], [-1 / 2, SQRT3 / 2], [-1 / 2, -SQRT3 / 2]])

    Z_ab = matmul(Z_uvw, uvw_2_ab)

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
