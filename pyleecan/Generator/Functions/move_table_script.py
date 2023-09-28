"""This script enables to go from two tables side by side (properties left, method right)
to two tables on top of eachother (properties on top, method bellow)
It also add the "as_dict Type" column for properties
"""
from os import walk, remove, rename
from os.path import isfile, join
from pyleecan.definitions import DOC_DIR
import csv

IS_OVERWRITE = True  # True to replace the files in place
if __name__ == "__main__":
    # Read all the csv files
    for dirpath, dirnames, filenames in walk(DOC_DIR):
        for file_name in filenames:
            input_file = join(dirpath, file_name)
            output_file = join(dirpath, file_name[0:-4] + "_tmp.csv")
            # Remove the old result file (if it exist)
            if isfile(output_file):
                remove(output_file)

            if "_tmp.csv" not in input_file:
                print("Converting " + input_file)
                with open(output_file, "w", newline="") as result:
                    writer = csv.writer(result)
                    # Read file to extract property part first
                    with open(input_file, "r") as source:
                        reader = csv.reader(source)
                        row_count = 0  # Current amount of rows processed
                        for row in reader:
                            if row[0] not in ["", None]:
                                # Add new column header "as_dict Type"
                                if row_count == 0:
                                    writer.writerow(row[:8] + ["as_dict Type"])
                                else:
                                    writer.writerow(row[:8])
                            row_count += 1
                    # Add empty line
                    writer.writerow(["", ""])
                    # Read file to extract method part
                    with open(input_file, "r") as source:
                        reader = csv.reader(source)
                        for row in reader:
                            if row[11] not in ["", None] or row[12] not in ["", None]:
                                writer.writerow(row[9:])
            if IS_OVERWRITE:
                remove(input_file)
                rename(output_file, input_file)
    print("Done")
