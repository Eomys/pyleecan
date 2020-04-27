from pyleecan.Classes.Material import Material
from pyleecan.Classes.MatMagnetics import MatMagnetics
from pyleecan.Classes.ImportMatrixXls import ImportMatrixXls
from os.path import dirname, abspath, join

file_path = abspath(join(dirname(__file__), "M530-65A.xlsx"))

M530_65A = Material(name="M530-65A")
M530_65A.mag = MatMagnetics()

M530_65A.mag.mur_lin = 2500.0
M530_65A.mag.Wlam = 0.0005
M530_65A.mag.BH_curve = ImportMatrixXls(file_path=file_path, sheet="BH")

M530_65A.struct.rho = 7650.0
M530_65A.struct.Ex = 215000000000.0
M530_65A.struct.Ey = 215000000000.0
M530_65A.struct.Ez = 80000000000.0
M530_65A.struct.Gxy = 0.0
M530_65A.struct.Gxz = 2000000000.0
M530_65A.struct.Gyz = 2000000000.0
M530_65A.struct.nu_xy = 0.3
M530_65A.struct.nu_xz = 0.03
M530_65A.struct.nu_yz = 0.03
