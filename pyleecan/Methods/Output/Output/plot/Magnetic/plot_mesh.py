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
    self, meshsolution, label=None, index=0, show_edges=False,
):
    """ Display mesh.

    Parameters
    ----------
    self : Output
        an Output object
    mesh : Mesh
        a Mesh object
    """
    #name_file_vtk = "plot_mesh.vtk"

    mesh_jt0 = meshsolution.get_mesh(index=index)
    meshpv = mesh_jt0.get_mesh_pv()

    if label is not None:
        solution_jt0 = meshsolution.get_field(index=index, label=label)
        meshpv[label] = solution_jt0
    else:
        show_edges = True

    # Add field to mesh
    # Add field to mesh

    # Configure plot
    p = pv.BackgroundPlotter()
    p.set_background("white")
    sargs = dict(
        interactive=True,
        title_font_size=20,
        label_font_size=16,
        font_family="arial",
        color="black",
    )

    p.add_mesh(
        meshpv,
        scalars=label,
        show_edges=show_edges,
        edge_color="white",
        line_width=1,
        # cmap=cmap,
        # clim=clim,
        scalar_bar_args=sargs,
    )
    p.show()
