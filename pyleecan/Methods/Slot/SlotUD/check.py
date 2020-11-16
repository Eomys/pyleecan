from ....Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the SlotUD is correctly defined"""

    if len(self.line_list) == 0:
        raise SlotCheckError("SlotUD must have at least one surface")

    for ii in range(len(self.line_list) - 1):
        if (
            abs(self.line_list[ii].get_end() - self.line_list[ii + 1].get_begin())
            > 1e-6
        ):
            raise SlotCheckError(
                "SlotUD line " + str(ii) + " and line " + str(ii + 1) + " doesn't match"
            )

    begin_id = self.wind_begin_index
    end_id = self.wind_end_index
    if begin_id is not None and end_id is not None:
        if begin_id > len(self.line_list):
            raise SlotCheckError(
                "SlotUD wind_begin_index is greater than line_list length"
            )
        if end_id > len(self.line_list):
            raise SlotCheckError(
                "SlotUD wind_end_index is greater than line_list length"
            )
        if begin_id > end_id:
            raise SlotCheckError(
                "SlotUD wind_begin_index is greater than wind_end_index"
            )
