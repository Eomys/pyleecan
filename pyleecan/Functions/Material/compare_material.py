from ...Classes.Material import Material


def compare_material(mat1, mat2):
    """
    compare materials except the name and the path

    Parameters
    ----------
    mat1: Material
    mat2: Material
    """

    tmp_mat1 = Material(init_dict=mat1.as_dict())
    tmp_mat2 = Material(init_dict=mat2.as_dict())
    tmp_mat1.name = ""
    tmp_mat2.name = ""
    tmp_mat1.path = ""
    tmp_mat2.path = ""

    return tmp_mat1 == tmp_mat2
