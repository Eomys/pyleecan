# -*- coding: utf-8 -*-

import pytest
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.NodeMat import NodeMat
import numpy as np

@pytest.mark.METHODS
class Test_set_submesh(object):
    """unittest to get elements containing specific node(s)"""
    def test_ElementMat_NodeMat(self):
        # Init 1
        # Init
        mesh = Mesh()
        mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        mesh.node = NodeMat()
        mesh.node.add_node(np.array([0, 0]))
        mesh.node.add_node(np.array([1, 0]))
        mesh.node.add_node(np.array([1, 2]))
        mesh.node.add_node(np.array([2, 3]))
        mesh.node.add_node(np.array([3, 3]))

        mesh.add_element(np.array([0, 1, 2]), "Triangle3", group=int(3))
        mesh.add_element(np.array([1, 2, 3]), "Triangle3", group=int(3))
        mesh.add_element(np.array([4, 2, 3]), "Triangle3", group=int(2))

        # Method test 1
        mesh_grp4 = mesh.set_submesh([3])
        # Check results
        solution = np.array([[0, 1, 2], [1, 2, 3]])
        results = mesh_grp4.element["Triangle3"].connectivity
        testA = np.sum(abs(solution - results))
        msg = "Wrong result: returned " + str(results) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA-0) < DELTA, msg

        # Method test 2
        mesh_grp4 = mesh.set_submesh([3, 2])
        # Check results
        solution = np.array([2, 3])
        results = mesh_grp4.element["Segment2"].connectivity
        testA = np.sum(abs(solution - results))
        msg = "Wrong result: returned " + str(results) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA-0) < DELTA, msg
