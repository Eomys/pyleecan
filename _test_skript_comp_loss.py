# --- Load Machine ------------------------------------------------------------------- #
# Change of directory to have pyleecan in the path
# from os import chdir
# chdir('..')

from pyleecan.Functions.load import load
from pyleecan.Classes.SolutionData import SolutionData
from numpy import abs, cos, pi, linspace, array

from SciDataTool import Data1D, DataTime
from SciDataTool.Functions.parser import read_input_strings

# Import the results
myResults = load("MyResults.json")

mySimu = myResults.simu
machine = mySimu.machine

print("Results loaded")

# --- Setup the Loss Model ----------------------------------------------------------- #
from pyleecan.Classes.Loss import Loss
from pyleecan.Classes.LossModel import LossModel
from pyleecan.Classes.LossModelBertotti import LossModelBertotti
from pyleecan.Classes.LossModelWinding import LossModelWinding

from pyleecan.Classes.ImportMatrixXls import ImportMatrixXls


myIronLoss = LossModelBertotti()
myWindingLoss = LossModelWinding()
mySimu.loss = Loss()
mySimu.loss.models = [myIronLoss, myWindingLoss]

myWindingLoss.lam = "machine.stator"

myIronLoss.name = "Stator Iron Losses"
myIronLoss.k_hy = None
myIronLoss.alpha_hy = 2
myIronLoss.k_ed = None
myIronLoss.alpha_ed = 2
myIronLoss.k_ex = 0
myIronLoss.alpha_ex = 1.5
myIronLoss.lam = "machine.stator"
myIronLoss.group = "stator core"

LossData = ImportMatrixXls()
# LossData.file_path = "pyleecan\\pyleecan\\Data\\Material\\M400-50A.xlsx"
LossData.file_path = "pyleecan\\Data\\Material\\M400-50A.xlsx"
LossData.is_transpose = False
LossData.sheet = "LossData"
LossData.skiprows = 2
LossData.usecols = None


machine.stator.mat_type.mag.LossData = LossData

# --- Run the Loss Simulation -------------------------------------------------------- #
myLoss = mySimu.loss
myLoss.run()

# myResults.mag.meshsolution.plot_contour(
#    label="B", group_names="stator", itime=0, clim=[0, 1.5]
# )

myResults.loss.meshsolutions[0].plot_contour(
    label="LossDens",
    itime=7,
)
myResults.loss.meshsolutions[0].plot_contour(
    label="LossDensSum",
    itime=0,
)

print(f"stator iron loss = {myResults.loss.losses[0].get_field([]).mean()} W")
print(f"stator winding loss = {myResults.loss.losses[1].get_field([]).mean()} W")
