# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.collections
import numpy as np


def plot_permeability(self, j_t0=0):
    """Plot the airgap flux as a function of space

    Parameters
    ----------
    self : Output
        an Output object
    j_t0 : int
        Index of the time vector to plot
    is_deg : bool
        True to plot in degree, False in rad
    out_list : list
        List of Output object to compare
    """

    ##########################################
    nodes = self.mag.mesh[j_t0].node
    connectivity = self.mag.mesh[j_t0].element
    mu = self.mag.mesh[j_t0].solution["mu"]

    def showMeshPlot(nodes, elements, values):
        y = nodes[:, 0]
        z = nodes[:, 1]

        def triplot(y, z, triangles, values, ax=None, **kwargs):
            if not ax: ax = plt.gca()
            yz = np.c_[y, z]
            verts = yz[triangles]
            pc = matplotlib.collections.PolyCollection(verts, **kwargs)
            pc.set_array(values)
            ax.add_collection(pc)
            ax.autoscale()
            return pc

        fig, ax = plt.subplots()
        ax.set_aspect('equal')

        pc = triplot(y, z, np.asarray(elements), values, ax=ax,
                     edgecolor="white",cmap="rainbow")
        fig.colorbar(pc, ax=ax)
        ax.plot(y, z, marker="o", markersize=0.1, ls="",
                color="white")  # Tu peux mettre "." sur le marker pou avoir des plus petits noeuds

        ax.set(title='This is the plot for: quad', xlabel='Y Axis', ylabel='Z Axis')

        plt.show()
        return fig, ax

    fig, ax = showMeshPlot(nodes, connectivity, mu)
    return fig, ax





