from pyleecan.SCIM.SCIMSimu import SCIMSimu

Pref = 3500
s = 0.05
i=0
out, para = SCIMSimu("SCIM_010.json", 50, s, 400)
P = out.elec.Pem_av_ref

'''
while i < 2 and not(abs(Pref-P) < Pref*0.1):
	if Pref-P > 0:
		s += 0.001
	else :
		s -= 0.001
	i +=1
	out = SCIMSimu("SCIM_010.json", 50, s, 400)
	P = out.elec.Pem_av_ref
'''
print(out.elec)
print(para)

#print(out.mag)

