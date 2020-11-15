# -*- coding: utf-8 -*-
import subprocess

from ....Classes.Magnetics import Magnetics


def gen_elmer_mesh(self, output):
    """Compute the additional axes required in the MagElmer module

    Parameters
    ----------
    self : Magnetic
        a Magnetic object
    output : Output
        an Output object (to update)

    Returns
    -------
    axes_dict: {Data}
        Dict containing Time_Tem axis used in MagFEMM to store torque result
    """
    # ElmerGrid must be installed and in the PATH

    cmd_elmergrid = ['ElmerGrid', '14', '2', 'stator.msh2', '-2d', '-autoclean', '-names']
    process_elmergrid = subprocess.Popen(cmd_elmergrid, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = process_elmergrid.communicate()

    process_elmergrid.wait()
    if process_elmergrid.returncode != 0:
        print(stdout)
        print(stderr)

    return True
