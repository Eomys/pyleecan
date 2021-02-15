from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.InputElec import InputElec


def initialize_simu(SCIM, eec_scim, simuname, slip, felec, Ud_ref):

	simu = Simu1(name=simuname, machine=SCIM)
	simu.elec = Electrical(
	    eec=eec_scim,
	)

	# Run only Electrical module
	simu.mag = None
	simu.force = None
	simu.struct = None

	# Definition of a sinusoidal current
	simu.input = InputElec()
	simu.input.felec = felec  # [Hz]
	simu.input.Id_ref = None  # [A]
	simu.input.Iq_ref = None  # [A]
	simu.input.Ud_ref = Ud_ref  # [V]
	simu.input.Uq_ref = 0  # [V]
	simu.input.Nt_tot = 360  # Number of time steps
	simu.input.Na_tot = 2048  # Spatial discretization
	simu.input.N0 = simu.input.felec*60/SCIM.get_pole_pair_number()*(1-slip)
	simu.input.rot_dir = 1  # To enforce the rotation direction
	simu.input.Nrev = 5

	return simu

