from numpy import ones, pi, array, linspace, zeros
from os.path import join
import pytest

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.PostPlot import PostPlot
from pyleecan.Classes.PostFunction import PostFunction
from pyleecan.Classes.Output import Output
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


@pytest.mark.MagFEMM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_compare():
    """Test the compare method"""
    # Create reference object
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    simu = Simu1(name="test_compare", machine=Toyota_Prius)

    # Initialization of the simulation starting point
    simu.input = InputCurrent()
    # Set time and space discretization
    simu.input.time = ImportMatrixVal(
        value=linspace(start=0, stop=0.015, num=4, endpoint=True)
    )
    simu.input.Na_tot = 1024

    # Definition of the enforced output of the electrical module
    simu.input.Is = ImportMatrixVal(
        value=array(  # Stator currents as a function of time
            [
                [6.97244193e-06, 2.25353053e02, -2.25353060e02],
                [-2.60215295e02, 1.30107654e02, 1.30107642e02],
                [-6.97244208e-06, -2.25353053e02, 2.25353060e02],
                [2.60215295e02, -1.30107654e02, -1.30107642e02],
            ]
        )
    )
    simu.input.Ir = None  # SPMSM machine => no rotor currents to define
    simu.input.N0 = 3000  # Rotor speed [rpm]
    simu.input.angle_rotor_initial = 0.5216 + pi  # Rotor position at t=0 [rad]

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(type_BH_stator=2, type_BH_rotor=2, is_periodicity_a=False)
    simu.force = None
    simu.struct = None
    simu.postproc_list = [
        PostPlot(param_list=[1, 2], param_dict={"test": 2}),
        PostFunction(run="lambda out: out.elec.N0"),
    ]

    # Create the differences
    simu2 = simu.copy()
    simu2.machine.stator.L1 = 2  # float
    simu2.machine.rotor.hole[0].magnet_0.mat_type.name = "Test "  # str
    simu2.input.Nt_tot = 1234  # int
    simu2.mag.is_periodicity_a = True  # bool
    # complex
    simu2.input.Is = zeros((4, 2))
    # list(ndarray)
    # dict(ndarray)
    simu2.mag.transform_list = ["bla"]  # len(list)
    simu2.postproc_list[0].param_list = [1, 3]  # list diff
    simu2.postproc_list[0].param_dict["test2"] = 3  # len(dict)
    simu2.postproc_list[1].run = "lambda out: out.elec.Id_ref"  # function
    # dict diff
    simu2.machine.stator.winding = WindingUD()  # pyleecan type diff
    # pyleecan dict
    # SciDataTool list
    # SciDataTool dict

    # Compare
    diff_list = simu.compare(simu2, "simu")
    assert "simu.machine.stator.L1" in diff_list
    assert "simu.machine.rotor.hole[0].magnet_0.mat_type.name" in diff_list
    assert "simu.input.Nt_tot" in diff_list
    assert "simu.mag.is_periodicity_a" in diff_list
    assert "simu.mag.transform_list" in diff_list
    assert "simu.postproc_list[0].param_list" in diff_list
    assert "simu.postproc_list[0].param_dict" in diff_list
    assert "type(simu.machine.stator.winding)" in diff_list
    assert "simu.input.Is.value" in diff_list
    assert "simu.postproc_list[1].run" in diff_list
    assert len(diff_list) == 10


if __name__ == "__main__":
    test_compare()
