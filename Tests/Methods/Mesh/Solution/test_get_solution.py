# -*- coding: utf-8 -*-

import pytest
from numpy import array, zeros, abs as np_abs
from random import randint
from unittest import TestCase

from SciDataTool import DataTime, Data1D, DataLinspace, VectorField

from pyleecan.Classes.SolutionData import SolutionData
from pyleecan.Classes.SolutionMat import SolutionMat
from pyleecan.Classes.SolutionVector import SolutionVector


@pytest.mark.MeshSol
class Test_get_solution(TestCase):
    """Tests for get_solution method from Solution classes"""

    def test_SolutionMat(self):
        DELTA = 1e-10

        solution = SolutionMat()
        solution.field = array([[1, 2, 3], [2, 3, 4]])
        solution.axis_name = ["time", "indice"]
        solution.axis_size = [2, 3]

        # result without explicit solution indices, i.e. solution.indice = None
        sol1 = solution.get_solution(indice=[0, 1])
        sol2 = solution.get_solution(indice=[0, 1, 2])
        sol3 = solution.get_solution(indice=[0, 1, 2, 3])

        expected = array([[1, 2], [2, 3]])
        result = np_abs(expected - sol1.field).sum()
        msg = "Wrong result: returned " + str(sol1) + ", expected: " + str(expected)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)

        expected = array([[1, 2, 3], [2, 3, 4]])
        result = np_abs(expected - sol2.field).sum()
        msg = "Wrong result: returned " + str(sol2) + ", expected: " + str(expected)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)

        result = np_abs(expected - sol3.field).sum()
        msg = "Wrong result: returned " + str(sol3) + ", expected: " + str(expected)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)

        # set explicit solution indices
        solution.indice = [999, 2000, 11857]

        # request indices that are part of the solution
        sol4 = solution.get_solution(indice=[999, 2000])
        sol5 = solution.get_solution(indice=[999, 2000, 11857])

        # request an indice that is not part of the solution
        sol6 = solution.get_solution(indice=[999, 2000, 11857, 1])

        expected = array([[1, 2], [2, 3]])
        result = np_abs(expected - sol4.field).sum()
        msg = "Wrong result: returned " + str(sol4) + ", expected: " + str(expected)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)

        expected = array([[1, 2, 3], [2, 3, 4]])
        result = np_abs(expected - sol5.field).sum()
        msg = "Wrong result: returned " + str(sol5) + ", expected: " + str(expected)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)

        result = np_abs(expected - sol6.field).sum()
        msg = "Wrong result: returned " + str(sol6) + ", expected: " + str(expected)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)

    def test_SolutionVector(self):
        DELTA = 1e-10

        Indices_Element = Data1D(name="indice", values=[0, 1, 2, 4], is_components=True)
        Time = DataLinspace(name="time", unit="s", initial=0, final=1, number=2)

        H = zeros((2, 4, 2))
        H[:, :, 0] = array([[1, 2, 3, 4], [2, 3, 4, 5]])
        H[:, :, 1] = array([[4, 5, 6, 7], [5, 6, 7, 8]])

        # Store the results for H
        componentsH = {}
        axes = [Time, Indices_Element]

        Hx_data = DataTime(
            name="Hx", unit="A/m", symbol="Hx", axes=axes, values=H[:, :, 0]
        )
        Hy_data = DataTime(
            name="Hy", unit="A/m", symbol="Hy", axes=axes, values=H[:, :, 1]
        )

        componentsH["comp_x"] = Hx_data
        componentsH["comp_y"] = Hy_data

        vecH = VectorField(name="Magnetic Field", symbol="H", components=componentsH)
        solution = SolutionVector(field=vecH, type_element="triangle", label="H")

        sol = solution.get_solution(indice=[1, 2, 4])
        field = sol.get_field("time", "indice", "component")

        expected = H[:, 1:, :]
        result = np_abs(expected - field).sum()
        msg = "Wrong result: returned " + str(field) + ", expected: " + str(expected)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)

    def test_SolutionData(self):
        DELTA = 1e-10

        Indices_Element = Data1D(name="indice", values=[0, 1, 2, 4], is_components=True)
        Time = DataLinspace(name="time", unit="s", initial=0, final=1, number=2)
        axes = [Time, Indices_Element]
        data = array([[1, 2, 3, 4], [2, 3, 4, 5]])

        # Store the results for H
        H = DataTime(name="Hx", unit="A/m", symbol="Hx", axes=axes, values=data)

        solution = SolutionData(field=H, type_element="triangle", label="H")

        field = solution.get_solution(indice=[1, 2, 4]).get_field()

        expected = data[:, 1:]
        result = np_abs(expected - field).sum()
        msg = "Wrong result: returned " + str(field) + ", expected: " + str(expected)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)

        field = solution.get_solution(indice=[1, 2, 4, 5]).get_field()
        result = np_abs(expected - field).sum()
        msg = "Wrong result: returned " + str(field) + ", expected: " + str(expected)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)


if __name__ == "__main__":
    test = Test_get_solution()
    test.test_SolutionData()
    test.test_SolutionMat()
    test.test_SolutionVector()
