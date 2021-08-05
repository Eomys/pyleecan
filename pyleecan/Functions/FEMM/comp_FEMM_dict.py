# -*- coding: utf-8 -*-

from ...Classes.LamHole import LamHole
from ...Classes.LamSlotMag import LamSlotMag
from ...Classes.MachineSIPMSM import MachineSIPMSM
from ...Functions.FEMM import acsolver, pbtype, precision, minangle
from ...Functions.FEMM import FEMM_GROUPS


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
        dictionary containing the main parameters of FEMM

    """

    # Recompute because machine may has been modified
    Hsy = machine.stator.comp_height_yoke()
    Hs = machine.stator.Rext - machine.stator.Rint
    Hstot = Hs - Hsy  # Works with holes and slot

    Wgap_mec = machine.comp_width_airgap_mec()

    Hry = machine.rotor.comp_height_yoke()
    Hr = machine.rotor.Rext - machine.rotor.Rint
    Hrtot = Hr - Hry  # Works with holes and slot

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

    # stator slot region mesh and segments max element size parameter
    # If Hstot = 0 there is no slot and the region parameter won't be used
    FEMM_dict["meshsize_slotS"] = max(Hstot, Hs / 2) / 8 / Kmesh_fineness
    FEMM_dict["elementsize_slotS"] = max(Hstot, Hs / 2) / 8 / Kmesh_fineness

    # stator yoke region mesh and segments max element size parameter
    FEMM_dict["meshsize_yokeS"] = min(Hsy, Hs / 2) / 4 / Kmesh_fineness
    FEMM_dict["elementsize_yokeS"] = min(Hsy, Hs / 2) / 4 / Kmesh_fineness

    # rotor slot region mesh and segments max element size parameter
    if type(machine.rotor) == LamSlotMag or type(machine.rotor) == LamHole:
        FEMM_dict["meshsize_slotR"] = Hry / 4 / Kmesh_fineness
        FEMM_dict["elementsize_slotR"] = Hry / 4 / Kmesh_fineness
    else:
        FEMM_dict["meshsize_slotR"] = Hrtot / 8 / Kmesh_fineness
        FEMM_dict["elementsize_slotR"] = Hrtot / 8 / Kmesh_fineness

    # rotor yoke region mesh and segments max element size parameter
    FEMM_dict["meshsize_yokeR"] = Hry / 4 / Kmesh_fineness
    FEMM_dict["elementsize_yokeR"] = Hry / 4 / Kmesh_fineness

    # airgap region mesh and segments max element size parameter
    if isinstance(machine, MachineSIPMSM):
        FEMM_dict["meshsize_airgap"] = Wgap_mec / 10 / Kmesh_fineness
        FEMM_dict["elementsize_airgap"] = Wgap_mec / 10 / Kmesh_fineness
    else:
        FEMM_dict["meshsize_airgap"] = Wgap_mec / 3 / Kmesh_fineness
        FEMM_dict["elementsize_airgap"] = Wgap_mec / 3 / Kmesh_fineness

    # stator magnet region mesh and segments max element size parameter
    if type(machine.stator) == LamSlotMag:
        Hmag = machine.stator.slot.comp_height_active()
        FEMM_dict["meshsize_magnetS"] = Hmag / 4 / Kmesh_fineness
        FEMM_dict["elementsize_magnetS"] = Hmag / 4 / Kmesh_fineness
    else:
        FEMM_dict["meshsize_magnetS"] = None

    # rotor magnet region mesh and segments max element size parameter
    if type(machine.rotor) == LamSlotMag:
        Hmag = machine.rotor.slot.comp_height_active()
        FEMM_dict["meshsize_magnetR"] = Hmag / 4 / Kmesh_fineness
        FEMM_dict["elementsize_magnetR"] = Hmag / 4 / Kmesh_fineness
    elif type(machine.rotor) == LamHole:
        Hmag = machine.rotor.hole[0].comp_height()
        FEMM_dict["meshsize_magnetR"] = Hmag / 4 / Kmesh_fineness
        FEMM_dict["elementsize_magnetR"] = Hmag / 4 / Kmesh_fineness
    else:
        FEMM_dict["meshsize_magnetR"] = None

    # mesh parameter for basic air regions (ventilation ducts etc)
    FEMM_dict["meshsize_air"] = Hry / 4 / Kmesh_fineness
    FEMM_dict["meshsize_wedge"] = Hstot / 20 / Kmesh_fineness

    # mesh parameter for stator and rotor slot region
    if type_calc_leakage == 1:
        FEMM_dict["is_close_model"] = 1
        FEMM_dict["meshsize_slotS"] = Hstot / 50
        FEMM_dict["meshsize_slotR"] = Hrtot / 50

    # Set groups
    FEMM_dict["groups"] = dict()
    for grp in FEMM_GROUPS:
        FEMM_dict["groups"][grp] = FEMM_GROUPS[grp]["ID"]

    return FEMM_dict
