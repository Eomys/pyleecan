# -*- coding: utf-8 -*-
"""@package comp_element_size
@date Created on août 07 10:53 2018
@author franco_i
"""

from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.LamSlotMag import LamSlotMag


def comp_draw_param(machine, Kgeo_fineness, Kmesh_fineness, type_calc_leakage=0):
    """Compute the parameters needed in FEMM when plotting

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
    draw_FEMM_param : dict
        dictionnary containing parameter used to plot in FEMM
    
    """

    # Recompute because machine may has been modified
    Hstot = machine.stator.slot.comp_height()
    Hsy = machine.stator.comp_height_yoke()
    Wgap_mec = machine.comp_width_airgap_mec()
    Hrtot = machine.rotor.slot.comp_height()
    Hry = machine.rotor.comp_height_yoke()

    draw_FEMM_param = dict()
    draw_FEMM_param["is_close_model"] = 0

    draw_FEMM_param["automesh"] = 0  # 1 to let the solver define the mesh in all
    # regions(except in the airgap), otherwise meshsize_XXX parameters are used
    draw_FEMM_param["automesh_airgap"] = 0  # 1 to let the solver define the mesh in the
    #  airgap, otherwise meshsize_airgap is used
    draw_FEMM_param["automesh_segments"] = 0  # 1 to let the solver define the mesh
    # points along arcs and segments, otherwise arcspan_XXX and
    # elementsize_XXX are used

    draw_FEMM_param["maxsegdeg"] = 1  # max angular width of elementary segment along
    # arc discretization(default: 1)
    draw_FEMM_param["maxelementsize"] = 1  # max length of elementary segment along
    # segment discretization(1 for automatic meshing) "elementsize" in FEMM doc
    draw_FEMM_param["arcspan"] = 1 / Kgeo_fineness  # max span of arc element in degrees

    if type(machine.stator) == LamSlot and Hstot > 0:  # if there is Slot on
        #  the stator
        # mesh parameter for stator slot region
        draw_FEMM_param["meshsize_slotS"] = Hstot / 10 / Kmesh_fineness

        draw_FEMM_param["elementsize_slotS"] = Hstot / 10  # max element size in m for
        # stator slot segments
    else:
        draw_FEMM_param["meshsize_slotS"] = Hsy / 10 / Kmesh_fineness  # mesh parameter
        # for stator slot region
        draw_FEMM_param["elementsize_slotS"] = Hsy / 10  # max element size in m for
        # stator slot segments

    if Hrtot > 0:
        draw_FEMM_param["meshsize_slotR"] = Hrtot / 10 / Kmesh_fineness  # mesh
        # parameter for rotor slot region
        draw_FEMM_param["elementsize_slotR"] = Hrtot / 10  # max element size in m for
        # stator slot segments
    else:
        draw_FEMM_param["meshsize_slotR"] = Hry / 10 / Kmesh_fineness  # mesh parameter
        # for rotor slot region
        draw_FEMM_param["elementsize_slotR"] = Hsy / 10  # max element size in m for
        # stator slot segments

    draw_FEMM_param["meshsize_yokeR"] = Hry / 4 / Kmesh_fineness  # mesh parameter for
    # rotor yoke region
    draw_FEMM_param["elementsize_yokeR"] = Hry / 4  # max element size in m for rotor
    # yoke segments

    draw_FEMM_param["meshsize_yokeS"] = Hsy / 4 / Kmesh_fineness  # mesh parameter for
    # stator yoke region
    draw_FEMM_param["elementsize_yokeS"] = Hsy / 4  # max element size in m for stator
    # yoke segments

    draw_FEMM_param["meshsize_airgap"] = Wgap_mec / 5 / Kmesh_fineness  # mesh parameter
    # for airgap region

    draw_FEMM_param["elementsize_airgap"] = Wgap_mec / 5  # max element size in m for
    # airgap segments

    if type(machine.stator) == LamSlotMag:
        Hmag = machine.stator.slot.magnet[0].Hmag
        draw_FEMM_param["meshsize_magnetS"] = Hmag / 4 / Kmesh_fineness  # mesh
        # parameter for magnet region
        draw_FEMM_param["elementsize_magnetS"] = Hmag / 4  # max element size in m for
        # magnet segments
    else:
        draw_FEMM_param["meshsize_magnetS"] = None

    if type(machine.rotor) == LamSlotMag:
        Hmag = machine.rotor.slot.magnet[0].Hmag
        draw_FEMM_param["meshsize_magnetR"] = Hmag / 4 / Kmesh_fineness  # mesh
        # parameter for magnet region
        draw_FEMM_param["elementsize_magnetR"] = Hmag / 4  # max element size in m for
        # magnet segments
    else:
        draw_FEMM_param["meshsize_magnetR"] = None

    draw_FEMM_param["meshsize_air"] = Hry / 4 / Kmesh_fineness  # mesh parameter for
    # basic air regions (ventilation ducts etc)
    draw_FEMM_param["meshsize_wedge"] = Hstot / 20 / Kmesh_fineness

    if type_calc_leakage == 1:
        draw_FEMM_param["is_close_model"] = 1
        # mesh parameter for stator slot region
        draw_FEMM_param["meshsize_slotS"] = Hstot / 50
        # % mesh parameter for stator slot region
        draw_FEMM_param["meshsize_slotR"] = Hrtot / 50

    return draw_FEMM_param
