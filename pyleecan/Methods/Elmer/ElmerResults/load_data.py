# -*- coding: utf-8 -*-
from os.path import exists
from numpy import loadtxt
from ....Methods.Elmer.ElmerResults import ElmerResultsError


def load_data(self):
    """Method to load the Elmer simulation results (as an alternative for direct input)

    Parameters
    ----------
    self : ElmerResults
        An ElmerResults object

    Returns
    -------
    data : list
        list of data

    """
    # TODO allow relative path
    filename = self.file

    # some first checks
    logger = self.get_logger()
    if filename is None:
        logger.warning("Filename (self.file) not defined.")
        return False
    if not exists(filename):
        logger.warning(f"Filename '{filename}' not found.")
        return False

    # load raw data
    usecols = self.usecols if self.usecols else None
    data = loadtxt(filename, unpack=False, usecols=usecols)
    data_size = data.shape[1]

    # check if columns names are avialable and get names in case
    if not self.columns:
        # TODO try to load names first
        logger.warning(f"Columns names not defined. Setting integers as names.")
        if not self.usecols:
            self.columns = [x + 1 for x in range(data_size)]
            self.usecols = self.columns
        else:
            self.columns = self.usecols

    # set data dict
    for k in range(min(len(self.columns), len(self.usecols))):
        i = self.usecols[k] - 1  # self.usecols starts with 1
        key = self.columns[k]
        if i < data_size and i >= 0:  # check index range
            self.data[key] = data[:, i]
        else:
            self.data[key] = None

    """
    # This order must match lines.dat.names
    # 1: Time step
    # 2: Iteration step
    # 3: Boundary condition
    # 4: Node index
    # 5: coordinate 1
    # 6: coordinate 2
    # 7: coordinate 3

    # 8: magnetic flux density 1
    # 9: magnetic flux density 2
    # 10: magnetic flux density 3
    # 11: magnetic flux density e 1
    # 12: magnetic flux density e 2
    # 13: magnetic flux density e 3
    Br_list = []
    Bt_list = []
    theta_list = []

    for i in range(skip_steps, steps + 1):
        index = np.where(data == i)
        data_step = data[index[0]]
        rho = np.sqrt(data_step[:, 1] ** 2 + data_step[:, 2] ** 2)
        theta = np.arctan2(data_step[:, 2], data_step[:, 1])
        Br1 = np.multiply(data_step[:, 3], np.cos(theta)) + np.multiply(
            data_step[:, 4], np.sin(theta)
        )
        Bt1 = -np.multiply(data_step[:, 3], np.sin(theta)) + np.multiply(
            data_step[:, 4], np.cos(theta)
        )
        max_theta = np.max(theta)
        min_theta = np.min(theta)
        data_step_polar = np.stack((rho, theta, Br1, Bt1), axis=-1)
        data_step_polar = data_step_polar[data_step_polar[:, 1].argsort()]
        cs_r = CubicSpline(data_step_polar[:, 1], data_step_polar[:, 2])
        cs_t = CubicSpline(data_step_polar[:, 1], data_step_polar[:, 3])
        theta_fine = np.linspace(min_theta, max_theta, num=int(2880 / fractions))
        Br_list.append(cs_r(theta_fine))
        Bt_list.append(cs_t(theta_fine))
        theta_list.append(theta_fine)

    
    """
    return True
