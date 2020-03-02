# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.collections
import numpy as np

from pyleecan.Methods.Machine import (
    STATOR_COLOR,
    ROTOR_COLOR,
    SHAFT_COLOR,
    ROTOR_COLOR,
    FRAME_COLOR,
    MAGNET_COLOR,
    BAR_COLOR,
    SCR_COLOR,
    VENT_COLOR,
    VENT_EDGE,
)
from pyleecan.Functions.FEMM import (
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


def plot_mesh(
    self, j_t0=0, mesh=None, title="No title", group=None, elem_type=["Triangle3"]
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

    if group is None:
        group = mesh.group

    def showMeshPlot(mesh, elem_type, group, title, colors):
        def triplot(mesh, elem_type, grp, color, ax=None, **kwargs):

            if not ax:
                ax = plt.gca()

            verts, nb_elem = mesh.get_vertice(elem_type, grp)
            pc = matplotlib.collections.PolyCollection(verts, **kwargs)
            col = np.ones(nb_elem)
            pc.set_facecolor(color)
            ax.add_collection(pc)
            ax.autoscale()
            return pc

        fig, ax = plt.subplots()
        # fig.show()
        ax.set_aspect("equal")

        for type in elem_type:
            ik = 0
            for grp in group:
                pc = triplot(
                    mesh,
                    type,
                    grp,
                    colors[ik],
                    ax=ax,
                    lw=0.1,
                    edgecolor="black",
                    cmap="rainbow",
                )
                ik = ik + 1

        # nodes, tags = mesh.get_all_node_coord()
        # x = nodes[:, 0]
        # y = nodes[:, 1]
        # ax.plot(x, y, marker=".", markersize=0.1, ls="", color="white")

        ax.set(title=title, xlabel="Y Axis", ylabel="Z Axis")
        return fig, ax

    colors = list()
    for grp in group:
        if grp == GROUP_SC:
            color = STATOR_COLOR
        elif grp == GROUP_RC:
            color = ROTOR_COLOR
        elif grp == GROUP_IN:
            color = SHAFT_COLOR
        elif grp == GROUP_RW:
            color = "r"
        elif grp == GROUP_SV or grp == GROUP_RV:
            color = VENT_COLOR
        else:
            color = "w"

        colors.extend(color)

    fig, ax = showMeshPlot(mesh, elem_type, group, title, colors)
    fig.show()
