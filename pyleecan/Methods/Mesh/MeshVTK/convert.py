# -*- coding: utf-8 -*-
from ....Classes.MeshMat import MeshMat
from ....Classes.NodeMat import NodeMat
from ....Classes.ElementMat import ElementMat
from ....Classes.Interpolation import Interpolation
from ....Classes.FPGNSeg import FPGNSeg
from ....Classes.FPGNTri import FPGNTri

from ....Classes.ScalarProductL2 import ScalarProductL2
from ....Classes.RefSegmentP1 import RefSegmentP1
from ....Classes.RefTriangle3 import RefTriangle3


from numpy import array, linspace


def convert(self, meshtype, scale):
    """Convert this object to another type of Mesh object.

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
    meshtype : str
        a type of Mesh object: MeshVTK or MeshMat
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

        connect_all = self.get_element()[0]
        nodes = array(self.get_node_coordinate())
        nb_node = nodes.shape[0]

        new_mesh.node = NodeMat(
            coordinate=scale * nodes,
            nb_node=nb_node,
            indice=linspace(0, nb_node - 1, nb_node),
        )

        min_indice = 0
        for key in connect_all:
            connect = connect_all[key]
            nb_element = connect.shape[0]
            indices = linspace(
                min_indice, min_indice + nb_element - 1, nb_element, dtype=int
            )
            min_indice = min_indice + nb_element

            if key == "line":
                new_mesh.element["line"] = ElementMat(
                    nb_node_per_element=2,
                    connectivity=connect,
                    nb_element=nb_element,
                    indice=indices,
                )
                interp = Interpolation()
                interp.gauss_point = FPGNSeg()
                interp.ref_element = RefSegmentP1()
                interp.scalar_product = ScalarProductL2()
                new_mesh.element["line"].interpolation = interp
            elif key == "line3":
                new_mesh.element["line3"] = ElementMat(
                    nb_node_per_element=3,
                    connectivity=connect,
                    nb_element=nb_element,
                    indice=indices,
                )
                interp = Interpolation()
                interp.gauss_point = None  # TODO
                interp.ref_element = None  # TODO
                interp.scalar_product = None  # TODO
                new_mesh.element["line3"].interpolation = interp
            elif key == "triangle3":
                new_mesh.element["triangle"] = ElementMat(
                    nb_node_per_element=3,
                    connectivity=connect,
                    nb_element=nb_element,
                    indice=indices,
                )
                interp = Interpolation()
                interp.gauss_point = FPGNTri()
                interp.ref_element = RefTriangle3()
                interp.scalar_product = ScalarProductL2()
                new_mesh.element["triangle"].interpolation = interp
            elif key == "quad9":
                new_mesh.element["quad9"] = ElementMat(
                    nb_node_per_element=9,
                    connectivity=connect,
                    nb_element=nb_element,
                    indice=indices,
                )
                interp = Interpolation()
                interp.gauss_point = None  # TODO
                interp.ref_element = None  # TODO
                interp.scalar_product = None  # TODO
                new_mesh.element["quad9"].interpolation = interp
    else:
        raise ValueError(
            f"Wrong meshtype value, expected MeshVTK or MeshMat, got {meshtype}."
        )

    return new_mesh
