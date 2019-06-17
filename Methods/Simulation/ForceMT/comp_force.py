import numpy as np


def comp_force(self, output):
    """Compute the air-gap surface force based on Maxwell Tensor (MT).

    Parameters
    ----------
    self : ForceMT
        A ForceMT object

    output : Output
        an Output object (to update)
    """

    mu_0 = 4 * np.pi * 1e-7

    # Load magnetic flux
    Br = output.mag.Br
    Bt = output.mag.Bt

    # Compute AGSF with MT formula
    Prad = (Br * Br - Bt * Bt) / (2 * mu_0)
    Ptan = Br * Bt / mu_0

    # Store the results
    output.struct.Prad = Prad
    output.struct.Ptan = Ptan
