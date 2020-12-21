# -*- coding: utf-8 -*-
import subprocess

from ....Functions.get_path_binary import get_path_binary


def gen_elmer_mesh(self, output):
    """Call ElmerGrid process to convert mesh from Gmsh format to Elmer's compatible

    Parameters
    ----------
    self : Magnetic
        a Magnetic object
    output : Output
        an Output object (to update)

    Returns
    -------
    success: {Boolean}
        Status flag
    """
    # ElmerGrid v8.4 must be installed and in the PATH
    project_name = self.get_path_save_fea(output)
    gmsh_filename = project_name + ".msh"
    elmermesh_folder = project_name
    ElmerGrid_binary = get_path_binary("ElmerGrid")
    cmd_elmergrid = [
        ElmerGrid_binary,
        "14",
        "2",
        gmsh_filename,
        "-2d",
        # "-autoclean",
        # "-names",
        "-out",
        elmermesh_folder,
    ]
    self.get_logger().info("Calling ElmerGrid: " + " ".join(map(str, cmd_elmergrid)))
    elmergrid = subprocess.Popen(
        cmd_elmergrid, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    (stdout, stderr) = elmergrid.communicate()
    elmergrid.wait()
    self.get_logger().info(stdout.decode("UTF-8"))
    if elmergrid.returncode != 0:
        self.get_logger().info("ElmerGrid [Error]: " + stderr.decode("UTF-8"))
        return False
    elmergrid.terminate()
    self.get_logger().info("ElmerGrid call complete!")

    return True
