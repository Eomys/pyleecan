import csv

import numpy as np

from ._utils import DEFAULT_COLUMN_ALIASES, validate_trajectory_dict


def _resolve_fieldnames(fieldnames, column_map=None):
    """Resolve canonical drive-cycle field names from a CSV header."""

    header_lookup = {name.strip().lower(): name for name in fieldnames}
    resolved = dict()

    if column_map is None:
        column_map = dict()

    for canonical, aliases in DEFAULT_COLUMN_ALIASES.items():
        if canonical in column_map:
            source_name = column_map[canonical]
            if source_name not in fieldnames:
                raise ValueError(
                    f"CSV column '{source_name}' declared for {canonical} was not found"
                )
            resolved[canonical] = source_name
            continue

        for alias in aliases:
            source_name = header_lookup.get(alias.lower())
            if source_name is not None:
                resolved[canonical] = source_name
                break

    if "time" not in resolved or "N0" not in resolved:
        raise ValueError("CSV must provide time and N0 columns")

    return resolved


def read_drive_cycle_csv(file_path, column_map=None, delimiter=","):
    """Read a drive-cycle CSV file into a validated trajectory dictionary.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.
    column_map : dict
        Optional mapping from canonical names (time, N0, Tem_av, Pem_av, Udc,
        T_amb, T_coolant) to CSV headers.
    delimiter : str
        CSV delimiter.

    Returns
    -------
    trajectory : dict
        Dictionary of 1D numpy arrays using canonical names.
    """

    with open(file_path, newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        if reader.fieldnames is None:
            raise ValueError(f"CSV file '{file_path}' does not contain a header row")

        resolved = _resolve_fieldnames(reader.fieldnames, column_map=column_map)
        trajectory = {key: [] for key in resolved}

        for line_number, row in enumerate(reader, start=2):
            for canonical, source_name in resolved.items():
                raw_value = row.get(source_name)
                if raw_value is None or raw_value == "":
                    raise ValueError(
                        f"Missing value for column '{source_name}' at line {line_number}"
                    )
                try:
                    trajectory[canonical].append(float(raw_value))
                except ValueError as error:
                    raise ValueError(
                        f"Unable to parse value '{raw_value}' for column "
                        f"'{source_name}' at line {line_number}"
                    ) from error

    return validate_trajectory_dict(
        {key: np.asarray(values, dtype=float) for key, values in trajectory.items()},
        require_target=False,
    )
