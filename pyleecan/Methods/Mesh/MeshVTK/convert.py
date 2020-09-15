# -*- coding: utf-8 -*-
from ....Classes.MeshMat import MeshMat
from ....Classes.PointMat import PointMat
from ....Classes.CellMat import CellMat
from ....Classes.Interpolation import Interpolation
from ....Classes.FPGNSeg import FPGNSeg
from ....Classes.FPGNTri import FPGNTri

from ....Classes.ScalarProductL2 import ScalarProductL2
from ....Classes.RefSegmentP1 import RefSegmentP1
from ....Classes.RefTriangle3 import RefTriangle3


from numpy import array, linspace


def convert(self, meshtype, scale):
    """ Convert this object to another type of Mesh object.

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
    meshtype : str
        a type of Mesh object
    scale : float
        scale factor

        Returns
    -------
    new_mesh : Mesh
        a Mesh object
    """

    if meshtype == "MeshVTK":
        new_mesh = self.copy()
    elif meshtype == "MeshMat":
        new_mesh = MeshMat(dimension=self.dimension)

        connect_all = self.get_cell()
        point = array(self.get_point())
        nb_pt = point.shape[0]

        new_mesh.point = PointMat(
            coordinate=scale * point, nb_pt=nb_pt, indice=linspace(0, nb_pt - 1, nb_pt)
        )

        min_indice = 0
        for key in connect_all:
            connect = connect_all[key]
            nb_cell = connect.shape[0]
            indices = linspace(min_indice, min_indice + nb_cell - 1, nb_cell, dtype=int)
            min_indice = min_indice + nb_cell

            if key == "line":
                new_mesh.cell["line"] = CellMat(
                    nb_pt_per_cell=2,
                    connectivity=connect,
                    nb_cell=nb_cell,
                    indice=indices,
                )
                interp = Interpolation()
                interp.gauss_point = FPGNSeg()
                interp.ref_cell = RefSegmentP1()
                interp.scalar_product = ScalarProductL2()
                new_mesh.cell["line"].interpolation = interp
            elif key == "triangle3":
                new_mesh.cell["triangle"] = CellMat(
                    nb_pt_per_cell=3,
                    connectivity=connect,
                    nb_cell=nb_cell,
                    indice=indices,
                )
                interp = Interpolation()
                interp.gauss_point = FPGNTri()
                interp.ref_cell = RefTriangle3()
                interp.scalar_product = ScalarProductL2()
                new_mesh.cell["triangle"].interpolation = interp

    return new_mesh
