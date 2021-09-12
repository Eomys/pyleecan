from math import ceil


def comp_mesh_dict(self, element_size, prefix=""):
    """Returns the number of mesh elements on each line of the surface
    to match the element_size.

    Parameters
    ----------
    self : Surface
        a Surface object

    element_size : float
        The size of each element on the mesh [m]
    prefix: str
        Label prefix for line


    Returns
    -------
    mesh_dict : dict
        Dictionary containing the number of element of each line of the surface
    """

    mesh_dict = dict()
    lines = self.get_lines()
    for ii, line in enumerate(lines):
        label = prefix + str(ii)
        length = line.comp_length()
        number_of_element = ceil(length / element_size)
        mesh_dict[label] = number_of_element

    return mesh_dict
