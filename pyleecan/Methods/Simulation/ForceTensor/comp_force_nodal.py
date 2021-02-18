import numpy as np
from SciDataTool import DataTime, VectorField, Data1D

from pyleecan.Classes.Interpolation import Interpolation
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.SolutionVector import SolutionVector


def comp_force_nodal(self, output):
    """Run the nodal forces calculation based on a tensor.

    from publications:


    Parameters
    ----------
    self : ForceVWP
        A ForceVWP object

    output : Output
        an Output object (to update)

    """
    dim = 2
    Nt_tot = output.mag.Nt_tot  # Number of time step

    meshsolution_mag = output.mag.meshsolution
    mesh_mag = output.mag.meshsolution.mesh
    meshsolution = MeshSolution(
        mesh=mesh_mag, is_same_mesh=True, dimension=meshsolution_mag.dimension
    )
    meshsolution.group = meshsolution_mag.group

    # output.struct.magnetic_mesh.is_same_mesh = meshsolution_mag.is_same_mesh

    mesh = meshsolution.get_mesh(0)
    B_sol = meshsolution_mag.get_solution(label="B")
    H_sol = meshsolution_mag.get_solution(label="H")
    mu_sol = meshsolution_mag.get_solution(label="\mu")

    B = B_sol.get_field()
    H = H_sol.get_field()

    axis = B_sol.get_axis()
    pos_indice = list(axis.keys()).index("indice")
    B = np.moveaxis(B, pos_indice, 0)
    H = np.moveaxis(H, pos_indice, 0)

    for key in mesh.cell:
        # [nodes_subpart]

        # For every type of element (now only Triangle3, TO BE extended)
        mesh.cell[key].interpolation = Interpolation()
        mesh.cell[key].interpolation.init_key(key=key, nb_gauss=1)

        nb_pt_per_cell = mesh.cell[key].nb_pt_per_cell
        connect = mesh.cell[key].get_connectivity()
        nb_elem = len(connect)

        nb_pt = mesh.point.nb_pt

        # Nodal forces init
        fx = np.zeros((Nt_tot, nb_pt), dtype=np.float)
        fy = np.zeros((Nt_tot, nb_pt), dtype=np.float)

        ref_cell = mesh.cell[key].interpolation.ref_cell

        # Gauss points
        pts_gauss, poidsGauss, nb_gauss = mesh.cell[
            key
        ].interpolation.gauss_point.get_gauss_points()

        indice_elem = mesh.cell[key].indice
        for ie in range(nb_elem):
            e_ind = indice_elem[ie]
            point_indices = connect[ie, :]
            vertice = mesh.get_vertice(e_ind)[key]

            Be = np.transpose(B[ie, :])
            He = np.transpose(H[ie, :])

            # TODO: Pre calc ...

            for i in range(nb_gauss):

                jacob, det_jacobian = ref_cell.jacobian(pts_gauss[i, 0:dim], vertice)
                grad_func = ref_cell.grad_shape_function(pts_gauss[i, 0:dim])

                inv_J = np.linalg.inv(jacob)

                # Volume ratio
                Ve0 = det_jacobian * poidsGauss[i]

                # Loop on nodes
                for n in range(nb_pt_per_cell):

                    inode = point_indices[n]

                    # TODO: Calc magnetostriction contribution to the current element

                    fxe = Ve0 * my_calcX
                    fx[:, inode] = fx[:, inode] + fxe

                    # Force toward Y-axis on n-th node
                    fye = Ve0 * my_calcY
                    fy[:, inode] = fy[:, inode] + fye

    indices_points = np.sort(np.unique(connect))
    Indices_Point = Data1D(name="indice", values=indices_points, is_components=True)
    Time = B_sol.field.components["x"].axes[0]
    components = {}
    if not np.all((fx == 0)):
        fx_data = DataTime(
            name="Nodal force (x)",
            unit="N",
            symbol="Fx",
            axes=[Time, Indices_Point],
            values=fx,
        )
        components["x"] = fx_data
    if not np.all((fy == 0)):
        fy_data = DataTime(
            name="Nodal force (y)",
            unit="N",
            symbol="Fy",
            axes=[Time, Indices_Point],
            values=fy,
        )
        components["y"] = fy_data

    vec_force = VectorField(name="Nodal forces", symbol="F", components=components)
    solforce = SolutionVector(field=vec_force, type_cell="point", label="F")
    meshsolution.solution.append(solforce)

    output.force.vwp_nodal = meshsolution
    pass
