from ....Classes.Segment import Segment
from ....definitions import PACKAGE_NAME


def split_line(self, Z1, Z2, is_join=False, prop_dict_join=None):
    """Cut the Surface in two part according to a line defined by two complex
    "Above" is in the coordinate system with Z1 in 0 and Z2 on the X>0 axis

    Parameters
    ----------
    self : Surface
        An Surface object
    Z1 : complex
        First point of the cutting Line
    Z2 : complex
        Second point of the cutting Line
    is_join : bool
        True to join the split_list with Segment on the cutting line
    prop_dict_join : dict
        Property dict to set on the join line

    Returns
    -------
    top_surf, bot_surf : SurfLine
        The two part of the Surface
        (one can be None if the line doesn't cut the surface)
    """

    # Dynamic import to avoid import loop
    module = __import__(PACKAGE_NAME + ".Classes.SurfLine", fromlist=["SurfLine"])
    SurfLine = getattr(module, "SurfLine")

    # Split all the lines of the surface
    lines = self.get_lines()
    top_split_list = list()  # List of line of the top part
    bot_split_list = list()  # List of line of the bot part
    for line in lines:
        line_top, line_bot = line.split_line(
            Z1=Z1,
            Z2=Z2,
            is_join=is_join,
            prop_dict_join=prop_dict_join,
        )
        top_split_list.extend(line_top)
        bot_split_list.extend(line_bot)

    # Make sure that the surface is closed (if needed)
    if is_join:
        top_split_list = join_surf_line(top_split_list, prop_dict_join)
        bot_split_list = join_surf_line(bot_split_list, prop_dict_join)

    # Create the resulting surface and update ref point
    if len(top_split_list) > 0:
        top_surf = SurfLine(label=self.label, line_list=top_split_list)
        top_surf.comp_point_ref(is_set=True)
    else:
        top_surf = None

    if len(bot_split_list) > 0:
        bot_surf = SurfLine(label=self.label, line_list=bot_split_list)
        bot_surf.comp_point_ref(is_set=True)
    else:
        bot_surf = None

    return top_surf, bot_surf


def join_surf_line(split_list, prop_dict_join):
    """Join the surface to make sur the the surface is closed"""
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
    return final_list
