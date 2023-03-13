from os.path import dirname, realpath, abspath, join, basename
from os import walk
import subprocess
from MermaidClass import MermaidClass

GEN_DIR = abspath(join(dirname(realpath(__file__)), ".."))


class Diagram:
    """A class representing an UML. It provides a method to write the mermaid
    code associated to it, given a list of classes.
    """

    folder_path_to_write_code = join(GEN_DIR, "UMLs", "code")
    folder_path_to_write_svg = join(GEN_DIR, "UMLs", "svg")

    def __init__(
        self,
        folder_path: list,
        name: str = None,
        direction: str = "TB",
        parent_class_name: str = None,
        composition: bool = True,
        only_class_names: bool = False,
        specify_direction: bool = False,
        exclude_list: list = None,
    ):
        """initialize an instance of the class

        Parameters
        ----------
        folder_path : list of folder paths
            All the csv files in all the folders listed will be parsed to create a class for each one.
            The directories will be traversed to find csv files in subdirectories.
        name : str, optional
            The name of the diagram (it will be the name of the .mmd and .svg files), by default None
        direction : str, optional
            Can be:
            -TB : top-bottom
            -BU: bottom-up
            -LR: left-right
            -RL: right-left
            It is the direction of the diagram, by default "TB"
        parent_class_name : str, optional
            The name of a class that will be the base of the diagram. If it is not
            provided, all the classes in the folders will appear in the diagram, by default None
        composition : bool, optional
            if False and a parent_class_name is provided, the component class will not
            be displayed on the diagram, only the descendants of the base class will
            appear. If no parent_class_name is provided, only the inheritance links
            will appear on the UML, by default True
        only_class_names : bool, optional
            if False, only the class names will appear in the diagram (not the names
            of the attributes and methods), by default False
        specify_direction : bool, optional
            if True, the direction will be appended to the name of the diagram, else not
        exclude_list : list, optional
            a list of class names to exclude from the diagram. The classes specified and
            all their descendants will be ignored when building the diagram.
        """
        # ------Storage of the parameters of the __init__ method--------
        self.parent_class_name = parent_class_name
        self.folder_path = folder_path
        self.direction = direction
        self.composition = composition
        self.only_class_names = only_class_names
        self.exclude_list = exclude_list
        if name:
            self.name = name
        else:
            self.name = "+".join([basename(path) for path in folder_path])
        if specify_direction:
            self.name += f"_{self.direction}"
        # ---------------------------------------------------------------
        print(f"Generating mermaid code for {self.name}")
        # Instanciate a dict that will contain all the MermaidClass objects
        # with their names as key
        self.folder_classes_dict = {}
        for path in folder_path:
            for root, _, files in walk(path):
                # Create a class for every .csv file in the folders
                for class_file in [csv for csv in files if csv.endswith(".csv")]:
                    file_path = join(root, class_file)
                    mermaid_class = MermaidClass(file_path)
                    self.folder_classes_dict[mermaid_class.name] = mermaid_class
        self.find_children()
        if self.composition:
            self.find_components()
        self.generate_classes_dict()
        self.exclude_classes()

    def find_components(self):
        """Find all the components of all the classes in self.folder_classes_dict
        and store their names in a set as an attribute of the classes
        """
        for mermaid_class in self.folder_classes_dict.values():
            # get the names of the components of the class
            composition_list = mermaid_class.get_clean_variable_types()
            for var_type in composition_list:
                if (
                    var_type in self.folder_classes_dict
                    and var_type != mermaid_class.name
                ):
                    mermaid_class.components_set.add(var_type)

    def find_children(self):
        """Find all the children of all the classes in self.folder_classes_dict
        and store their names in a list as an attribute of the classes
        """
        for mermaid_class in self.folder_classes_dict.values():
            parent = mermaid_class.parent
            if parent in self.folder_classes_dict:
                self.folder_classes_dict[parent].children_list.append(
                    mermaid_class.name
                )

    def find_relevant_classes(self):
        """Find all the relevant classes, that means the classes that will be included in the diagram.
        It is called only if a parent_classs_name is specified. This method finds all the descendants
        of the parent class and their components.
        -------
        The algorithm go from top to bottom. It starts with the base class and parse all the children
        to find their children, and so on until no children are found anymore.

        Returns
        -------
        list
            the list of names of the classes to include in the diagram
        """
        # The algorithme starts with the base class
        current_class = self.folder_classes_dict[self.parent_class_name]
        # The class list is instanciated. It will store all the relevant classes
        classes_list = [self.parent_class_name]
        # The current list is the list of classes names that are currently parsed
        current_list = list(current_class.components_set) + current_class.children_list
        temp_list = current_list[:]
        classes_list += temp_list
        # If current_list is empty, no children are found anymore and the algorithm can stop
        while current_list:
            temp_list = []
            for cls_name in current_list:
                current_class = self.folder_classes_dict[cls_name]
                # Appending to the temp_list all the children and components of the current_class
                temp_list += (
                    list(current_class.components_set) + current_class.children_list
                )
            # Stores the class names in the current list if they are not already in classes_list
            current_list = [item for item in temp_list if item not in classes_list]
            classes_list += current_list
        return classes_list

    def generate_classes_dict(self):
        """Generates the dictionnary of classes that will be included in the diagram.
        If no parent_class_name is specified, it is simply the self.folder_classes_dict.
        If a parent_class_name is specified, it calls the self.find_relevant_classes method to
        find all the classes to consider.
        """
        if self.parent_class_name:
            classes_list = self.find_relevant_classes()
            self.classes_dict = {
                name: self.folder_classes_dict[name] for name in classes_list
            }
        else:
            self.classes_dict = self.folder_classes_dict

    def exclude_classes(self):
        """This excludes some classes from the classes_dict generated by the method
        self.generate_classes_dict based on the self.exclude_list attribute. The classes
        specified in self.exclude_list are removed with all their descendants.
        It also creates a list self.full_exclude_list containing the names of all the classes
        removed.
        -------
        The algorithm is similar to the one used in the self.find_relevant_classes method
        to exclude all the descendants of the classes to exclude
        """
        if self.exclude_list:
            for class_name in self.exclude_list:
                current_class = self.folder_classes_dict[class_name]
                classes_list = [class_name]
                current_list = current_class.children_list
                temp_list = current_list[:]
                classes_list += temp_list
                while current_list:
                    temp_list = []
                    for cls_name in current_list:
                        current_class = self.folder_classes_dict[cls_name]
                        temp_list += current_class.children_list
                    current_list = [
                        item for item in temp_list if item not in classes_list
                    ]
                    classes_list += current_list
            self.full_exclude_list = classes_list
            for key in classes_list:
                self.classes_dict.pop(key, None)
        else:
            self.full_exclude_list = []

    def generate_mermaid_code(self):
        """This generate the mermaid code for the diagram, stored as a string in the
        self.mermaid_diagram attribute

        Returns
        -------
        string
            the mermaid diagram code that is to be written in a .mmd file
        """
        self.mermaid_diagram = f"classDiagram\ndirection {self.direction}\n"
        if not self.only_class_names:
            # The dict is sorted to ensure equality in the tests
            for mermaid_class in dict(sorted(self.classes_dict.items())).values():
                self.mermaid_diagram += mermaid_class.write_mermaid_class() + "\n"
            # The dict is sorted to ensure equality in the tests
        for mermaid_class in dict(sorted(self.classes_dict.items())).values():
            # The list is sorted to ensure equality in the tests
            for child in sorted(mermaid_class.children_list):
                # Check that the child class should not be excluded
                if child not in self.full_exclude_list:
                    self.mermaid_diagram += f"{mermaid_class.name}  <|--> {child}\n"
            # The list is sorted to ensure equality in the tests
            for var_type in sorted(mermaid_class.components_set):
                # Check that the component should not be excluded
                if var_type not in self.full_exclude_list:
                    self.mermaid_diagram += f"{mermaid_class.name} *--> {var_type}\n"
        return self.mermaid_diagram

    def save_mermaid_code(self):
        """This saves the mermaid code of the diagram stored in the self.mermaid_diagram
        attribute in a .mmd file. This file is named after self.name
        """
        file_path_to_write_code = join(
            self.folder_path_to_write_code, self.name + ".mmd"
        )
        with open(file_path_to_write_code, "w") as f:
            f.write(self.mermaid_diagram)

    def convert_to_svg(self):
        """This calls the mermaid CLI command to convert the diagram code to an svg file"""
        subprocess.run(
            [
                "powershell.exe",
                "./node_modules/.bin/mmdc.ps1",
                "-i",
                join(
                    self.folder_path_to_write_code, f"{self.name}.mmd"
                ),  # f"Diagrams_code/{self.name}.mmd",
                "-o",
                join(
                    self.folder_path_to_write_svg, f"{self.name}.svg"
                ),  # f"Diagrams_svg/{self.name}.svg",
                "-t",
                "forest",
                f"--configFile={join(dirname(__file__),'config.json')}",
            ]
        )

    def draw_diagram(self):
        """This calls all the methods necessary to get an svg diagram."""
        self.generate_mermaid_code()
        self.save_mermaid_code()
        self.convert_to_svg()
