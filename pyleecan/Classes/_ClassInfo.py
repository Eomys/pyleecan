from json import load as jload
from os.path import join, split


class ClassInfo:
    def __init__(self):
        self.class_dict = self.__init_dict__()

    def __init_dict__(self):
        """Method to get a dict on the pyleecan classes, i.e. class name, description,
        properties, methods, etc.

        Returns
        -------
        class_dict : dict
            dict of class information
        """
        # load the class dict
        path = split(__file__)[0]
        with open(join(path, "Class_Dict.json")) as fp:
            class_dict = jload(fp)

        # create inheritance information
        for cls_name in class_dict.keys():
            mother_name = class_dict[cls_name]["mother"]
            inherit = []
            while mother_name:
                inherit.append(mother_name)
                mother_name = class_dict[mother_name]["mother"]

            class_dict[cls_name]["inherit"] = inherit

        # from pprint import pprint
        # pprint(sorted([ClassInfo().get_prop_types()]))

        # complete properties and methods on each class
        for cls_dict in class_dict.values():
            prop_names = [prop["name"] for prop in cls_dict["properties"]]
            for mother in cls_dict["inherit"]:
                mother_props = class_dict[mother]["properties"]
                for mother_prop in mother_props:
                    if not mother_prop["name"] in prop_names:
                        cls_dict["properties"].append(mother_prop)

                # update property names
                prop_names = [prop["name"] for prop in cls_dict["properties"]]

            # convert properties to dict
            cls_dict["prop_dict"] = dict()
            for prop in cls_dict["properties"]:
                cls_dict["prop_dict"][prop["name"]] = prop

        return class_dict

    def get_dict(self):
        return self.class_dict

    def get_prop_types(self):
        """Get a set of all defined property types of all classes."""
        type_set = set()

        for cls in self.class_dict.values():
            for prop in cls["prop_dict"].values():
                type_set.add(prop["type"])

        return type_set

    def get_base_classes(self):
        """Get the base classes, i.e. classes that have no mother class."""
        bases = set()
        for key, item in self.class_dict.items():
            if not item["mother"]:
                bases.add(key)

        bases = sorted(list(bases))

        return bases

    def get_mothers(self, cls_name, stop=""):
        """Get a ordered list of the mothers of a class."""
        mothers = []
        if stop not in self.class_dict:
            stop = ""
        if cls_name in self.class_dict:
            mother = self.class_dict[cls_name]["mother"]
            while mother and cls_name != stop:
                mothers.append(mother)
                cls_name = mother
                mother = self.class_dict[mother]["mother"]

        return mothers
