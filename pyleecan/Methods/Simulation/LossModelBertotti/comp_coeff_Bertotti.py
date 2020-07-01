# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

from ....Methods.Simulation.LossModel import LossModelError

# define loss calculation function
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
    """
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
        return

    data = mat.mag.LossData.get_data()
    f = data[:, 1]
    B = data[:, 0]
    Loss = data[:, 2]

    # fit the data
    _comp_err = lambda Cx: (_comp_loss(self, C, Cx, f, B) - Loss) / (f) # TODO:
    C0 = np.ones([n_est])  # initial values for the parameters
    result = optimize.least_squares(_comp_err, C0[:], method="lm")

    C1 = result.x
    success = result.success
    message = result.message

    if success is None:
        raise LossModelError("ERROR: LossModel parameter fitting failed.")

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

    if False:
        print()

        L_ = _comp_loss(self, C, None, f, B)
        E = _comp_err(None)

        for x1, x2, x3, x4, x5 in zip(
            f, B, Loss, np.round(L_, 2), np.round(Loss - L_, 2)
        ):
            print([x1, x2, x3, x4, x5])

        print()
        print(C)
        print(success)
        print(message)
        print()
