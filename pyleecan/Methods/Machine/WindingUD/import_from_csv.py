from os.path import isfile
from csv import reader
from numpy import zeros, amax

ZS_COL = 0  # Slot id
COIL_COL = 1  # Ntcoil (+/-)
RAD_COL = 2  # Rad layer id
TAN_COL = 3  # Tan layer id


def import_from_csv(self, file_path=None):
    """Import the winding matrix from a csv file.
    One matrix for each phase
    Column Slot id, Ntcoil, Rad id, Tan id

    Parameters
    ----------
    self : WindingUD
        A: WindingUD object
    file_path : str
        Path to the file to load
    """

    # parse file_path
    if file_path[-4:] != ".csv":
        file_path += ".csv"
    if not isfile(file_path):
        raise FileNotFoundError(file_path + " is not a csv winding file")

    with open(file_path, "r") as csv_file:
        line_list = list(reader(csv_file))
        # Get matrix size
        if "(" in line_list[0][0] and ")" in line_list[0][0]:
            is_header, offset = True, 1
            wind_shape = eval(line_list[0][0])
        else:  # No Header
            is_header, offset = False, 0
            Nrad, Ntan, Zs, qs = -1, -1, -1, 0
            for line in line_list:
                if len(line) == 0:
                    qs += 1
                else:
                    Nrad = max(Nrad, int(line[RAD_COL]))
                    Ntan = max(Ntan, int(line[TAN_COL]))
                    Zs = max(Zs, int(line[ZS_COL]))
            wind_shape = (Nrad + 1, Ntan + 1, Zs + 1, qs)

        if self.parent is not None and self.parent.slot is not None:
            assert self.parent.slot.Zs == wind_shape[2], (
                "Mismatch between Lamination Zs ("
                + str(self.parent.slot.Zs)
                + ") and imported winding Zs ("
                + str(wind_shape[2])
                + ")"
            )
        self.clean()  # Remove periodicity
        self.wind_mat = zeros(wind_shape)

        # Load matrix
        qs_id = 0
        if is_header:  # Remove first line
            line_list.pop(0)
        for line in line_list:
            if len(line) == 0 or line[ZS_COL + offset] == "":
                qs_id += 1
            else:
                Rad_id = int(float(line[RAD_COL + offset]))
                Tan_id = int(float(line[TAN_COL + offset]))
                Zs_id = int(float(line[ZS_COL + offset]))
                self.wind_mat[Rad_id, Tan_id, Zs_id, qs_id] = line[COIL_COL + offset]

    # Update property
    self.Nlayer = wind_shape[0] * wind_shape[1]
    self.qs = wind_shape[3]
    self.Ntcoil = amax(self.wind_mat)
