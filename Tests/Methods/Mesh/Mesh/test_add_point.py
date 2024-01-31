# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.NodeMat import NodeMat
import numpy as np


@pytest.mark.MeshSol
class Test_add_node(object):
    """unittest for nodes getter methods"""

    @pytest.fixture
    def setup(self):
        mesh = MeshMat()
        mesh.node = NodeMat()
        mesh.node.add_node(np.array([0, 0]))
        mesh.node.add_node(np.array([1, 0]))
        mesh.node.add_node(np.array([1, 2]))
        mesh.node.add_node(np.array([2, 3]))
        mesh.node.add_node(np.array([3, 3]))

        return mesh

    def test_add_node(self, setup):
        """unittest with ElementMat and NodeMat objects, only Triangle3 elements are defined"""

        assert setup.node.add_node(np.array([1, 2])) == None
