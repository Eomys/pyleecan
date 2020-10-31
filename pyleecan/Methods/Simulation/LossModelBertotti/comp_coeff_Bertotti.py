# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

from ....Methods.Simulation.LossModel import LossModelError

# TODO define one loss calculation function to use everywhere in class
def _comp_loss(self, C, Cx, f, B):
    f_norm = f / self.F_REF
    B_norm = B / self.B_REF

    ii = 0
    _C = list(C)
    for idx, c in enumerate(_C):
        if c is None:
            _C[idx] = Cx[ii]
            ii += 1

    loss = (
        _C[0] * f_norm * B_norm ** _C[1]
        + _C[2] * (f_norm * B_norm) ** _C[3]
        + _C[4] * (f_norm * B_norm) ** _C[5]
    )

    return loss


def comp_coeff_Bertotti(self, mat):
    """
    Compute the missing (i.e. None-valued) Bertotti loss coefficients from the
    Material object data by data fitting.

    Parameters
    ----------
    self : LossModelBertotti
        A LossModelBertotti object

    mat : Material
        A Material object

    Return
    ------
    success : bool
        Return 'True' if parameter fitting was successful.

    """
    # Get logger
    logger = self.get_logger()

    # store loss model parameter
    C = []
    C.append(self.k_hy)
    C.append(self.alpha_hy)
    C.append(self.k_ed)
    C.append(self.alpha_ed)
    C.append(self.k_ex)
    C.append(self.alpha_ex)

    # check if parameters have to been estimated
    n_est = sum(x is None for x in C)
    if n_est == 0:
        return True

    data = mat.mag.LossData.get_data()
    f = data[:, 1]
    B = data[:, 0]
    Loss = data[:, 2]

    # fit the data
    # TODO Which normalization to use? 1/f or should it be user defined?
    _comp_err = lambda Cx: (_comp_loss(self, C, Cx, f, B) - Loss) / (f)
    C0 = np.ones([n_est])  # initial values for the parameters
    result = optimize.least_squares(_comp_err, C0[:], method="lm")

    C1 = result.x
    success = result.success

    if success is None:
        logger.info(f"'{self.name}' LossModel: Parameter fitting failed.")
        return False
    else:
        ii = 0
        for idx, c in enumerate(C):
            if c is None:
                C[idx] = C1[ii]
                ii += 1

        # set the estimated fitting parameters
        self.k_hy = C[0]
        self.alpha_hy = C[1]
        self.k_ed = C[2]
        self.alpha_ed = C[3]
        self.k_ex = C[4]
        self.alpha_ex = C[5]

        logger.debug(f"'{self.name}' LossModel: Parameters estimated coefficiants:")
        logger.debug(C)

        return True
