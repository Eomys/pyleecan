# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.collections
import numpy as np

from ......definitions import config_dict

from ......Functions.FEMM import (
    GROUP_SC,
    GROUP_AG,
    GROUP_RC,
    GROUP_SW,
    GROUP_RW,
    GROUP_AGM,
    GROUP_IN,
    GROUP_FM,
    GROUP_SV,
    GROUP_RV,
    GROUP_SSI,
    GROUP_RSI,
    GROUP_SN,
    GROUP_RN,
    GROUP_SH,
    GROUP_RH,
)

STATOR_COLOR = config_dict["color_dict"]["STATOR_COLOR"]
ROTOR_COLOR = config_dict["color_dict"]["ROTOR_COLOR"]
SHAFT_COLOR = config_dict["color_dict"]["SHAFT_COLOR"]
FRAME_COLOR = config_dict["color_dict"]["FRAME_COLOR"]
MAGNET_COLOR = config_dict["color_dict"]["MAGNET_COLOR"]
BAR_COLOR = config_dict["color_dict"]["BAR_COLOR"]
SCR_COLOR = config_dict["color_dict"]["SCR_COLOR"]
VENT_COLOR = config_dict["color_dict"]["VENT_COLOR"]
VENT_EDGE = config_dict["color_dict"]["VENT_EDGE"]

import pyvista as pv
from numpy import real, pi, linspace, exp
import meshio


def plot_mesh(
    self, meshsolution, field_name="", field_symbol="\mu", j_t0=0, title="No title"
):
    """ Display mesh.

    Parameters
    ----------
    self : Output
        an Output object
    mesh : Mesh
        a Mesh object
    title : str
        Title of the figure
    """
    name_file_vtk = "plot_mesh.vtk"

    mesh_jt0 = meshsolution.get_mesh(j_t0=j_t0)
    solution_jt0 = meshsolution.get_solution(
        j_t0=j_t0, field_name=field_name, field_symbol=field_symbol
    )

    points = mesh_jt0.get_point()
    connect = mesh_jt0.get_cell()

    cells = [("triangle", connect)]

    # Write .vtk file using meshio
    meshio.write_points_cells(
        filename="mesh.vtk", points=points, cells=cells, cell_data=solution_jt0,
    )

    meshio.write(name_file_vtk)

    # Read .vtk file with pyvista
    mesh = pv.read(name_file_vtk)
    mesh2 = mesh.warp_by_vector()

    # Plot
    pv.set_plot_theme("document")
    p = pv.Plotter(notebook=False)
    sargs = dict(interactive=True, n_colors=50)

    p.add_mesh(
        mesh2,
        color="grey",
        # opacity=0.5,
        show_edges=True,
        edge_color="white",
        line_width=0.0001,
        # clim=[-3.6e-12, 3.6e-12],
        # cmap="RdBu_r",
        # scalar_bar_args=sargs
    )
    p.remove_scalar_bar()
    p.show(use_panel=False, auto_close=False)

    # Close movie and delete object
    p.close()
