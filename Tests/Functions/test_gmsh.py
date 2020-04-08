# -*- coding: utf-8 -*-

from os import remove, getcwd
from os.path import isfile, join
from unittest import TestCase

try:
    from pyleecan.Functions.GMSH.gen_3D_mesh import gen_3D_mesh
except:
    gen_3D_mesh = None

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Tests import save_validation_path as save_path


class test_gmsh(TestCase):
    """unittest for gmsh 3d mesh"""

    def test_slot_10(self):
        """Check that you can generate the 3D mesh of Slot 10
        """
        if gen_3D_mesh == None:
            raise Exception("Fail to import gen_3D_mesh (gmsh package missing)")

        # SetUp
        stator = LamSlotWind(
            Rint=0.1325,
            Rext=0.2,
            Nrvd=0,
            L1=0.35,
            Kf1=0.95,
            is_internal=False,
            is_stator=True,
        )

        stator.slot = SlotW10(
            Zs=36, H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3
        )
        gen_3D_mesh(
            lamination=stator,
            save_path=join(save_path, "Lamination.msh"),
            mesh_size=5e-3,
            Nlayer=20,
            display=False,
        )
