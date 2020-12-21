# -*- coding: utf-8 -*-


def get_loss(self, loss_type="Iron", label="Stator", index=0):
    """Convenience method to get some specific loss component time data.

    Parameter
    ---------
    self : OutLoss
        an OutLoss object

    loss_type : str
        Type of loss, e.g. 'Iron', 'Magnet', 'Winding'

    label : str
        Label of the machine part, e.g. 'Stator'

    index : int
        Index of the Loss Model

    Return
    ------
    DataTime : DataTime
        Time data of the requested loss component

    """
    # check if loss_type exists
    loss_dict = getattr(self, loss_type.lower(), None)
    if loss_dict is not None:
        data_list = loss_dict.get(label, None)
        if -len(data_list) <= index < len(data_list):
            return data_list[index]

    return None
