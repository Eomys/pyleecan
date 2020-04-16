from ....Classes.Material import Material
from ....Classes.MatMagnetics import MatMagnetics


Magnet1 = Material(name="Magnet1")
Magnet1.mag = MatMagnetics()

Magnet1.elec.rho = 1.6e-06

Magnet1.mag.mur_lin = 1.05
Magnet1.mag.Hc = 757880.681389978
Magnet1.mag.alpha_Br = 0.0
Magnet1.mag.Brm20 = 1
Magnet1.mag.Wlam = 0

Magnet1.struct.rho = 7500.0
