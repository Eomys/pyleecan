# -*- coding: utf-8 -*-
from os.path import join
import subprocess

from ....Methods.Simulation.Input import InputError
from ....Functions.GMSH.draw_GMSH import draw_GMSH
from ....Functions.get_path_binary import get_path_binary


def gen_mesh(self, output):
    """Initialize the FEA simulation model

    Parameters
    ----------
    self : StructElmer object

    output : Output
        Output object that contains the StructElmer simulation

    Return
    ------


    """
    # readability
    machine = output.simu.machine
    sym, _, sym_r, is_antipert_r = machine.comp_periodicity()

    sym_r = sym_r * (1 + is_antipert_r)

    # temp. mesh settings

    n1 = 3
    n2 = 20

    mesh_dict = {
        "Magnet_0_Top": n2,
        "Magnet_0_Bottom": n2,
        "Magnet_0_Left": n1,
        "Magnet_0_Right": n1,
        "Magnet_1_Top": n2,
        "Magnet_1_Bottom": n2,
        "Magnet_1_Left": n1,
        "Magnet_1_Right": n1,
        "Hole_0_Top": 0,
        "Hole_0_Left": n1,
        "Hole_0_Right": n1,
        "Hole_1_Top": 0,
        "Hole_1_Left": n1,
        "Tangential_Bridge": 10,
        "Lamination_Rotor_Bore_Radius_Ext": 100,
    }

    # get the save path and file names
    save_dir = self.get_path_save_fea(output)

    # draw initial gmsh model
    file_gmsh_geo = join(save_dir, "GMSH_Machine_Model.geo")

    draw_GMSH(
        output=output,
        sym=sym_r,  # TODO is it possible to have to use draw_GMSH with sym_r > sym ?
        is_lam_only_S=False,
        is_lam_only_R=False,
        is_sliding_band=False,
        user_mesh_dict=mesh_dict,
        path_save=file_gmsh_geo,
        is_set_labels=True,
    )

    # preprocess GMSH model to get rotor lamination and magnet and set boundary names
    lam_name = "lamination.msh"
    mag_name = "magnets.msh" if self.include_magnets else None

    names = {}
    _, _, names["Lamination"] = self.process_mesh(
        file_gmsh_geo,
        join(save_dir, lam_name),
        is_get_lam=True,
        is_get_magnet=False,
    )

    if self.include_magnets:
        _, _, names["Magnets"] = self.process_mesh(
            file_gmsh_geo,
            join(save_dir, mag_name),
            is_get_lam=False,
            is_get_magnet=True,
        )

    # convert to ElmerGrid mesh
    _gen_mesh(save_dir, "Mesh", lam_name, mag_name, self.get_logger())

    return names


def _gen_mesh(cwd, out_name, lam_name, mag_name=None, logger=None):
    """Convert the mesh from GMSH format to ElmerGrid format

    Parameters
    ----------

    Returns
    -------

    """
    # ElmerGrid must be installed and in the PATH

    ElmerGrid_bin = get_path_binary("ElmerGrid")

    cmd = []
    cmd.append('"' + ElmerGrid_bin + '"')
    cmd.append("14 2")
    cmd.append(lam_name)
    if mag_name is not None:
        cmd.append("-in")
        cmd.append(mag_name)
        cmd.append("-unite")

    cmd.append("-out")
    cmd.append(out_name)
    cmd.append("-2d")
    cmd.append("-autoclean")
    cmd.append("-names")

    if logger:
        logger.info("Calling ElmerGrid: " + " ".join(map(str, cmd)))

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

    return True
