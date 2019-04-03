from pyleecan.Classes.Material import Material
from pyleecan.Classes.MatMagnet import MatMagnet


Magnet3 = Material(name="Magnet3")
Magnet3.mag = MatMagnet()

Magnet3.elec.rho = 1.6e-06

Magnet3.mag.mur_lin = 1.05
Magnet3.mag.Hc = 909456.817667973
Magnet3.mag.alpha_Br = 0.0
Magnet3.mag.Brm20 = 1.2

Magnet3.struct.rho = 7500.0
