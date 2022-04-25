import pytest
from pyleecan.Classes.MachineUD import MachineUD
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.Segment import Segment
from Tests import save_plot_path as save_path
from os.path import join, isdir, isfile
from os import makedirs, remove
from numpy import exp, pi
import matplotlib.pyplot as plt
from pyleecan.Functions.init_fig import init_fig
from pyleecan.Functions.Plot import (
    ARROW_WIDTH,
    SC_FONT_SIZE,
)

ARROW_COLOR = "r"
SCHEMATICS_PATH = join(save_path, "Schematics")

if not isdir(SCHEMATICS_PATH):
    makedirs(SCHEMATICS_PATH)


class Test_plot_dimensions(object):
    def test_Shaft_Rotor_Stator(self):
        """Slot Schematics"""
        file_name = "Dimension_Shaft_Rotor_Stator.png"
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Machine definition
        frame = Frame(Rint=0.8, Rext=1)
        stator = Lamination(
            Rint=0.6, Rext=frame.Rint, is_stator=True, is_internal=False
        )
        airgap = 0.1
        rotor = Lamination(
            Rint=0.2, Rext=stator.Rint - airgap, is_stator=False, is_internal=True
        )
        lam_list = [rotor, stator]
        shaft = Shaft(Drsh=rotor.Rint * 2)
        test_obj = MachineUD(frame=frame, lam_list=lam_list, shaft=shaft)
        # Plot
        (fig, ax, _, _) = init_fig(shape="default")
        test_obj.plot(
            fig=fig,
            ax=ax,
            is_show_fig=False,
            save_path=None,
        )
        # Figure clean up
        W = frame.Rext * 1.1
        fig = plt.gcf()
        ax = plt.gca()
        plt.axis("equal")
        ax.set_xlim(-W / 10, W)
        ax.set_ylim(-W / 10, W)
        ax.set_title("")
        ax.set_axis_off()
        # Add Schematics
        line = Segment(0, rotor.Rint * exp(1j * pi / 4 * 3))
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Rotor.Rint",
            offset_label=(-1.7 + 1j) * W / 10,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        line = Segment(0, rotor.Rext * exp(1j * pi / 6))
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Rotor.Rext",
            offset_label=(1 - 0.1j) * W / 10,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        line = Segment(0, stator.Rint * exp(1j * 2 * pi / 6))
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Stator.Rint",
            offset_label=(1 + 1j) * W / 10,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        line = Segment(0, stator.Rext * exp(1j * pi / 2))
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Stator.Rext",
            offset_label=(0.5 + 2j) * W / 10,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        line = Segment(rotor.Rext, stator.Rint)
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Airgap",
            offset_label=-1j * W / 15,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        line = Segment(frame.Rext, frame.Rint)
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Wfra",
            offset_label=-1j * W / 15,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        line = Segment(rotor.Rint, -rotor.Rint)
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Drsh",
            offset_label=-1j * W / 15,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        # Save Results
        fig.savefig(file_path)
        plt.close()

    def test_Rotor_Stator(self):
        """Slot Schematics"""
        file_name = "Dimension_Rotor_Stator.png"
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Machine definition
        frame = Frame(Rint=0.8, Rext=1)
        stator = Lamination(
            Rint=0.6, Rext=frame.Rint, is_stator=True, is_internal=False
        )
        airgap = 0.1
        rotor = Lamination(
            Rint=0, Rext=stator.Rint - airgap, is_stator=False, is_internal=True
        )
        lam_list = [rotor, stator]
        test_obj = MachineUD(frame=frame, lam_list=lam_list)
        # Plot
        (fig, ax, _, _) = init_fig(shape="default")
        test_obj.plot(
            fig=fig,
            ax=ax,
            is_show_fig=False,
            save_path=None,
        )
        # Figure clean up
        W = frame.Rext * 1.1
        fig = plt.gcf()
        ax = plt.gca()
        plt.axis("equal")
        ax.set_xlim(-W / 10, W)
        ax.set_ylim(-W / 10, W)
        ax.set_title("")
        ax.set_axis_off()
        # Add Schematics
        line = Segment(0, rotor.Rext * exp(1j * pi / 6))
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Rotor.Rext",
            offset_label=(1 - 0.1j) * W / 10,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        line = Segment(0, stator.Rint * exp(1j * 2 * pi / 6))
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Stator.Rint",
            offset_label=(1 + 1j) * W / 10,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        line = Segment(0, stator.Rext * exp(1j * pi / 2))
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Stator.Rext",
            offset_label=(0.5 + 2j) * W / 10,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        line = Segment(rotor.Rext, stator.Rint)
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Airgap",
            offset_label=-1j * W / 15,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        line = Segment(frame.Rext, frame.Rint)
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Wfra",
            offset_label=-1j * W / 15,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        # Save Results
        fig.savefig(file_path)
        plt.close()

    def test_Stator_Rotor(self):
        """Slot Schematics"""
        file_name = "Dimension_Stator_Rotor.png"
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Machine definition
        rotor = Lamination(Rint=0.6, Rext=1, is_stator=False, is_internal=False)
        airgap = 0.1
        stator = Lamination(
            Rint=0, Rext=rotor.Rint - airgap, is_stator=True, is_internal=True
        )
        lam_list = [rotor, stator]
        test_obj = MachineUD(lam_list=lam_list)
        # Plot
        (fig, ax, _, _) = init_fig(shape="default")
        test_obj.plot(
            fig=fig,
            ax=ax,
            is_show_fig=False,
            save_path=None,
        )
        # Figure clean up
        W = rotor.Rext * 1.1
        fig = plt.gcf()
        ax = plt.gca()
        plt.axis("equal")
        ax.set_xlim(-W / 10, W)
        ax.set_ylim(-W / 10, W)
        ax.set_title("")
        ax.set_axis_off()
        # Add Schematics
        line = Segment(0, rotor.Rext * exp(1j * pi / 2))
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Rotor.Rext",
            offset_label=(0.5 + 2j) * W / 10,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        line = Segment(0, rotor.Rint * exp(1j * 2 * pi / 6))
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Rotor.Rint",
            offset_label=(1 + 1j) * W / 10,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        line = Segment(0, stator.Rext * exp(1j * pi / 6))
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Stator.Rext",
            offset_label=(1 - 0.1j) * W / 10,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        line = Segment(rotor.Rint, stator.Rext)
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="Airgap",
            offset_label=-1j * W / 15,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        # Save Results
        fig.savefig(file_path)
        plt.close()

    def test_plot_SCR_schematics(self):
        """Generate the schematics for Short Circuit Ring"""
        file_name = "ShortCircuitRing_schematics.png"
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Plot schematics
        test_obj = LamSquirrelCage()
        test_obj.plot_schematics_scr(
            is_default=True, is_show_fig=False, save_path=file_path
        )


if __name__ == "__main__":
    a = Test_plot_dimensions()
    a.test_plot_SCR_schematics()
    print("Done")
