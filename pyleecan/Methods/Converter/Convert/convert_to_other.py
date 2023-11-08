from pyleecan.Classes.ConvertMC import ConvertMC
from pyleecan.Methods.Converter.ConvertMC.convert import convert


def convert_to_other(machine):
    """conversion obj machine in dict

    Parameters
    ----------
    machine : Machine
        A pyleecan machine

    Returns
    ---------
    other_dict : dict
        A dict with the conversion obj machine

    """
    converter = ConvertMC()
    converter.is_P_to_other = True
    converter.machine = machine

    # conversion machine in dict
    converter.other_dict = convert(converter)
    return converter.other_dict
