import os
from os.path import join

from ...Functions.FEMM.draw_FEMM import draw_FEMM
from ...Functions.Electrical.coordinate_transformation import n2dq
from ...Classes._FEMMHandler import _FEMMHandler
from ...Classes.OutMagFEMM import OutMagFEMM
from numpy import linspace, pi, split
from SciDataTool.Classes.Data1D import Data1D


def comp_fluxlinkage(obj, output):
    """Compute the flux linkage using FEMM and electrical output reference currents

    Parameters
    ----------
    obj : FluxLinkFEMM or IndMagFEMM
        a FluxLinkFEMM object or an IndMagFEMM object
    output : Output
        an Output object

    Return
    ------
    fluxdq : ndarray
        the calculated fluxlinkage
    """
    # get some machine and simulation parameters
    qs = output.simu.machine.stator.winding.qs
    zp = output.simu.machine.stator.get_pole_pair_number()
    Nt_tot = obj.Nt_tot
    rot_dir = output.get_rot_dir()

    # Get save path
    str_EEC = "EEC"

    path_res = output.get_path_result()

    save_dir = join(path_res, "Femm")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    if output.simu.machine.name not in [None, ""]:
        file_name = output.simu.machine.name + "_" + str_EEC + ".fem"
    elif output.simu.name not in [None, ""]:
        file_name = output.simu.name + "_" + str_EEC + ".fem"
    else:  # Default name
        file_name = "FEMM_" + str_EEC + ".fem"

    path_save = join(save_dir, file_name)

    # Set the symmetry factor according to the machine
    if obj.is_periodicity_a:
        (
            sym,
            is_antiper_a,
            _,
            _,
        ) = obj.parent.parent.parent.parent.get_machine_periodicity()
        if is_antiper_a:
            sym = sym * 2
    else:
        sym = 1
        is_antiper_a = False

    # store orignal elec and make a copy to do temp. modifications
    elec = output.elec
    output.elec = elec.copy()

    # Set rotor angle for the FEMM simulation
    angle_offset_initial = output.get_angle_offset_initial()
    angle_rotor = (
        linspace(0, -1 * rot_dir * 2 * pi / sym, Nt_tot, endpoint=False)
        + angle_offset_initial
    )

    # modify some quantities
    output.elec.Time = Data1D(
        name="time",
        unit="s",
        values=(angle_rotor - angle_rotor[0]) / (2 * pi * output.elec.N0 / 60),
    )
    output.elec.Is = None  # to compute Is from Id_ref and Iq_ref (that are mean val.)
    output.elec.Is = output.elec.get_Is()  # TODO get_Is disregards initial rotor angle

    # Open FEMM
    femm = _FEMMHandler()
    if output.elec.internal is None:
        output.elec.internal = OutMagFEMM()
    output.elec.internal.handler_list.append(femm)

    # Setup the FEMM simulation
    # Geometry building and assigning property in FEMM
    FEMM_dict = draw_FEMM(
        femm=femm,
        output=output,
        is_mmfr=1,
        is_mmfs=1,
        sym=sym,
        is_antiper=is_antiper_a,
        type_calc_leakage=obj.type_calc_leakage,
        kgeo_fineness=obj.Kgeo_fineness,  # TODO fix inconsistent lower/upper case
        path_save=path_save,
    )

    # Solve for all time step and store all the results in output
    Phi_wind = obj.solve_FEMM(femm, output, sym, FEMM_dict)

    # Close FEMM after simulation
    femm.closefemm()
    output.elec.internal.handler_list.remove(femm)

    # Define d axis angle for the d,q transform
    d_angle = (angle_rotor - angle_offset_initial) * zp
    fluxdq = split(n2dq(Phi_wind, d_angle, n=qs), 2, axis=1)

    # restore the original elec
    output.elec = elec

    return fluxdq
