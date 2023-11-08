from numpy import pi


def set_unit(self, unit):
    # appel methods dans convertMC -> unit -> list
    # self.other_dict["[Units]"]["Units_Length"]

    if unit == "m":
        unit = 1
    elif unit == "mm":
        unit = 1000
    elif unit == "rad":
        unit = 1
    elif unit == "deg":
        unit = 2 * pi / 180
    elif unit == "ED":  # pole_pair_number
        unit = 1
    elif unit == "":
        unit = 1
    else:
        unit = 1

    return unit
