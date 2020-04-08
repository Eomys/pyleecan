# -*- coding: utf-8 -*-

from unittest import TestCase

from ddt import data, ddt
from numpy import linspace, ones, pi, zeros, array, sqrt, transpose
from numpy.testing import assert_array_almost_equal

from ....Classes.ImportGenMatrixSin import ImportGenMatrixSin
from ....Classes.ImportGenVectLin import ImportGenVectLin
from ....Classes.ImportGenVectSin import ImportGenVectSin
from ....Classes.ImportMatrixVal import ImportMatrixVal
from ....Classes.InputCurrentDQ import InputCurrentDQ
from ....Classes.LamSlotWind import LamSlotWind
from ....Classes.MachineIPMSM import MachineIPMSM
from ....Classes.MachineDFIM import MachineDFIM
from ....Classes.Simulation import Simulation
from ....Classes.Output import Output
from ....Classes.WindingDW1L import WindingDW1L
from ....Methods.Simulation.Input import InputError

InputCurrentDQ_Error_test = list()
time_wrong = ImportMatrixVal(value=zeros((10, 2)))
time = ImportGenVectLin(0, 10, 100)

angle_wrong = ImportMatrixVal(value=zeros((10, 4)))
angle = ImportGenVectLin(0, 2 * pi, 1024)

I_1 = ImportMatrixVal(value=zeros((100, 2)))
I_2 = ImportMatrixVal(value=zeros((100, 3)))
I_3 = ImportMatrixVal(value=zeros((2, 100)))
I_4 = ImportMatrixVal(value=zeros((100)))

angle_rotor_wrong = ImportMatrixVal(value=zeros((10, 2)))
angle_rotor_wrong2 = ImportMatrixVal(value=zeros((102)))
angle_rotor = ImportMatrixVal(value=zeros((100)))

Nr_wrong = ImportMatrixVal(value=zeros((10, 2)))
Nr_wrong2 = ImportMatrixVal(value=zeros((102)))
Nr = ImportMatrixVal(value=zeros((100)))

# Winding stator only
M1 = MachineIPMSM()
M1.stator = LamSlotWind()
M1.stator.winding = WindingDW1L()
M1.stator.winding.qs = 3

# Machine without 'comp_initial_angle' method
M2 = MachineDFIM()
M2.stator = LamSlotWind()
M2.stator.winding.qs = 3
M2.rotor.winding = None


# Wrong time
test_obj = Simulation()
test_obj.input = InputCurrentDQ(time=None)
InputCurrentDQ_Error_test.append(
    {"test_obj": test_obj, "exp": "ERROR: InputCurrentDQ.time missing"}
)
test_obj = Simulation()
test_obj.input = InputCurrentDQ(time=time_wrong)
InputCurrentDQ_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrentDQ.time should be a vector, (10, 2) shape found",
    }
)
# Wrong angle
test_obj = Simulation()
test_obj.input = InputCurrentDQ(time=time, angle=None)
InputCurrentDQ_Error_test.append(
    {"test_obj": test_obj, "exp": "ERROR: InputCurrentDQ.angle missing"}
)
test_obj = Simulation()
test_obj.input = InputCurrentDQ(time=time, angle=angle_wrong)
InputCurrentDQ_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrentDQ.angle should be a vector, (10, 4) shape found",
    }
)
# Wrong Is
test_obj = Simulation(machine=M1)
test_obj.input = InputCurrentDQ(time=time, angle=angle, Is=None)
InputCurrentDQ_Error_test.append(
    {"test_obj": test_obj, "exp": "ERROR: InputCurrentDQ.Is missing"}
)
test_obj = Simulation(machine=M1)
test_obj.input = InputCurrentDQ(time=time, angle=angle, Is=I_3)
InputCurrentDQ_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrentDQ.Is must be a matrix with the shape (100, 2) (len(time), stator phase number), (2, 100) returned",
    }
)
test_obj = Simulation(machine=M1)
test_obj.input = InputCurrentDQ(time=time, angle=angle, Is=I_4)
InputCurrentDQ_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrentDQ.Is must be a matrix with the shape (100, 2) (len(time), stator phase number), (100,) returned",
    }
)
# 'comp_initial_angle' method not implemented
test_obj = Simulation(machine=M2)
test_obj.input = InputCurrentDQ(time=time, angle=angle, Is=I_1)
InputCurrentDQ_Error_test.append(
    {"test_obj": test_obj, "exp": "ERROR: 'comp_initial_angle' method not implemented"}
)

# Wrong Nr, alpha_rotor
test_obj = Simulation(machine=M1)
test_obj.input = InputCurrentDQ(
    time=time, angle=angle, Is=I_1, Ir=None, angle_rotor=None, Nr=None
)
InputCurrentDQ_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrentDQ.angle_rotor and InputCurrentDQ.Nr can't be None at the same time",
    }
)
test_obj = Simulation(machine=M1)
test_obj.input = InputCurrentDQ(
    time=time, angle=angle, Is=I_1, Ir=None, angle_rotor=angle_rotor_wrong, Nr=None
)
InputCurrentDQ_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrentDQ.angle_rotor should be a vector of the same length as time, (10, 2) shape found, (100,) expected",
    }
)
test_obj = Simulation(machine=M1)
test_obj.input = InputCurrentDQ(
    time=time, angle=angle, Is=I_1, Ir=None, angle_rotor=angle_rotor_wrong2, Nr=None
)
InputCurrentDQ_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrentDQ.angle_rotor should be a vector of the same length as time, (102,) shape found, (100,) expected",
    }
)
test_obj = Simulation(machine=M1)
test_obj.input = InputCurrentDQ(
    time=time, angle=angle, Is=I_1, Ir=None, angle_rotor=angle_rotor, Nr=Nr_wrong
)
InputCurrentDQ_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrentDQ.Nr should be a vector of the same length as time, (10, 2) shape found, (100,) expected",
    }
)
test_obj = Simulation(machine=M1)
test_obj.input = InputCurrentDQ(
    time=time, angle=angle, Is=I_1, Ir=None, angle_rotor=angle_rotor, Nr=Nr_wrong2
)
InputCurrentDQ_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrentDQ.Nr should be a vector of the same length as time, (102,) shape found, (100,) expected",
    }
)


@ddt
class unittest_InputCurrentDQ_meth(TestCase):
    """unittest for InputCurrentDQ object methods"""

    @data(*InputCurrentDQ_Error_test)
    def test_InputCurrentDQ_Error_test(self, test_dict):
        """Check that the input current raises the correct errors
        """
        output = Output(simu=test_dict["test_obj"])
        with self.assertRaises(
            InputError, msg="Expect: " + test_dict["exp"]
        ) as context:
            output.simu.input.gen_input()
        self.assertEqual(test_dict["exp"], str(context.exception))

    def test_InputCurrentDQ_Ok(self):
        """Check that the input current can return a correct output
        """
        test_obj = Simulation(machine=M1)
        output = Output(simu=test_obj)
        time = ImportGenVectLin(0, 1, 7)
        angle = ImportGenVectLin(0, 2 * pi, 20)
        Is = ImportMatrixVal(
            value=transpose(array([[2, 2, 2, 2, 2, 2, 2], [0, 0, 0, 0, 0, 0, 0]]))
        )

        Is_exp = transpose(
            array(
                [
                    [2, 1, -1, -2, -1, 1, 2],
                    [-1, 1, 2, 1, -1, -2, -1],
                    [-1, -2, -1, 1, 2, 1, -1],
                ]
            )
        )

        zp = M1.stator.get_pole_pair_number()
        angle_rotor_initial = M1.comp_initial_angle()
        angle_rotor_exp = linspace(0, 2 * pi / zp, 7) + angle_rotor_initial

        Nr = ImportMatrixVal(value=ones(7) * 60 / zp)
        test_obj.input = InputCurrentDQ(
            time=time,
            angle=angle,
            Is=Is,
            Ir=None,
            angle_rotor=None,
            Nr=Nr,
            angle_rotor_initial=angle_rotor_initial,
            rot_dir=1,
        )

        test_obj.input.gen_input()
        assert_array_almost_equal(output.elec.time, linspace(0, 1, 7))
        assert_array_almost_equal(output.elec.angle, linspace(0, 2 * pi, 20))
        assert_array_almost_equal(output.elec.Is, Is_exp)
        assert_array_almost_equal(output.elec.angle_rotor, angle_rotor_exp)
        assert_array_almost_equal(output.elec.Nr, ones(7) * 60 / zp)
