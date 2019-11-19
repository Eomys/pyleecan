# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.collections
import numpy as np


def plot_mesh_field(
    self,
    j_t0=0,
    nodes=None,
    connectivity=None,
    field=None,
    title="Magnetic field amplitude B",
):
    """ Display field amplitude per element

    Parameters
    ----------
    self : Output
        an Output object
    j_t0 : int
        Index of the time vector to plot
    nodes : ndarray
        Nodes coordinates (2D)
    connectivity : ndarray
        Connectivity matrix (3 nodes per element)
    field : ndarray
        Column vector with the field to be displayed
    """

    if nodes is None:
        nodes = self.mag.mesh[j_t0].node

    if connectivity is None:
        connectivity = self.mag.mesh[j_t0].element

    if field is None:
        field = np.linalg.norm(self.mag.mesh[j_t0].B, axis=1)

    def showMeshPlot(nodes, elements, values, title):
        y = nodes[:, 0]
        z = nodes[:, 1]

        def triplot(y, z, triangles, values, ax=None, **kwargs):
            if not ax:
                ax = plt.gca()
            yz = np.c_[y, z]
            verts = yz[triangles]
            pc = matplotlib.collections.PolyCollection(verts, **kwargs)
            pc.set_array(values)
            ax.add_collection(pc)
            ax.autoscale()
            return pc

        fig, ax = plt.subplots()
        ax.set_aspect("equal")

        pc = triplot(
            y, z, np.asarray(elements), values, ax=ax, edgecolor="white", cmap="rainbow"
        )
        fig.colorbar(pc, ax=ax)
        ax.plot(
            y, z, marker="o", markersize=0.1, ls="", color="white"
        )  # Tu peux mettre "." sur le marker pou avoir des plus petits noeuds

        ax.set(title=title, xlabel="Y Axis", ylabel="Z Axis")

        plt.show()
        return fig, ax

    fig, ax = showMeshPlot(nodes, connectivity, field, title)
    return fig, ax
