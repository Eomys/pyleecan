from os import remove
from os.path import join

from ....Classes.Material import Material
from ....Functions.load import load_matlib
from ....Functions.Material.compare_material import compare_material
from ....Functions.Material.replace_material_pyleecan_obj import (
    replace_material_pyleecan_obj,
)
from ....definitions import config_dict
from ....GUI import GUI_logger

from PyQt5.QtCore import QObject, pyqtSignal


class MatLib(QObject):
    saveNeeded = pyqtSignal()

    def __init__(self, path=None):
        """MatLib contains the material library and the specific machine materials.
        """
        # Dict containing the material library and the specific machine materials
        self.dict_mat = {
            "RefMatLib": [],  # Reference Material Library
            "MachineMatLib": [],  # Machine-specific materials
        }

        # Reference material library path
        self.ref_path = path

        # Load the material reference from the path
        if path:
            self.load_mat_ref(path)

        self.machine = None

    def load_mat_ref(self, path):
        """Remove the reference materials and load materials from the path
        
        Parameters
        ----------
        self: MatLib
        path: str
            new material library path
        """
        # Load a complete new matlib
        self.dict_mat["RefMatLib"] = load_matlib(path)

        # Remove MATLIB_DIR at the beginning of the material path
        for mat in self.dict_mat["RefMatLib"]:
            if config_dict["MAIN"]["MATLIB_DIR"].replace(
                "\\", " / "
            ) in mat.path.replace("\\", "/"):
                mat.path = mat.path.replace("\\", "/")[
                    len(config_dict["MAIN"]["MATLIB_DIR"].replace("\\", " / ")) + 1 :
                ]
            mat.path = mat.path.replace("\\", "/").strip("/")

        self.ref_path = path

    def add_machine_mat(self, machine):
        """
        Add machine materials if they are not in the MatLib 
        
        Parameters
        ----------
        self: MatLib
        
        machine: Machine
            Machine containing material to add 

        Returns
        -------
        is_change: bool
            Machine has changed
        """
        # Set the machine
        self.machine = machine

        # No change by default
        is_change = False

        # Remove previous machine materials
        self.dict_mat["MachineMatLib"] = []

        list_mach_mat = machine.get_material_list()
        if not isinstance(list_mach_mat, list):
            list_mach_mat = [list_mach_mat]

        # Copy the matlib and remove the name and the path to compare the materials
        list_mat_noname = [
            Material(init_dict=mat.as_dict()) for mat in self.dict_mat["RefMatLib"]
        ]
        for mat in list_mat_noname:
            mat.name = ""
            mat.path = ""

        # Add the material to machine material if it is not already contained in the Matlib
        for material in list_mach_mat:
            # Avoid materials from the default machine
            if material.is_isotropic == None or material == Material():
                continue

            # Store name and path to compare other attributes
            name = material.name
            path = material.path
            material.name = ""
            material.path = ""

            # Add the material if not in matlib
            if material not in list_mat_noname:
                material.name = name
                material.path = path
                self.dict_mat["MachineMatLib"].append(material)
                self.check_material_duplicated_name("MachineMatLib", -1)

                is_change_mat = replace_material_pyleecan_obj(
                    machine, material, material, False
                )
                is_change = is_change or is_change_mat

            # Replace the material in the machine by the MatLib one
            else:
                material.name = name
                material.path = path
                for mat in self.dict_mat["RefMatLib"]:
                    # Find the material in the matlib
                    if material == mat:  # Same name and path
                        # No need to change the material
                        break
                    elif compare_material(material, mat):
                        # Replace material by mat in machine
                        is_change_mat = replace_material_pyleecan_obj(
                            machine, material, mat, False
                        )

                        is_change = is_change or is_change_mat
                        break

        return is_change

    def move_mach_mat_to_ref(self, key, index):
        """
        Move a machine material into the matlib reference

        Parameters
        ----------
        self: MatLib 
        key: str
            machine name to move the right material  
        index: int
            position of the machine material in its machine materials list
        """

        # Move the material into the Material library
        mat = self.dict_mat["MachineMatLib"].pop(index)
        self.dict_mat["RefMatLib"].append(mat)

        # Set the path of the new matlib material
        new_path = self.dict_mat["RefMatLib"][-1].name + ".json"
        self.dict_mat["RefMatLib"][-1].path = new_path

        self.dict_mat["RefMatLib"][-1].save(
            join(config_dict["MAIN"]["MATLIB_DIR"], new_path)
        )

    def move_ref_mat_to_mach(self, key, index):
        """
        Move a material from the reference material library to 
        the machine materials

        self: MatLib
        key: str
            key to select the right machine list
        index: int
            material to move position in the reference material list
        """

        mat_to_move = self.dict_mat["RefMatLib"].pop(index)

        # Get material logger
        logger = mat_to_move.get_logger()

        # Try to remove the material from the material library
        try:
            remove(join(config_dict["MAIN"]["MATLIB_DIR"], mat_to_move.path))
            logger.info(
                'Delete material "{}" file: {}'.format(
                    mat_to_move.name,
                    join(config_dict["MAIN"]["MATLIB_DIR"], mat_to_move.path),
                )
            )
        except FileNotFoundError:
            logger.warning(
                'Couldn\'t delete material "{}" file: {}'.format(
                    mat_to_move.name,
                    join(config_dict["MAIN"]["MATLIB_DIR"], mat_to_move.path),
                )
            )

        self.dict_mat[key].append(mat_to_move)

    def delete_material(self, key, index):
        """
        Remove the material and delete the material file

        Parameters
        ----------
        self: MatLib

        key: str
            List selector in the dict : RefMatLib or MachineMatLib TODO MachineName in the future

        index: int
            position of the material to remove
        """
        # Get the material
        mat_to_del = self.dict_mat[key].pop(index)

        # Delete the material file if the material is in the Reference Material Library
        if key == "RefMatLib":
            GUI_logger.info("Deleting the material: " + mat_to_del.path)
            remove(
                join(config_dict["MAIN"]["MATLIB_DIR"], mat_to_del.path)
            )  # Delete the file

    def check_material_duplicated_name(self, key, index):
        """
        Check if a material name is already used, modify it and its path if needed

        Parameters
        ----------
        self: MatLib

        key: str
            List selector in the dict : RefMatLib or MachineMatLib TODO MachineName in the future
        index: int
            position of the material to check
        """
        if index == -1:
            index += len(self.dict_mat[key])

        is_renamed = False
        mat_duplicated = True

        # Get the material name
        name = self.dict_mat[key][index].name
        if name == None:
            is_renamed = True
            name = "Untitled"

        list_mat_name = []
        for key_iter in self.dict_mat.keys():
            for i, mat in enumerate(self.dict_mat[key_iter]):
                if i != index or key_iter != key:
                    list_mat_name.append(mat.name)

        # Browse the material list name and change the name while the name exist
        while mat_duplicated:
            mat_duplicated = False
            for ref_mat_name in list_mat_name:
                if ref_mat_name == name:
                    is_renamed = True
                    if name.endswith(")") and "(" in name:
                        idx = name.rfind("(")
                        num = int(name[idx + 1 : -1]) + 1
                        name = "{}({})".format(name[:idx], num)
                    else:
                        name += "(1)"
                    mat_duplicated = True
                    break

        # Change path to save the material
        if is_renamed:
            self.dict_mat[key][index].name = name
            path = self.dict_mat[key][index].path
            if path == None:
                path = ""
            else:
                path = path.replace("\\", " / ")

            # Remove the previous file if needed
            if key == "RefMatLib":
                try:
                    remove(path)
                except FileNotFoundError:
                    logger = self.dict_mat[key][index].get_logger()
                    logger.warning(
                        'Couldn\'t delete old material "{}" file: {}'.format(name, path)
                    )

            idx = path.rfind("/")
            if idx == -1:
                self.dict_mat[key][index].path = (
                    self.dict_mat[key][index].name + ".json"
                )
            else:
                self.dict_mat[key][index].path = (
                    path[: idx + 1] + self.dict_mat[key][index].name + ".json"
                )

    def add_new_mat_ref(self, material):
        """
        Add a new material in the reference matlib

        Parameters
        ----------
        self: MatLib
        material: Material
            material to add
        """
        self.dict_mat["RefMatLib"].append(material)

        # Check if the material is duplicated
        self.check_material_duplicated_name("RefMatLib", -1)

        material.path = material.name + ".json"

        GUI_logger.info("Creating the material: " + material.path)

        # Saving the material
        material.save(join(config_dict["MAIN"]["MATLIB_DIR"], material.path))

    def add_new_mat_mach(self, material):
        """
        Add a new material in the machine materials

        Parameters
        ----------
        self: MatLib
        material: Material
            material to add
        """
        self.dict_mat["MachineMatLib"].append(material)
        self.check_material_duplicated_name("MachineMatLib", -1)

    def replace_material(self, key, index, material, save=True):
        """
        Replace a material

        Parameters
        ----------
        self: MatLib
        key: str
            dict_mat key to select the right material list
        index: int
            index of the material to replace
        material: Material
            new material 
        save: bool 
            save modification in the MatLib file
        
        Returns
        -------

        is_change: bool
            Machine has been change 
        """
        is_change = False
        # Replace the material in the current machine
        if self.machine != None:
            is_change = replace_material_pyleecan_obj(
                self.machine, self.dict_mat[key][index], material, comp_name_path=False
            )

        # Material Library
        if key == "RefMatLib":
            if save:
                try:
                    # Delete the previous material
                    remove(
                        join(
                            config_dict["MAIN"]["MATLIB_DIR"],
                            self.dict_mat["RefMatLib"][index].path,
                        )
                    )
                except FileNotFoundError:
                    logger = material.get_logger()
                    logger.warning(
                        'Couldn\'t remove machine "{}" file: {}'.format(
                            material.name,
                            join(
                                config_dict["MAIN"]["MATLIB_DIR"],
                                self.dict_mat["RefMatLib"][index].path,
                            ),
                        )
                    )

            # Replace the material
            self.dict_mat[key][index] = material

            # Check its name
            self.check_material_duplicated_name(key, index)

            # Set its path
            material.path = material.name + ".json"

            if save:
                # Save it
                material.save(join(config_dict["MAIN"]["MATLIB_DIR"], material.path))

        # Machine material
        else:
            # Replace the material
            self.dict_mat[key][index] = material

            # Check its name
            self.check_material_duplicated_name(key, index)

        return is_change
