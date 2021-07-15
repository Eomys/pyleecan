# -*- coding: utf-8 -*-

# import pytest
from os.path import join

from pyleecan.Classes.FrameBar import FrameBar
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from numpy import pi

machine = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
# ipmsm = load(join(DATA_DIR, "Machine", "IPMSM_B.json"))

bar_mat = load(join(DATA_DIR, "Material", "Steel1.json"))
frame_mat = load(join(DATA_DIR, "Material", "Steel1.json"))
frame = FrameBar(
    Nbar=9, wbar=0.01, Lfra=0.12, Rint=0.140, Rext=0.145, mat_type=frame_mat
)
machine.frame = frame
# surf_list = frame.build_geometry_bar()

gap_height = frame.comp_height_gap() * 1000
print(f"Gap Height: {gap_height} mm")
bar_area = frame.comp_surface_bar() * 1e6
print(f"Bar Surface Area: {bar_area} mm^2")
gap_area = frame.comp_surface_gap() * 1e6
print(f"Gap Surface Area: {gap_area} mm^2")
# frame.plot()
machine.plot()
print("Test complete")

# # For AlmostEqual
# DELTA = 1e-4
