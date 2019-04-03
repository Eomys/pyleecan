# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


def plot_B_space(self, j_t0=0):
    """Plot the airgap flux as a function of space

    Parameters
    ----------
    self : Output
        an Output object
    """

    plt.plot(self.mag.angle, self.mag.Br[j_t0, :])
    plt.show()
