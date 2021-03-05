import numpy as np
from SciDataTool import DataTime, VectorField, Data1D

from pyleecan.Classes.Interpolation import Interpolation
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.SolutionVector import SolutionVector


def comp_force_nodal(self, output, axes_dict):
    """Run the nodal forces calculation based on a tensor.

    from publications:


    Parameters
    ----------
    self : ForceTensor
        A ForceTensor object

    output : Output
        an Output object (to update)

    """

    dim = 2
    Time = axes_dict["Time"]
    Nt_tot = Time.get_length()  # Number of time step

    meshsolution_mag = output.mag.meshsolution  # Comes from FEMM simulation

    # Select the target group (stator, rotor ...)
    meshsolution_group = meshsolution_mag.get_group(self.group)

    # TODO before: Check if is_same_mesh is True
    mesh = meshsolution_group.get_mesh()

    # New meshsolution object for output, that could be different from the one inputed
    meshsolution = MeshSolution(mesh=[mesh.copy()], is_same_mesh=True, dimension=dim)

    # Load magnetic flux B and H and mu objects
    B_sol = meshsolution_group.get_solution(label="B")
    H_sol = meshsolution_group.get_solution(label="H")
    mu_sol = meshsolution_group.get_solution(label="\mu")

    # Import time vector from Time Data object
    if self.is_periodicity_t is not None:
        is_periodicity_t = self.is_periodicity_t

    is_periodicity_t, is_antiper_t = Time.get_periodicity()
    time = Time.get_values(
        is_oneperiod=is_periodicity_t,
        is_antiperiod=is_antiper_t and is_periodicity_t,
    )

    # Load magnetic flux B and H of size (Nt_tot, nb_elem, dim) and mu (Nt_tot, nb_elem)
    resultB = B_sol.field.get_xyz_along(
        "indice",
        "time=axis_data",
        axis_data={"time": time},
    )
    indice = resultB["indice"]  # Store elements indices
    Bx = resultB["comp_x"]
    By = resultB["comp_y"]
    B = np.stack((Bx, By), axis=2)

    resultH = H_sol.field.get_xyz_along(
        "indice",
        "time=axis_data",
        axis_data={"time": time},
    )
    Hx = resultH["comp_x"]
    Hy = resultH["comp_y"]
    H = np.stack((Hx, Hy), axis=2)

    resultmu = mu_sol.field.get_along(
        "indice",
        "time=axis_data",
        axis_data={"time": time},
    )
    mu = resultmu["\\mu"]

    # Move time axis at the end for clarity purpose
    B = np.moveaxis(B, 0, -1)
    H = np.moveaxis(H, 0, -1)
    mu = np.moveaxis(mu, 0, -1)

    # For every type of element (now only Triangle3, TO BE extended)
    for key in mesh.cell:

        # mesh.cell[key].interpolation = Interpolation()
        # mesh.cell[key].interpolation.init_key(key=key, nb_gauss=1)

        nb_node_per_cell = mesh.cell[key].nb_node_per_cell  # Number of nodes per element
        connect = mesh.cell[key].get_connectivity()  # Each row of connect is an element
        nb_elem = len(connect)

        nb_node = mesh.node.nb_node  # Total nodes number

        # Nodal forces init
        f = np.zeros((nb_node, dim, Nt_tot), dtype=np.float)

        # ref_cell = mesh.cell[key].interpolation.ref_cell // pas besoin d'interpoler car tout est cst

        # Gauss nodes
        # pts_gauss, poidsGauss, nb_gauss = mesh.cell[
        #     key
        # ].interpolation.gauss_point.get_gauss_points()

        # indice_elem = mesh.cell[key].indice

        # Loop on element (elt)
        for e, e_ind in enumerate(indice):
            node_indices = connect[e, :]  # elt nodes indices
            vertice = mesh.get_vertice(e_ind)[key]  # elt nodes coordonates
            # elt physical fields values
            Be = B[e, :, :]
            He = H[e, :, :]
            mue = mu[e, :]

            Me = np.reshape(
                Be / mue - He, (dim, 1, Nt_tot)
            )  # reshaped for matrix product purpose
            # elt magnetostrictive tensor
            tme = self.comp_magnetrosctrictive_tensor(mue, Me, Nt_tot)

            # Triangle orientation, needed for normal orientation. 1 if trigo oriented, -1 otherwise
            orientation_sign = np.sign(
                np.cross(vertice[1] - vertice[0], vertice[2] - vertice[0])
            )

            # Loop on edges
            for n in range(nb_node_per_cell):

                # Get current node + next node indices (both needed since pression will be computed on edges because of Green Ostrogradski)
                inode = node_indices[n % nb_node_per_cell]
                next_inode = node_indices[(n + 1) % nb_node_per_cell]

                # Edge cooordonates
                edge_vector = (
                    vertice[(n + 1) % nb_node_per_cell] - vertice[n % nb_node_per_cell]
                )  # coordonées du vecteur nn+1

                # Volume ratio (Green Ostrogradski), with a conventional 1/2 for a share between 2 nodes
                L = np.linalg.norm(edge_vector)
                Ve0 = L / 2

                # Normalized normal vector n, that has to node outside the element (i.e. normal ^ edge same sign as the orientation)
                normal_to_edge_unoriented = (
                    np.array((edge_vector[1], -edge_vector[0])) / L
                )
                normal_to_edge = (
                    normal_to_edge_unoriented
                    * np.sign(np.cross(normal_to_edge_unoriented, edge_vector))
                    * orientation_sign
                )
                normal_to_edge.reshape(dim, 1)

                # Green Ostrogradski <normal, tensor> scalar product
                edge_force = np.tensordot(
                    normal_to_edge, tme, [[0], [0]]
                )  # [[0],[0]] means sum product over rows for normal (which is vertical) and over rows for tme

                # Total edge force contribution, to be added to the 2 nodes that made the edge
                fe = Ve0 * edge_force
                f[inode, :, :] = f[inode, :, :] + fe
                f[next_inode, :, :] = f[next_inode, :, :] + fe

    indices_nodes = np.sort(np.unique(connect))
    Indices_Point = Data1D(name="indice", values=indices_nodes, is_components=True)

    # Time axis goes back to first axis
    f = np.moveaxis(f, -1, 0)

    components = {}

    fx_data = DataTime(
        name="Nodal force (x)",
        unit="N",
        symbol="Fx",
        axes=[Time, Indices_Point],
        values=f[..., 0],
    )
    components["comp_x"] = fx_data

    fy_data = DataTime(
        name="Nodal force (y)",
        unit="N",
        symbol="Fy",
        axes=[Time, Indices_Point],
        values=f[..., 1],
    )
    components["comp_y"] = fy_data

    vec_force = VectorField(name="Nodal forces", symbol="F", components=components)
    solforce = SolutionVector(field=vec_force, type_cell="node", label="F")
    meshsolution.solution.append(solforce)

    out_dict = dict()
    out_dict["meshsolution"] = meshsolution

    return out_dict
