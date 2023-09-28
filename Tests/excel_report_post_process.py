import os
from os import walk
from os.path import isfile, join
import csv
import itertools
import pandas as pd
from Tests import TEST_DIR

"""
    Script to use after an excel report of the tests .
    (pytest --excelreport=report.xlsx)
    It allows to make the markers column more readable 
    and handier to sort the markers.
    There is also a verification for the time markers.

    Parameters
    ----------

    File at Test folder root named by report.xlsx

    Returns
    ---------

    Csv file with columns for differents types of markers.
"""

df = pd.read_excel(join(TEST_DIR, "report.xlsx"))
df.to_csv(join(TEST_DIR, "report.csv"))

# Additionnal tolerance time in seconds for the time marker verification
DELTA_TIME = 1

dict_markers = {
    "Machine": ["IPMSM", "SCIM", "SPMSM", "SIPMSM", "SynRM", "MachineUD"],
    "VarSimu": ["VarLoadCurrent", "VarParam", "SingleOP"],
    "Elec": ["EEC_PMSM", "EEC_SCIM"],
    "Magnetic": ["MagFEMM", "MagElmer"],
    "Force": ["ForceMT", "ForceTensor"],
    "Loss": ["Loss"],
    "Structurel": ["StructElmer"],
    "Topology": ["HoleUD", "SlotUD", "outer_rotor"],
    "Long": ["long_5s", "long_1m", "long_10m"],
    "Skip": ["skip"],
    "Other": ["MeshSol", "FEMM", "GMSH", "GMSH2D", "periodicity", "parallel"],
}

dict_time = {"long_5s": 5, "long_1m": 60, "long_10m": 600}

if __name__ == "__main__":
    nb_row = 0
    with open(join(TEST_DIR, "report.csv"), "r", encoding="utf8") as source:
        reader = csv.reader(
            source
        )  # Return n independent iterators from a single iterable.
        with open(
            join(TEST_DIR, "converted_report.csv"), "w", newline="", encoding="utf8"
        ) as result:
            writer = csv.writer(result, delimiter=";")
            for row in reader:
                # Copy Headers
                if nb_row == 0:
                    headers = row[1:] + list(dict_markers.keys())
                    writer.writerow(headers)

                # Copy other values
                else:
                    markers = row[9].split(", ")
                    markers_entry = [
                        "None" for idx in range(len(list(dict_markers.keys())))
                    ]
                    last_item = len(list(dict_markers.keys())) - 1

                    # Searching where to put the marker
                    for marker in markers:
                        index = 0
                        found = False
                        for key in dict_markers:
                            if marker in dict_markers[key]:
                                found = True
                                # If there is NONE, erase it
                                if markers_entry[index] == "None":
                                    markers_entry[index] = marker
                                # If not, just add the marker to the current marker
                                else:
                                    markers_entry[index] += ", " + marker
                            index += 1

                        # If not found, put the marker in OTHER column
                        if not found:
                            if markers_entry[last_item] == "None":
                                markers_entry[last_item] = marker
                            else:
                                markers_entry[last_item] += ", " + marker

                        # If time marker is inferior than the duration of the test, a message is sent
                        if marker in dict_time:
                            if int(dict_time[marker]) + DELTA_TIME < int(row[5][0]):
                                print(
                                    "Time marker can be updated for : "
                                    + row[1]
                                    + ". Line in excel : "
                                    + row[0]
                                    + ". Duration : "
                                    + row[5][0]
                                    + "s with marker : "
                                    + marker
                                    + "."
                                )

                    entry = row[1:] + markers_entry

                    writer.writerow(entry)
                nb_row = nb_row + 1
