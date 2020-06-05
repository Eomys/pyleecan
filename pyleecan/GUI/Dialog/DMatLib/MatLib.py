from os import remove
from os.path import join

from ....Classes.Material import Material
from ....Functions.load import load_matlib
from ....Functions.Material.compare_material import compare_material
from ....Functions.Material.replace_material_pyleecan_obj import (
    replace_material_pyleecan_obj,
)
from ....GUI import GUI_logger


class MatLib(object):
    def __init__(self, path):
        """MatLib contains the material library and the specific machine materials.
        """
        # List containing the material library and the specific machine materials
        self.list_mat = [] 
        
        # Pointer on the first machine material in the list
        self.index_first_mat_mach = 1

        # Reference material library path
        self.ref_path = path

        # Load the material reference from the path
        self.load_mat_ref(path)

    def load_mat_ref(self, path):
        """Remove the reference materials and load materials from the path
        
        Parameters
        ----------
        self: MatLib
        path: str
            new material library path
        """
        # Load a complete new matlib 
        if len(self.list_mat) in [0, self.index_first_mat_mach]:
            self.list_mat = load_matlib(path)
            self.index_first_mat_mach = len(self.list_mat)
        else:
            list_mat = load_matlib(path)
            for _ in range(self.index_first_mat_mach):
                self.list_mat.pop(0)
            self.index_first_mat_mach = len(list_mat)
            for idx, material in enumerate(list_mat):
                self.list_mat.insert(idx,material)
        
        self.ref_path = path

    
    def add_machine_mat(self, machine):
        """
        Add machine materials if it is not in the MatLib 
        
        Parameters
        ----------
        self: MatLib
        
        machine: Machine
            Machine containing material to add 
        """

        list_mach_mat = machine.get_material_list()
        if not isinstance(list_mach_mat,list):
            list_mach_mat = [list_mach_mat]

        # Copy the matlib and remove the name and the path to compare the materials
        list_mat_noname = [
            Material(init_dict=mat.as_dict())
            for mat in self.list_mat
        ]
        for mat in list_mat_noname:
            mat.name = ""
            mat.path = ""

        # Add the material to machine material if it is not already contained in the Matlib
        for material in list_mach_mat:
            # Avoid materials from the default machine
            if material.is_isotropic == None:
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
                self.list_mat.append(material)
                self.check_material_duplicated_name(-1)

            # Replace the material in the machine by the MatLib one
            else: 
                for mat in self.list_mat:
                    # Find the material in the matlib
                    if compare_material(material, mat):
                        # Replace material by mat in machine
                        replace_material_pyleecan_obj(
                            machine, material, mat
                        )
                        break

    def move_mach_mat_to_ref(self, index):
        """
        Move a machine material into the matlib reference

        Parameters
        ----------
        self: MatLib 

        index: int
            position of the machine material
        """
        assert index >= self.index_first_mat_mach, ValueError(
            'The material {} is already in the Material Library'.format(self.list_mat[index].name)
            )

        from ....definitions import MATLIB_DIR
        # Move the material into the Material library
        mat = self.list_mat.pop(index)
        index = self.index_first_mat_mach
        self.index_first_mat_mach += 1
        self.list_mat.insert(index, mat)

        # Set the path of the new matlib material
        new_path = join(MATLIB_DIR, self.list_mat[index].name + ".json").replace(
            "\\", "/"
        )
        self.list_mat[index].path = new_path
        self.list_mat[index].save(new_path)


    def delete_material(self, index):
        """
        Remove the material and delete the material file

        Parameters
        ----------
        self: MatLib

        index: int
            position of the material to remove
        """

        # Get the material
        mat_to_del = self.list_mat.pop(index)

        GUI_logger.info("Deleting the material: " + mat_to_del.path)

        # Reference material
        if index < self.index_first_mat_mach:
            remove(mat_to_del.path) # Delete the file 

            # Change index_first_mat_mach
            self.index_first_mat_mach -= 1

            

    def check_material_duplicated_name(self, index):
        """
        Check if a material name is already used, modify it and its path if needed

        Parameters
        ----------
        self: MatLib

        index: int
            position of the material to check
        """
        if index == -1:
            index += len(self.list_mat)

        is_renamed = False
        mat_duplicated = True

        # Get the material name
        name = self.list_mat[index].name
        if name == None:
            is_renamed = True
            name = "Untitled"

        list_mat_name =[mat.name for i, mat in enumerate(self.list_mat) if i != index]

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
            self.list_mat[index].name = name
            path = self.list_mat[index].path
            if path == None:
                path = ""
            else:
                path = path.replace("\\", "/")

            idx = path.rfind("/")
            if idx == -1:
                self.list_mat[index].path = self.list_mat[index].name + ".json"
            else:
                self.list_mat[index].path = (
                    path[: idx + 1] + self.list_mat[index].name + ".json"
                )

    def add_mat_ref(self, material):
        """
        Add a material in the reference matlib

        Parameters
        ----------
        self: MatLib
        material: Material
            material to add
        """
        from ....definitions import MATLIB_DIR

        self.list_mat.insert(self.index_first_mat_mach, material)
        self.index_first_mat_mach +=1
        
        # Check if the material is duplicated
        self.check_material_duplicated_name(self.index_first_mat_mach-1)
        
        material.path= join(
            MATLIB_DIR, material.name + ".json"
        ).replace("\\", "/")

        GUI_logger.info(
            "Creating the material: " + material.path
        )
        
        # Saving the material
        material.save(material.path)

    def add_mat_mach(self, material):
        """
        Add a material in the machine materials

        Parameters
        ----------
        self: MatLib
        material: Material
            material to add
        """
        self.list_mat.append(material)
        self.check_material_duplicated_name(-1)

    def replace_material(self, index, material):
        """
        
        """
        from ....definitions import MATLIB_DIR

        # Material Library
        if index < self.index_first_mat_mach:
            # Delete the previous material
            remove(self.list_mat[index].path)

            # Replace the material
            self.list_mat[index] = material

            # Check its name 
            self.check_material_duplicated_name(index)

            # Set its path
            material.path= join(
                MATLIB_DIR, material.name + ".json"
            ).replace("\\", "/")

            # Save it 
            material.save()

        # Machine material
        else: 
            # Replace the material
            self.list_mat[index] = material

            # Check its name 
            self.check_material_duplicated_name(index)
            