from os.path import join
from pyleecan.Generator import MAIN_DIR

import numpy as np
import os

def comp_force_nodal(self, output):
    """Run the nodal forces calculation based on Virtual Work Principle (VWP) with vectorized calculations.

    Parameters
    ----------
    self : SimuImportMag
        A SimuImportMag object

    output : Output
        an Output object (to update)

    """
    # Internal inits
    #path_save = join(MAIN_DIR, "Results", "Femm", "Mesh") + '\\'

    poidsGauss = 1 / 2
    mu_0 = 4*np.pi*1e-7
    nodalforces = dict()
    fxfy = dict()

    # External inputs
    Nt_tot = output.mag.Nt_tot  # Number of time step
    mesh = output.mag.mesh # Mesh dictionary
    Rsbo = output.simu.machine.stator.get_Rbo()

    for ii in range(1):
        # Load FEA mesh nodes and connectivity
        listNd = mesh[ii].node
        listElem = mesh[ii].element # Triangles
        # indice_stator = mesh[ii].submeshe["stator"]
        NbNd = mesh[ii].nb_node
        NbElem = mesh[ii].nb_elem

        # Define radius of nodes
        xx = listNd[:, 0]
        yy = listNd[:, 1]
        r_nodes = np.sqrt(xx*xx + yy*yy)
        r_nodes = np.reshape(r_nodes, (NbNd, 1))

        # Load magnetic FEA solution data
        Bx = mesh[ii].solution["Bx"]
        By = mesh[ii].solution["By"]
        Hx = mesh[ii].solution["Hx"]
        Hy = mesh[ii].solution["Hy"]
        mu = mesh[ii].solution["mu"]

        # Nodal forces init*
        fx = np.zeros((NbNd, 1), dtype = np.float)
        fy = np.zeros((NbNd, 1))
        mu_node = np.zeros((NbNd, 1))

        # Jacob init
        #jacob = np.zeros((NbElem, 1))
        detJ = np.zeros((NbElem, 1))
        Ve0 = np.zeros((NbElem, 1))

        # Gradient of linear triangle (to be generalized)
        T = np.array([[-1, 1, 0], [-1, 0, 1]])

        for ie in range(NbElem):

            # Coordinates of the element nodes
            coordElement = listNd[listElem[ie, 0:3], 0:2]

            # Calculation of the elements jacobian
            #jacob[ie] = np.dot(T, coordElement)
            jacob = np.dot(T, coordElement)
            detJ[ie] = np.linalg.det(jacob)

            # Volume of the triangle (to be generalized)
            Ve0[ie] = detJ[ie] * poidsGauss

            # Compute the co-energy
            # Ie = range(NbElem) # Elements might be filtered later
            B = [Bx[ie], By[ie]]
            H = [Hx[ie], Hy[ie]]
            # M = B/mu[ie] - H

            coee = 0.5*np.dot(B, H) # - np.dot(B,M)  # Linear co-energy

            # Loop on nodes
            for n in range(3):

                inode = listElem[ie, n]
                if mu_node[inode] == 0:
                    mu_node[inode] = mu[ie]
                else:
                    if mu_node[inode] != mu[ie]:
                        mu_node[inode] = -2

                # Force toward X-axis on n-th node
                direction = np.zeros((3, 2))
                direction[n, :] = [1, 0]

                derivee_Jx = np.dot(T, direction)
                mata = np.c_[derivee_Jx[:,0], jacob[:,1]]
                matb = np.c_[jacob[:,0], derivee_Jx[:,1]]
                derivee_detJx = np.linalg.det(mata) + np.linalg.det(matb)

                coee_part = coee*derivee_detJx/detJ[ie,0]
                gap_part = np.dot(-np.transpose(B), np.dot(np.linalg.inv(jacob), np.dot(derivee_Jx, H)))

                # Nodal force
                fxe = Ve0[ie,0]*(gap_part + coee_part)
                fx[inode] = fx[inode] + fxe

                # Force toward X-axis on n-th node
                direction = np.zeros((3, 2))
                direction[n, :] = [0, 1]

                derivee_Jy = np.dot(T, direction)
                mata = np.c_[derivee_Jy[:,0], jacob[:,1]]
                matb = np.c_[jacob[:,0], derivee_Jy[:,1]]
                derivee_detJy = np.linalg.det(mata) + np.linalg.det(matb)

                coee_part = coee*derivee_detJy/detJ[ie,0]
                gap_part = np.dot(-np.transpose(B), np.dot(np.linalg.inv(jacob), np.dot(derivee_Jy, H)))

                fye = Ve0[ie,0]*(gap_part + coee_part)
                fy[inode] = fy[inode] + fye

        # nodes_stator = listElem[indice_stator,:]
        Iforces = np.logical_and(abs(mu_node) > 1.06, r_nodes > Rsbo*0.997)
        row_mask = Iforces.all(axis=1)
        fxfy["posf"] = listNd[row_mask, :]
        fx_red = fx[row_mask]
        fy_red = fy[row_mask]
        fxfy["fx"] = fx_red
        fxfy["fy"] = fy[row_mask]
        nodalforces[ii] = fxfy

        if self.is_save_force:

            path_save = join(MAIN_DIR, "Results", self.parent.parent.name, "NodalForce") + '\\'

            if not os.path.exists(path_save):
                os.makedirs(path_save)

            mat_fxfy = np.zeros([len(fx[row_mask]), 4], dtype=np.float)
            mat_fxfy[:,0] = fx_red[:,0]
            mat_fxfy[:,1] = fy_red[:,0]
            mat_fxfy[:,2] = listNd[row_mask, 0]
            mat_fxfy[:, 3] = listNd[row_mask, 1]
            # saving:
            np.savetxt(path_save + 'Nodalforces_' + str(ii) + '.dat', mat_fxfy, header="fx fy posx posy")

    output.struct.nodal_forces = nodalforces