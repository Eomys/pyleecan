import femm
from numpy import savetxt, zeros, pi, roll, mean, max as np_max, min as np_min
from os.path import join

from pyleecan.Generator import MAIN_DIR
from pyleecan.Functions.FEMM.update_FEMM_simulation import update_FEMM_simulation
from pyleecan.Functions.FEMM.comp_FEMM_torque import comp_FEMM_torque
from pyleecan.Functions.FEMM.comp_FEMM_Phi_wind import comp_FEMM_Phi_wind
from Methods.Simulation.MagFEMM.get_FEMM_mesh import get_FEMM_mesh

from Classes.MeshMat import MeshMat


def solve_FEMM(self, output, sym, FEMM_dict):

    # Loading parameters for readibility
    angle = output.mag.angle
    qs = output.simu.machine.stator.winding.qs  # Winding phase number
    Npcpp = output.simu.machine.stator.winding.Npcpp
    L1 = output.simu.machine.stator.comp_length()
    Nt_tot = output.mag.Nt_tot  # Number of time step
    Na_tot = output.mag.Na_tot  # Number of angular step

    # Create the mesh
    femm.mi_createmesh()

    # Initialize results matrix
    Br = zeros((Nt_tot, Na_tot))
    Bt = zeros((Nt_tot, Na_tot))
    Tem = zeros((Nt_tot, 1))
    Phi_wind_stator = zeros((Nt_tot, qs))

    if self.is_save_mesh or self.is_save_FEA:
        mesh = [MeshMat() for ii in range(Nt_tot)]
    else:
        mesh = [MeshMat()]

    # Compute the data for each time step
    for ii in range(Nt_tot):
        # Update rotor position and currents
        update_FEMM_simulation(
            output,
            FEMM_dict["materials"],
            FEMM_dict["circuits"],
            self.is_mmfs,
            self.is_mmfr,
            j_t0=ii,
        )
        # Run the computation
        femm.mi_analyze()
        femm.mi_loadsolution()
        # Get the flux result
        for jj in range(Na_tot):
            Br[ii, jj], Bt[ii, jj] = femm.mo_getgapb("bc_ag2", angle[jj] * 180 / pi)
        # Compute the torque
        Tem[ii] = comp_FEMM_torque(FEMM_dict, sym=sym)
        # Phi_wind computation
        Phi_wind_stator[ii, :] = comp_FEMM_Phi_wind(
            qs, Npcpp, is_stator=True, Lfemm=FEMM_dict["Lfemm"], L1=L1, sym=sym
        )
        # Load mesh data & solution
        if self.is_save_mesh or self.is_save_FEA:
            mesh[ii] = self.get_FEMM_mesh(self.is_save_mesh, self.is_save_FEA, ii)

    # Shift to take into account stator position
    roll_id = int(self.angle_stator * Na_tot / (2 * pi))
    Br = roll(Br, roll_id, axis=1)
    Bt = roll(Bt, roll_id, axis=1)

    # Store the results
    output.mag.Br = Br
    output.mag.Bt = Bt
    output.mag.Tem = Tem
    output.mag.Tem_av = mean(Tem)
    if output.mag.Tem_av != 0:
        output.mag.Tem_rip = abs((np_max(Tem) - np_min(Tem)) / output.mag.Tem_av)
    output.mag.Phi_wind_stator = Phi_wind_stator
    output.mag.mesh = mesh
    if self.is_save_FEA:
        # saving:
        path_save = join(MAIN_DIR, "Results", self.parent.name, "Femm") + '\\'
        savetxt(path_save + 'Br.dat', Br)
        savetxt(path_save + 'Bt.dat', Bt)

    # Electromotive forces computation (update output)
    self.comp_emf()
