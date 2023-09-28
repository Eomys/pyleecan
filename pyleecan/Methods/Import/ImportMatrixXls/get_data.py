# -*- coding: utf-8 -*-
from pandas import read_excel, ExcelFile
from ....Methods.Import.ImportMatrixXls import XlsFileError
from os.path import isfile

from ....Functions.path_tools import abs_file_path


def get_data(self):
    """Return the object's matrix

    Parameters
    ----------
    self : ImportMatrixVal
        An ImportMatrixVal object

    Returns
    -------
    matrix: ndarray
        The object's matrix

    """
    file_path = abs_file_path(self.file_path, is_check=False)
    if not isfile(file_path):
        raise XlsFileError("ERROR: The xls file doesn't exist " + self.file_path)
    if self.usecols == "":
        self.usecols = None

    if self.is_allsheets:
        xl = ExcelFile("file.xlsx")
        Nsheets = len(xl.sheet_names)
        for i in range(Nsheets):
            df = read_excel(
                file_path, i, header=None, usecols=self.usecols, skiprows=self.skiprows
            )
            values = df.values
            # Extract axes
            if self.axes_colrows is not None:
                axes_dict = {}
                if len(axes_dict) == 1:
                    is_first = False
                else:
                    is_first = True
                for axis in self.axes_colrows:
                    if self.axes_colrows[axis] == "1":
                        if is_first:
                            axes_dict[axis] = values[0, 1:]
                            is_first = False
                        else:
                            axes_dict[axis] = values[0, :]
                        values = values[1:, :]
                    elif self.axes_colrows[axis] == "A":
                        if is_first:
                            axes_dict[axis] = values[1:, 0]
                            is_first = False
                        else:
                            axes_dict[axis] = values[:, 0]
                        values = values[:, 1:]
                    else:
                        raise Exception(
                            "ERROR: axes_colrows should contain either '1' or 'A'"
                        )

            # Transpose if necessary
            values = self.edit_matrix(values)

            # Store in 3D matrix
            if i == 0:
                values_3d = values[..., None]
            else:
                values_3d.append(values_3d, values[..., None], axis=-1)

        if self.axes_colrows is not None:
            return values_3d, axes_dict
        else:
            return values_3d

    else:
        df = read_excel(
            file_path,
            self.sheet,
            header=None,
            usecols=self.usecols,
            skiprows=self.skiprows,
        )
        values = df.values

        # Extract axes
        if self.axes_colrows is not None:
            axes_dict = {}
            if len(axes_dict) == 1:
                is_first = False
            else:
                is_first = True
            for axis in self.axes_colrows:
                if self.axes_colrows[axis] == "1":
                    if is_first:
                        axes_dict[axis] = values[0, 1:]
                        is_first = False
                    else:
                        axes_dict[axis] = values[0, :]
                    values = values[1:, :]
                elif self.axes_colrows[axis] == "A":
                    if is_first:
                        axes_dict[axis] = values[1:, 0]
                        is_first = False
                    else:
                        axes_dict[axis] = values[:, 0]
                    values = values[:, 1:]
                else:
                    raise Exception(
                        "ERROR: axes_colrows should contain either '1' or 'A'"
                    )
        else:
            axes_dict = None

        # Transpose if necessary
        values = self.edit_matrix(values)

        if self.axes_colrows is not None:
            return values, axes_dict
        else:
            return values
