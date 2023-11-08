from pyleecan.Classes.ConvertMC import ConvertMC
from pyleecan.Methods.Converter.ConvertMC.convert import convert


def convert_to_P(path_to_other):
    """conversion file in obj machine

    Parameters
    ----------
    path_to_other : str
        A path to file

    Returns
    ---------
    machine : Machine
        A pyleecan machine
    """
    converter = ConvertMC()
    converter.is_P_to_other = False
    converter.file_path = path_to_other

    # conversion file in dict
    converter.other_dict = converter.convert_other_to_dict()

    # conversion dict in machine
    machine = convert(converter)

    return machine
