# -*- coding: utf-8 -*-


def get_loss_dist(self, loss_type="Iron", label="Stator", index=0):
    """Convenience method to get some specific loss distribution component.

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
    meshsolution : MeshSolution
        MeshSoltution of the requested loss component

    """
    # check if loss_type exists
    loss_dict = self.meshsolution.get(loss_type, None)
    if loss_dict is not None:
        mshsol_list = loss_dict.get(label, None)
        if -len(mshsol_list) <= index < len(mshsol_list):
            return mshsol_list[index]

    return None
