import logging
import os
log_folder_path = os.path.join(os.path.dirname(__file__),"log")
from datetime import datetime
class Logger():
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        if not os.path.exists(log_folder_path):
            os.mkdir(log_folder_path)
        path = os.path.join(log_folder_path,datetime.now().strftime("%Y%m%d-%H%M.log"))
        fh = logging.FileHandler(path)
        ch = logging.StreamHandler()
        formatter = logging.Formatter("[%(levelname)s] %(asctime)s %(module)s %(funcName)s (%(lineno)d) %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.handlers = []
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        self.logger.info("Create logger!")
    def get_logger(self):
        return self.logger