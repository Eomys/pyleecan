from os.path import join, split
import re


def convert_mot_dict():
    # Ouvrir le fichier
    path = split(__file__)[0]
    file = open(join(path, "EMD240_v16.mot"))

    mot_dict = {}
    # utilisez readline() pour lire la première ligne
    for line in file:
        if line[:1] == "[":
            temp_dict = {}
            l = line.split("\n")
            mot_dict[l[0]] = temp_dict

        elif line == "\n":
            pass

        else:
            l = line.split("=")
            l1 = l[1].split("\n")

            if isint(l1[0]):
                l1[0] = int(l1[0])

            elif l1[0] == ("True"):
                l1[0] = True
            elif l1[0] == ("False"):
                l1[0] = False

            elif isfloat(l1[0]):
                l1[0] = float(l1[0])

            if l1[0] == (""):
                pass
            else:
                temp_dict[l[0]] = l1[0]

    dict_tmp = mot_dict["[Calc_Options]"]
    print(dict_tmp["Motor_Type"])
    return mot_dict


def isfloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    convert_mot_dict()
