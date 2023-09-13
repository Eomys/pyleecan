import numpy as np


def comp_magnetostrictive_tensor(
    self,
    M,
    Nt_tot,
    polynomial_coeffs=[[0.719, -0.078, -0.042], [-0.391, 0.114, 0.004]],
):
    """Compute magnetostrictive tensor.

    From publications: L. Vandevelde, J. Gyselinck, M. A. C. De Wulf and J. A. A. Melkebeek, "Finite-element computation of the deformation of ferromagnetic material taking into account magnetic forces and magnetostriction," in IEEE Transactions on Magnetics, vol. 40, no. 2, pp. 565-568, March 2004, doi: 10.1109/TMAG.2004.824540.

    Parameters
    ----------

    M : array
        Magnetization vector in the elements, field, material, ...

    Nt_tot: scalar
        Number of time steps

    polynomial_coeffs : 2x3 List, optional
        alpha(i,j) coeffs for polynomal expression of alpha1 and alpha2


    Return
    ----------
    magnetostric_tensor : dim * dim * Nt_tot array
        magnetrostictive tensor in the current element for differents time steps


    """
    # Coeffs from a reference material in IEEETranMagn2004
    a10 = polynomial_coeffs[0][0]
    a12 = polynomial_coeffs[0][1]
    a14 = polynomial_coeffs[0][2]
    a20 = polynomial_coeffs[1][0]
    a22 = polynomial_coeffs[1][1]
    a24 = polynomial_coeffs[1][2]

    mu_0 = 4 * np.pi * 1e-7

    M_norm = np.linalg.norm(M, axis=(0, 1))  # M matrices are in the first two axes
    mu_times_Mnorm_squared = np.multiply(mu_0, M_norm) ** 2

    alpha1 = a10 + a12 * mu_times_Mnorm_squared + a14 * mu_times_Mnorm_squared ** 2
    alpha2 = a20 + a22 * mu_times_Mnorm_squared + a24 * mu_times_Mnorm_squared ** 2

    magnetostric_tensor = np.zeros((2, 2, Nt_tot))

    # Iteration over time step
    for ti in range(Nt_tot):
        M_times_M = np.dot(M[:, :, ti], np.transpose(M[:, :, ti]))

        M_norm_squared = np.linalg.norm(M[:, :, ti]) ** 2
        I = np.eye(2, 2)

        first_member = -alpha1[ti] * mu_0 * M_times_M
        second_member = -alpha2[ti] * mu_0 * M_norm_squared * I

        magnetostric_tensor[:, :, ti] = first_member + second_member

    return magnetostric_tensor
