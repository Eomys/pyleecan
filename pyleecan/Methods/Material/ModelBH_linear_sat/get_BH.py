# -*- coding: utf-8 -*-
import numpy as np

def get_BH(self):
    """
    Return the B(H) curve of the material according to Langevin model.

    Parameters
    ----------
    self : ModelBH
        a ModelBH object

    Returns
    -------
    BH: numpy.ndarray
        B(H) values (two colums matrix: H and B(H))

    """

    H0 = 1
    Bmax = self.Bmax
    if self.Bs is not None and self.mu_a is not None:
        if Bmax is not None:
            delta = self.delta
            Hmax = H0
            iteration = 0
            new_B = 0
            while new_B < Bmax and iteration < 1000:
                Hmax += delta
                iteration += 1
                new_B = self.BH_func(Hmax, self.Bs, self.mu_a)
        else:
            Hmax = self.Hmax
        
        if Hmax is not None:
            H = np.linspace(H0, Hmax, 200)
            B = self.BH_func(H, self.Bs, self.mu_a)

            BH = np.zeros((len(H), 2))
            BH[:, 0] = H
            BH[:, 1] = B

            return BH
