# -*- coding: utf-8 -*-
from os.path import join

from ....Classes.ElmerResultsVTU import ElmerResultsVTU

# TODO define "Results" dir, etc. in __init__


def get_meshsolution(self, output):
    """Get and set the mesh data and solution data.

    Parameters
    ----------
    self : StructElmer
        a StructElmer object
    save_path: str
        Full path to folder in which the results are saved

    Returns
    -------
    success: bool
        Information if meshsolution could be created

    """
    # logger
    logger = self.get_logger()

    fea_path = self.get_path_save_fea(output)

    # if meshsoltion is not requested set meshsolution to None
    if not self.is_get_mesh or not self.is_save_FEA:
        logger.info("StructElmer: MeshSolution is not stored by request.")
        output.struct.meshsolution = None
        return False

    # setup Elmer result helper class
    ElmerVtu = ElmerResultsVTU()

    ElmerVtu.store_dict = {
        "displacement": {
            "name": "Displacement",
            "unit": "mm",
            "symbol": "disp",
            "norm": 1e-3,
        },
        "vonmises": {
            "name": "Von Mises Stress",
            "unit": "MPa",
            "symbol": "vonmises",
            "norm": 1e6,
        },
    }

    ElmerVtu.label = "Elmer Structural"
    ElmerVtu.file_path = join(fea_path, "Results", "case_t0001.vtu")

    output.struct.meshsolution = ElmerVtu.get_meshsolution()

    return True
