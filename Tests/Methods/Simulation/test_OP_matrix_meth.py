import pytest
from numpy import array, mean, ones, pi
from numpy.testing import assert_array_almost_equal
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.OPMatrix import OPMatrix
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent


class Test_OP_matrix_meth(object):
    """unittest for OP_matrix object methods"""

    def test_OP_matrix_out_of_order(self):
        """Check that you can set/get an OP_matrix out of order"""
        # Constant column matrix
        OP_matrix = ones((10, 7))
        for ii in range(OP_matrix.shape[1]):
            OP_matrix[:, ii] *= ii + 1
        # Set Parameters out of "normal" order
        OP_obj = OPMatrix()
        OP_obj.set_OP_array(OP_matrix, "Tem", "Pem", "Id", "Iq", "N0", "Ud", "Uq")
        # Check that the set is correct
        assert mean(OP_obj.Tem_av_ref) == 1
        assert mean(OP_obj.Pem_av_ref) == 2
        assert mean(OP_obj.Id_ref) == 3
        assert mean(OP_obj.Iq_ref) == 4
        assert mean(OP_obj.N0) == 5
        assert mean(OP_obj.Ud_ref) == 6
        assert mean(OP_obj.Uq_ref) == 7
        # Check that getter works as well
        OP_mat2 = OP_obj.get_OP_array("Uq", "Ud", "N0", "Iq", "Id", "Pem", "Tem")
        assert OP_mat2.shape == (10, 7)
        for ii in range(OP_mat2.shape[1]):
            assert mean(OP_mat2[:, ii]) == 7 - ii

    def test_OP_matrix_convert(self):
        """Check that you can set/get an OP_matrix with convertion"""
        # Constant column matrix
        OP_matrix = ones((10, 4))
        OP_matrix[:, 0] *= 2
        OP_matrix[:, 1] *= pi / 2
        OP_matrix[:, 2] *= 4
        OP_matrix[:, 3] *= -pi / 2
        # Set Parameters out of "normal" order
        OP_obj = OPMatrix()
        OP_obj.set_OP_array(OP_matrix, "I0", "Phi0", "U0", "UPhi0")
        # Check that the set is correct
        assert mean(OP_obj.Id_ref) == pytest.approx(0, rel=1e-4)
        assert mean(OP_obj.Iq_ref) == 2
        assert mean(OP_obj.Ud_ref) == pytest.approx(0, rel=1e-4)
        assert mean(OP_obj.Uq_ref) == -4
        # Check that getter works as well
        OP_mat2 = OP_obj.get_OP_array("I0", "Phi0", "U0", "UPhi0")
        assert OP_mat2.shape == (10, 4)
        assert mean(OP_mat2[:, 0]) == 2
        assert mean(OP_mat2[:, 1]) == pi / 2
        assert mean(OP_mat2[:, 2]) == 4
        assert mean(OP_mat2[:, 3]) == -pi / 2

    def test_get_all(self):
        """Check that all the matrix can be extracted with all"""
        # Constant column matrix
        OP_matrix = ones((10, 5))
        for ii in range(OP_matrix.shape[1]):
            OP_matrix[:, ii] *= ii + 1
        # Set Parameters out of "normal" order
        OP_obj = OPMatrix()
        OP_obj.set_OP_array(OP_matrix, "N0", "Id", "Iq", "Tem", "Pem")
        # Check that the set is correct
        assert mean(OP_obj.N0) == 1
        assert mean(OP_obj.Id_ref) == 2
        assert mean(OP_obj.Iq_ref) == 3
        assert mean(OP_obj.Tem_av_ref) == 4
        assert mean(OP_obj.Pem_av_ref) == 5
        assert OP_obj.col_names == ["N0", "Id", "Iq", "Tem", "Pem"]
        # Check that getter works as well
        OP_mat2 = OP_obj.get_OP_array("all")
        assert OP_mat2.shape == (10, 5)
        for ii in range(OP_mat2.shape[1]):
            assert mean(OP_mat2[:, ii]) == ii + 1
        # Check without col_names for retro / flexibility
        OP_obj.col_names = None
        OP_mat3 = OP_obj.get_OP_array("all")
        assert OP_mat3.shape == (10, 5)
        for ii in range(OP_mat3.shape[1]):
            assert mean(OP_mat3[:, ii]) == ii + 1

    def test_simu_get_OP_array(self):
        """Check that you can set/get an OP_matrix from a simulation"""
        simu = Simu1()
        simu.input.OP = OPdq(Id_ref=1, Iq_ref=2, N0=3, Tem_av_ref=4)
        OP_1 = simu.get_OP_array("Id", "Iq", "N0", "T")
        assert_array_almost_equal(OP_1, array([[1, 2, 3, 4]]))

        simu.var_simu = VarLoadCurrent()
        OP_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        simu.var_simu.set_OP_array(OP_matrix, "N0", "Id", "Iq", "T")
        OP_2 = simu.get_OP_array("N0", "Id", "Iq", "T")
        assert_array_almost_equal(OP_2, OP_matrix)
        # Check input update by set_OP_array
        assert simu.input.OP.N0 == 1
        assert simu.input.OP.Id_ref == 2
        assert simu.input.OP.Iq_ref == 3
        assert simu.input.OP.Tem_av_ref == 4


# To run it without pytest
if __name__ == "__main__":

    a = Test_OP_matrix_meth()
    a.test_OP_matrix_out_of_order()
    a.test_OP_matrix_convert()
    a.test_simu_get_OP_array()
    a.test_get_all()
    print("Done")
