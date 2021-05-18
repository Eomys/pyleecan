from pyleecan.Classes.import_all import *
from numpy import array, zeros, ones, pi, sqrt, linspace, exp, cos, sin
from os import remove, getcwd
from os.path import isfile, join, isdir
from pyleecan.Functions.load import load
import matplotlib.pyplot as plt
from Tests import save_plot_path as save_path
from Tests.Plot.LamWind import wind_mat
from pyleecan.definitions import DATA_DIR

m = load(join(DATA_DIR, "Machine", "Tesla_S.json"))

R2 = LamSquirrelCageMag(init_dict=m.rotor.as_dict())
R2.hole = list()
R2.hole.append(HoleM52(Zh=4, W0=0.02, H0=0.03, H1=0.005, H2=0.002, W3=0.002))
R2.plot(sym=2)
m.plot()
plt.show()
