# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.PointMat import PointMat
from pyleecan.Classes.Simulation import Simulation
from pyleecan.Classes.Output import Output
from os.path import join
import matplotlib.pyplot as plt
from Tests import save_validation_path as save_path
import numpy as np


class unittest_plot_mesh_field(TestCase):
    """unittest to get elements containing specific node(s)"""

    def setUp(self):

        self.simu = Simulation()
        self.out = Output(simu=self.simu)
        self.mesh = Mesh()
        self.mesh.element["Triangle3"] = CellMat(nb_node_per_element=3)
        self.mesh.node = PointMat()
        self.mesh.node.add_node(np.array([0, 0]))
        self.mesh.node.add_node(np.array([1, 0]))
        self.mesh.node.add_node(np.array([0, 1]))
        self.mesh.node.add_node(np.array([1, 1]))
        self.mesh.node.add_node(np.array([2, 0]))

        self.mesh.add_element(np.array([0, 1, 2]), "Triangle3", group=int(3))
        self.mesh.add_element(np.array([1, 2, 3]), "Triangle3", group=int(3))
        self.mesh.add_element(np.array([4, 1, 3]), "Triangle3", group=int(2))

    def test_Mesh_ElementMat_NodeMat_3Tgl(self):

        field = np.array([1, 2, 3])
        self.out.plot_mesh_field(mesh=self.mesh, title="Permeability", field=field)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_plot_mesh_field.png"))
