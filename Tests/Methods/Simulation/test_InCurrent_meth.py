# -*- coding: utf-8 -*-

from numpy import linspace, ones, pi, zeros, array, sqrt, transpose
from numpy.testing import assert_array_almost_equal

from pyleecan.Classes.ImportGenMatrixSin import ImportGenMatrixSin
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportGenVectSin import ImportGenVectSin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.Simulation import Simulation
from pyleecan.Classes.Output import Output
from pyleecan.Methods.Simulation.Input import InputError
import pytest

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

Nr_wrong = ImportMatrixVal(value=zeros((10, 2)))
Nr_wrong2 = ImportMatrixVal(value=zeros((102)))
Nr = ImportMatrixVal(value=zeros((100)))

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
test_obj = Simulation()
test_obj.input = InputCurrent(time=None)
InputCurrent_Error_test.append(
    {"test_obj": test_obj, "exp": "ERROR: InputCurrent.time missing"}
)
test_obj = Simulation()
test_obj.input = InputCurrent(time=time_wrong)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.time should be a vector, (10, 2) shape found",
    }
)
# Wrong angle
test_obj = Simulation()
test_obj.input = InputCurrent(time=time, angle=None)
InputCurrent_Error_test.append(
    {"test_obj": test_obj, "exp": "ERROR: InputCurrent.angle missing"}
)
test_obj = Simulation()
test_obj.input = InputCurrent(time=time, angle=angle_wrong)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.angle should be a vector, (10, 4) shape found",
    }
)
# Wrong Is
test_obj = Simulation(machine=M1)
test_obj.input = InputCurrent(time=time, angle=angle, Is=None)
InputCurrent_Error_test.append(
    {"test_obj": test_obj, "exp": "ERROR: InputCurrent.Is missing"}
)
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
# Wrong Nr, alpha_rotor
test_obj = Simulation(machine=M3)
test_obj.input = InputCurrent(
    time=time, angle=angle, Is=I_1, Ir=I_2, angle_rotor=None, Nr=None
)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.angle_rotor and InputCurrent.Nr can't be None at the same time",
    }
)
test_obj = Simulation(machine=M3)
test_obj.input = InputCurrent(
    time=time, angle=angle, Is=I_1, Ir=I_2, angle_rotor=angle_rotor_wrong, Nr=None
)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.angle_rotor should be a vector of the same length as time, (10, 2) shape found, (100,) expected",
    }
)
test_obj = Simulation(machine=M3)
test_obj.input = InputCurrent(
    time=time, angle=angle, Is=I_1, Ir=I_2, angle_rotor=angle_rotor_wrong2, Nr=None
)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.angle_rotor should be a vector of the same length as time, (102,) shape found, (100,) expected",
    }
)
test_obj = Simulation(machine=M3)
test_obj.input = InputCurrent(
    time=time, angle=angle, Is=I_1, Ir=I_2, angle_rotor=angle_rotor, Nr=Nr_wrong
)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.Nr should be a vector of the same length as time, (10, 2) shape found, (100,) expected",
    }
)
test_obj = Simulation(machine=M3)
test_obj.input = InputCurrent(
    time=time, angle=angle, Is=I_1, Ir=I_2, angle_rotor=angle_rotor, Nr=Nr_wrong2
)
InputCurrent_Error_test.append(
    {
        "test_obj": test_obj,
        "exp": "ERROR: InputCurrent.Nr should be a vector of the same length as time, (102,) shape found, (100,) expected",
    }
)


@pytest.mark.METHODS
class Test_InCurrent_meth(object):
    """unittest for InputCurrent object methods"""

    @pytest.mark.parametrize("test_dict", InputCurrent_Error_test)
    def test_InputCurrent_Error_test(self,test_dict):
        """Check that the input current raises the correct errors
            """
        output = Output(simu=test_dict["test_obj"])
        with pytest.raises(InputError) as context:
            output.simu.input.gen_input()
            assert test_dict["exp"]== str(context.exception)

    def test_InputCurrent_Ok(self):
        """Check that the input current can return a correct output
            """
        test_obj = Simulation(machine=M3)
        output = Output(simu=test_obj)
        time = ImportGenVectLin(0, 1, 16)
        angle = ImportGenVectLin(0, 2 * pi, 20)
        Is = ImportGenMatrixSin(is_transpose=True)
        Is.init_vector(f=[2, 2, 2], A=[2, 2, 2], Phi=[pi / 2, 0, -pi / 2], N=16, Tf=1)
        S = sqrt(2)
        Is_exp = transpose(    
            array(    
                [    
                    [2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S, -2, -S, 0, S],    
                    [0, S, 2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S, -2, -S],    
                    [-2, -S, 0, S, 2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S],    
                ]    
            )    
        )

        Ir = ImportGenMatrixSin(is_transpose=True)
        Ir.init_vector(f=[2, 2], A=[2, 2], Phi=[0, -pi / 2], N=16, Tf=1)
        Ir_exp = transpose(    
            array(    
                [    
                    [0, S, 2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S, -2, -S],    
                    [-2, -S, 0, S, 2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S],    
                ]    
            )    
        )

        angle_rotor = ImportGenVectLin(0, 2 * pi, 16)
        Nr = ImportMatrixVal(value=ones(16) * 10)
        test_obj.input = InputCurrent(    
            time=time, angle=angle, Is=Is, Ir=Ir, angle_rotor=angle_rotor, Nr=Nr    
        )

        test_obj.input.gen_input()
        assert_array_almost_equal(output.elec.time, linspace(0, 1, 16))
        assert_array_almost_equal(output.elec.angle, linspace(0, 2 * pi, 20))
        assert_array_almost_equal(output.elec.Is, Is_exp)
        assert_array_almost_equal(output.elec.Ir, Ir_exp)
        assert_array_almost_equal(output.elec.angle_rotor, linspace(0, 2 * pi, 16))
        assert_array_almost_equal(output.elec.Nr, ones(16) * 10)
