# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the Structural module"""
    if self.parent is None:
        raise InputError(
            "ERROR: The Structural object must be in a Simulation object to run"
        )
    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )

    output = self.parent.parent

    self.comp_axes(output)

    # setup the mesh
    mesh_names = self.gen_mesh(output)

    # setup the Elmer case file
    self.gen_case(output, mesh_names)

    # Compute the magnetic force according to the Force model
    self.solve_FEA(output)

    # Post processing
