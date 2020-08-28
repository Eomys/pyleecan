# -*- coding: utf-8 -*-

from ....Classes.Skew import Skew
from ....Methods.Simulation.Input import InputError


def comp_skew(self):
    """Computes skew angles for each lamination 
    
    Parameters
    ----------
    self : SkewModel
        a SkewModel object

    """

    if self.parent is None:
        raise InputError(
            "ERROR: The SkewModel object must be in a Magnetics object to run"
        )

    is_undef_stator = False
    is_undef_rotor = False

    stator = self.parent.parent.machine.stator
    rotor = self.parent.parent.machine.rotor

    # Stator skew init
    if stator.skew is None:
        stator.skew = Skew(type="user-defined")
        is_undef_stator = True

    # Rotor skew init
    if rotor.skew is None:
        rotor.skew = Skew(type="user-defined")
        is_undef_rotor = True

    # Check if Nslices should be even or odd
    if stator.skew.type == "vshape" and stator.skew.is_step:
        is_odd_stator = True
        is_even_stator = False
    elif stator.skew.type == "vshape" and not stator.skew.is_step:
        is_odd_stator = False
        is_even_stator = True
    else:
        is_odd_stator = False
        is_even_stator = False

    if rotor.skew.type == "vshape" and rotor.skew.is_step:
        is_odd_rotor = True
        is_even_rotor = False
    elif rotor.skew.type == "vshape" and not rotor.skew.is_step:
        is_odd_rotor = False
        is_even_rotor = True
    else:
        is_even_rotor = False
        is_odd_rotor = False

    if is_even_stator == True and is_odd_rotor == True:
        raise InputError(
            "Cannot use vshape skew with both linear and step (incompatible number of slices)"
        )
    elif is_odd_stator == True and is_even_rotor == True:
        raise InputError(
            "Cannot use vshape skew with both linear and step (incompatible number of slices)"
        )
    else:
        is_even = is_even_stator or is_even_rotor
        is_odd = is_odd_stator or is_odd_rotor

    # Compute slice distribution
    self.comp_dist(is_even=is_even, is_odd=is_odd)

    # Add zero for undefined skew
    if is_undef_stator:
        stator.skew.is_step = rotor.skew.is_step
        self.angle_list_stator = [0 for z in self.z_list]
    if is_undef_rotor:
        rotor.skew.is_step = stator.skew.is_step
        self.angle_list_rotor = [0 for z in self.z_list]

    # Compute skew
    z_list_stator = stator.skew.comp_angle(
        z_list=self.z_list, angle_list=self.angle_list_stator
    )
    z_list_rotor = rotor.skew.comp_angle(
        z_list=self.z_list, angle_list=self.angle_list_rotor
    )

    # Store skew axis in Outmag
    self.parent.parent.parent.mag.skew_axis = sorted(set(z_list_stator + z_list_rotor))
