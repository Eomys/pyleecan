# -*- coding: utf-8 -*-
"""@package

@date Created on Wed Jan 13 11:17:10 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from matplotlib.pyplot import subplots


def init_fig(fig):
    """Get all the handle and legend of a figure or initialize them
    (for matplotlib)

    Parameters
    ----------
    fig : Matplotlib.figure.Figure
        The figure to get the handle from (can be None)

    Returns
    -------
    (fig,axes,patch_leg,label_leg): Matplotlib.figure.Figure, matplotlib.axes._subplots.AxesSubplot, patch, string
        Figure handle, Axes Handle, List of legend patches, List of legend label

    """
    if fig is None:
        # Create a new figure with empty legend
        fig, axes = subplots()
        patch_leg, label_leg = [], []
    else:
        axes = fig.axes[0]
        if axes.legend_ is None:
            # Empty legend
            patch_leg, label_leg = [], []
        else:
            # Get the symbol and label of all legend entry
            patch_leg = axes.legend_.get_patches()
            label_leg = [t.get_text() for t in axes.legend_.get_texts()]

    return (fig, axes, patch_leg, label_leg)
