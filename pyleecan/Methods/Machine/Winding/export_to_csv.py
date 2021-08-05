from ....Functions.Winding.gen_phase_list import gen_name

ZS_NAME = "Slot Id"
COIL_NAME = "Ntcoil"
RAD_NAME = "Rad Layer Id"
TAN_NAME = "Tan Layer Id"
SEP = ","


def export_to_csv(self, file_path=None, is_add_header=True, is_skip_empty=False):
    """Export the winding matrix to a csv file. One matrix for each phase
    Column Slot id, Ntcoil, Rad id, Tan id

    Parameters
    ----------
    self : Winding
        A: Winding object
    file_path : str
        Path to the file to save
    is_add_header : bool
        True to add first line and first column
    is_skip_empty : bool
        True to remove the lines with Ntcoil=0
    """

    # parse file_path
    if file_path[-4:] != ".csv":
        file_path += ".csv"

    # Get matrix
    wind_mat = self.get_connection_mat()
    Nrad = wind_mat.shape[0]
    Ntan = wind_mat.shape[1]
    Zs = wind_mat.shape[2]
    qs = wind_mat.shape[3]

    # Write the file
    csv_txt = ""
    if is_add_header:
        csv_txt = (
            '"'
            + str(wind_mat.shape)
            + '"'
            + SEP
            + ZS_NAME
            + SEP
            + COIL_NAME
            + SEP
            + RAD_NAME
            + SEP
            + TAN_NAME
            + "\n"
        )

    phases = gen_name(qs, is_add_phase=True)
    for ii, name in enumerate(phases):
        Nb_line = 0  # Add header on first line only
        for jj in range(Zs):
            for kk in range(Nrad):
                for ll in range(Ntan):
                    value = wind_mat[kk, ll, jj, ii]
                    if not (is_skip_empty and wind_mat[kk, ll, jj, ii] == 0):
                        if is_add_header and Nb_line == 0:
                            csv_txt += name + " Layout" + SEP
                        elif is_add_header:
                            csv_txt += SEP
                        csv_txt += str(jj) + SEP
                        csv_txt += str(value) + SEP
                        csv_txt += str(kk) + SEP
                        csv_txt += str(ll) + SEP + "\n"
                        Nb_line += 1
        # Separate each phase by an empty line
        csv_txt += "\n"

    # Write the csv file
    with open(file_path, "w") as csv_file:
        csv_file.write(csv_txt)
