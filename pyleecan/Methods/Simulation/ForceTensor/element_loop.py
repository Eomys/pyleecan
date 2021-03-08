import numpy as np


def element_loop(self, mesh, B, H, mu, indice, dim, Nt_tot, polynomial_coeffs=[[0.719, -0.078, -0.042], [-0.391, 0.114, 0.004]]):
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

        # ref_cell = mesh.cell[key].interpolation.ref_cell // pas besoin d'interpoler car tout est cst

        # Gauss nodes
        # pts_gauss, poidsGauss, nb_gauss = mesh.cell[
        #     key
        # ].interpolation.gauss_point.get_gauss_points()

        # indice_elem = mesh.cell[key].indice

        # Loop on element (elt)
        for e, e_ind in enumerate(indice):
            node_indices = mesh_cell_key.get_connectivity(e_ind)  # elt nodes indices
            vertice = mesh.get_vertice(e_ind)[key]  # elt nodes coordonates
            # elt physical fields values
            Be = B[e, :, :]
            He = H[e, :, :]
            mue = mu[e, :]

            Me = np.reshape(
                Be / mue - He, (dim, 1, Nt_tot)
            )  # reshaped for matrix product purpose
            # elt magnetostrictive tensor
            tme = self.comp_magnetrosctrictive_tensor(mue, Me, Nt_tot,polynomial_coeffs)

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

                # Green Ostrogradski <normal, tensor> scalar product
                edge_force = np.tensordot(
                    normal_to_edge, tme, [[0], [0]]
                )  # [[0],[0]] means sum product over rows for normal (which is vertical) and over rows for tme

                # Total edge force contribution, to be added to the 2 nodes that made the edge
                fe = Ve0 * edge_force
                f[inode, :, :] = f[inode, :, :] + fe
                f[next_inode, :, :] = f[next_inode, :, :] + fe

    return f, connect
