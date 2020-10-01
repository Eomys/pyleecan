# --- Load Machine ------------------------------------------------------------------- #
# Change of directory to have pyleecan in the path
# from os import chdir
# chdir('..')

from pyleecan.Functions.load import load

# Import the machine from a script
IPMSM_A = load("pyleecan/Data/Machine/IPMSM_A.json")
# IPMSM_A = load("pyleecan/pyleecan/Data/Machine/IPMSM_A.json")

# Plot the machine
# %matplotlib notebook
im = IPMSM_A.plot()

# --- Simulation Setup --------------------------------------------------------------- #
from numpy import ones, pi, array, linspace
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.MagFEMM import MagFEMM

rotor_speed = 2000  # [rpm]

# Create the Simulation
mySimu = Simu1(name="EM_SIPMSM_AL_001", machine=IPMSM_A)

# Defining Simulation Input
mySimu.input = InputCurrent()

# time discretization [s]
n_step = 16
pp = IPMSM_A.rotor.get_pole_pair_number()
mySimu.input.time = ImportMatrixVal()
mySimu.input.time.value = linspace(
    start=0, stop=60 / rotor_speed / pp, num=n_step, endpoint=False
)  # n_step timesteps

# Angular discretization along the airgap circonference for flux density calculation
mySimu.input.angle = ImportMatrixVal()
mySimu.input.angle.value = linspace(
    start=0, stop=2 * pi, num=2048, endpoint=False
)  # 2048 steps

# Rotor speed [rpm]
mySimu.input.N0 = rotor_speed

# Stator currents [A]
mySimu.input.Id_ref = -100
mySimu.input.Iq_ref = 0
mySimu.input.rot_dir = 1

from pyleecan.Classes.MagFEMM import MagFEMM

# Definition of the magnetic simulation (is_mmfr=False => no flux from the magnets)
mySimu.mag = MagFEMM(
    type_BH_stator=0,  # 0 to use the B(H) curve,
    # 1 to use linear B(H) curve according to mur_lin,
    # 2 to enforce infinite permeability (mur_lin =100000)
    type_BH_rotor=0,  # 0 to use the B(H) curve,
    # 1 to use linear B(H) curve according to mur_lin,
    # 2 to enforce infinite permeability (mur_lin =100000)
    angle_stator=0,  # Angular position shift of the stator
    file_name="",  # Name of the file to save the FEMM model
    Kmesh_fineness=1,  # mesh fineness (1:default ,>1: finner ,<1: less fine)
    Kgeo_fineness=1,  # geometry fineness (1:default ,>1: finner ,<1: less fine)
)

# We only use the magnetic part
mySimu.force = None
mySimu.struct = None

mySimu.mag.is_symmetry_a = True  # 0 Compute on the complete machine,
# 1 compute according to sym_a and is_antiper_a
mySimu.mag.sym_a = 4  # Number of symmetry for the angle vector
mySimu.mag.is_antiper_a = False  # To add an antiperiodicity to the angle vector

mySimu.mag.is_get_mesh = True  # To get FEA mesh for latter post-procesing
mySimu.mag.is_save_FEA = False  # To save FEA results in a dat file

# --- Run the Simulation ------------------------------------------------------------- #
from pyleecan.Classes.Output import Output

myResults = Output(simu=mySimu)

mySimu.run()

# --- Save the results ----------------------------------------------------------------#
myResults.save(save_path="MyResults.json")
