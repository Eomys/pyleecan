from SciDataTool import DataFreq

from ....Classes.SolutionData import SolutionData
from ....Classes.MeshSolution import MeshSolution

from ....Functions.Electrical.comp_loss_joule import comp_loss_joule


def get_loss_scalar(self, group, felec):

    # Store coeff_dict
    if "coeff_dict" in out_dict:
        self.coeff_dict = out_dict.pop("coeff_dict")

    if lam is None:
        lam = self.parent.simu.machine.stator

    if OP is None:
        OP = self.parent.elec.OP

    felec = OP.get_felec(p=lam.get_pole_pair_number())
