from numpy import pi


def init_other_unit(self):
    """Selection unit and create a dict with all conversion

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object

    Returns
    ---------
    other_unit_dict : dict
        dict with unit to make conversion
    """
    other_unit_dict = {}

    # set length
    # pyleecan m we want in mm
    other_unit_dict["m"] = 1000
    # we want to have m so we need to multiply by 1000

    other_unit_dict["rad"] = 1

    # conversion electrical degree
    pole_pair_number = self.machine.get_pole_pair_number()
    other_unit_dict["ED"] = (pole_pair_number) * (180 / pi)

    other_unit_dict[""] = 1

    return other_unit_dict
