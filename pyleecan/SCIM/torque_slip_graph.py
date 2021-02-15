#generate torque-slip curve

from pyleecan.SCIM.SCIMSimu import SCIMSimu
import matplotlib.pyplot as plt



slip = range(100)
P = [0]*len(slip)
T = [0]*len(slip)
i = 0
for s in slip:
	out = SCIMSimu("SCIM_010.json", 50, s/len(slip), 400)
	P[i] = out.elec.Pem_av_ref
	T[i] = out.elec.Tem_av_ref
	i += 1 
	print(str(s)+ "% Done", end="\r")


plt.figure()
plt.plot(slip,P)
plt.ylabel('Vermogen')
plt.xlabel('Slip')
plt.show()


plt.figure()
plt.plot(slip,T)
plt.ylabel('Koppel')
plt.xlabel('Slip')
plt.show()