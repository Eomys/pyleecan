# -*- coding: utf-8 -*-
"""
Package: 
File Created: Thursday, 5th March 2020 11:32:19 am
Last Modified: Thursday, 5th March 2020 11:33:16 am
Author: Sebastian Guenther
"""

from unittest import TestCase

from ddt import ddt
from numpy import pi, array
from numpy.testing import assert_array_almost_equal

from pyleecan.Functions.Electrical.coordinate_transformation import (
    ab2uvw,
    uvw2ab,
    dq2ab,
    ab2dq,
)


@ddt
class unittest_InCurrentDQ_meth(TestCase):
    """unittest for coordinate transformation functions"""

    def test_coordinate_transformation_Ok(self):
        """Check that the coordinate transformations can return a correct output
        """

    X_uvw = array([[1, -0.5, -0.5], [-1, 0.5, 0.5]])
    X_ab = array([[1, 0], [0, 1]])

    th_90 = pi / 2
    th_180 = pi

    X_dq90 = array([[0, -1], [1, 0]])
    X_dq180 = array([[-1, 0], [0, -1]])

    assert_array_almost_equal(ab2uvw(uvw2ab(X_uvw)), X_uvw)
    assert_array_almost_equal(dq2ab(ab2dq(X_ab, 0), 0), X_ab)
    assert_array_almost_equal(dq2ab(ab2dq(X_ab, th_90), th_90), X_ab)

    assert_array_almost_equal(ab2dq(X_ab, th_90), X_dq90)
    assert_array_almost_equal(ab2dq(X_ab, th_180), X_dq180)

