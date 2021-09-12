from ....Methods.Slot.Slot import SlotCheckError


def check(self):
    """Check that the SlotUD2 is correctly defined"""

    if self.line_list is None:
        self.line_list = list()

    if len(self.line_list) == 0:
        raise SlotCheckError("SlotUD2 must have at least one line")

    for ii in range(len(self.line_list) - 1):
        if (
            abs(self.line_list[ii].get_end() - self.line_list[ii + 1].get_begin())
            > 1e-6
        ):
            raise SlotCheckError(
                "SlotUD line " + str(ii) + " and line " + str(ii + 1) + " doesn't match"
            )
