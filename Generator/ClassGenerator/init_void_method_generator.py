from pyleecan.Generator import TAB, TAB2, TAB3


def generate_init_void():
    """Generate the code for the init method with no property

    Returns
    -------
    init_str : str
        String containing the code to initialize a class with no property
    """

    init_str = ""

    init_str += TAB + "def __init__(self, init_dict=None):\n"
    init_str += TAB2 + '"""Constructor of the class. Can be use in two ways ' ":\n"
    init_str += (
        TAB2 + "- __init__ (arg1 = 1, arg3 = 5) every parameters "
        "have name and default values\n"
    )
    init_str += (
        TAB3 + "for Matrix, None will initialise the property with " "an empty Matrix\n"
    )
    init_str += TAB3 + "for pyleecan type, None will call the default " "constructor\n"
    init_str += (
        TAB2 + "- __init__ (init_dict = d) d must be a dictionnary "
        "wiht every properties as keys\n\n"
    )
    init_str += TAB2 + "ndarray or list can be given for Vector and Matrix\n"
    init_str += TAB2 + 'object or dict can be given for pyleecan Object"""\n\n'

    init_str += TAB2 + "if init_dict is not None:  # Initialisation by dict\n"
    init_str += TAB3 + "check_init_dict(init_dict, [])\n"

    init_str += (
        TAB2 + "# The class is frozen, for now it's impossible to "
        "add new properties\n"
    )
    init_str += TAB2 + "self.parent = None\n"
    init_str += TAB2 + "self._freeze()\n"

    return init_str
