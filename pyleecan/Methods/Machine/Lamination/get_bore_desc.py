from numpy import exp, pi, angle

from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3


def get_bore_desc(self, sym=1, prop_dict=None):
    """This method returns an ordered description of the elements
    that defines the bore radius of the lamination

    Parameters
    ----------
    self : Lamination
        A Lamination object
    prop_dict : dict
        Property dictionary to apply on the lines

    Returns
    -------
    bore_desc : list
        list of dictionary with key: "begin_angle", "end_angle", "obj"
    bore_line : list
        list of lines to draw the bore radius
    """

    is_notch = self.notch and any([not notch.is_yoke for notch in self.notch])

    if not is_notch:
        bore_lines = self.get_bore_line(sym=1, prop_dict=prop_dict)

        # Cut the bore lines for symmetry if needed
        if sym != 1:
            # First cut Ox
            first_cut = list()
            for line in bore_lines:
                top, _ = line.split_line(-1.2 * self.Rext, 1.2 * self.Rext)
                first_cut.extend(top)
            if sym > 2:
                # Second cut 0Sym
                bore_lines = list()
                for line in first_cut:
                    top, _ = line.split_line(
                        1.2 * self.Rext * exp(1j * 2 * pi / sym), 0
                    )
                    bore_lines.extend(top)
            else:  # Cutting lamination in half
                bore_lines = first_cut

        return None, bore_lines

    bore_desc = list()
    if is_notch:  # Notches => Generate Full lines and cut (if needed)
        # Get all the notches and bore lines
        notch_list = self.get_notch_list(sym=1, is_yoke=False)
        bore_lines = self.get_bore_line(prop_dict=prop_dict)

        # generate bore_line description
        bore_list = list()
        for bore_line in bore_lines:
            desc = dict()
            desc["begin_angle"] = angle(bore_line.get_begin())
            desc["end_angle"] = angle(bore_line.get_end())
            desc["obj"] = bore_line
            bore_list.append(desc)

        # cut the actual bore lines with the notches
        # # TODO: case where starting or end points of bore and notch are the same
        for notch in notch_list:
            bore_list_new = list()
            for bore in bore_list:
                lines = list()
                notch_begin, notch_end = notch["begin_angle"], notch["end_angle"]
                bore_begin, bore_end = bore["begin_angle"], bore["end_angle"]
                if is_angle_between(notch_begin, bore_begin, bore_end):
                    _, line = bore["obj"].split_line(0, notch["obj"][0].get_begin())
                    lines.extend(line)
                if is_angle_between(notch_end, bore_begin, bore_end):
                    line, _ = bore["obj"].split_line(0, notch["obj"][-1].get_end())
                    lines.extend(line)

                # TODO check that there is only one line per split

                if not lines:
                    bore_list_new.append(bore)
                else:
                    for line in lines:
                        desc = dict()
                        desc["begin_angle"] = angle(line.get_begin())
                        desc["end_angle"] = angle(line.get_end())
                        desc["obj"] = line
                        bore_list_new.append(desc)

            bore_list = bore_list_new

        # sort lists in the range from 0 to 2pi for later merge
        bore_list = sorted(bore_list, key=lambda k: k["begin_angle"] % (2 * pi))
        notch_list = sorted(notch_list, key=lambda k: k["begin_angle"] % (2 * pi))

        # merge bore and notch lists by angle
        while notch_list or bore_list:
            if notch_list and bore_list:
                ang_notch = notch_list[0]["begin_angle"] % (2 * pi)
                ang_bore = bore_list[0]["begin_angle"] % (2 * pi)
                if ang_notch < ang_bore:
                    line = notch_list.pop(0)
                else:
                    line = bore_list.pop(0)
            elif not notch_list:
                line = bore_list.pop(0)
            else:
                line = notch_list.pop(0)

            bore_desc.append(line)

        # move line that crosses x axis to first position otherwise split will not work
        if bore_desc[-1]["begin_angle"] < 0 and bore_desc[-1]["end_angle"] > 0:
            bore_desc.insert(0, bore_desc.pop(-1))

        bore_lines = _convert_desc(bore_desc, prop_dict)

        # Cut the bore lines for symmetry if needed
        if sym != 1:
            # First cut Ox
            first_cut = list()
            for line in bore_lines:
                top, _ = line.split_line(-1.2 * self.Rext, 1.2 * self.Rext)
                first_cut.extend(top)
            if sym > 2:
                # Second cut 0Sym
                bore_lines = list()
                for line in first_cut:
                    top, _ = line.split_line(
                        1.2 * self.Rext * exp(1j * 2 * pi / sym), 0
                    )
                    bore_lines.extend(top)
            else:  # Cutting lamination in half
                bore_lines = first_cut

        return bore_desc, bore_lines


def _convert_desc(bore_desc, prop_dict):
    # Convert the description to lines
    bore_lines = list()
    for bore in bore_desc:
        if isinstance(bore["obj"], (Arc1, Arc3)):
            # Set bore line properties
            if bore["obj"].prop_dict is None:
                bore["obj"].prop_dict = prop_dict
            else:
                bore["obj"].prop_dict.update(prop_dict)
            bore_lines.append(bore["obj"])
        elif "lines" in bore:  # Duplicated slot
            for line in bore["lines"]:
                bore_lines.append(line.copy())
                bore_lines[-1].rotate((bore["begin_angle"] + bore["end_angle"]) / 2)
        else:  # Notches
            bore_lines.extend(bore["obj"])
    return bore_lines


def is_angle_between(angle, begin, end):
    """
    Check if angle is between begin and end
    """
    # normalize all angles to [0, 2pi]
    angle = angle % (2 * pi)
    begin = begin % (2 * pi)
    end = end % (2 * pi)

    if begin > end:
        # check if angle is between [begin, 2pi] or [0, end]
        return (angle > begin) or (angle < end)

    return (angle > begin) and (angle < end)
