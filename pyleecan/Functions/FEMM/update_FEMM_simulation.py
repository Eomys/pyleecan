# -*- coding: utf-8 -*-
import femm
from numpy import pi

from ...Functions.FEMM.comp_FEMM_Jcus import comp_FEMM_Jcus
from ...Functions.FEMM.set_FEMM_circuit_prop import set_FEMM_circuit_prop
from ...Functions.FEMM.set_FEMM_wind_material import set_FEMM_wind_material


def update_FEMM_simulation(
    output, materials, circuits, is_mmfs, is_mmfr, j_t0, is_sliding_band
):
    """Update the simulation by changing the rotor position and
    updating the currents


    Parameters
    ----------
    output :
        Output object
    """
    angle_rotor = output.get_angle_rotor()

    if is_sliding_band:  # No rotation without sliding band.
        # Rotor rotation using sliding band
        if output.simu.machine.rotor.is_internal:
            femm.mi_modifyboundprop("bc_ag2", 10, 180 * angle_rotor[j_t0] / pi)
        else:
            femm.mi_modifyboundprop("bc_ag2", 11, 180 * angle_rotor[j_t0] / pi)
        # Update currents
        for label in circuits:
            if "Circs" in label:  # Stator
                set_FEMM_circuit_prop(
                    circuits,
                    label,
                    output.elec.get_Is(),
                    is_mmfs,
                    output.simu.machine.stator.winding.Npcpp,
                    j_t0,
                )
            if "Circr" in label:  # Rotor
                set_FEMM_circuit_prop(
                    circuits,
                    label,
                    output.elec.Ir,
                    is_mmfr,
                    output.simu.machine.stator.winding.Npcpp,
                    j_t0,
                )
        # Update winding materials
        for mat in materials:
            if "Js" in mat:  # Stator winding
                Jcus = comp_FEMM_Jcus(
                    output.simu.machine.stator, mat, output.elec.get_Is(), j_t0, is_mmfs
                )
                materials = set_FEMM_wind_material(materials, mat, Jcus)
            elif "Jr" in mat:  # Rotor winding
                Jcus = comp_FEMM_Jcus(
                    output.simu.machine.rotor, mat, output.elec.Ir, j_t0, is_mmfr
                )
                materials = set_FEMM_wind_material(materials, mat, Jcus)
