from numpy import pi, all as np_all



def comp_force(self, output, axes_dict):
    """Compute the air-gap surface force based on Maxwell Tensor (MT).

    Parameters
    ----------
    self : ForceMT
        A ForceMT object
    output : Output
        an Output object (to update)
    axes_dict: {Data}
        Dict of axes used for force calculation

    Returns
    -------
    out_dict: dict
        Dict containing the following quantities:
            AGSF_r : ndarray
                Airgap radial Maxwell stress (Nt,Na,Nz) [N/m²]
            AGSF_t : ndarray
                Airgap tangential Maxwell stress (Nt,Na,Nz) [N/m²]
            AGSF_z : ndarray
                Airgap axial Maxwell stress (Nt,Na,Nz) [N/m²]

    """

    # Test comp_force_nodal #

    self.comp_force_nodal(output, axes_dict)

    pass
