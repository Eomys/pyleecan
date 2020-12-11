from ...Classes.SurfLine import SurfLine
from ...Classes.Segment import Segment
from ...Classes.Arc import Arc
from ...Classes.Arc2 import Arc2


class SurfaceError(Exception):
    pass


def create_surface(line_list):
    """Create a surface from a list of Line

    Parameters
    ----------
    line_list: list
        list of line forming the surface

    Returns
    -------
    surface: SurfLine
    """
    ordered_list = [line_list.pop(0)]
    first_element = ordered_list[0]
    if isinstance(first_element, (Arc, Segment)):
        end = first_element.get_end()
    else:
        raise NotImplementedError(
            "The function create_surface only handles Arc and Segment lines."
        )
    surface_points = []
    for _ in range(len(line_list)):
        surface_points.append(end)
        found = False
        for line in line_list[:]:
            if abs(end - line.get_begin()) < 1e-09:
                new_line = line.copy()
                new_line.begin = end
                ordered_list.append(new_line)
                end = new_line.get_end()
                found = True
                line_list.remove(line)
                break
            elif abs(end - line.get_end()) < 1e-09:
                if isinstance(line, Segment):
                    new_line = Segment(begin=end, end=(line.begin))
                elif isinstance(line, Arc):
                    new_line = Arc2(
                        begin=end, center=(line.get_center()), angle=(-line.get_angle())
                    )
                else:
                    raise NotImplementedError(
                        "The function create_surface only handles Arc and Segment lines."
                    )
                ordered_list.append(new_line)
                end = new_line.get_end()
                line_list.remove(line)
                found = True
                break

        assert found, SurfaceError("Cannot find the next line of the surface")

    ordered_list[0].begin = ordered_list[(-1)].get_end()
    return SurfLine(
        line_list=ordered_list, point_ref=(sum(surface_points) / len(surface_points))
    )
