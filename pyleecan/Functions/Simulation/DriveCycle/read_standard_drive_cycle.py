from os.path import join

from ....definitions import DATA_DIR
from .read_drive_cycle_csv import read_drive_cycle_csv


STANDARD_DRIVE_CYCLES = {
    "nedc": "NEDC_segment.csv",
    "nedc_segment": "NEDC_segment.csv",
    "wltp": "WLTP_class3_segment.csv",
    "wltp_class3": "WLTP_class3_segment.csv",
    "wltp_class3_segment": "WLTP_class3_segment.csv",
}


def list_standard_drive_cycles():
    """Return the built-in lightweight drive-cycle identifiers."""

    return tuple(sorted(STANDARD_DRIVE_CYCLES))


def read_standard_drive_cycle(name, column_map=None):
    """Read a packaged lightweight drive-cycle CSV by name.

    Parameters
    ----------
    name : str
        Built-in identifier such as ``"nedc"`` or ``"wltp_class3"``.
    column_map : dict, optional
        Optional canonical-column mapping forwarded to ``read_drive_cycle_csv``.

    Returns
    -------
    trajectory : dict
        Validated trajectory dictionary with at least ``time``, ``N0`` and
        ``Tem_av`` arrays when using the packaged files.
    """

    key = str(name).strip().lower().replace("-", "_").replace(" ", "_")
    if key not in STANDARD_DRIVE_CYCLES:
        available = ", ".join(list_standard_drive_cycles())
        raise ValueError(f"Unknown drive cycle '{name}'. Available cycles: {available}")

    return read_drive_cycle_csv(
        join(DATA_DIR, "DriveCycle", STANDARD_DRIVE_CYCLES[key]),
        column_map=column_map,
    )
