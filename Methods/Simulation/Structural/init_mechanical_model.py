# -*- coding: utf-8 -*-

from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.Solution import Solution


def init_mechanical_model(self, output, group):
    """Generate or load the mechanical model (mesh, boundary condition, material ...)

    Parameters
    ----------
    self : Structural
        a Structural object
    output : Output
        an Output object (to update)
    Nt_tot : int
        Total time steps number
    group : array
        Define the part of the machine for the mechanical simulation
    """

    # TODO:
    if self.mechanical_mesh is not None:
        output.struct.mechanical_mesh = self.mechanical_mesh.get_data(output, group)
    else:
        output.struct.mechanical_mesh = self.gen_mechanical_mesh()
