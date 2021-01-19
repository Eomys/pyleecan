from ....loggers import gen_logger_config_dict, DEFAULT_LOG_NAME
from logging.config import dictConfig
from os.path import join


def init_logger(self, output, is_create=True, is_log_start=True):
    """Create all the logger for the simulation"""
    if self.name in [None, ""]:
        log_name = DEFAULT_LOG_NAME
    else:
        log_name = self.name

    if is_create:
        log_dict = gen_logger_config_dict(log_name)

        # Update log file
        log_path = join(output.get_path_result(), log_name + ".log")
        log_dict["handlers"]["file_handler"]["filename"] = log_path
        # Create the loggers
        dictConfig(log_dict)

    # Set the logger in the simulation
    self.logger_name = log_name
    self.machine.logger_name = log_name + ".Machine"
    if self.elec is not None:
        self.elec.logger_name = log_name + ".Electrical"
    if self.mag is not None:
        self.mag.logger_name = log_name + ".Magnetics"
    if self.force is not None:
        self.force.logger_name = log_name + ".Force"
    if self.struct is not None:
        self.struct.logger_name = log_name + ".Structural"
    # Set the logger in the Output
    output.logger_name = log_name
    output.elec.logger_name = log_name + ".Electrical"
    output.mag.logger_name = log_name + ".Magnetics"
    output.force.logger_name = log_name + ".Force"
    output.struct.logger_name = log_name + ".Structural"

    if is_log_start:
        # Display start of simulation
        msg = "Starting running simulation"
        if self.name not in ["", None]:
            msg += " " + self.name
        if self.machine.name not in ["", None]:
            msg += " (machine=" + self.machine.name + ")"
        self.get_logger().debug("###################################")
        self.get_logger().info(msg)
