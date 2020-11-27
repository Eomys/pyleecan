# -*- coding: utf-8 -*-
from os.path import join
import subprocess

from ....Methods.Simulation.Input import InputError
from ....Functions.GMSH.draw_GMSH import draw_GMSH


def init_model(self, output):
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
    file_gmsh_lam = join(save_dir, "lamination.msh")
    file_gmsh_mag = join(save_dir, "magnets.msh")

    gmsh, grps, grp_names = self.preprocess_model(
        file_in=file_gmsh_geo,
        file_out=file_gmsh_lam,
        is_get_lam=True,
        is_get_magnet=False,
    )

    gmsh, grps, grp_names = self.preprocess_model(
        file_in=file_gmsh_geo,
        file_out=file_gmsh_mag,
        is_get_lam=False,
        is_get_magnet=True,
    )

    # convert to ElmerGrid mesh
    _gen_mesh(save_dir, file_gmsh_lam, file_gmsh_mag)


def _gen_mesh(output_path, lamination_file, magnets_file):
    """Convert the GMSH mesh to ElmerGrid mesh

    Parameters
    ----------

    Returns
    -------

    """
    # ElmerGrid must be installed and in the PATH
    # TODO add test

    cmd_elmergrid = [
        "ElmerGrid 14 2",
        ' "' + lamination_file + '" ',
        "-in",
        ' "' + magnets_file + '" ',
        "-out" ' "' + output_path + '" ',
        "-2d -autoclean -names",
    ]
    process_elmergrid = subprocess.Popen(
        cmd_elmergrid, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    (stdout, stderr) = process_elmergrid.communicate()

    process_elmergrid.wait()
    if process_elmergrid.returncode != 0:
        print(stdout)
        print(stderr)

    return True
