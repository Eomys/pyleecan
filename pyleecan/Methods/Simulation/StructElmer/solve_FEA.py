# -*- coding: utf-8 -*-

from ....Methods.Simulation.StructElmer import _execute


def solve_FEA(self, output):
    """Solve the FEA simulation

    Parameters
    ----------


    Return
    ------


    """
    cwd = self.get_path_save_fea(output)  # current working dir

    logger = self.get_logger()

    for info in _execute("ElmerSolver", cwd, logger):
        print(info, end="")
