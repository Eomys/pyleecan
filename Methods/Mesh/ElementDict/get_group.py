# -*- coding: utf-8 -*-


def get_group(self, name_submesh):
    """Define a mesh object as submesh of parent mesh object

    Parameters
    ----------
    :param self : an Mesh object
    :param elem_id: ids of the elements which define the submesh

    Returns
    -------

    """
    submesh = None
    for im in range(len(self.submesh)):
        if self.submesh[im].name == name_submesh:
            submesh = self.submesh[im]

    return submesh
