from ...Classes.LamH import LamH
from ...Classes.LamSlotMag import LamSlotMag
from ...Classes.MachineSIPMSM import MachineSIPMSM

from ...Functions.FEMM import FEMM_GROUPS
from ...Functions.FEMM import acsolver, pbtype, precision, minangle
from ...Functions.labels import ROTOR_LAB


def comp_FEMM_dict(
    machine, Kgeo_fineness, Kmesh_fineness, T_mag, type_calc_leakage=0, sym=1
):
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
    T_mag: float
        Permanent magnet temperature [deg Celsius]
    type_calc_leakage : int
        0 no leakage calculation
        1 calculation using single slot
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)

    Returns
    -------
    FEMM_dict : dict
        dictionary containing the main parameters of FEMM

    """

    FEMM_dict = dict()
    # Gather the main Simulation/model related parameters
    FEMM_dict["simu"] = dict()
    if type_calc_leakage == 1:
        FEMM_dict["simu"]["is_close_model"] = 1
    else:
        FEMM_dict["simu"]["is_close_model"] = 0
    FEMM_dict["simu"]["acsolver"] = acsolver
    FEMM_dict["simu"]["pbtype"] = pbtype
    FEMM_dict["simu"]["precision"] = precision
    FEMM_dict["simu"]["minangle"] = minangle
    FEMM_dict["simu"]["freqpb"] = 0  # setting 2D magnetostatic problem
    # assign unitary length to calculate torque and flux linkage per meter unit
    FEMM_dict["simu"]["Lfemm"] = 1
    FEMM_dict["simu"]["T_mag"] = T_mag

    # Gather all mesh related parameters
    FEMM_dict["mesh"] = dict()
    FEMM_dict["mesh"]["smart_mesh"] = 0
    FEMM_dict["mesh"]["automesh"] = 0  # 1 to let the solver define the mesh in all
    # regions(except in the airgap), otherwise meshsize_XXX parameters are used
    FEMM_dict["mesh"][
        "automesh_airgap"
    ] = 0  # 1 to let the solver define the mesh in the
    #  airgap, otherwise meshsize_airgap is used
    FEMM_dict["mesh"]["automesh_segments"] = 0  # 1 to let the solver define the mesh
    # points along arcs and segments, otherwise arcspan_XXX and
    # elementsize_XXX are used

    FEMM_dict["mesh"]["maxsegdeg"] = 1  # max angular width of elementary segment along
    # arc discretization(default: 1)
    FEMM_dict["mesh"]["maxelementsize"] = 1  # max length of elementary segment along
    # segment discretization(1 for automatic meshing) "elementsize" in FEMM doc
    FEMM_dict["mesh"]["arcspan"] = (
        1 / Kgeo_fineness
    )  # max span of arc element in degrees

    # Add all mesh size for all Laminations
    for lam in machine.get_lam_list():
        label = lam.get_label()
        # Recompute because machine may has been modified
        Hsy = lam.comp_height_yoke()
        Hs = lam.Rext - lam.Rint
        Hstot = Hs - Hsy  # Works with holes and slot

        # Store all the elements size for the lamination
        FEMM_dict["mesh"][label] = dict()
        if lam.is_stator:
            # stator slot region mesh and segments max element size parameter
            # If Hstot = 0 there is no slot and the region parameter won't be used
            FEMM_dict["mesh"][label]["meshsize_slot"] = (
                max(Hstot, Hs / 2) / 8 / Kmesh_fineness
            )
            FEMM_dict["mesh"][label]["elementsize_slot"] = (
                max(Hstot, Hs / 2) / 8 / Kmesh_fineness
            )
            # stator yoke region mesh and segments max element size parameter
            FEMM_dict["mesh"][label]["meshsize_yoke"] = (
                min(Hsy, Hs / 2) / 4 / Kmesh_fineness
            )
            FEMM_dict["mesh"][label]["elementsize_yoke"] = (
                min(Hsy, Hs / 2) / 4 / Kmesh_fineness
            )
        else:
            # rotor slot region mesh and segments max element size parameter
            if isinstance(lam, (LamSlotMag, LamH)):
                FEMM_dict["mesh"][label]["meshsize_slot"] = Hsy / 4 / Kmesh_fineness
                FEMM_dict["mesh"][label]["elementsize_slot"] = Hsy / 4 / Kmesh_fineness
            else:
                FEMM_dict["mesh"][label]["meshsize_slot"] = Hstot / 8 / Kmesh_fineness
                FEMM_dict["mesh"][label]["elementsize_slot"] = (
                    Hstot / 8 / Kmesh_fineness
                )
            # rotor yoke region mesh and segments max element size parameter
            FEMM_dict["mesh"][label]["meshsize_yoke"] = Hsy / 4 / Kmesh_fineness
            FEMM_dict["mesh"][label]["elementsize_yoke"] = Hsy / 4 / Kmesh_fineness
        # Wedge mesh
        FEMM_dict["mesh"][label]["meshsize_wedge"] = Hstot / 20 / Kmesh_fineness

        # mesh parameter for stator and rotor slot region
        if type_calc_leakage == 1:
            FEMM_dict["mesh"][label]["meshsize_slot"] = Hstot / 50

        # magnet region mesh and segments max element size parameter
        if isinstance(lam, LamSlotMag):
            Hmag = lam.slot.comp_height_active()
            FEMM_dict["mesh"][label]["meshsize_magnet"] = Hmag / 4 / Kmesh_fineness
            FEMM_dict["mesh"][label]["elementsize_magnet"] = Hmag / 4 / Kmesh_fineness
        elif isinstance(lam, LamH):
            Hmag = lam.get_hole_list()[0].comp_height()
            FEMM_dict["mesh"][label]["meshsize_magnet"] = Hmag / 4 / Kmesh_fineness
            FEMM_dict["mesh"][label]["elementsize_magnet"] = Hmag / 4 / Kmesh_fineness
        else:
            FEMM_dict["mesh"][label]["meshsize_magnet"] = None

    # airgap region mesh and segments max element size parameter
    Wgap_mec = machine.comp_width_airgap_mec()
    if isinstance(machine, MachineSIPMSM):
        FEMM_dict["mesh"]["meshsize_airgap"] = Wgap_mec / 10 / Kmesh_fineness
        FEMM_dict["mesh"]["elementsize_airgap"] = Wgap_mec / 10 / Kmesh_fineness
    else:
        FEMM_dict["mesh"]["meshsize_airgap"] = Wgap_mec / 3 / Kmesh_fineness
        FEMM_dict["mesh"]["elementsize_airgap"] = Wgap_mec / 3 / Kmesh_fineness

    # mesh parameter for basic air regions (ventilation ducts etc)
    Hry = machine.get_lam_by_label(ROTOR_LAB).comp_height_yoke()
    FEMM_dict["mesh"]["meshsize_air"] = Hry / 4 / Kmesh_fineness

    # Set groups (to select area by type)
    FEMM_dict["groups"] = dict()
    for grp in FEMM_GROUPS:
        if grp != "lam_group_list":
            FEMM_dict["groups"][grp] = FEMM_GROUPS[grp]["ID"]
    grp_max = max(FEMM_dict["groups"].values())

    # Adding lam_group_list linking lam name to related ID
    FEMM_dict["groups"]["lam_group_list"] = dict()
    for key, val in FEMM_GROUPS["lam_group_list"].items():
        FEMM_dict["groups"]["lam_group_list"][key] = list(val)

    # Adding a group for each magnet on the lamination
    if isinstance(machine.rotor, (LamSlotMag, LamH)):
        nb_mag = machine.rotor.get_magnet_number(sym=sym)
        ndigit = max(len(str(nb_mag)), len(str(grp_max)) - 1)
        grp0 = FEMM_dict["groups"]["GROUP_RM"] * 10 ** ndigit
        list_mag = [grp0 + ii for ii in range(nb_mag)]
        FEMM_dict["groups"]["GROUP_RM"] = list_mag
        FEMM_dict["groups"]["lam_group_list"][machine.rotor.get_label()].extend(
            list_mag
        )

    # Init empty list
    FEMM_dict["materials"] = list()
    FEMM_dict["circuits"] = list()

    return FEMM_dict
