# -*- coding: utf-8 -*-

from ....Classes.MeshSolution import MeshSolution
from ....Classes.Mesh import Mesh
from ....Classes.Solution import Solution


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
