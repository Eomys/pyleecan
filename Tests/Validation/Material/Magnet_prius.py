from pyleecan.Classes.Material import Material
from pyleecan.Classes.MatMagnetics import MatMagnetics


Magnet_prius = Material(name="Magnet_prius")
Magnet_prius.mag = MatMagnetics()

Magnet_prius.elec.rho = 1.6e-06

Magnet_prius.mag.mur_lin = 1.05
Magnet_prius.mag.Hc = 902181.163126629
Magnet_prius.mag.alpha_Br = -0.001
Magnet_prius.mag.Brm20 = 1.24
Magnet_prius.mag.Wlam = 0

Magnet_prius.struct.rho = 7500.0
