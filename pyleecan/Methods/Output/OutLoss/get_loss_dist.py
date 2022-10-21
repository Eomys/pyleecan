# -*- coding: utf-8 -*-

# TODO add a 'loss_type' info to model to get loss by type rather than index
def get_loss_dist(self, part_label="Stator", index=None):
    """Convenience method to get some specific loss distribution component.

    Parameters
    ----------
    self : OutLoss
        an OutLoss object

    part_label : str
        Label of the machine part, e.g. 'Stator'

    index : int
        Index of the Loss Model

    Returns
    -------
    meshsolution : MeshSolution
        MeshSoltution of the requested loss component

    """
    logger = self.get_logger()

    # check
    if not part_label in self.loss_index.keys():
        logger.warning(
            f"OutLoss.get_loss_dist(): No part with label " + f"'{part_label}' found."
        )
        return None

    # get the index
    if self.loss_index[part_label].keys():
        if index is None:
            keys = [key for key in self.loss_index[part_label].keys()]
            index = keys[0]

        if index not in self.loss_index[part_label].keys():
            logger.warning(
                f"OutLoss.get_loss_dist(): Part '{part_label}' "
                + f"got no loss index {index}."
            )
            return None

        ii = self.loss_index[part_label][index]

        return self.meshsol_list[ii]

    # if there are no loss on the part
    else:
        logger.warning(
            f"OutLoss.get_loss_dist(): Part '{part_label}' got no losses output."
        )
        return None
