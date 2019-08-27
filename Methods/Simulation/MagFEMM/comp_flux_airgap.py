# -*- coding: utf-8 -*-
"""@package comp_flux_airgap
@date Created on août 01 15:46 2018
@author franco_i
"""

from pyleecan.Functions.FEMM.draw_FEMM import draw_FEMM


def comp_flux_airgap(self, output):
    """Compute using FEMM the flux in the airgap

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    output : Output
        an Output object
    """

    # Set the symmetry factor if needed
    if self.is_symmetry_a:
        sym = self.sym_a
        if self.is_antiper_a:
            sym *= 2
    else:
        sym = 1

    # if self.is_load_FEA:
    #     path_save = join(MAIN_DIR, "Results", "Femm", "Mesh") + '\\'
    #     Nt_tot = output.mag.Nt_tot
    #     mesh = [MeshMat() for ii in range(Nt_tot)]
    #     mesh_tmp = MeshTriangle()
    #
    #     for ii in range(Nt_tot):
    #
    #        listElem  = np.loadtxt(path_save + 'Mesh_elem' + str(ii) +  '.dat')
    #        listElem = listElem.astype(int)
    #        mesh_tmp.nb_elem = len(listElem)
    #        mesh_tmp.element = listElem
    #
    #        listNd = np.loadtxt(path_save + 'Mesh_nodes' + str(ii) +  '.dat')
    #        mesh_tmp.nb_node = len(listNd)
    #        mesh_tmp.node = listNd
    #
    #        results = np.loadtxt(path_save + 'Solution_' + str(ii) + '.dat')
    #        mesh_tmp.solution = dict()
    #        mesh_tmp.solution["Bx"] = results[:, 0]
    #        mesh_tmp.solution["By"] = results[:, 1]
    #        mesh_tmp.solution["Hx"] = results[:, 2]
    #        mesh_tmp.solution["Hy"] = results[:, 3]
    #        mesh_tmp.solution["mu"] = results[:, 4]
    #
    #        mesh[ii] = mesh_tmp
    #
    #     output.mag.mesh = mesh
    #
    # else:

        # Setup the FEMM simulation
    # Geometry building and assigning property in FEMM
    FEMM_dict = draw_FEMM(
        output,
        is_mmfr=self.is_mmfr,
        is_mmfs=self.is_mmfs,
        sym=sym,
        is_antiper=self.is_antiper_a,
        type_calc_leakage=self.type_calc_leakage,
        is_remove_vent=self.is_remove_vent,
        is_remove_slotS=self.is_remove_slotS,
        is_remove_slotR=self.is_remove_slotR,
        is_stator_linear_BH=self.is_stator_linear_BH,
        is_rotor_linear_BH=self.is_rotor_linear_BH,
        kgeo_fineness=self.Kgeo_fineness,
        kmesh_fineness=self.Kmesh_fineness,
        user_FEMM_dict=self.FEMM_dict,
        path_save=self.get_path_save(output),
    )

    # Solve for all time step and store all the results in output
    self.solve_FEMM(output, sym, FEMM_dict)

