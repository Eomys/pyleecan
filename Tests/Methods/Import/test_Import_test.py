# -*- coding: utf-8 -*-
"""
@date Created on Fri Feb 22 13:36:22 2019
@author pierre_b
"""

from unittest import TestCase
from ddt import ddt, data

from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportGenMatrixSin import ImportGenMatrixSin
from pyleecan.Classes.ImportGenVectSin import ImportGenVectSin
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from numpy.random import uniform
from numpy import array_equal, transpose, sqrt, array, pi
from numpy.testing import assert_array_almost_equal
from pyleecan.Methods.Import.ImportGenMatrixSin import (
    GenSinEmptyError,
    GenSinDimError,
    GenSinTransposeError,
)

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


@ddt
class unittest_Import_meth(TestCase):
    """unittest for Import object methods"""

    @data(*ImportMatrix_test)
    def test_ImportMatrix(self, test_dict):
        """Check that the import of a Matrix is correct
        """

        result = test_dict["test_obj"].get_data()
        assert_array_almost_equal(test_dict["exp"], result)

    def test_ImportGenMatrixSin_Error(self):
        """Check that the ImportGenMatrixSin can detect wrong input
        """
        test_obj = ImportGenMatrixSin(sin_list=[], is_transpose=True)
        with self.assertRaises(GenSinEmptyError):
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
        with self.assertRaises(GenSinDimError):
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
        with self.assertRaises(GenSinTransposeError):
            test_obj.get_data()
