# -*- coding: utf-8 -*-
from pyleecan.Classes.SubMesh import SubMesh

import numpy as np


def get_submesh(self, group):
    """Define a mesh object as submesh of parent mesh object

    Parameters
    ----------
    :param self : an MeshFEMM object
    :param group: id of the targeted group

    Returns
    -------

    """

    # Check if the submesh is already existing
    if len(self.submesh) > 1:
        for isub in range (len(self.submesh)):
            if self.submesh[isub].group_number == group:
                return self.submesh[isub]
    else:
        if len(self.submesh) == 1:
            if self.submesh.group_number == group:
                return self.submesh

    # Else, the submesh is defined
    submesh = SubMesh()
    submesh.group_number = group
    submesh.set_submesh(self)

    return submesh

