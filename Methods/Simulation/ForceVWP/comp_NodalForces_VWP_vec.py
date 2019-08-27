import numpy as np


def my_det(jacob):
    """ Compute jacobian determinant for vectorized problem

    :param jacob:
    :return:
    """
    det = jacob[:, 0, 0]*jacob[:, 1, 1] - jacob[:, 1, 0]*jacob[:, 0, 1]
    return det


def my_solve2D(Y1,Y2, detJ):
    """ Solve  Jacob0 * X = Y
    :param Y1:
    :param Y2: 
    :return: 
    """
    X = np.concatenate((my_det(Y1)/detJ, my_det(Y2)/detJ))
    return X

def get_coee_gap_part(direction, NbElem, jacob, coee, detJ, B, H, T):
    """ Compute the coenergy and permeability gap contributions to nodal forces

    :param direction:
    :param NbElem:
    :param jacob:
    :param coee:
    :param detJ:
    :param B:
    :param H:
    :return:
    """
    #direction = np.repeat(direction, [1, 1, NbElem, 2])
    direction = np.repeat(direction[:, :, np.newaxis], NbElem, axis=2)
    direction = np.repeat(direction[:, :, :, np.newaxis], 2, axis=3)
    direction = np.transpose(direction, [2, 0, 1, 3])

    # Corresponding Jacobian's derivatives
    derivee_J = np.transpose(np.squeeze(np.sum(T*direction, axis=1)), [0, 2, 1])

    Mata = np.zeros((NbElem, 2, 2))
    Mata[:, :, 0] = derivee_J[:, :, 0]
    Mata[:, :, 1] = jacob[:, :, 1]

    Matb = np.zeros((NbElem, 2, 2))
    Matb[:, :, 0] = jacob[:, :, 0]
    Matb[:, :, 1] = derivee_J[:, :, 1]

    derivee_detJ = my_det(Mata) + my_det(Matb)
    coee_part = coee*derivee_detJ/detJ

    dJ_H = np.squeeze(np.sum(np.transpose(derivee_J, [0, 2, 1])*np.repeat(H[:,:,np.newaxis], 2, axis=2), axis = 1))
    Mata[:, :, 0] = dJ_H
    Matb[:, :, 1] = dJ_H
    jac_dJ_H = np.reshape(my_solve2D(Mata, Matb, detJ), [NbElem, 2])
    gap_part = -np.sum(B*jac_dJ_H, axis=1)

    return coee_part, gap_part


def comp_NodalForces_VWP(self, output):
    """Run the nodal forces calculation based on Virtual Work Principle (VWP) with vectorized calculations.

    Parameters
    ----------
    self : SimuImportMag
        A SimuImportMag object

    output : Output
        an Output object (to update)

    """
    # Internal inits
    poidsGauss = 1 / 2
    mu_0 = 4*np.pi*1e-7
    nodalforces = dict()
    fxfy = dict()

    # External inputs
    Nt_tot = output.mag.Nt_tot  # Number of time step
    mesh = output.mag.FEMM_Mesh # Mesh dictionary

    for ii in range(Nt_tot):
        # Load FEA mesh nodes and connectivity
        listNd = mesh[ii].nodes
        listElem = mesh[ii].elements[0].connectivity # Triangles
        NbNd = len(listNd)
        NbElem = len(listElem)

        # Load magnetic FEA solution data
        Bx = mesh[ii].elements[0].solution_dict["Bx"]
        By = mesh[ii].elements[0].solution_dict["By"]
        Hx = mesh[ii].elements[0].solution_dict["Hx"]
        Hy = mesh[ii].elements[0].solution_dict["Hy"]
        mu = mesh[ii].elements[0].solution_dict["mu"]

        # Nodal forces init
        fx = np.zeros((NbNd, 1))
        fxe = np.zeros((NbElem, 1))
        fy = np.zeros((NbNd, 1))
        fye = np.zeros((NbElem, 3))

        # Gradient of linear triangle (to be generalized)
        T = np.array([[-1, 1, 0], [-1, 0, 1]])
        T = np.repeat(T[:, :, np.newaxis], NbElem, axis=2)
        T = np.repeat(T[:, :, :, np.newaxis], 2, axis=3)
        T = np.transpose(T, [2, 1, 0, 3])
        T = np.transpose(T, [0, 1, 3, 2])

        # Coordinates of the element nodes
        coordElement = listNd[listElem[:, 0:3], 0:2]
        coordElement = np.repeat(coordElement[:, :, :, np.newaxis], 2, axis=3)

        # Calculation of the elements jacobian
        jacob = np.transpose((np.sum(T*coordElement, axis=1)), [0, 2, 1])
        detJ = my_det(jacob)

        # Volume of the triangle (to be generalized)
        Ve0 = detJ * poidsGauss

        # Compute the co-energy
        #Ie = range(NbElem) # Elements might be filtered later
        B = np.c_[Bx, By]
        H = np.c_[Hx, Hy]
        coee = 0.5*np.sum(B*H, axis=1) # Linear co-energy

        #Loop on nodes
        for n in range(3):

            # Force toward X-axis on n-th node
            direction = np.zeros((3, 2))
            direction[n, :] = [1, 0]

            # VWP terms calculation
            [coee_part, gap_part] = get_coee_gap_part(direction, NbElem, jacob, coee, detJ, B, H, T)

            # Nodal force
            fxe = Ve0*(gap_part + coee_part)
            fxn = np.bincount(listElem[:, n], weights=fxe, minlength=NbNd)
            #fxn = [fxn, np.zeros((NbNd - len(fxn), 1))]
            fx = fx + np.reshape(fxn, (NbNd, 1))

            # Force toward X-axis on n-th node
            direction = np.zeros((3, 2))
            direction[n, :] = [0, 1]

            # VWP terms calculation
            [coee_part, gap_part] = get_coee_gap_part(direction, NbElem, jacob, coee, detJ, B, H, T)

            fye = Ve0*(gap_part + coee_part)
            fyn = np.bincount(listElem[:, n], weights=fye, minlength=NbNd)
            #fyn = [fyn, np.zeros((NbNd-len(fyn), 1))]
            fy = fy + np.reshape(fyn, (NbNd, 1))

        fxfy["fx"] = fx
        fxfy["fy"] = fy
        fxfy["posf"] = listNd
        nodalforces[ii] = fxfy

    output.forces.nodal_forces = nodalforces

