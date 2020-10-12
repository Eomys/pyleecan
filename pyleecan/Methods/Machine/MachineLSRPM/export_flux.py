# -*- coding: utf-8 -*-
"""@package Methods.Machine.Machine.export_flux
Export the machine point to flux plot methods
@date Created on Fri Feb 12 11:06:16 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from os import getcwd
from os.path import join

from pyleecan.Functions.gen_flux_code import GAP_COLOR
from pyleecan.Functions.gen_flux_code.gen_flux_application import gen_flux_application
from pyleecan.Functions.gen_flux_code.gen_flux_assembly import gen_flux_assembly
from pyleecan.Functions.gen_flux_code.gen_flux_circle import gen_flux_circle
from pyleecan.Functions.gen_flux_code.gen_flux_extrude import gen_flux_extrude
from pyleecan.Functions.gen_flux_code.gen_flux_material import gen_flux_material
from pyleecan.Functions.gen_flux_code.gen_flux_param import gen_flux_param
from pyleecan.Functions.gen_flux_code.gen_flux_set import gen_flux_set


def export_flux(self, file_path=None):
    """Generate the code needed to create the Lamination in Flux

    Parameters
    ----------
    self :
        A Slot object
    file_path :
        Path to save the code, if None, use default path

    Returns
    -------
    (str, dict)
        code,obj_cpt: The code needed to create the slot and the
        object counter

    """

    obj_cpt = {"Point": 0, "Line": 0}
    if file_path is None:
        file_path = join(getcwd(), "Machine_flux_export.py")

    # Open the context to draw the geometry
    code = "#! Flux3D 12.1\n\n"
    code += "newProject()\n"

    # Get all the length of the machine for extrude
    L_dict = self.stator.get_length()
    L_dict.update(self.rotor.get_length())
    L_dict.update(self.frame.get_length())
    L_dict.update(self.shaft.get_length())
    L_dict["Lgap"] = max(self.stator.L1, self.rotor.L1) * 1.1
    # Create the associated parameters in Flux
    code += "\n#Creating length parameters\n"
    for name, value in L_dict.items():
        code = gen_flux_param(code, name, "", value)
    code += "\n"
    # Create application and Mechanical set
    code = gen_flux_application(code)
    code = gen_flux_set(code)

    # Adding material
    mat_list = list()
    mat_list.append(self.rotor.mat_type)
    if self.stator.mat_type.name != self.rotor.mat_type.name:
        mat_list.append(self.stator.mat_type)
    if self.shaft.mat_type.name not in [
        self.stator.mat_type.name,
        self.rotor.mat_type.name,
    ]:
        mat_list.append(self.shaft.mat_type)
    if self.frame.mat_type.name not in [
        self.shaft.mat_type.name,
        self.stator.mat_type.name,
        self.rotor.mat_type.name,
    ]:
        mat_list.append(self.frame.mat_type)

    code = gen_flux_material(code, mat_list)

    code += "openModelerContext()\n"
    code += "lastInstance = Sketch(name='Sketch_1',\n\
       referencePlane=ReferencePlane['XY_PLANE'])\n"
    code += "Sketch[1].openContext()\n\n"

    # Get the code needed to plot the Machine Geometry
    (code, obj_cpt) = self.frame.export_geo_flux(code, obj_cpt)

    code += "\n#Stator\n"
    (code, obj_cpt) = self.stator.export_geo_flux(code, obj_cpt)

    code += "\n#Rotor\n"
    (code, obj_cpt) = self.rotor.export_geo_flux(code, obj_cpt)

    # Add the Airgap
    Rgap = (self.stator.comp_mec_radius() + self.rotor.comp_mec_radius()) / 2.0
    (code, obj_cpt) = gen_flux_circle(code, obj_cpt, Zc=0, R=Rgap, color="BLACK")

    # All the geometry code is generated (and evaluated)
    # Resolve all the conflict in the geometry (intersection and superposition)
    code += "healAndSimplifyAllGeometry()\n"
    code += "Sketch[1].closeContext()\n\n"

    # Assign all the region to the generated Faces
    code += "FaceAutomatic[ALL].setVisible()\n"
    code += "Line[ALL].setVisible()\n\n"

    # Get the minimum length of the machine for extrude
    key_min = min(L_dict, key=L_dict.get)
    Lmin = (key_min, L_dict[key_min])

    code = self.shaft.export_vol_flux(code, Lmin)
    code = self.frame.export_vol_flux(code, Lmin)
    code = self.stator.export_vol_flux(code, Lmin)
    code = self.rotor.export_vol_flux(code, Lmin)

    # Create the Airgap Volume
    mec_gap = self.comp_width_airgap_mec()
    if self.rotor.is_internal:
        code = gen_flux_extrude(
            code,
            Rgap - mec_gap / 4.0,
            "R_Gap",
            GAP_COLOR,
            ("Lgap", L_dict["Lgap"]),
            Lmin,
        )
        code = gen_flux_extrude(
            code,
            Rgap + mec_gap / 4.0,
            "S_Gap",
            GAP_COLOR,
            ("Lgap", L_dict["Lgap"]),
            Lmin,
        )
    else:
        code = gen_flux_extrude(
            code,
            Rgap - mec_gap / 4.0,
            "S_Gap",
            GAP_COLOR,
            ("Lgap", L_dict["Lgap"]),
            Lmin,
        )
        code = gen_flux_extrude(
            code,
            Rgap + mec_gap / 4.0,
            "R_Gap",
            GAP_COLOR,
            ("Lgap", L_dict["Lgap"]),
            Lmin,
        )
    code += "startMacroTransaction()\n"
    code += "RegionVolume['R_GAP'].magneticDC3D=MagneticDC3DVolumeVacuum()\n"
    code += "RegionVolume['R_GAP'].mechanicalSet=MechanicalSet['ROTOR_SET']\n"
    code += "RegionVolume['S_GAP'].magneticDC3D=MagneticDC3DVolumeVacuum()\n"
    code += "RegionVolume['S_GAP'].mechanicalSet=MechanicalSet['STATOR_SET']\n"
    code += "endMacroTransaction()\n"

    # Create the Assembly of All object
    obj_list = ["S_Gap", "R_Gap", "R_Lam"]
    if self.shaft.Drsh > 0:
        obj_list.append("R_Shaft")
    if self.frame.comp_equivalent_height() > 0:
        obj_list.append("S_Frame")
    code = gen_flux_assembly(code, "Machine", "S_Lam", obj_list)

    code += "closeModelerContext()\n"
    # Infinity Box
    if self.rotor.is_internal:
        ext_rad = self.stator.Rext + self.frame.comp_equivalent_height()
    else:
        ext_rad = self.rotor.Rext + self.frame.comp_equivalent_height()

    # Get the maximum length of the machine for infinity box (should be shaft)
    Lmax = max(L_dict, key=L_dict.get)

    code += (
        "lastInstance = InfiniteBoxCylinderZ(size=['"
        + str(ext_rad * 1.1)
        + "',\n\
                                              '"
        + str(ext_rad * 1.3)
        + "',\n\
                                              '"
        + Lmax
        + "*0.6',\n\
                                              '"
        + Lmax
        + "*0.8'])\n"
    )
    code += "InfiniteBoxCylinderZ['InfiniteBoxCylinderZ'].complete3D(buildingOption='Volumes',\n\
           coordSys=CoordSys['XYZ1'],\n\
           linkMesh='NoLinkMesh')\n"
    code += "InfiniteBoxCylinderZ['InfiniteBoxCylinderZ'].setInvisible()\n"

    # Write the file with the generated lines
    with open(file_path, "w") as m_file:
        m_file.write(code)
