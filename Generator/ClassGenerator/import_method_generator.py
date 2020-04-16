from ...Generator import TAB


def import_method(class_pack, class_name, meth):
    """Method to generate the code to import a method (with import check)

    Parameters
    ----------
    class_pack : str
        Package of the class (Machine, Simulation, Material...)
    class_name : str
        Name of the class
    meth : str
        Path to the method in the class Method folder
        (subfolder.name if any subfolder)

    Returns
    -------
    code: str
        Corresponding code
    """

    meth_name = meth.split(".")[-1]
    code = "try:\n"
    code += (
        TAB
        + "from ..Methods."
        + class_pack
        + "."
        + class_name
        + "."
        + meth
        + " import "
        + meth_name
        + "\n"
    )
    code += "except ImportError as error:\n"
    code += TAB + meth_name + " = error\n\n"
    return code
