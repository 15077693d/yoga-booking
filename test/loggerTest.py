import os
import pathlib
import unittest

from resources.logger import Logger


class TestPureDriver(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = Logger(name="test").get_logger()

    def test_01_init_have_log_file(self):
        log_folder_path = os.path.join(pathlib.Path(os.path.dirname(__file__)).parent, "resources/log")
        expect = True
        actual = os.path.exists(log_folder_path)
        self.assertEqual(expect, actual)
