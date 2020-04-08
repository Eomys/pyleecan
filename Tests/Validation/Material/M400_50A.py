from ....Classes.Material import Material
from ....Classes.MatMagnetics import MatMagnetics
from ....Classes.ImportMatrixXls import ImportMatrixXls
from os.path import dirname, abspath, join

file_path = abspath(join(dirname(__file__), "M400-50A.xlsx"))

M400_50A = Material(name="M400-50A")
M400_50A.mag = MatMagnetics()

M400_50A.mag.mur_lin = 2500.0
M400_50A.mag.Wlam = 0.0005
M400_50A.mag.BH_curve = ImportMatrixXls(file_path=file_path, sheet="BH")

M400_50A.struct.rho = 7650.0
M400_50A.struct.Ex = 215000000000.0
M400_50A.struct.Ey = 215000000000.0
M400_50A.struct.Ez = 80000000000.0
M400_50A.struct.Gxy = 0.0
M400_50A.struct.Gxz = 2000000000.0
M400_50A.struct.Gyz = 2000000000.0
M400_50A.struct.nu_xy = 0.3
M400_50A.struct.nu_xz = 0.03
M400_50A.struct.nu_yz = 0.03
