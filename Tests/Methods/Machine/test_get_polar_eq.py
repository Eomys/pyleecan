# -*- coding: utf-8 -*-
"""
@date Created on Wed Jan 13 17:33:49 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""
from os.path import join
from unittest import TestCase

import matplotlib.pyplot as plt
from numpy import pi

from pyleecan.Tests.Validation.Machine.SCIM_001 import SCIM_001
from pyleecan.Tests import save_plot_path as save_path


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
        self.assertEqual(len(fig.axes[0].patches), 217)
