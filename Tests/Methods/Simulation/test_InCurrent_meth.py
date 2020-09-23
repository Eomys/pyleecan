# -*- coding: utf-8 -*-
from os import chdir

chdir("../../..")

from os.path import join
from unittest import TestCase

from ddt import data, ddt
from numpy import array, linspace, ones, pi, sqrt, transpose, zeros
from numpy.testing import assert_array_almost_equal

from pyleecan.Classes.ImportGenMatrixSin import ImportGenMatrixSin
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportGenVectSin import ImportGenVectSin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.Output import Output
from pyleecan.Classes.Simulation import Simulation
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load
from pyleecan.Methods.Simulation.Input import InputError

IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))
InputCurrent_Error_test = list()
time_wrong = ImportMatrixVal(value=zeros((10, 2)))
time = ImportGenVectLin(0, 10, 100)

angle_wrong = ImportMatrixVal(value=zeros((10, 4)))
angle = ImportGenVectLin(0, 2 * pi, 1024)

I_1 = ImportMatrixVal(value=zeros((100, 3)))
I_2 = ImportMatrixVal(value=zeros((100, 2)))
I_3 = ImportMatrixVal(value=zeros((2, 100)))
I_4 = ImportMatrixVal(value=zeros((100)))

angle_rotor_wrong = ImportMatrixVal(value=zeros((10, 2)))
angle_rotor_wrong2 = ImportMatrixVal(value=zeros((102)))
angle_rotor = ImportMatrixVal(value=zeros((100)))

# Quick fix added by Cedric 30/07/20 Nr -> N0
N0_wrong = 1
N0_wrong2 = 1
N0 = 1

# Winding stator only
M1 = MachineDFIM()
M1.stator = LamSlotWind()
M1.stator.winding.qs = 3
M1.rotor.winding = None
# Winding rotor only
M2 = MachineDFIM()
M2.rotor = LamSlotWind()
M2.rotor.winding.qs = 2
M2.stator.winding = None
# Winding rotor + stator
M3 = MachineDFIM()
M3.stator = LamSlotWind()
M3.stator.winding.qs = 3
M3.rotor = LamSlotWind()
M3.rotor.winding.qs = 2


# Wrong time
test_obj = Simulation(machine=IPMSM_A)
test_obj.input = InputCurrent(time=None)
InputCurrent_Error_test.append(
    {"test_obj": test_obj, "exp": "ERROR: InputCurrent.time missing"}
)
# Wong time shape
test_obj = Simulation(machine=IPMSM_A)
test_obj.input = InputCurrent(time=time_wrong)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.time should be a vector, (10, 2) shape found",
    }
)
# Wrong angle shape
test_obj = Simulation(machine=IPMSM_A)
test_obj.input = InputCurrent(time=time, angle=angle_wrong)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.angle should be a vector, (10, 4) shape found",
    }
)
# Missing Is
test_obj = Simulation(machine=M1)
test_obj.input = InputCurrent(time=time, angle=angle, Is=None)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.Is, InputCurrent.Id_ref, and InputCurrent.Iq_ref missing",
    }
)
# Is wrong shape
test_obj = Simulation(machine=M1)
test_obj.input = InputCurrent(time=time, angle=angle, Is=I_3)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.Is must be a matrix with the shape (100, 3) (len(time), stator phase number), (2, 100) returned",
    }
)
test_obj = Simulation(machine=M1)
test_obj.input = InputCurrent(time=time, angle=angle, Is=I_4)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.Is must be a matrix with the shape (100, 3) (len(time), stator phase number), (100,) returned",
    }
)
# Wrong Ir
test_obj = Simulation(machine=M2)
test_obj.input = InputCurrent(time=time, angle=angle, Ir=None)
InputCurrent_Error_test.append(
    {"test_obj": test_obj, "exp": "ERROR: InputCurrent.Ir missing"}
)
test_obj = Simulation(machine=M2)
test_obj.input = InputCurrent(time=time, angle=angle, Ir=I_3)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.Ir must be a matrix with the shape (100, 2) (len(time), rotor phase number), (2, 100) returned",
    }
)
test_obj = Simulation(machine=M2)
test_obj.input = InputCurrent(time=time, angle=angle, Ir=I_4)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.Ir must be a matrix with the shape (100, 2) (len(time), rotor phase number), (100,) returned",
    }
)
# Wrong N0, alpha_rotor
test_obj = Simulation(machine=M3)
test_obj.input = InputCurrent(
    time=time, angle=angle, Is=I_1, Ir=I_2, angle_rotor=None, N0=None
)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.angle_rotor and InputCurrent.N0 can't be None at the same time",
    }
)
test_obj = Simulation(machine=M3)
test_obj.input = InputCurrent(
    time=time, angle=angle, Is=I_1, Ir=I_2, angle_rotor=angle_rotor_wrong, N0=None
)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.angle_rotor should be a vector of the same length as time, (10, 2) shape found, (100,) expected",
    }
)
test_obj = Simulation(machine=M3)
test_obj.input = InputCurrent(
    time=time, angle=angle, Is=I_1, Ir=I_2, angle_rotor=angle_rotor_wrong2, N0=None
)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.angle_rotor should be a vector of the same length as time, (102,) shape found, (100,) expected",
    }
)


@ddt
class unittest_InputCurrent_meth(TestCase):
    """unittest for InputCurrent object methods"""

    @data(*InputCurrent_Error_test)
    def test_InputCurrent_Error_test(self, test_dict):
        """Check that the input current raises the correct errors"""
        output = Output(simu=test_dict["test_obj"])
        with self.assertRaises(
            InputError, msg="Expect: " + test_dict["exp"]
        ) as context:
            output.simu.input.gen_input()
        self.assertEqual(test_dict["exp"], str(context.exception))

    def test_InputCurrent_Ok(self):
        """Check that the input current can return a correct output"""
        test_obj = Simulation(machine=M3)
        output = Output(simu=test_obj)
        time = ImportGenVectLin(0, 1, 16)
        angle = ImportGenVectLin(0, 2 * pi, 20)
        Is = ImportGenMatrixSin(is_transpose=True)
        Is.init_vector(f=[2, 2, 2], A=[2, 2, 2], Phi=[pi / 2, 0, -pi / 2], N=16, Tf=1)
        S = sqrt(2)
        Is_exp = array(
            [
                [2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S, -2, -S, 0, S],
                [0, S, 2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S, -2, -S],
                [-2, -S, 0, S, 2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S],
            ]
        )

        Ir = ImportGenMatrixSin(is_transpose=True)
        Ir.init_vector(f=[2, 2], A=[2, 2], Phi=[0, -pi / 2], N=16, Tf=1)
        Ir_exp = array(
            [
                [0, S, 2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S, -2, -S],
                [-2, -S, 0, S, 2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S],
            ]
        )

        angle_rotor = ImportGenVectLin(0, 2 * pi, 16)
        N0 = 10
        test_obj.input = InputCurrent(
            time=time, angle=angle, Is=Is, Ir=Ir, angle_rotor=angle_rotor, N0=N0
        )

        test_obj.input.gen_input()
        assert_array_almost_equal(output.elec.time, linspace(0, 1, 16))
        assert_array_almost_equal(output.elec.angle, linspace(0, 2 * pi, 20))
        assert_array_almost_equal(output.elec.Is.values, Is_exp)
        assert_array_almost_equal(output.elec.Ir.values, Ir_exp)
        assert_array_almost_equal(output.elec.angle_rotor, linspace(0, 2 * pi, 16))
        assert_array_almost_equal(output.elec.N0, ones(16) * 10)

    def test_InputCurrent_DQ(self):
        """Check that the input current can return a correct output"""
        test_obj = Simulation(machine=IPMSM_A)
        output = Output(simu=test_obj)
        time = ImportGenVectLin(0, 1, 7)
        angle = ImportGenVectLin(0, 2 * pi, 20)
        Id_ref = 2
        Iq_ref = 0

        Is_exp = array(
            [
                [2, 1, -1, -2, -1, 1, 2],
                [-1, -2, -1, 1, 2, 1, -1],
                [-1, 1, 2, 1, -1, -2, -1],
            ]
        )

        zp = IPMSM_A.stator.get_pole_pair_number()
        angle_rotor_initial = IPMSM_A.comp_angle_offset_initial()
        angle_rotor_exp = linspace(0, 2 * pi / zp, 7) + angle_rotor_initial

        N0 = 60 / zp
        test_obj.input = InputCurrent(
            time=time,
            angle=angle,
            Is=None,
            Iq_ref=Iq_ref,
            Id_ref=Id_ref,
            Ir=None,
            angle_rotor=None,
            N0=N0,
            angle_rotor_initial=angle_rotor_initial,
            rot_dir=1,
        )

        test_obj.input.gen_input()
        assert_array_almost_equal(output.elec.time, linspace(0, 1, 7))
        assert_array_almost_equal(output.elec.angle, linspace(0, 2 * pi, 20))
        assert_array_almost_equal(output.elec.get_Is().values, Is_exp)
        assert_array_almost_equal(output.get_angle_rotor(), angle_rotor_exp)
        assert_array_almost_equal(output.elec.N0, ones(7) * 60 / zp)

    def test_InputCurrent_I0Phi0(self):
        """Check that the input current can return a correct output"""
        test_obj = Simulation(machine=IPMSM_A)
        output = Output(simu=test_obj)
        time = ImportGenVectLin(0, 1, 7)
        angle = ImportGenVectLin(0, 2 * pi, 20)
        Id_ref = 2
        Iq_ref = 0

        Is_exp = transpose(
            array(
                [
                    [2, 1, -1, -2, -1, 1, 2],
                    [-1, -2, -1, 1, 2, 1, -1],
                    [-1, 1, 2, 1, -1, -2, -1],
                ]
            )
        )
        Is = ImportMatrixVal(value=Is_exp)

        zp = IPMSM_A.stator.get_pole_pair_number()
        angle_rotor_initial = IPMSM_A.comp_angle_offset_initial()
        angle_rotor_exp = linspace(0, 2 * pi / zp, 7) + angle_rotor_initial

        N0 = 60 / zp

        test_obj.input = InputCurrent(
            time=time,
            angle=angle,
            Is=Is,
            Ir=None,
            angle_rotor=None,
            angle_rotor_initial=angle_rotor_initial,
            N0=N0,
            rot_dir=1,
        )

        test_obj.input.gen_input()
        assert_array_almost_equal(output.elec.time, linspace(0, 1, 7))
        assert_array_almost_equal(output.elec.angle, linspace(0, 2 * pi, 20))
        assert_array_almost_equal(output.get_angle_rotor(), angle_rotor_exp)
        assert_array_almost_equal(output.elec.Id_ref, Id_ref)
        assert_array_almost_equal(output.elec.Iq_ref, Iq_ref)
        assert_array_almost_equal(output.elec.N0, ones(7) * 60 / zp)
