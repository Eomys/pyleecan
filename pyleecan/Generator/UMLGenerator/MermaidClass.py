from os.path import split
import pandas as pd


class MermaidClass:
    """This represents a Pyleecan class, getting the attributes and methods from
    a csv file, and providing a method to write the mermaid code associated
    to it.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.name = split(self.file_path)[1].split(".")[0]
        self.df = pd.read_csv(
            file_path,
            usecols=[0, 4, 10, 11, 14],
            names=["Variable name", "Type", "Inherit", "Methods", "Class description"],
            header=0,
        )
        self.variables = (
            self.df["Variable name"].dropna().to_list()
            if not pd.isnull(self.df["Variable name"][0])
            else []
        )
        self.variable_types = (
            self.df["Type"].dropna().to_list()
            if not pd.isnull(self.df["Type"][0])
            else []
        )
        self.methods = (
            self.df["Methods"].dropna().to_list()
        )  # if not pd.isnull(self.df["Methods"][0]) else []
        self.parent = (
            self.df["Inherit"][0] if not pd.isnull(self.df["Inherit"][0]) else None
        )
        try:
            self.is_abstract = (
                True if "Abstract" in self.df["Class description"][0] else False
            )
        except (KeyError, TypeError):
            self.is_abstract = False
        self.components_set = set()
        self.children_list = []

    def write_mermaid_class(self):
        """This build a string representing the class definition in the mermaid syntax, to
        be written in a .mmd file

        Returns
        -------
        string
            The definition of the class in the mermaid syntax
        """
        mermaid_class = f"class {self.name}{{\n"
        for var, var_type in zip(self.variables, self.variable_types):
            if "{" in var_type:
                var_type = var_type.replace("}", "")
                var_type = var_type.replace("{", "")
                var_type = f"dict~{var_type}~"
            if "[" in var_type:
                var_type = var_type.replace("[", "")
                var_type = var_type.replace("]", "")
                var_type = f"list~{var_type}~"
            mermaid_class += f"\t{var} : {var_type}\n"
        for met in self.methods:
            mermaid_class += f"\t{met}()\n"
        mermaid_class += "}"
        return mermaid_class

    def get_clean_variable_types(self):
        """This allows to get all the types of the attributes of the class to build
        composition links in the diagram. That will remove lists and dictionnary indications
        to keep only the type of the elements

        Returns
        -------
        list
            list of types of the attributes of the class
        """
        clean_variable_types = []
        for var_type in self.variable_types:
            var_type = var_type.replace("}", "")
            var_type = var_type.replace("{", "")
            var_type = var_type.replace("[", "")
            var_type = var_type.replace("]", "")
            var_type = var_type.split(".")[-1]
            clean_variable_types.append(var_type)
        return clean_variable_types

    def __str__(self):
        return f"MermaidClass({self.name})"

    def __repr__(self):
        return f"MermaidClass({self.name})"
