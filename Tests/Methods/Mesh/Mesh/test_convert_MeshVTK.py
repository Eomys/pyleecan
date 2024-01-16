# -*- coding: utf-8 -*-
from os.path import join

import pytest
from numpy.testing import assert_array_almost_equal

from pyleecan.Classes.ImportMeshMat import ImportMeshMat
from pyleecan.Classes.MeshVTK import MeshVTK
from Tests import TEST_DATA_DIR


@pytest.mark.MeshSol
def test_convert_MeshVTK():
    """test convert method of MeshVTK with some vtu file"""
    mesh = MeshVTK(
        path=join(TEST_DATA_DIR, "StructElmer"), name="case_t0001", format="vtu"
    )

    meshmat = mesh.convert(meshtype="MeshMat", scale=1)

    nodes_pv = mesh.get_node_coordinate()
    nodes = meshmat.get_node_coordinate()
    assert_array_almost_equal(nodes_pv, nodes, decimal=6)

    elements_pv, _, _ = mesh.get_element()
    elements, _, _ = meshmat.get_element()
    assert_array_almost_equal(elements_pv["quad9"], elements["quad9"], decimal=1)


@pytest.mark.MeshSol
def test_convert_MeshMat():
    meshmat = ImportMeshMat(
        file_path=join(TEST_DATA_DIR, "Mesh\\mesh_test_mixte.unv"),
    ).get_data()

    meshvtk = meshmat.convert("MeshVTK")

    nodes_pv = meshvtk.get_node_coordinate()
    nodes = meshmat.get_node_coordinate()
    assert_array_almost_equal(nodes_pv, nodes, decimal=6)

    elements_pv, _, _ = meshvtk.get_element()
    elements, _, _ = meshmat.get_element()
    assert_array_almost_equal(elements_pv["quad"], elements["quad"], decimal=1)
    assert_array_almost_equal(elements_pv["triangle"], elements["triangle"], decimal=1)


if __name__ == "__main__":
    test_convert_MeshVTK()
    test_convert_MeshMat()
