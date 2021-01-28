# -*- coding: utf-8 -*-
from os.path import join
from numpy import pi
import pytest
from Tests import save_path, TEST_DATA_DIR
from pyleecan.definitions import DATA_DIR

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.StructElmer import StructElmer
from pyleecan.Classes.Output import Output
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Functions.load import load


# get the machine
machine_1 = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))

# mesh settings, original line label names have to be used (not the translated)
n1 = 3
n2 = 20

mesh_dict_1 = {
    "Magnet_0_Top": n2,
    "Magnet_0_Bottom": n2,
    "Magnet_0_Left": n1,
    "Magnet_0_Right": n1,
    "Magnet_1_Top": n2,
    "Magnet_1_Bottom": n2,
    "Magnet_1_Left": n1,
    "Magnet_1_Right": n1,
    "Hole_0_Top": 0,
    "Hole_0_Left": n1,
    "Hole_0_Right": n1,
    "Hole_1_Top": 0,
    "Hole_1_Left": n1,
    "Tangential_Bridge": 40,
    "Radial_Bridge": 40,
    "ROTOR_BORE_CURVE": 100,
    "Lamination_Rotor_Bore_Radius_Ext": 100,
}


@pytest.mark.long
@pytest.mark.StructElmer
# @pytest.mark.DEV
class Test_StructElmer(object):
    """Test some basic workflow of StructElmer simulations"""

    def test_HoleM50(self):
        """Test StructElmer simulation with 2 magnets on HoleM50 rotor"""

        # copy the machine
        machine = machine_1.copy()

        # some modifications to geometry
        machine.rotor.hole[0].W2 = 1.0e-3

        # setup the simulation
        simu = Simu1(name="HoleM50_2_magnets", machine=machine)
        output = Output(simu=simu)
        output.path_result = save_path

        simu.struct = StructElmer()
        simu.struct.FEA_dict_enforced = mesh_dict_1
        simu.struct.is_get_mesh = True

        # set rotor speed and run simulation
        simu.input.N0 = 10000  # rpm
        simu.run()

        return output

    def test_HoleM50_no_magnets(self):
        """Test StructElmer simulation without magnets on HoleM50 rotor"""

        # get the machine
        machine = machine_1.copy()

        # some modifications to geometry
        machine.rotor.hole[0].W2 = 1.0e-3
        # machine.rotor.hole[0].H2 = 0.0e-3
        # machine.rotor.hole[0].W1 = 1.0e-3

        # setup the simulation
        simu = Simu1(name="HoleM50_no_magnets", machine=machine)
        output = Output(simu=simu)

        simu.struct = StructElmer()
        simu.struct.FEA_dict_enforced = mesh_dict_1
        simu.struct.include_magnets = False
        simu.struct.is_get_mesh = True

        # set rotor speed and run simulation
        simu.input.N0 = 10000  # rpm
        simu.run()

        return output

    def test_disk_geometry(self):
        """Test StructElmer simulation with disc geometry (i.e. slotless rotor)"""
        # TODO compare to analytical values

        # setup new machine and copy stator props of ref. machine
        machine = MachineSIPMSM()
        machine.stator = machine_1.stator.copy()
        machine.rotor = LamSlotMag()
        machine.rotor.magnet = None

        machine.rotor.Rint = machine_1.rotor.Rint
        machine.rotor.Rext = machine_1.rotor.Rext
        machine.rotor.mat_type = machine_1.rotor.mat_type.copy()

        machine.rotor.slot = SlotM11(H0=0, W0=pi / 16)
        machine.rotor.slot.Zs = 8
        machine.rotor.is_stator = False

        # setup the simulation
        simu = Simu1(name="Disc", machine=machine)
        output = Output(simu=simu)

        simu.struct = StructElmer()
        # simu.struct.FEA_dict_enforced = mesh_dict_1
        simu.struct.include_magnets = False
        simu.struct.is_get_mesh = True

        # set rotor speed and run simulation
        simu.input.N0 = 10000  # rpm
        simu.run()

        return output


# To run it without pytest
if __name__ == "__main__":
    # create test object
    obj = Test_StructElmer()
    # test IPMSM_A (HoleM50-Rotor) with minor modification
    out = obj.test_HoleM50()
    # out = obj.test_HoleM50_wo_magnets()

    # test centrifugal force on a disc
    # out = obj.test_disk_geometry()

    # plot some results
    out.struct.meshsolution.plot_deflection(label="disp", factor=20)
    # out.struct.meshsolution.plot_contour(label='disp')
    # out.struct.meshsolution.plot_mesh()
