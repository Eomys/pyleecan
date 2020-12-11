"""
From tuto_Elec.ipynb
modified to test InputElec class
"""

# --- Load the machine ---
from os.path import join
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

SCIM = load(join(DATA_DIR, "Machine", "SCIM_010.json"))

# --- Initialization of the Simulation ---
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_SCIM import EEC_SCIM
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.InputElec import InputElec

from numpy import angle, cos

# Definition of the electrical simulation
simu = Simu1(name="tuto_elec", machine=SCIM)

eec_scim = EEC_SCIM()

simu.elec = Electrical(
    eec=eec_scim,
)

# eec_scim.parameters = {
#     "Lm": 0.6106,
#     # 'Lm_': 0.6077,
#     "Lr_norm": 0.0211,
#     "Ls": 0.0154,
#     "Rfe": None,
#     "slip": None,
# }

# Run only Electrical module
simu.mag = None
simu.force = None
simu.struct = None

# Definition of a sinusoidal current
simu.input = InputElec()
simu.input.felec = 50  # [Hz]
simu.input.Id_ref = None  # [A]
simu.input.Iq_ref = None  # [A]
simu.input.Ud_ref = 400  # [V]
simu.input.Uq_ref = 0  # [V]
simu.input.Nt_tot = 360  # Number of time steps
simu.input.Na_tot = 2048  # Spatial discretization
simu.input.N0 = 1418  # 1363.63  # Rotor speed [rpm]
simu.input.rot_dir = 1  # To enforce the rotation direction
simu.input.Nrev = 5


out = simu.run()

# compute some quantites
Us = out.elec.Ud_ref + 1j * out.elec.Uq_ref
Is = out.elec.Id_ref + 1j * out.elec.Iq_ref

PF = cos(angle(Us) - angle(Is))

# --- Print voltage and torque ---
print("Ud: " + str(abs(Us)))
print("Uq: " + str(abs(Is)))
print("PF: " + str(PF))

print("Tem: " + str(out.elec.Tem_av_ref))

# Plot the currents and plot the voltages
out.plot_2D_Data("elec.Is", "time", "phase")
out.plot_2D_Data("elec.Ir", "time", "phase[0]")
out.plot_2D_Data("elec.Us", "time", "phase")
