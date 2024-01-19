import numpy as np
import pytest

from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.SolutionMat import SolutionMat
from Tests import save_plot_path as save_path


@pytest.mark.MeshSol
def test_plot_contour_1group():
    mesh = MeshMat(dimension=3)
    mesh.node = NodeMat()
    mesh.node.add_node([0, 0, 0])
    mesh.node.add_node([0, 1, 0])
    mesh.node.add_node([1, 0, 0])
    mesh.node.add_node([1, 1, 0])
    mesh.node.add_node([2, 1, 0])

    mesh.element_dict["triangle"] = ElementMat(nb_node_per_element=3)
    mesh.add_element([0, 1, 2], "triangle")
    mesh.add_element([1, 2, 3], "triangle")
    mesh.add_element([2, 3, 4], "triangle")
    mesh.element_dict["triangle"].indice = np.array([11, 12, 13])

    solution = SolutionMat()
    solution.field = np.array([[1, 2, 3], [2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4]])
    solution.axis_name = ["time", "indice"]
    solution.axis_size = [5, 3]
    solution.indice = np.array([11, 12, 13])
    solution.type_element = "triangle"
    solution.label = "B"

    MSol = MeshSolution(mesh=mesh, solution_dict={solution.label: solution})
    MSol.group = {"stator core": np.array([11, 12])}

    MSol.plot_contour(is_show_fig=False, save_path=save_path + "/plot_mesh.png")
    Msol_stator = MSol.get_group("stator core")
    Msol_stator.plot_contour(
        is_show_fig=False,
        save_path=save_path + "/plot_mesh_stator.png",
    )


def test_plot_contour_2group():
    mesh = MeshMat()
    mesh.element_dict["triangle"] = ElementMat(nb_node_per_element=3)
    mesh.node = NodeMat()
    mesh.node.add_node(np.array([0, 0]))
    mesh.node.add_node(np.array([1, 0]))
    mesh.node.add_node(np.array([1, 2]))
    mesh.node.add_node(np.array([2, 3]))
    mesh.node.add_node(np.array([3, 3]))

    mesh.node.add_node(np.array([-1, 0]))
    mesh.node.add_node(np.array([-1, -2]))
    mesh.node.add_node(np.array([-2, -3]))
    mesh.node.add_node(np.array([-3, -3]))

    mesh.add_element(np.array([0, 1, 2]), "triangle")
    mesh.add_element(np.array([1, 2, 3]), "triangle")
    mesh.add_element(np.array([4, 2, 3]), "triangle")
    mesh.add_element(np.array([0, 5, 6]), "triangle")
    mesh.add_element(np.array([5, 6, 7]), "triangle")
    mesh.add_element(np.array([8, 6, 7]), "triangle")

    mesh.element_dict["triangle"].indice = np.array([11, 12, 13, 98, 100, 101])

    solution = SolutionMat()
    solution.field = np.array(
        [[1, 2, 3], [2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4], [7, 8, 9]]
    )
    solution.axis_name = ["indice", "time"]
    solution.axis_size = [6, 3]
    solution.indice = np.array([11, 12, 13, 98, 100, 101])
    solution.type_element = "triangle"
    solution.label = "B"

    meshsol = MeshSolution()
    meshsol.mesh = mesh
    meshsol.solution_dict = {solution.label: solution}
    meshsol.group = dict()
    meshsol.group["stator"] = np.array([11])
    meshsol.group["rotor"] = np.array([98, 100, 101])

    meshsol.plot_contour(is_show_fig=False, save_path=save_path + "/plot_mesh.png")
    meshsol.get_group(["stator", "rotor"]).plot_contour(
        is_show_fig=False,
        save_path=save_path + "/plot_mesh_stator.png",
    )


if __name__ == "__main__":
    test_plot_contour_1group()
    test_plot_contour_2group()
