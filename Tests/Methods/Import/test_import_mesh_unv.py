# -*- coding: utf-8 -*-

# TODO: debug mesh with mix of elements (not handled in pyuff)

from os import mkdir
from os.path import basename, isdir, join, splitext

import pytest

from pyleecan.Classes.ImportMeshMat import ImportMeshMat
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.definitions import TEST_DIR
from Tests import save_plot_path as save_path

save_path = join(save_path, "Import")
if not isdir(save_path):
    mkdir(save_path)

list_param = [
    {
        "path": "Data\Mesh\mesh_test_quad_consecutive.unv",
        "n_points": 8,
        "element_types": ["quad"],
        "n_elements": [6],
    },
    {
        "path": "Data\Mesh\mesh_test_quad.unv",
        "n_points": 8,
        "element_types": ["quad"],
        "n_elements": [6],
    },
    {
        "path": "Data\Mesh\mesh_test_tri.unv",
        "n_points": 4,
        "element_types": ["triangle"],
        "n_elements": [4],
    },
    {
        "path": "Data\Mesh\mesh_test_mixte.unv",
        "n_points": 5,
        "element_types": ["triangle", "quad"],
        "n_elements": [3, 1],
    },
    {
        "path": "Data\Mesh\mesh_test_quad_set82.unv",
    },
]


@pytest.mark.MeshSol
@pytest.mark.parametrize(
    "unv_file",
    list_param,
)
def test_import_mesh_unv(unv_file):
    """Check that .unv file are correctly imported"""

    test_obj = ImportMeshMat(
        file_path=join(TEST_DIR, unv_file["path"]),
    )
    mesh = test_obj.get_data()

    meshsol = MeshSolution(dimension=3)
    meshsol.mesh = mesh
    meshsol.plot_mesh(
        save_path=join(save_path, splitext(basename(unv_file["path"]))[0] + ".png"),
        is_show_axes=True,
        is_show_fig=False,
    )


if __name__ == "__main__":
    for param in list_param:
        test_import_mesh_unv(param)
