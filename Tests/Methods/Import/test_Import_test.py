# -*- coding: utf-8 -*-

from numpy import array, array_equal, linspace, pi, sqrt, transpose
from numpy.random import uniform
from numpy.testing import assert_array_almost_equal

from pyleecan.Classes.ImportGenMatrixSin import ImportGenMatrixSin
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportGenVectSin import ImportGenVectSin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportMatrixXls import ImportMatrixXls
from pyleecan.Methods.Import.ImportGenMatrixSin import (
    GenSinDimError,
    GenSinEmptyError,
    GenSinTransposeError,
)
from Tests.Methods.Import import test_file
import pytest

ImportMatrix_test = list()
mat = uniform(0, 1, (4, 4))
# Direct import
ImportMatrix_test.append(
    {"test_obj": ImportMatrixVal(value=mat, is_transpose=False), "exp": mat}
)
# Direct import transpose
ImportMatrix_test.append(
    {"test_obj": ImportMatrixVal(value=mat, is_transpose=True), "exp": transpose(mat)}
)

# Lin Vector generation
exp = array([0, 1, 2, 3, 4, 5, 6, 7])
ImportMatrix_test.append(
    {
        "test_obj": ImportGenVectLin(
            start=0, stop=7, num=8, endpoint=True, is_transpose=False
        ),
        "exp": exp,
    }
)

# Lin Vector generation + transpose
exp = transpose(array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]))
ImportMatrix_test.append(
    {
        "test_obj": ImportGenVectLin(
            start=0, stop=1, num=10, endpoint=False, is_transpose=True
        ),
        "exp": exp,
    }
)

# Sin Vector import 1 period
S = sqrt(2)
exp = array([0, S, 2, S, 0, -S, -2, -S])
ImportMatrix_test.append(
    {
        "test_obj": ImportGenVectSin(A=2, f=1, Phi=0, N=8, Tf=1, is_transpose=False),
        "exp": exp,
    }
)
# Sin Vector import 2 period
exp = array([0, S, 2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S, -2, -S])
ImportMatrix_test.append(
    {
        "test_obj": ImportGenVectSin(A=2, f=1, Phi=0, N=16, Tf=2, is_transpose=False),
        "exp": exp,
    }
)
# Sin vector import + transpose
exp = transpose(array([0, S, 2, S, 0, -S, -2, -S]))
ImportMatrix_test.append(
    {
        "test_obj": ImportGenVectSin(A=2, f=1, Phi=0, N=8, Tf=1, is_transpose=True),
        "exp": exp,
    }
)
# Sin vector import + Phi and f=2
exp = array([2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S, -2, -S, 0, S])
ImportMatrix_test.append(
    {
        "test_obj": ImportGenVectSin(
            A=2, f=2, Phi=pi / 2, N=16, Tf=1, is_transpose=False
        ),
        "exp": exp,
    }
)
# Sin matrix import
exp = array(
    [
        [2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S, -2, -S, 0, S],
        [0, S, 2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S, -2, -S],
        [-2, -S, 0, S, 2, S, 0, -S, -2, -S, 0, S, 2, S, 0, -S],
    ]
)
sin_list = list()
sin_list.append(ImportGenVectSin(A=2, f=2, Phi=pi / 2, N=16, Tf=1, is_transpose=False))
sin_list.append(ImportGenVectSin(A=2, f=2, Phi=0, N=16, Tf=1, is_transpose=False))
sin_list.append(ImportGenVectSin(A=2, f=2, Phi=-pi / 2, N=16, Tf=1, is_transpose=False))
ImportMatrix_test.append(
    {"test_obj": ImportGenMatrixSin(sin_list=sin_list, is_transpose=False), "exp": exp}
)
# Sin matrix import + transpose
ImportMatrix_test.append(
    {
        "test_obj": ImportGenMatrixSin(sin_list=sin_list, is_transpose=True),
        "exp": transpose(exp),
    }
)
# Sin matrix import + transpose vector
sin_list = list()
sin_list.append(ImportGenVectSin(A=2, f=2, Phi=pi / 2, N=16, Tf=1, is_transpose=True))
sin_list.append(ImportGenVectSin(A=2, f=2, Phi=0, N=16, Tf=1, is_transpose=True))
sin_list.append(ImportGenVectSin(A=2, f=2, Phi=-pi / 2, N=16, Tf=1, is_transpose=True))
ImportMatrix_test.append(
    {
        "test_obj": ImportGenMatrixSin(sin_list=sin_list, is_transpose=False),
        "exp": transpose(exp),
    }
)
# Load from xls
exp = array([0, 1, 2, 3, 4, 5, 6, 7], ndmin=2)
ImportMatrix_test.append(
    {
        "test_obj": ImportMatrixXls(
            file_path=test_file,
            sheet="Test1",
            usecols=None,
            skiprows=0,
            is_transpose=False,
        ),
        "exp": transpose(exp),
    }
)
# Load from xls skiprow + transpose
exp = array([2, 3, 4, 5, 6, 7], ndmin=2)
ImportMatrix_test.append(
    {
        "test_obj": ImportMatrixXls(
            file_path=test_file,
            sheet="Test1",
            usecols=None,
            skiprows=2,
            is_transpose=True,
        ),
        "exp": exp,
    }
)
# Usecols test
exp = array([[0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7]])
ImportMatrix_test.append(
    {
        "test_obj": ImportMatrixXls(
            file_path=test_file,
            sheet="Test2",
            usecols="B:G",
            skiprows=1,
            is_transpose=False,
        ),
        "exp": exp,
    }
)
exp = array([[0, 2, 3], [1, 3, 4], [2, 4, 5]])
ImportMatrix_test.append(
    {
        "test_obj": ImportMatrixXls(
            file_path=test_file,
            sheet="Test2",
            usecols="B,D,E",
            skiprows=1,
            is_transpose=False,
        ),
        "exp": exp,
    }
)


@pytest.mark.METHODS
class Test_Import_test(object):
    """unittest for Import object methods"""

    @pytest.mark.parametrize("test_dict", ImportMatrix_test)
    def test_ImportMatrix(self, test_dict):
        """Check that the import of a Matrix is correct"""

        result = test_dict["test_obj"].get_data()
        assert_array_almost_equal(test_dict["exp"], result)

    def test_ImportGenMatrixSin_init(self):
        """Check that the ImportGenMatrixSin can be set by list"""
        f = [100, 100, 100]
        A = [1, 0.5, 2]
        Phi = linspace(0, 2 * pi, 3, endpoint=False)
        test_obj = ImportGenMatrixSin(sin_list=[], is_transpose=True)
        test_obj.init_vector(f=f, A=A, Phi=Phi, N=1024, Tf=2.5)

        assert len(test_obj.sin_list) == 3
        assert test_obj.sin_list[0].f == 100
        assert test_obj.sin_list[1].f == 100
        assert test_obj.sin_list[2].f == 100

        assert test_obj.sin_list[0].A == 1
        assert test_obj.sin_list[1].A == 0.5
        assert test_obj.sin_list[2].A == 2

        assert test_obj.sin_list[0].Phi == 0
        assert test_obj.sin_list[1].Phi == 2 * pi / 3
        assert test_obj.sin_list[2].Phi == 4 * pi / 3

        assert test_obj.sin_list[0].N == 1024
        assert test_obj.sin_list[1].N == 1024
        assert test_obj.sin_list[2].N == 1024

        assert test_obj.sin_list[0].Tf == 2.5
        assert test_obj.sin_list[1].Tf == 2.5
        assert test_obj.sin_list[2].Tf == 2.5

    def test_ImportGenMatrixSin_Error(self):
        """Check that the ImportGenMatrixSin can detect wrong input"""
        test_obj = ImportGenMatrixSin(sin_list=[], is_transpose=True)
        with pytest.raises(GenSinEmptyError):
            test_obj.get_data()

        sin_list = list()
        sin_list.append(
            ImportGenVectSin(A=2, f=2, Phi=pi / 2, N=16, Tf=1, is_transpose=False)
        )
        sin_list.append(
            ImportGenVectSin(A=2, f=2, Phi=0, N=8, Tf=1, is_transpose=False)
        )
        sin_list.append(
            ImportGenVectSin(A=2, f=2, Phi=-pi / 2, N=16, Tf=1, is_transpose=False)
        )
        test_obj = ImportGenMatrixSin(sin_list=sin_list, is_transpose=True)
        with pytest.raises(GenSinDimError):
            test_obj.get_data()

        sin_list = list()
        sin_list.append(
            ImportGenVectSin(A=2, f=2, Phi=pi / 2, N=16, Tf=1, is_transpose=False)
        )
        sin_list.append(
            ImportGenVectSin(A=2, f=2, Phi=0, N=16, Tf=1, is_transpose=False)
        )
        sin_list.append(
            ImportGenVectSin(A=2, f=2, Phi=-pi / 2, N=16, Tf=1, is_transpose=True)
        )
        test_obj = ImportGenMatrixSin(sin_list=sin_list, is_transpose=True)
        with pytest.raises(GenSinTransposeError):
            test_obj.get_data()
