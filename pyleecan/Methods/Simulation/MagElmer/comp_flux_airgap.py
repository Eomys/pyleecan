# -*- coding: utf-8 -*-

from ....Functions.GMSH.draw_GMSH import draw_GMSH


def comp_flux_airgap(self, output, axes_dict):
    """Build and solve Elmer model to calculate and store magnetic quantities

    Parameters
    ----------
    self : MagElmer
        a MagElmer object
    output : Output
        an Output object
    axes_dict: {Data}
        Dict of axes used for magnetic calculation
    """

    # Set the symmetry factor according to the machine
    sym, is_antiper_a = axes_dict["Angle"].get_periodicity()

    # Setup the Elmer simulation
    # Geometry building
    if not self.import_file:  # True if None or len == 0
        self.get_logger().debug("Drawing machine in Gmsh...")
        # output.mag.FEM_dict = draw_GMSH()
        pass
    else:
        self.get_logger().debug("Reusing the FEM file: " + self.import_file)
        # output.mag.FEM_dict = self.FEM_dict
        pass

    # post process GMSH mesh with ElmerGrid
    # TODO
    if self.nb_worker > 1:
        pass
    else:
        pass

    # setup Elmer solver
    # TODO

    # Solve for all time step and store all the results in output
    self.solve_FEA(output, sym, axes_dict)
