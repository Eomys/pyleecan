# -*- coding: utf-8 -*-
from os.path import join
import subprocess

from ....Functions.get_path_binary import get_path_binary
from ....Methods.Simulation.Input import InputError


def solve_FEA(self, output):
    """Solve the FEA simulation

    Parameters
    ----------


    Return
    ------


    """
    # Elmer must be installed and in the PATH

    ElmerSolver_bin = get_path_binary("ElmerSolver")

    cmd = ['"' + ElmerSolver_bin + '"']
    cwd = self.get_path_save_fea(output)  # current working dir

    logger = self.get_logger()
    logger.info("Calling ElmerSolver: " + " ".join(map(str, cmd)))

    process = subprocess.Popen(
        " ".join(cmd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        cwd=cwd,
    )
    (stdout, stderr) = process.communicate()

    process.wait()
    print(stdout.decode())
    if process.returncode != 0:
        print(stderr.decode())