import unittest
from model.util import *


class TestPureDriver(unittest.TestCase):
    def test_01_time_date_2_xpath(self):
        expect = '//td[@data-date="Fri Oct 9" and @data-time="07:00"]'
        actual =  time_date_2_xpath("07:00","Fri Oct 9")
        self.assertEqual(expect, actual)

    def test_02_get_target_date(self):
        expect = (datetime.now() + timedelta(days=2)).strftime("%a %b %d")
        actual = get_target_date()
        self.assertEqual(expect, actual)
