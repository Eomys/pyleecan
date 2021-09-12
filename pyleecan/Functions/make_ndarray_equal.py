# -*- coding: utf-8 -*-

import numpy as np


def make_ndarray_equal(vec_ref, vec_to_sort):
    """Compare two ndarray, sort the second to match with the first one.

    Parameters
    ----------
    vec_ref : ndarray
        reference vector
    vec_to_sort : ndarray
        vector to sort

    Returns
    -------
    Isort: ndarray
        Vector of indice to sort the vec_to_sort
    vec: ndarray
        Sorted vector

    """

    nb = len(vec_ref)
    Isort = np.zeros(nb)

    for i in range(nb):
        Isort[i] = np.where(vec_ref[i] == vec_to_sort)

    return Isort, vec_to_sort[Isort]
