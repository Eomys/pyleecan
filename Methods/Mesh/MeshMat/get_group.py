# -*- coding: utf-8 -*-


def get_group(self, name_submesh):
    """Define a mesh object as submesh of parent mesh object

    Parameters
    ----------
    self : MeshFEMM
        a MeshFEMM object
    group : int
        id of the targeted group

        Returns
    -------
    submesh: Submesh
        a Submesh object

    """
    submesh = None
    for im in range(len(self.submesh)):
        if self.submesh[im].name == name_submesh:
            submesh = self.submesh[im]

    return submesh
