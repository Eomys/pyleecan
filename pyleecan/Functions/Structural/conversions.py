# -*- coding: utf-8 -*-

from numpy import (
    pi,
    column_stack,
    exp,
    real,
    imag,
    cos,
    sin,
    abs as np_abs,
    angle as np_angle,
)


class DimError(Exception):
    """Raised when the dimension of the field does not match requested operation (3D vs 1D)"""

    pass


def xyz_to_rphiz(values):
    """Converts axis values from cartesian coordinates into cylindrical coordinates

    Parameters
    ----------
    values: array
        Values of the axis to convert (Nx3)
    Returns
    -------
    ndarray of the axis (Nx3)
    """

    x = values[:, 0]
    y = values[:, 1]
    z = values[:, 2]

    affixe = x + 1j * y
    r = np_abs(affixe)
    phi = (np_angle(affixe) + 2 * pi) % (2 * pi)

    return column_stack((r, phi, z))


def rphiz_to_xyz(values):
    """Converts axis values from cylindrical coordinates into cartesian coordinates

    Parameters
    ----------
    values: array
        Values of the axis to convert (Nx3)
    Returns
    -------
    ndarray of the axis (Nx3)
    """

    r = values[:, 0]
    phi = values[:, 1]
    z = values[:, 2]

    affixe = r * exp(1j * phi)
    x = real(affixe)
    y = imag(affixe)

    return column_stack((x, y, z))


def xyz_to_rphiz_field(values, phi):
    """Converts field values from cartesian coordinates into cylindrical coordinates

    Parameters
    ----------
    values: array
        Values of the field to convert (Nx3)
    phi: array
        Values of the angle axis (N)
    Returns
    -------
    ndarray of the field (Nx3)
    """

    field_x = values[:, 0]
    field_y = values[:, 1]
    field_z = values[:, 2]

    cos_phi = cos(phi)
    sin_phi = sin(phi)

    field_r = cos_phi * field_x + sin_phi * field_y
    field_phi = -sin_phi * field_x + cos_phi * field_y

    return column_stack((field_r, field_phi, field_z))


def rphiz_to_xyz_field(values, phi):
    """Converts field values from cylindrical coordinates into cartesian coordinates

    Parameters
    ----------
    values: array
        Values of the field to convert (Nx3)
    phi: array
        Values of the angle axis (N)
    Returns
    -------
    ndarray of the field (Nx3)
    """

    field_r = values[:, 0]
    field_phi = values[:, 1]
    field_z = values[:, 2]

    cos_phi = cos(phi)
    sin_phi = sin(phi)

    field_x = cos_phi * field_r - sin_phi * field_phi
    field_y = sin_phi * field_r + cos_phi * field_phi

    return column_stack((field_x, field_y, field_z))


def cart2pol(values, points):
    """Converts field values from cartesian coordinates into cylindrical coordinates

    Parameters
    ----------
    values: array
        Values of the field to convert (Nx3)
    phi: array
        Values of the angle axis (N)
    Returns
    -------
    ndarray of the field (Nx3)
    """

    phi = xyz_to_rphiz(points)[:, 1]
    return xyz_to_rphiz_field(values, phi)


def pol2cart(values, points):
    """Converts field values from cylindrical coordinates into cartesian coordinates

    Parameters
    ----------
    values: array
        Values of the field to convert (Nx3)
    phi: array
        Values of the angle axis (N)
    Returns
    -------
    ndarray of the field (Nx3)
    """

    phi = xyz_to_rphiz(points)[:, 1]
    return rphiz_to_xyz_field(values, phi)
