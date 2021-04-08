# -*- coding: utf-8 -*-

import pytest

from os.path import join
from Tests import save_path, TEST_DATA_DIR
from pyleecan.Classes.ElmerResults import ElmerResults


@pytest.mark.StructElmer
# @pytest.mark.dev
class Test_ElmerResults(object):
    def test_ElmerResults(self):
        """Test that load_data method is working"""
        # TODO improve by different settings and compare values
        res = ElmerResults()
        res.file = join(TEST_DATA_DIR, "StructElmer/LineValues.dat")

        res.columns = [
            "Iteration step"
            "Boundary condition"
            "Node index"
            "coordinate 1"
            "coordinate 2"
            "coordinate 3"
            "displacement 1"
            "displacement 2"
            "principal stress 1"
            "principal stress 2"
            "vonmises"
        ]

        res.load_data()

        return res


# To run it without pytest
if __name__ == "__main__":
    # create test object and test to load result file
    obj = Test_ElmerResults()
    res = obj.test_ElmerResults()
