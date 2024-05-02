from ...Classes.Segment import Segment
from ...Classes.Arc1 import Arc1
from ...Classes.Arc2 import Arc2
from math import cos, sin, pi
from logging import getLogger
from ...loggers import GUI_LOG_NAME
from ...Classes._FEMMHandler import _FEMMHandler
from qtpy.QtWidgets import QMessageBox


def dxf_to_pyleecan_list(entities):
    """
    Create the pyleecan object corresponding to the DXF entities
    Currently handles Line and Arc
    """
    obj_list = []
    for entity in entities:
        dxftype = entity.dxftype()
        dxf = entity.dxf
        if dxftype == "LINE":  # {"LINE", "XLINE", "RAY"}:
            start = complex(*dxf.start[:-1])
            end = complex(*dxf.end[:-1])
            obj_list.append(Segment(start, end))
        elif dxftype == "ARC":
            start_angle = dxf.start_angle / 180 * pi
            end_angle = dxf.end_angle / 180 * pi
            if start_angle > pi:
                start_angle -= 2 * pi
            if end_angle > pi:
                end_angle -= 2 * pi
            center = complex(*dxf.center[:-1])
            begin = (
                dxf.center[0]
                + dxf.radius * cos(start_angle)
                + 1j * (dxf.center[1] + dxf.radius * sin(start_angle))
            )
            end = (
                dxf.center[0]
                + dxf.radius * cos(end_angle)
                + 1j * (dxf.center[1] + dxf.radius * sin(end_angle))
            )
            obj_list.append(
                Arc1(begin=begin, end=end, radius=dxf.radius, is_trigo_direction=True)
            )
        else:
            getLogger(GUI_LOG_NAME).warning(
                "Unable to load dxftype="
                + str(dxftype)
                + ". Removing element from preview"
            )

    return obj_list


def convert_dxf_with_FEMM(self, file_path, tol):
    """Convert a DXF file with FEMM:
    - Merge point according to tolerance
    - Convert lines to Arc and Segments

    Parameters
    ----------
    self : (DXF_Hole, DXF_Slot, DXF_Surf)
        GUI DXF widget
    file_path : str
        Path to the file to convert
    tol : float
        Tolerance to merge point [local unit]
    """
    conv_path = file_path[:-4] + "_converted.dxf"
    # Read/convert DXF file
    try:
        femm = _FEMMHandler()
        femm.openfemm(1)
        femm.newdocument(0)
        femm.mi_readdxf2(file_path, tol)
    except Exception as e:
        err_msg = "Error while importing dxf file " + file_path + " :\n" + str(e)
        if "Orphaned" in str(e):  # Some lines may have issues but we can continue
            getLogger(GUI_LOG_NAME).warning(err_msg)
            # No popup
        else:
            getLogger(GUI_LOG_NAME).error(err_msg)
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr(err_msg),
            )
            # Keep FEMM open
            return file_path  # Continue with original file

    # Saving converted file
    try:
        femm.mi_savedxf2(conv_path, tol)
    except Exception as e:
        err_msg = "Error while saving dxf file to " + conv_path + " :\n" + str(e)
        getLogger(GUI_LOG_NAME).error(err_msg)
        QMessageBox().critical(
            self,
            self.tr("Error"),
            self.tr(err_msg),
        )
        # Keep FEMM open
        return file_path  # Continue with original file

    # Close FEMM and continue with converted file
    femm.mi_close()
    return conv_path
