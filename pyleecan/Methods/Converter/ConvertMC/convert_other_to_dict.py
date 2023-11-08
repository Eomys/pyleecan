from os.path import join, split


def convert_other_to_dict(self):
    """conversion file .mot in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object

    Returns:
        dict: dict with param present in file .mot
    """

    file_path = self.file_path
    liste_path = file_path.split(".")
    if not liste_path[-1] == "mot":
        raise NameError("the file is not a .mot, please select a .mot to convert")

    path = split(__file__)[0]
    file = open(join(path, file_path))

    other_dict = {}

    for line in file:
        # separation different part like .mot
        if line[:1] == "[":
            temp_dict = {}
            # deleted \n in line
            line = line.split("\n")
            other_dict[line[0]] = temp_dict

        elif line == "\n":
            pass

        else:
            # lb = line before =
            lb = line.split("=")
            value = lb[1].split("\n")

            # changement type after equal (value)
            if isint(value[0]):
                value[0] = int(value[0])

            elif value[0] == ("True"):
                value[0] = True
            elif value[0] == ("False"):
                value[0] = False

            elif isfloat(value[0]):
                value[0] = float(value[0])

            if value[0] == (""):
                pass
            else:
                temp_dict[lb[0]] = value[0]

    return other_dict


# conversion str in float
def isfloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


# conversion str in int
def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
