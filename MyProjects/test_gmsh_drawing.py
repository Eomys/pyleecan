import json

from os import makedirs
from os.path import join, isdir


from pyleecan.Functions.load import load
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Output import Output
from pyleecan.definitions import DATA_DIR
import matplotlib.pyplot as plt
from pyleecan.Functions.GMSH.draw_GMSH import draw_GMSH
from pyleecan.Methods.Simulation.MagElmer import MagElmer_BP_dict
from Tests import save_plot_path

save_path = join(save_plot_path, "GMSH")
if not isdir(save_path):
    makedirs(save_path)
mesh_dict = {
    "Lamination_Rotor_Bore_Radius_Ext": 180,
}

def test_gmsh():
    if True:
        #machine = load(join(DATA_DIR,"Machine", "Toyota_Prius.json"))
        machine = load("./MyProjects/12s8p_HWA_Audi.json")
        #machine.stator.slot.H1 = 1e-3
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        # It needs a change on the slot toothtip height
        # Sym=8 works but wrong bondary conditions
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1, #8
                sym=4,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_model_ipm.geo"),
                is_run=True,
            )

    if False:
        # machine = load(join(DATA_DIR,"Machine", "AUDI_eTron_loss.json"))
        machine = load(join(DATA_DIR,"Machine", "AUDI_eTron.json"))
        #machine.rotor.slot.W0 = 1e-3
        #print(machine.comp_periodicity_spatial())
        #print(machine.stator.winding.get_periodicity())
        #print(machine.rotor.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        # Sym=2 fails due to pyleecan runtime error (airgap issue)
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#2
                sym=2,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_audi_etron_loss.geo"),
                is_run=True,
            )

    if False:
        machine = load(join(DATA_DIR,"Machine", "Benchmark.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        # Sym=2 fails due to No Attribute 'is_trigo_direction' (airgap issue)
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#2
                sym=2,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        machine = load(join(DATA_DIR,"Machine", "BMW_i3.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        # Sym=12 works but wrong bondary conditions rotor/stator
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#12
                sym=12,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        # TO-DO: Something fails in the rotor-magnet-pocket sym=1,4
        machine = load(join(DATA_DIR,"Machine", "IPMSM_B.json"))
        machine.stator.slot.H1 = 1e-3
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        # It needs a change on the slot toothtip height
        # Sym=8 Still fails with newer modification and without airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#4
                sym=4,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        machine = load(join(DATA_DIR,"Machine", "IPMSM_xxx.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#8
                sym=8,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        # TO-DO: Rotor-air gap not drawn correctly sym=1,2
        machine = load(join(DATA_DIR,"Machine", "LSPM_001.json"))
        #print(machine.comp_periodicity_spatial())
        #print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#2
                sym=2,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        # TO-DO: Sliding Band Air gap does not work and Sym=1 either
        # sym=9 works without sliding band
        machine = load(join(DATA_DIR,"Machine", "Protean_InWheel.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#8
                sym=8,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=False,
                is_airbox=False,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        # TO-DO: Ducts are not removed from rotor core
        machine = load(join(DATA_DIR,"Machine", "Railway_Traction.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                sym=1,#
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        machine = load(join(DATA_DIR,"Machine", "Renault_Zoe.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#4
                sym=4,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        machine = load(join(DATA_DIR,"Machine", "SCIM_006.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#4
                sym=4,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        machine = load(join(DATA_DIR,"Machine", "SCIM_010.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#4
                sym=4,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        # TO-DO: Won't cut magnets from rotor in sym=2
        machine = load(join(DATA_DIR,"Machine", "SIPMSM_001.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#2
                sym=2,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        # TO-DO: Sliding Band with Sym=1 won't work because boolean intersection
        # Works with sym=4
        machine = load(join(DATA_DIR,"Machine", "Slotless_CEFC.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#4
                sym=4,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
    	# TO-DO: Won't cut magnets from rotor in sym=2
        machine = load(join(DATA_DIR,"Machine", "SPMSM_001.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#2
                sym=2,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        machine = load(join(DATA_DIR,"Machine", "SPMSM_002.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#2
                sym=2,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        machine = load(join(DATA_DIR,"Machine", "SPMSM_003.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#2
                sym=2,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        # TO-DO: Sliding Band does not work for outer rotor and Sym=1 either
        # sym=9 works without sliding band
        machine = load(join(DATA_DIR,"Machine", "SPMSM_015.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#9
                sym=9,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=False,
                is_airbox=False,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        machine = load(join(DATA_DIR,"Machine", "SPMSM_18s16p_loss.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#2
                sym=2,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        machine = load(join(DATA_DIR,"Machine", "SPMSM_020.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#2
                sym=2,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        # TO-DO: All the notches create air ragions not accounted for the air gap
        # surfaces
        machine = load(join(DATA_DIR,"Machine", "SPMSM_LamSlotMultiWind.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#2
                sym=2,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=False,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        machine = load(join(DATA_DIR,"Machine", "SPMSM_skew.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#2
                sym=2,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )


    if False:
        machine = load(join(DATA_DIR,"Machine", "SynRM_001.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#4
                sym=4,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    if False:
        machine = load(join(DATA_DIR,"Machine", "TESLA_S.json"))
        print(machine.comp_periodicity_spatial())
        print(machine.stator.winding.get_periodicity())
        #machine.plot(is_show_fig=True)
        #plt.show() 
        mySimu = Simu1(name="foo", machine=machine)
        myResults = Output(simu=mySimu)
        # Sym=1 fails due to airgap
        gmsh_dict = draw_GMSH(
                output=myResults,
                #sym=1,#2
                sym=2,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=mesh_dict,
                is_sliding_band=True,
                is_airbox=True,
                path_save=join(save_path, "GSMH_benchmark.geo"),
                is_run=True,
            )

    with open(join(save_path,"gmsh_dict.json"), "w") as fw:
            json.dump(gmsh_dict, fw, default=encode_complex, indent=4)

    return gmsh_dict


def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)

if __name__ == "__main__":
    gmsh_dict = test_gmsh()