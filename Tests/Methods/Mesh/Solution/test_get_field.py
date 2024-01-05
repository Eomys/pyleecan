# -*- coding: utf-8 -*-

import pytest
import numpy as np
from unittest import TestCase

from SciDataTool import DataTime, Data1D, DataLinspace, VectorField

from pyleecan.Classes.SolutionData import SolutionData
from pyleecan.Classes.SolutionMat import SolutionMat
from pyleecan.Classes.SolutionVector import SolutionVector


@pytest.mark.MeshSol
def test_SolutionMat():
    """Tests for get_field method from SolutionMat class"""
    DELTA = 1e-10

    field = np.zeros((2, 3, 2))
    field[:, :, 0] = np.array([[1, 2, 3], [2, 3, 4]])
    field[:, :, 1] = np.array([[11, 21, 31], [21, 31, 41]])

    solution = SolutionMat()
    solution.field = field
    solution.axis_name = ["time", "indice", "z"]
    solution.axis_size = [2, 3, 2]

    field = solution.get_field()

    correction = field
    result = np.sum(np.abs(correction - field))
    msg = "Wrong result: returned " + str(field) + ", expected: " + str(correction)
    np.testing.assert_almost_equal(result, 0, err_msg=msg)

    field = solution.get_field("time[1]", "indice[1,2]", is_squeeze=True)

    correction = np.array([[3, 4]])
    result = np.sum(np.abs(correction - field))
    msg = "Wrong result: returned " + str(field) + ", expected: " + str(correction)
    np.testing.assert_almost_equal(result, 0, err_msg=msg)

    field = solution.get_field("z[1]", "indice[1,2]", is_squeeze=True)
    correction = np.array([[21, 31]])
    result = np.sum(np.abs(correction - field))
    msg = "Wrong result: returned " + str(field) + ", expected: " + str(correction)
    np.testing.assert_almost_equal(result, 0, err_msg=msg)


@pytest.mark.MeshSol
def test_SolutionVector():
    DELTA = 1e-10

    Indices_Element = Data1D(name="indice", values=[0, 1, 2, 4], is_components=True)
    Time = DataLinspace(
        name="time",
        unit="s",
        initial=0,
        final=1,
        number=10,
    )

    H = np.ones((10, 4, 2))

    # Store the results for H
    componentsH = {}

    Hx_data = DataTime(
        name="Magnetic Field Hx",
        unit="A/m",
        symbol="Hx",
        axes=[Time, Indices_Element],
        values=H[:, :, 0],
    )
    componentsH["comp_x"] = Hx_data

    Hy_data = DataTime(
        name="Magnetic Field Hy",
        unit="A/m",
        symbol="Hy",
        axes=[Time, Indices_Element],
        values=H[:, :, 1],
    )
    componentsH["comp_y"] = Hy_data
    vecH = VectorField(name="Magnetic Field", symbol="H", components=componentsH)
    solution = SolutionVector(field=vecH, type_element="triangle", label="H")

    field = solution.get_field()

    correction = np.ones((10, 4, 2))
    result = np.sum(np.abs(correction - field))
    msg = "Wrong result: returned " + str(field) + ", expected: " + str(correction)
    np.testing.assert_almost_equal(result, 0, err_msg=msg)

    field = solution.get_field("time[0]", "indice[1,2]")

    correction = np.ones((2, 2))
    result = np.sum(np.abs(correction - field))
    msg = "Wrong result: returned " + str(field) + ", expected: " + str(correction)
    np.testing.assert_almost_equal(result, 0, err_msg=msg)


@pytest.mark.MeshSol
def test_SolutionData():
    DELTA = 1e-10

    Indices_Element = Data1D(name="indice", values=[0, 1, 2, 4], is_components=True)
    Time = DataLinspace(
        name="time",
        unit="s",
        initial=0,
        final=1,
        number=10,
    )

    # Store the results for H
    H = DataTime(
        name="Magnetic Field Hx",
        unit="A/m",
        symbol="Hx",
        axes=[Time, Indices_Element],
        values=np.ones((10, 4)),
    )

    solution = SolutionData(field=H, type_element="triangle", label="H")

    field = solution.get_field()

    correction = np.ones((10, 4))
    result = np.sum(np.abs(correction - field))
    msg = "Wrong result: returned " + str(field) + ", expected: " + str(correction)
    np.testing.assert_almost_equal(result, 0, err_msg=msg)

    field = solution.get_field("time[0]", "indice[1,2]")

    correction = correction[0, 1:3]
    result = np.sum(np.abs(correction - field))
    msg = "Wrong result: returned " + str(field) + ", expected: " + str(correction)
    np.testing.assert_almost_equal(result, 0, err_msg=msg)


if __name__ == "__main__":
    test_SolutionMat()
    test_SolutionData()
    test_SolutionVector()
    # test_plot_contour_2group()
