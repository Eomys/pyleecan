# -*- coding: utf-8 -*-


def get_loss(self, part_label="Stator", index=None):
    """Convenience method to get some specific loss component time data.

    Parameters
    ----------
    self : OutLoss
        an OutLoss object

    part : str
        Label of the machine part, e.g. 'Stator'

    index : int
        Index of the Loss Model

    Returns
    -------
    DataTime : DataTime
        Time data of the requested loss component

    """
    logger = self.get_logger()

    # check
    if not part_label in self.loss_index.keys():
        logger.warning(
            f"OutLoss.get_loss(): No part with label " + f"'{part_label}' found."
        )
        return None

    # get index
    if self.loss_index[part_label].keys():
        if index is None:
            keys = [key for key in self.loss_index[part_label].keys()]
            index = keys[0]

        if index not in self.loss_index[part_label].keys():
            logger.warning(
                f"OutLoss.get_loss(): Part '{part_label}' got no loss index {index}."
            )
            return None

        ii = self.loss_index[part_label][index]

        return self.loss_list[ii]

    # if there are no loss on the part
    else:
        logger.warning(f"OutLoss.get_loss(): Part '{part_label}' got no losses output.")
        return None
