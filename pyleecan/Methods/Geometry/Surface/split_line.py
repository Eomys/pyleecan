from ....Classes.Segment import Segment
from ....definitions import PACKAGE_NAME


def split_line(self, Z1, Z2, is_top=True, is_join=False, prop_dict_join=None):
    """Cut the Surface according to a line defined by two complex

    Parameters
    ----------
    self : Surface
        An Surface object
    Z1 : complex
        First point of the cutting Line
    Z2 : complex
        Second point of the cutting Line
    is_top : bool
        True to keep the part above the cutting line.
        "Above" is in the coordinate system with Z1 in 0 and Z2 on the X>0 axis
    is_join : bool
        True to join the split_list with Segment on the cutting line
    prop_dict_join : dict
        Property dict to set on the join line

    Returns
    -------
    split_surf : SurfLine
        The selected part of the Surface
    """

    # Dynamic import to avoid import loop
    module = __import__(PACKAGE_NAME + ".Classes.SurfLine", fromlist=["SurfLine"])
    SurfLine = getattr(module, "SurfLine")

    # Split all the lines of the surface
    lines = self.get_lines()
    split_list = list()
    for line in lines:
        split_list.extend(
            line.split_line(
                Z1=Z1,
                Z2=Z2,
                is_top=is_top,
                is_join=is_join,
                prop_dict_join=prop_dict_join,
            )
        )

    # Make sure that the surface is closed (if needed)
    if is_join:
        final_list = list()
        for ii in range(len(split_list) - 1):
            final_list.append(split_list[ii])
            if abs(split_list[ii].get_end() - split_list[ii + 1].get_begin()) > 1e-6:
                final_list.append(
                    Segment(
                        begin=split_list[ii].get_end(),
                        end=split_list[ii + 1].get_begin(),
                        prop_dict=prop_dict_join,
                    )
                )
        final_list.append(split_list[-1])
        # Add last line
        if abs(split_list[-1].get_end() - split_list[0].get_begin()) > 1e-6:
            final_list.append(
                Segment(
                    begin=split_list[-1].get_end(),
                    end=split_list[0].get_begin(),
                    prop_dict=prop_dict_join,
                )
            )
        split_list = final_list

    # Create the resulting surface and update ref point
    surf = SurfLine(label=self.label, line_list=split_list)
    surf.comp_point_ref(is_set=True)

    return surf
