from pyleecan.Classes.import_all import *
from numpy import array, zeros, ones, pi, sqrt, linspace, exp, cos, sin
from os import remove, getcwd
from os.path import isfile, join, isdir
from pyleecan.Functions.load import load
import matplotlib.pyplot as plt
from Tests import save_plot_path as save_path
from Tests.Plot.LamWind import wind_mat
from pyleecan.definitions import DATA_DIR

from pyleecan.Classes.MachineUD import MachineUD
import matplotlib.pyplot as plt

LSPM = MachineUD()
from numpy import pi



Copper1 = load(join(DATA_DIR, "Material", "Copper1.json"))
M400_50A = load(join(DATA_DIR, "Material", "M400-50A.json"))


mm = 1e-3  # Millimeter

# Stator Lamination setup
stator = LamSlotWind(
    Rint=132.5 * mm, # internal radius [m]
    Rext=200 * mm, # external radius [m]
    L1=350 * mm, # Lamination stack active length [m] without radial ventilation airducts 
                # but including insulation layers between lamination sheets
    Nrvd=0, # Number of radial air ventilation duct
    Kf1=0.95, # Lamination stacking / packing factor
    is_internal=False,
    is_stator=True, 
)


# Stator Slot setup
stator.slot = SlotW10(
    Zs=48, # Slot number
    H0=1.0 * mm,  # Slot isthmus height
    H1=1*mm, # Height
    H2=30 * mm, # Slot height below wedge 
    W0=12 * mm,  # Slot isthmus width
    W1=14 * mm, # Slot top width
    W2=12 * mm, # Slot bottom width
)

#rotor winding setup
stator.winding = WindingDW1L(
    qs=3,  # number of phases
    Lewout=0,  # staight length of conductor outside lamination before EW-bend
    p=2,  # number of pole pairs
    Ntcoil=9,  # number of turns per coil
    Npcpp=1,  # number of parallel circuits per phase
    Nslot_shift_wind=0,  # 0 not to change the stator winding connection matrix built by pyleecan number 
                         # of slots to shift the coils obtained with pyleecan winding algorithm 
                         # (a, b, c becomes b, c, a with Nslot_shift_wind1=1)
    is_reverse_wind=False # True to reverse the default winding algorithm along the airgap 
                         # (c, b, a instead of a, b, c along the trigonometric direction)
)





#rotor Lamination setup
rotor = LamSquirrelCageMag(Rint=45 * mm,
    Rext=131 * mm,
    is_internal=True, 
    is_stator=False,
    L1=stator.L1,
    Hscr=20* mm,
    Lscr=15* mm,
    ring_mat=Copper1,
    )

# rotor magnets setup
rotor.hole = list()
rotor.hole.append(
    
    
    HoleM52(Zh=4, 
    W0=60 *mm,
     H0=25 * mm,
     H1=20 * mm,
      H2=0 *mm,
       W3=15*mm))







#rotor slot Setup
rotor.slot = SlotW21(
    Zs=28, # Slot number
    H0=3.0 * mm,  # Slot isthmus height
    H1=0 * mm,
    H2=15 * mm, # Slot height below wedge 
    W0=3 * mm,  # Slot isthmus width
    W1=13 * mm,
    W2=10 * mm, # Slot bottom width
)

#squirrel cage Setup
rotor.winding=WindingSC(is_reverse_wind=False,
              Nslot_shift_wind=0,
              qs=14,
              Ntcoil=1, 
              Npcpp=1,
              type_connection=0,
              p=3,
              Lewout=17* mm,
              conductor=-1,
              init_dict=None,
              init_str=None)

# Squirrel Cage Conductor bars Setup
rotor.winding.conductor = CondType21(
    Hbar=20* mm, 
    Wbar=10* mm, 
    Wins=0,
    cond_mat=-1, 
    ins_mat=-1,
    init_dict=None,
    init_str=None
)
#material setup
stator.mat_type = M400_50A  # Stator Lamination material
rotor.mat_type = M400_50A  # Rotor Lamination material
stator.winding.conductor.cond_mat = Copper1  # Stator winding conductor material





LSPM.lam_list = [stator,rotor]



LSPM.save('LSPM.json')

LSPM.plot()
fig = plt.gcf()
fig.savefig(join(save_path, "test1_LSPM.png"))
plt.show()
