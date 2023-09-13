import os
from os import walk
from os.path import isfile, join
from ...definitions import MAIN_DIR, DOC_DIR, INT_DIR
import csv

if __name__ == "__main__":
    # Read the open source doc
    for dirpath, dirnames, filenames in walk(DOC_DIR):
        for file_name in filenames:
            input_file = join(dirpath, file_name)
            output_file = join(dirpath, file_name[0:-4] + "_tmp.csv")
            cols_to_remove = []  # Column indexes to be removed (starts at 0)
            # cols_to_remove = sorted(cols_to_remove, reverse=True)  # Reverse so we remove from the end first
            row_count = 0  # Current amount of rows processed

            with open(input_file, "r") as source:
                reader = csv.reader(source)
                with open(output_file, "w", newline="") as result:
                    writer = csv.writer(result)
                    for row in reader:
                        if row_count == 0:
                            if "Observations" in row:
                                cols_to_remove.append(row.index("Observations"))
                            if "Level" in row:
                                cols_to_remove.append(row.index("Level"))
                            if "Daughter classes" in row:
                                cols_to_remove.append(row.index("Daughter classes"))
                            if "Description (FR)" in row:
                                cols_to_remove.append(row.index("Description (FR)"))
                            if "Classe Fille" in row:
                                cols_to_remove.append(row.index("Classe Fille"))

                            cols_to_remove = sorted(
                                cols_to_remove, reverse=True
                            )  # Reverse so we remove from the end first
                        row_count += 1
                        # print('\r{0}'.format(row_count), end='')  # Print rows processed
                        for col_index in cols_to_remove:
                            del row[col_index]
                        writer.writerow(row)

            os.remove(input_file)
            os.rename(output_file, input_file)
