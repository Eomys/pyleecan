from pyleecan.Classes.Material import Material
from pyleecan.Classes.MatMagnet import MatMagnet


Magnet1 = Material(name="Magnet1")
Magnet1.mag = MatMagnet()

Magnet1.elec.rho = 1.6e-06

Magnet1.mag.mur_lin = 1.05
Magnet1.mag.Hc = 757880.681389978
Magnet1.mag.alpha_Br = 0.0
Magnet1.mag.Brm20 = 1

Magnet1.struct.rho = 7500.0
