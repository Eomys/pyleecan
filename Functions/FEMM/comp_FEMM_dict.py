# -*- coding: utf-8 -*-
"""@package comp_element_size
@date Created on août 07 10:53 2018
@author franco_i
"""

from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Functions.FEMM import acsolver, pbtype, precision, minangle
from pyleecan.Functions.FEMM import (
    GROUP_RC,
    GROUP_RH,
    GROUP_RV,
    GROUP_RW,
    GROUP_SC,
    GROUP_SH,
    GROUP_SV,
    GROUP_SW,
    GROUP_AG,
)


def comp_FEMM_dict(machine, Kgeo_fineness, Kmesh_fineness, type_calc_leakage=0):
    """Compute the parameters needed for FEMM simulations

    Parameters
    ----------
    machine : Machine
        The machine to draw
    Kgeo_fineness : float
        global coefficient to adjust geometry fineness in FEMM
        (1 : default ; > 1 : finner ; < 1 : less fine)
    Kmesh_fineness : float
        global coefficient to adjust mesh fineness in FEMM
        (1 :default ; > 1 : finner ; < 1 : less fine)
    type_calc_leakage : int
        0 no leakage calculation
        1 calculation using single slot

    Returns
    -------
    FEMM_dict : dict
        Dictionnary containing the main parameters of FEMM
    
    """

    # Recompute because machine may has been modified
    Hsy = machine.stator.comp_height_yoke()
    Hstot = machine.stator.Rext - machine.stator.Rint - Hsy  # Works with holes and slot
    Wgap_mec = machine.comp_width_airgap_mec()
    Hry = machine.rotor.comp_height_yoke()
    Hrtot = machine.rotor.Rext - machine.rotor.Rint - Hry  # Works with holes and slot

    FEMM_dict = dict()
    FEMM_dict["is_close_model"] = 0
    FEMM_dict["acsolver"] = acsolver
    FEMM_dict["pbtype"] = pbtype
    FEMM_dict["precision"] = precision
    FEMM_dict["minangle"] = minangle
    FEMM_dict["freqpb"] = 0  # setting 2D magnetostatic problem

    FEMM_dict["smart_mesh"] = 0
    FEMM_dict["automesh"] = 0  # 1 to let the solver define the mesh in all
    # regions(except in the airgap), otherwise meshsize_XXX parameters are used
    FEMM_dict["automesh_airgap"] = 0  # 1 to let the solver define the mesh in the
    #  airgap, otherwise meshsize_airgap is used
    FEMM_dict["automesh_segments"] = 0  # 1 to let the solver define the mesh
    # points along arcs and segments, otherwise arcspan_XXX and
    # elementsize_XXX are used

    FEMM_dict["maxsegdeg"] = 1  # max angular width of elementary segment along
    # arc discretization(default: 1)
    FEMM_dict["maxelementsize"] = 1  # max length of elementary segment along
    # segment discretization(1 for automatic meshing) "elementsize" in FEMM doc
    FEMM_dict["arcspan"] = 1 / Kgeo_fineness  # max span of arc element in degrees

    FEMM_dict["Lfemm"] = (
        machine.stator.comp_length() + machine.rotor.comp_length()
    ) / 2

    # If Hstot = 0 there is no slot and this parameter won't be used
    FEMM_dict["meshsize_slotS"] = Hstot / 8 / Kmesh_fineness
    # max element size in m for stator slot segments
    FEMM_dict["elementsize_slotS"] = Hstot / 8 / Kmesh_fineness

    # parameter for rotor slot region
    FEMM_dict["meshsize_slotR"] = Hrtot / 8 / Kmesh_fineness
    # max element size in m for rotor slot segments
    FEMM_dict["elementsize_slotR"] = Hrtot / 8 / Kmesh_fineness

    # mesh parameter for rotor yoke region
    FEMM_dict["meshsize_yokeR"] = Hry / 4 / Kmesh_fineness
    # max element size in m for rotor yoke segments
    FEMM_dict["elementsize_yokeR"] = Hry / 4 / Kmesh_fineness

    # mesh parameter for stator yoke region
    FEMM_dict["meshsize_yokeS"] = Hsy / 4 / Kmesh_fineness
    # max element size in m for stator yoke segments
    FEMM_dict["elementsize_yokeS"] = Hsy / 4 / Kmesh_fineness

    # mesh parameter for airgap region
    FEMM_dict["meshsize_airgap"] = Wgap_mec / 3 / Kmesh_fineness
    # max element size in m for airgap segments
    FEMM_dict["elementsize_airgap"] = Wgap_mec / 3 / Kmesh_fineness

    if type(machine.stator) == LamSlotMag:
        Hmag = machine.stator.slot.magnet[0].Hmag
        # mesh parameter for magnet region
        FEMM_dict["meshsize_magnetS"] = Hmag / 4 / Kmesh_fineness
        # max element size in m for magnet segments
        FEMM_dict["elementsize_magnetS"] = Hmag / 4 / Kmesh_fineness
    else:
        FEMM_dict["meshsize_magnetS"] = None

    if type(machine.rotor) == LamSlotMag:
        Hmag = machine.rotor.slot.magnet[0].Hmag
        # mesh parameter for magnet region
        FEMM_dict["meshsize_magnetR"] = Hmag / 4 / Kmesh_fineness
        # max element size in m for magnet segments
        FEMM_dict["elementsize_magnetR"] = Hmag / 4 / Kmesh_fineness
    elif type(machine.rotor) == LamHole:
        Hmag = machine.rotor.hole[0].get_height_magnet()
        # mesh parameter for magnet region
        FEMM_dict["meshsize_magnetR"] = Hmag / 4 / Kmesh_fineness
        # max element size in m for magnet segments
        FEMM_dict["elementsize_magnetR"] = Hmag / 4 / Kmesh_fineness
    else:
        FEMM_dict["meshsize_magnetR"] = None

    # mesh parameter for basic air regions (ventilation ducts etc)
    FEMM_dict["meshsize_air"] = Hry / 4 / Kmesh_fineness
    FEMM_dict["meshsize_wedge"] = Hstot / 20 / Kmesh_fineness

    if type_calc_leakage == 1:
        FEMM_dict["is_close_model"] = 1
        # mesh parameter for stator slot region
        FEMM_dict["meshsize_slotS"] = Hstot / 50
        # % mesh parameter for stator slot region
        FEMM_dict["meshsize_slotR"] = Hrtot / 50

    # Set groups
    FEMM_dict["groups"] = dict()
    FEMM_dict["groups"]["GROUP_RC"] = GROUP_RC
    FEMM_dict["groups"]["GROUP_RH"] = GROUP_RH
    FEMM_dict["groups"]["GROUP_RV"] = GROUP_RV
    FEMM_dict["groups"]["GROUP_RW"] = GROUP_RW
    FEMM_dict["groups"]["GROUP_SC"] = GROUP_SC
    FEMM_dict["groups"]["GROUP_SH"] = GROUP_SH
    FEMM_dict["groups"]["GROUP_SV"] = GROUP_SV
    FEMM_dict["groups"]["GROUP_SW"] = GROUP_SW
    FEMM_dict["groups"]["GROUP_AG"] = GROUP_AG

    return FEMM_dict
