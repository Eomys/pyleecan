# -*- coding: utf-8 -*-

import numpy as np


def jacobian(self, point, vertice):
    """Compute jacobian, jacobian determinant and jacobian derivatives for linear triangle.

    Parameters
    ----------
    :param self : a RefElement object

    Returns
    -------

    """

    grad_func = self.grad_shape_function(point)
    jacob = np.dot(grad_func, vertice[:, 0:2])
    det_jacob = np.linalg.det(jacob)

    return jacob, det_jacob
