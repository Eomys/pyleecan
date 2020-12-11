def __len__(self):
    """Method to behave like a list and iterate in the object"""
    if self.nb_simu != None:
        return self.nb_simu
    else:
        return len(self.output_list)
