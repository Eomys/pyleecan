# -*- coding: utf-8 -*-

import pytest
from numpy import array_equal
from pyleecan.Classes.ParamExplorerInterval import ParamExplorerInterval
from pyleecan.Classes.ParamExplorerSet import ParamExplorerSet

param_test = list()
param_test.append(
    {
        "obj": ParamExplorerInterval(
            min_value=0, max_value=4, N=5, type_value_gen=0, type_value=0
        ),
        "value": [0, 1, 2, 3, 4],
        "min": 0,
        "max": 4,
        "N": 5,
    }
)
param_test.append(
    {
        "obj": ParamExplorerInterval(
            min_value=0, max_value=4.5, N=3, type_value_gen=0, type_value=0
        ),
        "value": [0, 2.25, 4.5],
        "min": 0,
        "max": 4.5,
        "N": 3,
    }
)
param_test.append(
    {
        "obj": ParamExplorerInterval(
            min_value=0, max_value=4.5, N=3, type_value_gen=0, type_value=1
        ),
        "value": [0, 2, 4],
        "min": 0,
        "max": 4,
        "N": 3,
    }
)
param_test.append(
    {
        "obj": ParamExplorerSet(value=[10, 5, 2, 20]),
        "value": [10, 5, 2, 20],
        "min": 2,
        "max": 20,
        "N": 4,
    }
)
param_test.append(
    {
        "obj": ParamExplorerSet(value=["test", "test2"]),
        "value": ["test", "test2"],
        "min": None,
        "max": None,
        "N": 2,
    }
)


class Test_ParamExplorer(object):
    @pytest.mark.parametrize("test_dict", param_test)
    def test_get_value(self, test_dict):
        """Check that values are correctly generated"""

        obj = test_dict["obj"]
        value = obj.get_value()
        assert array_equal(value, test_dict["value"])

    @pytest.mark.parametrize("test_dict", param_test)
    def test_get_min(self, test_dict):
        """Check that min is correctly returned"""

        obj = test_dict["obj"]
        result = obj.get_min()
        assert result == test_dict["min"]

    @pytest.mark.parametrize("test_dict", param_test)
    def test_get_max(self, test_dict):
        """Check that max is correctly returned"""

        obj = test_dict["obj"]
        result = obj.get_max()
        assert result == test_dict["max"]

    @pytest.mark.parametrize("test_dict", param_test)
    def test_get_N(self, test_dict):
        """Check that N is correctly returned"""

        obj = test_dict["obj"]
        result = obj.get_N()
        assert result == test_dict["N"]
