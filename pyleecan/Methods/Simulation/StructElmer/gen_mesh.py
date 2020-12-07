# -*- coding: utf-8 -*-
from os.path import join

from ....Functions.GMSH.draw_GMSH import draw_GMSH
from ....Methods.Simulation.StructElmer import _execute

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
    _, _, sym_r, is_antipert_r = machine.comp_periodicity()

    sym_r = sym_r * (1 + is_antipert_r)

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
        user_mesh_dict=self.FEA_dict_enforced,
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
    # command line parameter to ElmerGrid
    parameter = []
    parameter.append("14 2")
    parameter.append(lam_name)
    if mag_name is not None:
        parameter.append("-in")
        parameter.append(mag_name)
        parameter.append("-unite")

    parameter.append("-out")
    parameter.append(out_name)
    parameter.append("-2d")
    parameter.append("-autoclean")
    parameter.append("-names")

    # execute ElmerGrid
    for info in _execute('ElmerGrid', cwd, logger, parameter=parameter):
            print(info, end="")
    
    return True
