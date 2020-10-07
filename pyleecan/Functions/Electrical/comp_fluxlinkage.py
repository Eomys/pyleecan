from ...Functions.FEMM.draw_FEMM import draw_FEMM
from ...Functions.Electrical.coordinate_transformation import n2dq
from ...Classes._FEMMHandler import FEMMHandler
from numpy import zeros, linspace, pi, split, mean


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
    qs = output.simu.machine.stator.winding.qs
    zp = output.simu.machine.stator.get_pole_pair_number()
    Nt_tot = obj.Nt_tot
    rot_dir = output.get_rot_dir()

    # Set the symmetry factor if needed
    if obj.is_symmetry_a:
        sym = obj.sym_a
        if obj.is_antiper_a:
            sym *= 2
        if obj.is_sliding_band:
            obj.is_sliding_band = (
                True  # When there is a symmetry, there must be a sliding band.
            )
    else:
        sym = 1

    # store orignal elec and make a copy to do temp. modifications
    elec = output.elec
    output.elec = elec.copy()

    # Set rotor angle for the FEMM simulation
    angle_offset_initial = output.get_angle_offset_initial()
    angle = linspace(0, 2 * pi / sym, Nt_tot, endpoint=False) + angle_offset_initial
    output.elec.angle_rotor = rot_dir * angle

    # modify some quantities
    output.elec.time = (angle - angle[0]) / (2 * pi * output.elec.N0 / 60)
    output.elec.Is = None  # to compute Is from Id_ref and Iq_ref (that are mean val.)
    output.elec.Is = output.elec.get_Is()  # TODO get_Is disregards initial rotor angle

    # Open FEMM
    femm = FEMMHandler()

    # Setup the FEMM simulation
    # Geometry building and assigning property in FEMM
    FEMM_dict = draw_FEMM(
        femm=femm,
        output=output,
        is_mmfr=1,
        is_mmfs=1,
        sym=sym,
        is_antiper=obj.is_antiper_a,
        type_calc_leakage=obj.type_calc_leakage,
        kgeo_fineness=obj.Kgeo_fineness,  # TODO fix inconsistent lower/upper case
    )

    # Solve for all time step and store all the results in output
    Phi_wind = obj.solve_FEMM(femm, output, sym, FEMM_dict)

    # Define d axis angle for the d,q transform
    d_angle = (angle - angle_offset_initial) * zp
    fluxdq = split(n2dq(Phi_wind, d_angle, n=qs), 2, axis=1)

    # restore the original elec
    output.elec = elec

    return fluxdq
