# -*- coding: utf-8 -*-


def set_submesh(self, group_number):
    """Define a mesh object as submesh of parent mesh object

     Parameters
     ----------
     self : Mesh
         an Mesh object
     group_number : int
         a group number which define the elements which constitute the submesh

     Returns
     -------

     """
    # Dynamic import of MeshFEMM
    module = __import__("pyleecan.Classes." + "Mesh", fromlist=["Mesh"])
    submesh = getattr(module, "Mesh")()

    for i_group in range(len(group_number)):
        if group_number[i_group] == -1:
            for i_group in range(len(group_number) - 2):
                submesh = submesh.interface(self.submesh[i_group])

            submesh.node = self.node.get_group(
                element=submesh.element
            )  # Create a new Node object which corresponds to selection of element
            self.submesh.append(submesh)

        else:
            submesh = getattr(module, "Mesh")()
            submesh.element = self.element.get_group(
                group_number[i_group]
            )  # Create a new Element object which is restrained to group_number
            submesh.node = self.node.get_group(
                element=submesh.element
            )  # Create a new Node object which corresponds to selection of element
            self.submesh.append(submesh)

    self.submesh.append(submesh)

    return submesh
