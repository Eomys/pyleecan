# -*- coding: utf-8 -*-
"""@package Methods.Machine.Machine.plot
Machine plot method
@date Created on Wed Dec 10 14:58:51 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""
from matplotlib.pyplot import axis, subplots


def plot(self, sym=1, alpha=0, delta=0):
    """Plot the Machine in a matplotlib fig

    Parameters
    ----------
    self : Machine
        A Machine object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation

    Returns
    -------
    None

    """

    # Display
    fig, axes = subplots()
    # Get the patches to display from corresponding plot
    # The order in the list matters (largest to smallest)
    if self.frame is not None:
        self.frame.plot(fig, sym=sym, alpha=alpha, delta=delta)  # Frame
        Wfra = self.frame.comp_height_eq()
    else:
        Wfra = 0

    if self.rotor.is_internal:
        self.stator.plot(fig, sym=sym, alpha=alpha, delta=delta)  # Stator
        self.rotor.plot(fig, sym=sym, alpha=alpha, delta=delta)  # Rotor

        if self.rotor.Rint > 0:  # Add the shaft only for internal rotor
            self.shaft.plot(fig, sym=sym, alpha=alpha, delta=delta)
        Lim = (self.stator.Rext + Wfra) * 1.5  # Axes limit for plot
    else:
        self.rotor.plot(fig, sym=sym, alpha=alpha, delta=delta)  # Rotor
        self.stator.plot(fig, sym=sym, alpha=alpha, delta=delta)  # Stator
        Lim = (self.rotor.Rext + Wfra) * 1.5  # Axes limit for plot

    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    axes.set_title("Machine")

    # Axis Setup
    axis("equal")

    # The Lamination is centered in the figure
    axes.set_xlim(-Lim, Lim)
    axes.set_ylim(-Lim, Lim)
    fig.show()
