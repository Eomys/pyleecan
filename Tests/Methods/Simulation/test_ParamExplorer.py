# -*- coding: utf-8 -*-

import pytest
from numpy import array_equal
from pyleecan.Classes.ParamExplorerInterval import ParamExplorerInterval


param_test = list()
param_test.append(
    {
        "obj": ParamExplorerInterval(
            min_value=0, max_value=4, N=5, type_value_gen=0, type_value=0
        ),
        "value": [0, 1, 2, 3, 4],
    }
)
param_test.append(
    {
        "obj": ParamExplorerInterval(
            min_value=0, max_value=4.5, N=3, type_value_gen=0, type_value=0
        ),
        "value": [0, 2.25, 4.5],
    }
)
param_test.append(
    {
        "obj": ParamExplorerInterval(
            min_value=0, max_value=4.5, N=3, type_value_gen=0, type_value=1
        ),
        "value": [0, 2, 4],
    }
)


@pytest.mark.METHODS
class Test_ParamExplorerInterval(object):
    @pytest.mark.parametrize("test_dict", param_test)
    def test_get_value(self, test_dict):
        """Check that values are correctly generated"""

        obj = test_dict["obj"]
        value = obj.get_value()
        assert array_equal(value, test_dict["value"])
