# -*- coding: utf-8 -*-

from numpy import zeros, array

# User defined winding matrix for plot test (Nrad=2, Ntan=2)
wind_mat = zeros((2, 2, 6, 4))  # Nrad, Ntan, Zs, qs
wind_mat[0, 0, :, :] = array(
    [[1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, -1, -1, 0], [0, -1, 0, 0, 0, 1]]
).T

wind_mat[1, 0, :, :] = array(
    [[0, 0, 0, 0, 0, 0], [-1, 0, -1, 0, 0, -1], [0, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0]]
).T

wind_mat[0, 1, :, :] = array(
    [[-1, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, -1, 0, 0, -1]]
).T

wind_mat[1, 1, :, :] = array(
    [[0, 0, 0, -1, -1, 0], [1, 0, 0, 0, 0, 1], [0, -1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
).T

# For radial winding
wind_mat2 = zeros((2, 1, 6, 3))
wind_mat2[0, 0, :, :] = array(
    [[1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1]]
).T

wind_mat2[1, 0, :, :] = array(
    [[-1, 0, 0, 0, 0, -1], [0, -1, 0, -1, 0, 0], [0, 0, -1, 0, -1, 0]]
).T
