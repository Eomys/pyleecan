from pyleecan.Classes.Material import Material
from pyleecan.Classes.MatMagnetics import MatMagnetics


Magnet5 = Material(name="Magnet5")
Magnet5.mag = MatMagnetics()

Magnet5.elec.rho = 1.6e-06

Magnet5.mag.mur_lin = 1.05
Magnet5.mag.Hc = 917035.624481873
Magnet5.mag.alpha_Br = 0.0
Magnet5.mag.Brm20 = 1.21
Magnet5.mag.Wlam = 0

Magnet5.struct.rho = 7500.0
