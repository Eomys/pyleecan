def get_name(self):
    """Return the name of file or function

    Parameters
    ----------
    self : Rule
        A Rule object
    """
    if type(self).__name__ == "RuleComplex":
        return self.fct_name
    else:
        return self.file_name
