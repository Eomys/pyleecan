# -*- coding: utf-8 -*-
from ....definitions import PACKAGE_NAME


def set_submesh(self, group_number):
    """Define a mesh object as submesh of parent mesh object

     Parameters
     ----------
     self : Mesh
         an Mesh object
     group_number : numpy.array
         a group number which define the elements which constitute the submesh

     Returns
     -------

     """
    # Dynamic import of MeshFEMM
    module = __import__(PACKAGE_NAME + ".Classes." + "Mesh", fromlist=["Mesh"])
    submesh = getattr(module, "Mesh")()

    for i_group in range(len(group_number)):

        submesh_tmp = getattr(module, "Mesh")()
        for key in self.element:
            element = self.element[key]

            # Create a new Element object which is restrained to group_number
            submesh_tmp.element[key] = element.get_group(group_number[i_group])

            # Create a new Node object which corresponds to selection of element
            submesh_tmp.node = self.node.get_group(submesh_tmp.element[key])

        if i_group > 0:
            # TODO: This part is not tested

            # Keep only the common elements (and create interface ones)
            submesh = submesh.interface(submesh_tmp)
            # # Create a new Node object which corresponds to selection of element
            # submesh.node = self.node.get_group(element=submesh.element)
        else:
            submesh = submesh_tmp

    self.submesh.append(submesh)

    return submesh
