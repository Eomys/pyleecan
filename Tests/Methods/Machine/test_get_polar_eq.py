# -*- coding: utf-8 -*-
from os.path import join
import pytest

import matplotlib.pyplot as plt
from numpy import pi

from Tests import save_plot_path as save_path
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


class Test_get_polar_eq(object):
    """unittest to convert machine to polar and plot them"""

    def test_get_polar_eq_SCIM(self):
        """Test that you can create polar equivalent of SCIM machine"""
        SCIM_001 = load(join(DATA_DIR, "Machine", "Railway_Traction.json"))
        polar_eq = SCIM_001.get_polar_eq()

        plt.close("all")
        SCIM_001.plot(comp_machine=polar_eq, is_show_fig=False)

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_get_polar_eq_SCIM_001.png"))
        assert len(fig.axes[0].patches) == 227


if __name__ == "__main__":
    a = Test_get_polar_eq()
    a.test_get_polar_eq_SCIM()
