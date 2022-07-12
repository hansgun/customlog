import logging
import os


## set log levle 
LOGLEVEL = logging.ERROR # NOTSET | DEBUG | INFO | WARNING | ERROR | CRITICAL = 0,10,20,30,40,50 


class PaipLogFormatter(logging.Formatter):
    def format(self, record):
        if hasattr(record, 'func_name_override'):
            record.funcName = record.func_name_override
        if hasattr(record, 'file_name_override'):
            record.filename = record.file_name_override
        return super(PaipLogFormatter, self).format(record)


def get_logger(log_file_name, log_dir_param=None, log_sub_dir=""):
    """ Creates a Log File and returns Logger object """

    windows_log_dir = 'c:\\logs_dir\\'
    linux_log_dir = './logs_dir/'

    # Build Log file directory, based on the OS and supplied input
    if log_dir_param is not None : 
        log_dir = log_dir_param
    else : 
        log_dir = windows_log_dir if os.name == 'nt' else linux_log_dir
        log_dir = os.path.join(log_dir, log_sub_dir)

    # Create Log file directory if not exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Build Log File Full Path
    logPath = log_file_name if os.path.exists(log_file_name) else os.path.join(log_dir, (str(log_file_name) + '.log'))

    # Create logger object and set the format for logging and other attributes
    logger = logging.Logger(log_file_name)
    logger.setLevel(LOGLEVEL)
    handler = logging.FileHandler(logPath, 'a+')
    """ Set the formatter of 'PaipLogFormatter' type as we need to log base function name and base file name """
    handler.setFormatter(PaipLogFormatter('%(asctime)s - %(levelname)-10s - %(filename)s - %(funcName)s - %(message)s'))
    logger.addHandler(handler)

    # Return logger object
    return logger 
