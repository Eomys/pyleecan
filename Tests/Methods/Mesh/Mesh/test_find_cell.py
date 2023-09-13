# -*- coding: utf-8 -*-
import numpy as np
import pytest

from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.Interpolation import Interpolation
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.RefSegmentP1 import RefSegmentP1
from pyleecan.Classes.RefTriangle3 import RefTriangle3


@pytest.mark.MeshSol
def test_line():
    DELTA = 1e-10

    mesh = MeshMat()
    mesh.cell["line"] = CellMat(nb_node_per_cell=2)
    mesh.node = NodeMat()
    mesh.node.add_node(np.array([0, 0]))
    mesh.node.add_node(np.array([1, 0]))
    mesh.node.add_node(np.array([0, 1]))

    mesh.add_cell(np.array([0, 1]), "line")
    mesh.add_cell(np.array([0, 2]), "line")
    mesh.add_cell(np.array([1, 2]), "line")

    c_line = mesh.cell["line"]

    c_line.interpolation = Interpolation()
    c_line.interpolation.ref_cell = RefSegmentP1()

    # This node is inside
    test_pt = np.array([0.7, 0])
    sol = 0
    cells = mesh.find_cell(test_pt, 1)[0][1]
    testA = np.sum(abs(cells - sol))
    msg = "Wrong result: returned " + str(cells) + ", expected: " + str(sol)
    assert testA == pytest.approx(0, abs=DELTA), msg

    # This node is outside but in the error margin, so it is considered "inside"
    test_pt = np.array([0.0001, 0.4])
    sol = 1
    cells = mesh.find_cell(test_pt, 1)[0][1]
    testA = np.sum(abs(cells - sol))
    msg = "Wrong result: returned " + str(cells) + ", expected: " + str(sol)
    assert testA == pytest.approx(0, abs=DELTA), msg

    # This node is outside any element, so it must return None
    test_pt = np.array([0.1, 0.4])
    cells = mesh.find_cell(test_pt, 1)
    testA = cells == [None]
    msg = "Wrong result: returned " + str(cells) + ", expected: " + str([None])
    assert testA is True


@pytest.mark.MeshSol
def test_triangle3():
    DELTA = 1e-10

    mesh = MeshMat(dimension=2)
    mesh.node = NodeMat()
    mesh.node.add_node(np.array([0, 0]))
    mesh.node.add_node(np.array([2, 0]))
    mesh.node.add_node(np.array([2, 2]))
    mesh.node.add_node(np.array([0, 2]))

    mesh.cell["triangle"] = CellMat(nb_node_per_cell=3)
    mesh.add_cell(np.array([0, 1, 2]), "triangle")
    mesh.add_cell(np.array([0, 3, 2]), "triangle")

    c_tgl = mesh.cell["triangle"]
    c_tgl.interpolation = Interpolation()
    c_tgl.interpolation.ref_cell = RefTriangle3()

    # This node is inside cell 0
    test_pt = np.array([1, 0.5])
    sol = 0
    cells = mesh.find_cell(test_pt, 1)[0][1]
    testA = np.sum(abs(cells - sol))
    msg = "Wrong result: returned " + str(cells) + ", expected: " + str(sol)
    assert testA == pytest.approx(0, abs=DELTA), msg

    # This node is inside cell 1
    test_pt = np.array([0.5, 1])
    sol = 1
    cells = mesh.find_cell(test_pt, 1)[0][1]
    testA = np.sum(abs(cells - sol))
    msg = "Wrong result: returned " + str(cells) + ", expected: " + str(sol)
    assert testA == pytest.approx(0, abs=DELTA), msg

    # This node is outside but in the error margin, so it is considered "inside"
    test_pt = np.array([-0.0001, 0.4])
    sol = 1
    cells = mesh.find_cell(test_pt, 1)[0][1]
    testA = np.sum(abs(cells - sol))
    msg = "Wrong result: returned " + str(cells) + ", expected: " + str(sol)
    assert testA == pytest.approx(0, abs=DELTA), msg

    # This node is outside any element, so it must return None
    test_pt = np.array([-0.1, 10])
    cells = mesh.find_cell(test_pt, 1)
    testA = cells == [None]
    msg = "Wrong result: returned " + str(cells) + ", expected: " + str([None])
    assert testA is True


if __name__ == "__main__":
    test_line()
    test_triangle3()
