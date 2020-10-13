import time
import unittest

from model.pureDriver import PureDriver
from model.util import *


class TestPureDriver(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = PureDriver(headless=False)
        cls.driver.go_booking_with_location_id()
        cls.driver.sign_in()
        time.sleep(3)
        expect = 'Sign In'
        actual = cls.driver.find_element_by_xpath(
            '//button[@style="display: none;" and @class="btn btn-primary navbar-btn"]').get_attribute("innerText")

    def test_01_init_headless_false(self):
        driver = PureDriver(headless=False)
        actual = driver.execute_script("return window.chrome")
        expect = {'app': {'InstallState': {'DISABLED': 'disabled',
                                           'INSTALLED': 'installed',
                                           'NOT_INSTALLED': 'not_installed'},
                          'RunningState': {'CANNOT_RUN': 'cannot_run',
                                           'READY_TO_RUN': 'ready_to_run',
                                           'RUNNING': 'running'},
                          'getDetails': {},
                          'getIsInstalled': {},
                          'installState': {},
                          'isInstalled': False,
                          'runningState': {}},
                  'csi': {},
                  'loadTimes': {}}
        driver.quit()
        self.assertEqual(expect, actual)

    def test_01_init_headless_true(self):
        driver = PureDriver(headless=True)
        actual = driver.execute_script("return window.chrome")
        expect = None
        driver.quit()
        self.assertEqual(expect, actual)

    def test_03_go_booking_with_location_id_Millennium_City(self):
        expect = "Yoga - Millennium City 5"
        actual = self.driver.find_element_by_xpath('//span[@id="select2-location-container"]').get_attribute(
            'innerText')
        self.assertEqual(expect, actual)

    def test_03_sign_in(self):
        time.sleep(3)
        expect = 'Sign In'
        actual = self.driver.find_element_by_xpath(
            '//button[@style="display: none;" and @class="btn btn-primary navbar-btn"]').get_attribute("innerText")
        self.assertEqual(expect, actual)

    def test_04_get_time_list(self):
        actual = len(self.driver.get_time_list()) > 0
        expect = True
        self.assertEqual(expect, actual)

    def test_05_get_date_list(self):
        actual = datetime.now().strftime("%a %b %d") in self.driver.get_date_list()
        expect = True
        self.assertEqual(expect, actual)

    def test_07_get_lesson_dict(self):
        actual = len(self.driver.get_lesson_dict(['//td[@data-date="Fri Oct 9" and @data-time="08:30"]',
                                                              '//td[@data-date="Mon Oct 5" and @data-time="08:30"]',
                                                              '//td[@data-date="Wed Oct 7" and @data-time="07:00"]']))
        expect = 2
        self.assertEqual(expect, actual)

    def test_08_extract_lesson_tutor_name_mins_button(self):
        element = self.driver.find_element_by_xpath('//td[@data-date="Sun Oct 11" and @data-time="09:00"]')
        actual = extract_lesson_tutor_name_mins_button(element)['lesson']
        expect = "Vinyasa Gentle"
        self.assertEqual(expect, actual)

    def test_09_click_book(self):
        element = self.driver.find_element_by_xpath('//td[@data-date="Sun Oct 11" and @data-time="09:00"]')
        lesson_dict = extract_lesson_tutor_name_mins_button(element)
        self.driver.click_book(lesson_dict=lesson_dict)
        time.sleep(5)

    def test_10_go_next_week(self):
        self.driver.go_next_week()
        actual = get_target_date() in self.driver.get_date_list()
        expect = True
        self.assertEqual(expect, actual)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
