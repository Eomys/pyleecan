# -*- coding: utf-8 -*-
from typing import Literal

from numpy import arange, array

from ....Classes.ElementMat import ElementMat
from ....Classes.FPGNSeg import FPGNSeg
from ....Classes.FPGNTri import FPGNTri
from ....Classes.Mesh import Mesh
from ....Classes.NodeMat import NodeMat
from ....Classes.RefLine3 import RefLine3
from ....Classes.RefQuad9 import RefQuad9
from ....Classes.RefSegmentP1 import RefSegmentP1
from ....Classes.RefTriangle3 import RefTriangle3
from ....Classes.ScalarProductL2 import ScalarProductL2


def convert(
    self,
    meshtype: Literal["MeshVTK", "MeshMat"] = "MeshMat",
    scale: float = 1.0,
) -> Mesh:
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
        new_mesh.node.coordinate *= scale
    elif meshtype == "MeshMat":
        # Avoid circular import
        from ....Classes.MeshMat import MeshMat

        new_mesh = MeshMat(dimension=self.dimension)

        connect_all = self.get_element()[0]
        nodes = array(self.get_node_coordinate())
        nb_node = nodes.shape[0]

        new_mesh.node = NodeMat(
            coordinate=scale * nodes,
            nb_node=nb_node,
            indice=arange(nb_node),
        )

        min_indice = 0
        for key in connect_all:
            connect = connect_all[key]
            nb_element = connect.shape[0]
            indices = arange(min_indice, min_indice + nb_element)
            min_indice += nb_element

            if key == "line":
                new_mesh.element_dict["line"] = ElementMat(
                    nb_node_per_element=2,
                    connectivity=connect,
                    nb_element=nb_element,
                    indice=indices,
                    gauss_point=FPGNSeg(),
                    ref_element=RefSegmentP1(),
                    scalar_product=ScalarProductL2(),
                )
            elif key == "line3":
                new_mesh.element_dict["line3"] = ElementMat(
                    nb_node_per_element=3,
                    connectivity=connect,
                    nb_element=nb_element,
                    indice=indices,
                    ref_element=RefLine3(),
                    gauss_point=None,  # TODO
                )
            elif key == "triangle3":
                new_mesh.element_dict["triangle"] = ElementMat(
                    nb_node_per_element=3,
                    connectivity=connect,
                    nb_element=nb_element,
                    indice=indices,
                    gauss_point=FPGNTri(),
                    ref_element=RefTriangle3(),
                    scalar_product=ScalarProductL2(),
                )
            elif key == "quad9":
                new_mesh.element_dict["quad9"] = ElementMat(
                    nb_node_per_element=9,
                    connectivity=connect,
                    nb_element=nb_element,
                    indice=indices,
                    ref_element=RefQuad9(),
                )
    else:
        raise ValueError(
            f"Wrong meshtype value, expected MeshVTK or MeshMat, got {meshtype}."
        )

    return new_mesh
