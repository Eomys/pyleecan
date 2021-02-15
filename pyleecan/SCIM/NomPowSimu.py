from os.path import join
from pyleecan.SCIM.SCIMSimu import SCIMSimu


def NomPowSimu(refVal, refType, V, f)


	s = 0.05
	i=0
	out, para = SCIMSimu("SCIM_010.json", f, s, V)

	if refType == 'power':
		simVal = out.elec.Pem_av_ref
	else:
		simVal = out.elec.Tem_av_ref

	while i < 2 and not(abs(refVal-simVal) < Pref*0.1):
		if refVal-simVal > 0:
			s += 0.001
		else :
			s -= 0.001
		i +=1
		out = SCIMSimu("SCIM_010.json", f, s, V)
		if refType == 'power':
			simVal = out.elec.Pem_av_ref
		else:
			simVal = out.elec.Tem_av_ref

	return out


