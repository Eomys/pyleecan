# -*- coding: utf-8 -*-

import numpy as np


def jacobian(self, point, vertices):
    """Compute jacobian, jacobian determinant and jacobian derivatives for linear triangle.

    Parameters
    ----------
    :param self : a RefElement object

    Returns
    -------

    """

    grad_func = self.grad_shape_function(point)
    jacob = np.dot(grad_func, vertices)
    det_jacob = (
        np.sqrt(
            (vertices[1, 0] - vertices[0, 0]) ** 2
            + (vertices[1, 1] - vertices[0, 1]) ** 2
        )
        / 2
    )

    return jacob, det_jacob
