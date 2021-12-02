def get_Is(
    self, Time=None, is_dqh=False, is_fund_only=False, is_harm_only=False, is_freq=None
):
    """Return the stator current DataND object

    Parameters
    ----------
    self : OutElec
        an OutElec object
    Time : Data
        Time axis
    is_dqh : bool
        True to rotate in DQH frame
    is_fund_only : bool
        True to return only fundamental component
    is_harm_only : bool
        True to return only components at higher frequencies than fundamental component
    is_freq: bool
        None not to force to return DataFreq/DataTime, True to force to return DataFreq, False to force to return DataTime

    Returns
    -------
    Is: DataND
        stator current
    """

    label = self.parent.simu.machine.stator.get_label()
    Idq_dict = self.OP.get_Id_Iq()

    data_dict = {
        "name": "Stator current",
        "unit": "A",
        "symbol": "I_s",
        "lam_label": label,
        "Ad": Idq_dict["Id"],
        "Aq": Idq_dict["Iq"],
    }

    Is = self.get_electrical(
        data_dict,
        Time=Time,
        is_dqh=is_dqh,
        is_fund_only=is_fund_only,
        is_harm_only=is_harm_only,
        is_freq=is_freq,
    )

    return Is
