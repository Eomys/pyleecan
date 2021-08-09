# -*- coding: utf-8 -*-

import pytest
from os.path import join

from pyleecan.Classes.FrameBar import FrameBar
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from Tests import save_plot_path as save_path

# Add FrameBar to machine template
machine = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
frame_mat = load(join(DATA_DIR, "Material", "Steel1.json"))
frame = FrameBar(
    Nbar=9, wbar=0.01, Lfra=0.12, Rint=0.140, Rext=0.145, mat_type=frame_mat
)
machine.frame = frame

# # For AlmostEqual
DELTA = 1e-4


def test_comp_height_gap():
    """Test computation of gap height of FrameBar"""
    gap_height = frame.comp_height_gap() * 1000
    assert gap_height == pytest.approx(5.38)


def test_comp_surface_bar():
    """Test computation of bar surface area of FrameBar"""
    bar_area = frame.comp_surface_bar() * 1e6
    assert bar_area == pytest.approx(493.989, rel=DELTA)


def test_comp_surface_gap():
    """Test computation of gap surface area of FrameBar"""
    gap_area = frame.comp_surface_gap() * 1e6
    assert gap_area == pytest.approx(3982.7805, rel=DELTA)


def test_comp_surface():
    """Test computation of total frame surface area of FrameBar"""
    frame_area = frame.comp_surface() * 1e6
    assert frame_area == pytest.approx(4970.7585, rel=DELTA)


def test_build_geometry():
    """Test creation of geometry of of FrameBar"""
    machine.plot(is_show_fig=False, save_path=join(save_path, "test_FrameBar.png"))


if __name__ == "__main__":
    test_comp_height_gap()
    test_comp_surface_bar()
    test_comp_surface_gap()
    test_comp_surface()
    test_build_geometry()
