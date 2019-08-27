#import numpy as np


def comp_force(self, output):
    """Run the air-gap surface force (AGSF) calculation based on Maxwell Tensor (MT).

    Parameters
    ----------
    self : SimuImportMag
        A SimuImportMag object

    output : Output
        an Output object (to update)

    """

