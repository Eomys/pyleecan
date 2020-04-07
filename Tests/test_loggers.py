import pytest
from logging import Logger
from pyleecan.Generator.read_fct import read_all
from pyleecan.definitions import DOC_DIR
from pyleecan.Classes.import_all import *

# Get the dict of all the classes and their information
gen_dict = read_all(DOC_DIR)  # dict of class dict
# Remove one list level (packages Machine, Simulation, Material...)
class_list = list(gen_dict.values())

@pytest.mark.logger
@pytest.mark.parametrize("class_dict",class_list)
def test_loggers(class_dict):
    test_obj = eval(class_dict["name"] + "()")
    logger = test_obj.get_logger()
    logger.info('test')
    assert isinstance(logger,Logger)