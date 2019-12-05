# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.collections
import numpy as np


def plot_mesh_field(
    self, meshsolution=None, mesh=None, solution=None, field=None, title="No title"
):
    """ Display 2D field amplitude per element. Several possible inputs combinations: meshsolution only,
        mesh and solution, or mesh and field.

    Parameters
    ----------
    self : Output
        an Output object
    meshsolution: MeshSolution
        a MeshSolution object. Can be replaced by mesh and field.
    mesh : Mesh
        a Mesh object
    solution : Solution
        a Solution object
    field : array
        Column vector with the field to be displayed
    title : str
        Title of the figure
    """

    if meshsolution is None:
        connectivity = mesh.element.get_connectivity()
        nodes = mesh.node.get_coord()
        if solution is not None:
            field = solution.get_field()
    else:
        nodes = meshsolution.mesh.node.get_coord()
        connectivity = meshsolution.mesh.element.get_all_node_tags()
        field = meshsolution.solution.get_field()

    if field is None:
        # field = np.linalg.norm(self.mag.mesh[j_t0].solution[0].B, axis=1)
        field = 1

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
