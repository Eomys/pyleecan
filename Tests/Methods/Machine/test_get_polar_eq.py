# -*- coding: utf-8 -*-
from os.path import join
from unittest import TestCase

import matplotlib.pyplot as plt
from numpy import pi

from ....Tests.Validation.Machine.SCIM_001 import SCIM_001
from ....Tests import save_plot_path as save_path


class test_get_polar_eq(TestCase):
    """unittest to convert machine to polar and plot them
    """

    def test_get_polar_eq_SCIM(self):
        """Test that you can create polar equivalent of SCIM machine
        """
        polar_eq = SCIM_001.get_polar_eq()

        plt.close("all")
        SCIM_001.plot(comp_machine=polar_eq)

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_get_polar_eq_SCIM_001.png"))
        self.assertEqual(len(fig.axes[0].patches), 275)
