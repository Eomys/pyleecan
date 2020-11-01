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
        self.get_logger().debug("Drawing machine in GMSH...")
        # output.mag.FEA_dict = draw_GMSH() # TODO add inputs
        pass
    else:
        self.get_logger().debug("Reusing the FEA file: " + self.import_file)
        # output.mag.FEA_dict = self.FEA_dict
        pass

    # post process GMSH mesh with ElmerGrid
    # TODO add respective function (or method)

    # setup Elmer solver
    # TODO add respective functions or methods

    # Solve for all time step and store all the results in output
    self.solve_FEA(output, sym, axes_dict)
