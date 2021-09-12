from os import remove, getcwd
from os.path import isfile, join
import pytest

try:
    from pyleecan.Functions.GMSH.gen_3D_mesh import gen_3D_mesh
except:
    gen_3D_mesh = ImportError

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW10 import SlotW10
from Tests import save_validation_path as save_path


@pytest.mark.GMSH
@pytest.mark.long_5s
def test_slot_10():
    """Check generation of the 3D mesh of Slot 10 with gmsh"""
    if isinstance(gen_3D_mesh, ImportError):
        raise ImportError("Fail to import gen_3D_mesh (gmsh package missing)")

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
