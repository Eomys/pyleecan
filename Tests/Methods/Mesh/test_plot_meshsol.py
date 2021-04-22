import pytest
import numpy as np

from SciDataTool import DataLinspace, DataFreq, VectorField

from pyleecan.Functions.load import load

from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.SolutionVector import SolutionVector
from pyleecan.Classes.MeshSolution import MeshSolution
from Tests import save_plot_path as save_path

@pytest.fixture(scope="module")
def fixture_gen_mesh():
    mesh = MeshMat(dimension=3)
    mesh.node = NodeMat()
    mesh.node.add_node([1, 0, -1])
    mesh.node.add_node([0.707, 0.707, -1])
    mesh.node.add_node([0, 1, -1])
    mesh.node.add_node([-0.707, 0.707, -1])
    mesh.node.add_node([-1, 0, -1])
    mesh.node.add_node([-0.707, -0.707, -1])
    mesh.node.add_node([0, -1, -1])
    mesh.node.add_node([0.707, -0.707, -1])
    mesh.node.add_node([1, 0, 1])
    mesh.node.add_node([0.707, 0.707, 1])
    mesh.node.add_node([0, 1, 1])
    mesh.node.add_node([-0.707, 0.707, 1])
    mesh.node.add_node([-1, 0, 1])
    mesh.node.add_node([-0.707, -0.707, 1])
    mesh.node.add_node([0, -1, 1])
    mesh.node.add_node([0.707, -0.707, 1])

    mesh.cell["quad"] = CellMat(nb_node_per_cell=4)
    mesh.add_cell([0, 8, 9, 1], "quad")
    mesh.add_cell([1, 9, 10, 2], "quad")
    mesh.add_cell([2, 10, 11, 3], "quad")
    mesh.add_cell([3, 11, 12, 4], "quad")
    mesh.add_cell([4, 12, 13, 5], "quad")
    mesh.add_cell([5, 13, 14, 6], "quad")
    mesh.add_cell([6, 14, 15, 7], "quad")
    mesh.add_cell([7, 15, 8, 0], "quad")
    mesh.cell["quad"].indice = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    
    return mesh

@pytest.fixture(scope="module")
def fixture_gen_field():
    alpha = np.arange(8) * 2 * np.pi / 8
    k = -2
    field = np.exp(1j * k * alpha)
    field = np.hstack((field.T, field.T))
    Indice = DataLinspace(
        name="indice",
        initial=0,
        final=15,
        number=16,
    )
    field_rad = DataFreq(
        name="Radial field",
        unit="",
        symbol="F_{rad}",
        axes=[Indice],
        values=field,
    )
    field_circ = DataFreq(
        name="Circ. field",
        unit="",
        symbol="F_{circ}",
        axes=[Indice],
        values=field,
    )
    components = {}
    components["radial"] = field_rad
    components["circ"] = field_circ
    vectorfield = VectorField(
        name="Field",
        symbol="F",
        components=components,
    )
    solution = SolutionVector(
        field=vectorfield,
        label="Field",
    )

    return solution

@pytest.mark.MeshSol
@pytest.mark.METHODS
# @pytest.mark.DEV
def test_plot_glyph(fixture_gen_mesh, fixture_gen_field):
    mesh = fixture_gen_mesh
    solution = fixture_gen_field
    MSol = MeshSolution(
        mesh=[mesh],
        solution=[solution],
        dimension=3,
    )
    MSol.plot_glyph(
        is_show_fig=False, 
        is_point_arrow=True,
        factor=0.2,
        save_path=save_path + "/plot_glyph.png",
    )

@pytest.mark.MeshSol
@pytest.mark.METHODS
# @pytest.mark.DEV
def test_plot_glyph_animated(fixture_gen_mesh, fixture_gen_field):
    mesh = fixture_gen_mesh
    solution = fixture_gen_field
    MSol = MeshSolution(
        mesh=[mesh],
        solution=[solution],
        dimension=3,
    )
    MSol.plot_glyph_animated(
        is_point_arrow=True,
        factor=0.2,
        gif_name="plot_glyph_animated.gif",
        gif_path=save_path,
    )

@pytest.mark.MeshSol
@pytest.mark.METHODS
# @pytest.mark.DEV
def test_plot_deflection(fixture_gen_mesh, fixture_gen_field):
    mesh = fixture_gen_mesh
    solution = fixture_gen_field
    MSol = MeshSolution(
        mesh=[mesh],
        solution=[solution],
        dimension=3,
    )
    MSol.plot_deflection(
        factor=0.2,
        save_path=save_path + "/plot_deflection.png",
    )

@pytest.mark.MeshSol
@pytest.mark.METHODS
# @pytest.mark.DEV
def test_plot_deflection_animated(fixture_gen_mesh, fixture_gen_field):
    mesh = fixture_gen_mesh
    solution = fixture_gen_field
    MSol = MeshSolution(
        mesh=[mesh],
        solution=[solution],
        dimension=3,
    )
    MSol.plot_deflection_animated(
        factor=0.2,
        gif_name="plot_glyph_animated.gif",
        gif_path=save_path,
    )
