from math import ceil, sqrt
from ...Functions.labels import BOUNDARY_PROP_LAB
from ...Functions.labels import short_label
 

def comp_gmsh_mesh_dict(surface, element_size, user_mesh_dict={}):
    """Returns the number of mesh elements on each line of the surface
    to match the element_size.

    Parameters
    ----------
    self : Surface
        a Surface object

    element_size : float
        The default size of each element on the mesh [m]
    
    user_mesh_dict: dictionary
        User specified mesh properties


    Returns
    -------
    mesh_dict : dict
        Dictionary containing the number of element of each line of the surface
    """

    mesh_dict = dict()
    # TO-DO: Airgap surfaces are special cases due to the boolean operations
    if "Airgap" in short_label(surface.label):
        return mesh_dict
    lines = surface.get_lines()
    if short_label(surface.label) in user_mesh_dict:
        elements_in_surface = user_mesh_dict[short_label(surface.label)]
        area = surface.comp_surface()
        element_size = area / elements_in_surface
        # Assumption: equilateral triangle
        side_size = sqrt(element_size * 4.0 / 1.73)
    else:
        side_size = element_size
    
    for ii, line in enumerate(lines):
        label = str(ii)
        # Overwrite number of elements given by boundary name in user_mesh_dict
        if (
            line.prop_dict
            and BOUNDARY_PROP_LAB in line.prop_dict
            and line.prop_dict[BOUNDARY_PROP_LAB] in user_mesh_dict
        ):
            mesh_dict[label] = user_mesh_dict[line.prop_dict[BOUNDARY_PROP_LAB]]
        else:
            length = line.comp_length()
            number_of_element = ceil(length / side_size)
            mesh_dict[label] = number_of_element

    return mesh_dict
