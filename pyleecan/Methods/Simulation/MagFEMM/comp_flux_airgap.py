# -*- coding: utf-8 -*-

from ....Functions.FEMM.draw_FEMM import draw_FEMM
from ....Classes._FEMMHandler import FEMMHandler


def comp_flux_airgap(self, output, axes_dict):
    """Build and solve FEMM model to calculate and store magnetic quantities

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    output : Output
        an Output object
    axes_dict: {Data}
        Dict containing Time axis used in MagFEMM to store torque result
    """

    # Set the symmetry factor according to the machine
    sym, is_antiper_a = output.mag.Angle.get_periodicity()

    # Setup the FEMM simulation
    # Geometry building and assigning property in FEMM
    # Instanciate a new FEMM
    femm = FEMMHandler(not self.is_close_femm)
    if not self.import_file:  # True if None or len == 0
        self.get_logger().debug("Drawing machine in FEMM...")
        output.mag.FEMM_dict = draw_FEMM(
            femm,
            output,
            is_mmfr=self.is_mmfr,
            is_mmfs=self.is_mmfs,
            sym=sym,
            is_antiper=is_antiper_a,
            type_calc_leakage=self.type_calc_leakage,
            is_remove_vent=self.is_remove_vent,
            is_remove_slotS=self.is_remove_slotS,
            is_remove_slotR=self.is_remove_slotR,
            type_BH_stator=self.type_BH_stator,
            type_BH_rotor=self.type_BH_rotor,
            kgeo_fineness=self.Kgeo_fineness,
            kmesh_fineness=self.Kmesh_fineness,
            user_FEMM_dict=self.FEMM_dict,
            path_save=self.get_path_save_fem(output),
            is_sliding_band=self.is_sliding_band,
            transform_list=self.transform_list,
            rotor_dxf=self.rotor_dxf,
            stator_dxf=self.stator_dxf,
        )
    else:
        self.get_logger().debug("Reusing the FEMM file: " + self.import_file)
        output.mag.FEMM_dict = self.FEMM_dict
        # Open the document
        femm.openfemm(1)
        # femm.main_minimize()
        femm.opendocument(self.import_file)

    # Solve for all time step and store all the results in output
    Time_Tem = axes_dict["Time_Tem"]
    if self.nb_worker > 1:
        self.solve_FEMM_parallel(femm, output, sym, Time_Tem)
    else:
        self.solve_FEMM(femm, output, sym, Time_Tem)
