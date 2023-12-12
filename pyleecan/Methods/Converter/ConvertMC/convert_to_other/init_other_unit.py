from numpy import pi


def init_other_unit(self):
    """Selects units and creates a dict with all conversion

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    self.other_unit_dict = {}

    # set length
    # pyleecan unit=m, MC unit = mm
    self.other_unit_dict["m"] = 0.001

    self.other_unit_dict["rad"] = 1
    self.other_unit_dict["deg"] = 180 / pi

    # conversion electrical degree
    pole_pair_number = self.machine.get_pole_pair_number()
    self.other_unit_dict["ED"] = (4 / pole_pair_number) * (pi / 180)

    self.other_unit_dict[None] = 1  # No unit => No scale
    self.other_unit_dict[""] = 1  # No unit => No scale
    self.other_unit_dict["-"] = 1  # No unit => No scale
    self.other_unit_dict["[]"] = 1  # No unit => No scale
