def printout(out):
	print("Average torque: " + str(out.elec.Tem_av_ref))
	print("Average power: " + str(out.elec.Pem_av_ref))
	print("Joule losses: " + str(out.elec.Pj_losses))
	print("Rotor speed: " + str(out.elec.N0))