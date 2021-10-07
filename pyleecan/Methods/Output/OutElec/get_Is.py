def get_Is(self, Time=None, is_current_harm=False):
    """Return the stator current DataTime object

    Parameters
    ----------
    self : OutElec
        an OutElec object

    """
    # Calculate stator currents if Is is not in OutElec
    if self.Is is None or not is_current_harm:
        Is = self.get_I_fund(Time=Time)

    if self.Is is None:
        self.Is = Is

    return self.Is
