from os.path import join
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_SCIM import EEC_SCIM
from pyleecan.Classes.InputElec import InputElec
from pyleecan.SCIM.initialize_simu import initialize_simu
from pyleecan.SCIM.printout import printout
from numpy import angle, cos

def SCIMSimu(machinefile, felec, slip, U):

	""" Run SCIM simulation

    Parameters
    ----------
    machinefile: string
        location of the .json file of the wanted machine

    felec: float
    	Electrical frequency

    slip: float
    	The slip of the machine

    U: float
    	Voltage applied to the stator




    Returns
    -------
    Rrot: out
         output of the simulation

    """


	SCIM = load(join(DATA_DIR, "Machine", machinefile))


	# electrical parameter estimation (N0, felec, ... are independent of elec. simu.)
	eec_scim = EEC_SCIM()
	eec_scim.is_periodicity_a = True
	eec_scim.I = 2
	eec_scim.N0 = felec*60*(1-slip)/SCIM.get_pole_pair_number()
	eec_scim.felec = felec
	eec_scim.Nrev = 1 / 6
	eec_scim.Nt_tot = 8
	eec_scim.nb_worker = 4

	simu = initialize_simu(SCIM, eec_scim, "SCIMSimu", slip, felec, U)


	out = simu.run()

	para = eec_scim.parameters
	#print(simu.input)
	#printout(out)

	return out, para


