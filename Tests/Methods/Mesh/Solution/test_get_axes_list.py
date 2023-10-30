# -*- coding: utf-8 -*-

import pytest
import numpy as np
from unittest import TestCase

from SciDataTool import DataTime, Data1D, DataLinspace, VectorField

from pyleecan.Classes.SolutionData import SolutionData
from pyleecan.Classes.SolutionMat import SolutionMat
from pyleecan.Classes.SolutionVector import SolutionVector


@pytest.mark.MeshSol
class Test_get_axes_list(TestCase):
    """Tests for get_axis_list method from Solution classes"""

    def test_SolutionMat(self):
        DELTA = 1e-10

        solution = SolutionMat()
        solution.field = np.array([[1, 2, 3], [2, 3, 4]])
        solution.axis_name = ["time", "indice"]
        solution.axis_size = [2, 3]

        axname, axsize = solution.get_axes_list()

        msg = (
            "Wrong result: returned "
            + str(axsize)
            + ", expected: "
            + str(solution.axis_size)
        )
        self.assertAlmostEqual(axsize, solution.axis_size, msg=msg, delta=DELTA)

    def test_SolutionVector(self):
        DELTA = 1e-10

        Indices_Element = Data1D(name="indice", values=[0, 1, 2, 4], is_components=True)
        Time = DataLinspace(
            name="time",
            unit="s",
            initial=0,
            final=1,
            number=10,
        )

        H = np.zeros((10, 4, 2))

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

        axname, axsize = solution.get_axes_list()

        correction = [10, 4, 2]
        msg = "Wrong result: returned " + str(axsize) + ", expected: " + str(correction)
        self.assertAlmostEqual(axsize, correction, msg=msg, delta=DELTA)

    def test_SolutionData(self):
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
            values=np.zeros((10, 4)),
        )

        solution = SolutionData(field=H, type_element="triangle", label="H")

        axname, axsize = solution.get_axes_list()

        correction = [10, 4]
        msg = "Wrong result: returned " + str(axsize) + ", expected: " + str(correction)
        self.assertAlmostEqual(axsize, correction, msg=msg, delta=DELTA)
