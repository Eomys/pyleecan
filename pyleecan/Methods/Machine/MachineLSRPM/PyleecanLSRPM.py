from os.path import join

import json
import pytest
import matplotlib.pyplot as plt
from export_flux import export_flux
from numpy import pi
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.HoleMLSRPM import HoleMLSRPM
from Tests import save_plot_path as save_path
from pyleecan.Classes.SlotWLSRPM import SlotWLSRPM
from pyleecan.Classes.WindingCW2LT import WindingCW2LT
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.Material import Material
from pyleecan.Classes.MatMagnetics import MatMagnetics
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load

mm = 1e-3  # Millimeter

# Lamination setup
stator = LamSlotWind(
    Rint=50.7 * mm,  # internal radius [m]
    Rext=72.5 * mm,  # external radius [m]
    L1=950
    * mm,  # Lamination stack active length [m] without radial ventilation airducts
    # but including insulation layers between lamination sheets
    Nrvd=0,  # Number of radial air ventilation duct
    Kf1=0.95,  # Lamination stacking / packing factor
    is_internal=False,
    is_stator=True,
)

# Slot setup
stator.slot = SlotWLSRPM(
    Zs=12, W1=8e-3, W3=11.6e-3, H2=14.8e-3, R1=0.75e-3  # Slot number
)

# Winding setup
stator.winding = WindingCW2LT(qs=3, p=4, Lewout=0)

# Conductor setup
stator.winding.conductor = CondType11(
    Nwppc_tan=1,  # stator winding number of preformed wires (strands)
    # in parallel per coil along tangential (horizontal) direction
    Nwppc_rad=1,  # stator winding number of preformed wires (strands)
    # in parallel per coil along radial (vertical) direction
    Wwire=0.000912,  #  single wire width without insulation [m]
    Hwire=2e-3,  # single wire height without insulation [m]
    Wins_wire=1e-6,  # winding strand insulation thickness [m]
    type_winding_shape=0,  # type of winding shape for end winding length calculation
    # 0 for hairpin windings
    # 1 for normal windings
)

# Rotor setup
rotor = LamHole(Rint=14e-3, Rext=50e-3, is_stator=False, is_internal=True, L1=0.95)

# Magnet setup
rotor.hole = list()
rotor.hole.append(
    HoleMLSRPM(
        Zh=8,
        W0=3.88e-3,
        W1=12.6 / 180 * pi,
        W2=0.0007,
        H1=0.0023515058436089,
        R1=0.0003,
        R2=0.019327,
        R3=0.0165,
    )
)


# Set shaft
shaft = Shaft(
    Drsh=rotor.Rint * 2,  # Diamater of the rotor shaft [m]
    # used to estimate bearing diameter for friction losses
    Lshaft=1.2,  # length of the rotor shaft [m]
)


# Loading Materials
M400_50A = load(join(DATA_DIR, "Material", "M400-50A.json"))
Copper1 = load(join(DATA_DIR, "Material", "Copper1.json"))

# Defining magnets
Magnet_prius = Material(name="Magnet_prius")

# Definition of the magnetic properties of the material
Magnet_prius.mag = MatMagnetics(
    mur_lin=1.05,  # Relative magnetic permeability
    Hc=902181.163126629,  # Coercitivity field [A/m]
    alpha_Br=-0.001,  # temperature coefficient for remanent flux density /°C compared to 20°C
    Brm20=1.24,  # magnet remanence induction at 20°C [T]
    Wlam=0,  # lamination sheet width without insulation [m] (0 == not laminated)
)

# Definition of the electric properties of the material
Magnet_prius.elec.rho = 1.6e-06  # Resistivity at 20°C

# Definition of the structural properties of the material
Magnet_prius.struct.rho = 7500.0  # mass per unit volume [kg/m3]


# Set Materials
stator.mat_type = M400_50A
rotor.mat_type = M400_50A
stator.winding.conductor.cond_mat = Copper1

# Set magnets in the rotor hole
rotor.hole[0].magnet_0.mat_type = Magnet_prius
rotor.hole[0].magnet_0.type_magnetization = 1

# matplotlib notebook
LSRPM = MachineIPMSM(
    name="LSRPM LSEE", stator=stator, rotor=rotor, shaft=shaft, frame=None
)
LSRPM.save("LSRPM LSEE.json")
export_flux(LSRPM)

LSRPM.plot()
plt.show()
