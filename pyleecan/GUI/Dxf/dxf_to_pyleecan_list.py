from ...Classes.Segment import Segment
from ...Classes.Arc2 import Arc2
from math import cos, sin, pi


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
        elif dxftype == "CIRCLE":
            raise NotImplementedError
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
            angle = end_angle - start_angle
            obj_list.append(Arc2(begin=begin, center=center, angle=angle))
        else:
            raise NotImplementedError

    return obj_list
