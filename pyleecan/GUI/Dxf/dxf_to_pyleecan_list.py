from ...Classes.Segment import Segment
from ...Classes.Arc1 import Arc1
from ...Classes.Arc2 import Arc2
from math import cos, sin, pi
from logging import getLogger
from ...loggers import GUI_LOG_NAME


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
