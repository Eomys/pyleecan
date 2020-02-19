# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.collections
import numpy as np


def plot_mesh_field(
    self,
    meshsolution=None,
    field_name="mu",
    j_t0=0,
    mesh=None,
    solution=None,
    field=None,
    title="No title",
    group=None,
    elem_type="Triangle3",
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
    if meshsolution is not None:
        mesh = meshsolution.get_mesh(j_t0)
        solution = meshsolution.get_solution(j_t0)

    if group is not None:
        mesh = mesh.set_submesh(group)

    if field is None:
        field = solution.get_field(field_name)

    def showMeshPlot(mesh, elem_type, field, title):
        def triplot(mesh, elem_type, values, ax=None, **kwargs):

            if not ax:
                ax = plt.gca()

            verts = mesh.get_vertice(elem_type)
            pc = matplotlib.collections.PolyCollection(verts, **kwargs)
            pc.set_array(values)
            ax.add_collection(pc)
            ax.autoscale()
            return pc

        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        pc = triplot(
            mesh, elem_type, field, ax=ax, lw=0.1, edgecolor="white", cmap="rainbow"
        )
        fig.colorbar(pc, ax=ax)

        nodes, tags = mesh.get_all_node_coord()
        x = nodes[:, 0]
        y = nodes[:, 1]
        ax.plot(x, y, marker=".", markersize=0.1, ls="", color="white")

        ax.set(title=title, xlabel="Y Axis", ylabel="Z Axis")
        return fig, ax

    fig, ax = showMeshPlot(mesh, elem_type, field, title)
    fig.show()
