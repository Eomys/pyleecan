# -*- coding: utf-8 -*-
import numpy as np
import pytest

from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.MeshMat import MeshMat


@pytest.mark.MeshSol
class Test_add_element(object):
    """unittest for add_element method in Mesh classes"""

    def setup_method(self, method):
        self.mesh = MeshMat()
        self.mesh.element_dict["triangle3"] = ElementMat(nb_node_per_element=3)
        self.mesh.element_dict["segment2"] = ElementMat(nb_node_per_element=2)
        self.DELTA = 1e-10

    def test_MeshMat_add_1element(self):
        """unittest with ElementMat, add 1 element"""

        points_test = np.array([0, 1])
        self.mesh.add_element(np.array([0, 1]), "segment2")
        # Check result
        testA = np.sum(
            abs(self.mesh.element_dict["segment2"].connectivity - points_test)
        )
        msg = (
            "Wrong result: returned "
            + str(self.mesh.element_dict["segment2"].connectivity)
            + ", expected: "
            + str(points_test)
        )
        assert abs(testA - 0) < self.DELTA, msg

        msg = (
            "Wrong result: returned "
            + str(self.mesh.element_dict["segment2"].nb_element)
            + ", expected: "
            + str(1)
        )
        assert abs(self.mesh.element_dict["segment2"].nb_element - 1) < self.DELTA, msg

    def test_MeshMat_add_3element(self):
        """unittest with MeshMat, add 3 different elements"""

        points_test = np.array([0, 1])
        self.mesh.add_element(points_test, "segment2")
        points_test = np.array([1, 2])
        self.mesh.add_element(points_test, "segment2")
        points_test = np.array([0, 1, 2])
        self.mesh.add_element(points_test, "triangle3")

        # Check result
        solution = np.array([[0, 1], [1, 2]])
        testA = np.sum(abs(self.mesh.element_dict["segment2"].connectivity - solution))
        msg = (
            "Wrong result: returned "
            + str(self.mesh.element_dict["segment2"].connectivity)
            + ", expected: "
            + str(solution)
        )
        assert abs(testA - 0) < self.DELTA, msg

        msg = (
            "Wrong result: returned "
            + str(self.mesh.element_dict["segment2"].nb_element)
            + ", expected: "
            + str(2)
        )
        assert abs(self.mesh.element_dict["segment2"].nb_element - 2) < self.DELTA, msg

        solution = np.array([[0, 1, 2]])
        testA = np.sum(abs(self.mesh.element_dict["triangle3"].connectivity - solution))
        msg = (
            "Wrong result: returned "
            + str(self.mesh.element_dict["triangle3"].connectivity)
            + ", expected: "
            + str(solution)
        )
        assert abs(testA - 0) < self.DELTA, msg

        msg = (
            "Wrong result: returned "
            + str(self.mesh.element_dict["segment2"].nb_element)
            + ", expected: "
            + str(1)
        )
        assert abs(self.mesh.element_dict["triangle3"].nb_element - 1) < self.DELTA, msg

    def test_MeshMat_add_exist(self):
        """unittest with MeshMat, try to add an already existing element."""
        points_test = np.array([0, 1])
        self.mesh.add_element(points_test, "segment2")
        points_test = np.array([1, 2])
        self.mesh.add_element(points_test, "segment2")
        points_test = np.array([0, 1, 2])
        self.mesh.add_element(points_test, "triangle3")

        points_test = np.array([1, 2])
        self.mesh.add_element(points_test, "segment2")

        msg = (
            "Wrong result: returned "
            + str(self.mesh.element_dict["segment2"].nb_element)
            + ", expected: "
            + str(2)
        )
        assert abs(self.mesh.element_dict["segment2"].nb_element - 2) < self.DELTA, msg

    def test_MeshMat_add_stupid(self):
        """unittest with ElementMat and 2 segment element and 1 triangle, add 1 triangle with a group number."""

        self.mesh.add_element(np.array([0, 1]), "segment2")
        test1 = self.mesh.add_element(None, "segment2")
        assert not test1
        test2 = self.mesh.add_element(np.array([0, 1, 2]), "segment2")
        assert not test2
        test3 = self.mesh.add_element(np.array([1, 1]), "segment2")
        assert not test2

        solution = np.array([0, 1], dtype=int)
        result = self.mesh.element_dict["segment2"].connectivity
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA - 0) < DELTA, msg
