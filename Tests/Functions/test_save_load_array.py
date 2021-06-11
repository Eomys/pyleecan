# -*- coding: utf-8 -*-
from os import remove
from os.path import isfile, join

import pytest
from numpy import all as np_all
from numpy import round as np_round
from numpy.random import rand
from pyleecan.Functions.Load.load_array import load_array
from pyleecan.Functions.Save.save_array import save_array
from Tests import save_load_path as save_path
from Tests import x as logger

logger.info(save_path)

"""test for save and load functions"""

data_list = [rand(5), rand(1, 5), rand(5, 1), rand(5, 2), rand(5, 2, 3, 4)]


@pytest.mark.parametrize("test_data", data_list)
def test_save_load_array(test_data):
    """Check that you can save and load an array"""
    # SetUp
    file_path = join(save_path, "test_data.csv")
    if isfile(file_path):
        remove(file_path)
    assert isfile(file_path) == False

    # Save Test
    save_array(
        file_path,
        test_data,
        fmt="%7.2f",
        delimiter=",",
        header="data",
        slice="slice",
        sep=":",
    )
    assert isfile(file_path)

    # Load Test
    load_data = load_array(file_path, sep=":", delimiter=",")
    assert np_all(load_data == np_round(test_data, 2))

    # Failure Test
    load_data = load_array(file_path, sep=":", delimiter=".")
    assert load_data is None
