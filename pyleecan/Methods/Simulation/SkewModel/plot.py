# -*- coding: utf-8 -*-

from ....Functions.init_fig import init_fig


def plot(self):
    """Plots skew for all laminations 
    
    Parameters
    ----------
    self : SkewModel
        a SkewModel object

    """

    (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")

    # Stator skew
    self.parent.parent.machine.stator.skew.plot(
        skew_axis=self.z_list, fig=fig, lam_name="Stator"
    )

    # Rotor skew
    self.parent.parent.machine.rotor.skew.plot(
        skew_axis=self.z_list, fig=fig, lam_name="Rotor"
    )
