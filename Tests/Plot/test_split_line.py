from os.path import join
from unittest import TestCase

import matplotlib.pyplot as plt
from numpy import pi
from pyleecan.Classes.Circle import Circle
from Tests import save_plot_path as save_path


class test_split_line(TestCase):
    """unittest for splitting surface with lines
    """

    def test_splitting_circle(self):
        """Test cutting a circle
        """

        # Ref circle
        circle = Circle(radius=1, center=0, point_ref=0)
        # Cut the circle in half
        cut = circle.split_line(Z1=0, Z2=1, is_top=True, is_join=True)
        # Cut the result
        cut2 = cut.split_line(Z1=1j, Z2=1, is_top=True, is_join=True)
        # Reverse second cut side
        cut3 = cut.split_line(Z1=1j, Z2=1, is_top=False, is_join=True)

        # Plot the result
        plt.close("all")
        cut.plot(color="r", edgecolor="r")
        fig = plt.gcf()
        cut2.plot(fig=fig, color="g", edgecolor="g", is_disp_point_ref=True)
        circle.plot(fig=fig, color=(0, 0, 0, 0), edgecolor="k", linestyle="--")
        fig.savefig(join(save_path, "test_split_circle_1.png"))

        plt.close("all")
        cut.plot(color="r", edgecolor="r")
        fig = plt.gcf()
        cut3.plot(fig=fig, color="g", edgecolor="g", is_disp_point_ref=True)
        circle.plot(fig=fig, color=(0, 0, 0, 0), edgecolor="k", linestyle="--")
        fig.savefig(join(save_path, "test_split_circle_2.png"))
