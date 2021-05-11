import numpy as np
import matplotlib.pyplot as plt
import csv


def element_loop(
    self,
    mesh,
    B,
    H,
    mu,
    indice,
    dim,
    Nt_tot,
    polynomial_coeffs=[[0.719, -0.078, -0.042], [-0.391, 0.114, 0.004]],
):
    """compute nodal forces with a loop on elements and nodes

    from publications:


    Parameters
    ----------
    self : ForceTensor
        A ForceTensor object

    mesh :
        A Mesh object




    polynomial_coeffs : 2x3 List, optional
        alpha(i,j) coeffs for polynomal expression of alpha1 and alpha2

    Return
    ----------
    f : (nb_nodes*dim*Nt_tot) array
        nodal forces

    connect : (nb_element*nb_node_per_cell) array
        table of mesh connectivity

    """

    # For every type of element (now only Triangle3, TO BE extended)
    for key in mesh.cell:

        # mesh.cell[key].interpolation = Interpolation()
        # mesh.cell[key].interpolation.init_key(key=key, nb_gauss=1)

        nb_node_per_cell = mesh.cell[
            key
        ].nb_node_per_cell  # Number of nodes per element

        mesh_cell_key = mesh.cell[key]
        connect = mesh.cell[key].get_connectivity()  # Each row of connect is an element

        nb_elem = len(connect)

        nb_node = mesh.node.nb_node  # Total nodes number

        # Nodal forces init
        f = np.zeros((nb_node, dim, Nt_tot), dtype=np.float)

        node_indice_set = set(())
        node_number_set = set(())
        nodes_x = []
        nodes_y = []

        # ref_cell = mesh.cell[key].interpolation.ref_cell // pas besoin d'interpoler car tout est cst

        # Gauss nodes
        # pts_gauss, poidsGauss, nb_gauss = mesh.cell[
        #     key
        # ].interpolation.gauss_point.get_gauss_points()

        # indice_elem = mesh.cell[key].indice

        # Loop on element (elt)
        for elt_indice, elt_number in enumerate(indice):

            node_number = mesh_cell_key.get_connectivity(
                elt_number
            )  # elt nodes numbers, can differ from indices
            vertice = mesh.get_vertice(elt_number)[key]  # elt nodes coordonates

            node_to_find = 1935

            if (
                node_number[0] == node_to_find
                or node_number[1] == node_to_find
                or node_number[2] == node_to_find
            ):
                print(node_number)
                print(vertice)

            # elt physical fields values
            Be = B[elt_indice, :, :]
            He = H[elt_indice, :, :]
            mue = mu[elt_indice, :]

            Me = np.reshape(
                Be / mue - He, (dim, 1, Nt_tot)
            )  # reshaped for matrix product purpose
            # elt magnetostrictive tensor
            tme = self.comp_magnetostrictive_tensor(mue, Me, Nt_tot, polynomial_coeffs)

            # Triangle orientation, needed for normal orientation. 1 if trigo oriented, -1 otherwise
            orientation_sign = np.sign(
                np.cross(vertice[1] - vertice[0], vertice[2] - vertice[0])
            )

            # Loop on edges
            for n in range(nb_node_per_cell):

                # Get current node + next node indices (both needed since pression will be computed on edges because of Green Ostrogradski)
                node_indice = np.where(mesh.node.indice == node_number[n])[0][0]

                next_node_indice = np.where(
                    mesh.node.indice == node_number[(n + 1) % nb_node_per_cell]
                )[0][0]

                if not (node_indice in node_indice_set):

                    node_indice_set.add(node_indice)
                    node_number_set.add(node_number[n])
                    nodes_x.append(vertice[n][0])
                    nodes_y.append(vertice[n][1])

                # Edge cooordonates
                edge_vector = (
                    vertice[(n + 1) % nb_node_per_cell] - vertice[n % nb_node_per_cell]
                )  # coordonées du vecteur nn+1

                # Volume ratio (Green Ostrogradski)
                L = np.linalg.norm(edge_vector)
                Ve0 = L / 2

                # Normalized normal vector n, that has to be directed outside the element (i.e. normal ^ edge same sign as the orientation)
                normal_to_edge_unoriented = (
                    np.array((edge_vector[1], -edge_vector[0])) / L
                )
                normal_to_edge = (
                    normal_to_edge_unoriented
                    * np.sign(np.cross(normal_to_edge_unoriented, edge_vector))
                    * orientation_sign
                )
                normal_to_edge.reshape(dim, 1)

                # Green Ostrogradski <tensor, normal> scalar product
                edge_force = np.tensordot(
                    tme, normal_to_edge, [[1], [0]]
                )  # [[1],[0]] means sum product over rows for normal (which is vertical) and over rows for tme

                # Total edge force contribution, to be added to the 2 nodes that made the edge
                fe = -Ve0 * edge_force / 2
                f[node_indice, :, :] = f[node_indice, :, :] + fe
                f[next_node_indice, :, :] = f[next_node_indice, :, :] + fe

    # plt.plot(nodes_x,nodes_y,'og',markersize=1)

    path = "C:/Users/Utilisateur/Desktop/Jean-Guillaume/magneto/Benchmark_model_stator_ms.csv"

    nodes_x2 = []
    nodes_y2 = []
    f2 = np.zeros((nb_node, dim))
    with open(path, "r") as file:
        reader = csv.reader(file, skipinitialspace=True)
        next(reader)
        next(reader)
        next(reader)
        for row in reader:

            nodes_x2.append(float(row[1]) / 1000)
            nodes_y2.append(float(row[2]) / 1000)
            f2[int(row[0])][0] = float(row[3])
            f2[int(row[0])][1] = float(row[4])

    # plt.plot(nodes_x2,nodes_y2,'or',markersize=1)
    score_x = np.abs(f.reshape(nb_node, dim)[:, 0] - f2[:, 0]) / np.abs(f2[:, 0])
    score_y = np.abs(f.reshape(nb_node, dim)[:, 1] - f2[:, 1]) / np.abs(f2[:, 1])
    plt.plot(list(node_indice_set), score_x, "o")
    plt.xlabel("node")
    plt.ylabel("relative err to f2")
    plt.title("fx-fx2 / fx2, Ve0 = L/2")
    # plt.ylim([-1,10])
    plt.show()

    return f, connect
