# -*- coding: utf-8 -*-
from ....Functions.MeshSolution.get_area import get_area
from ....Functions.MeshSolution.get_indices_limited import get_indices_limited


def get_demag(self, Hmax, group_name=None):
    """Get the surface area of the magnets that exceed a given field strenght H

    Parameters
    ----------
    Hmax : float
        demagnetization field strenght

    group_name : str
        optional name of the group, default group is 'rotor magnets'

    Return
    ------
    area : float
        surface area that exceed the max. field strength

    area_ref : float
        total magnets surface area as a reference

    indices : list
        list of elements indices that exceed the max. field strength

    """
    if group_name is None:
        group_name = "rotor magnets"
    if group_name in self.meshsolution.group.keys():
        inds = get_indices_limited(
            self.meshsolution, label="H", group_names=group_name, max_value=Hmax
        )

        area_ref = get_area(self.meshsolution, group_names=group_name)
        area = get_area(self.meshsolution, group_names=group_name, indices=inds)
    else:
        area, area_ref, inds = None, None, []

    return area, area_ref, inds
