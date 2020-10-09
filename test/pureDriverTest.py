import unittest
from model.pureDriver import PureDriver


class TestPureDriver(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = PureDriver( headless=True)

    def test_01_init_headless_false(self):
        driver = PureDriver( headless=False)
        actual = driver.execute_script("return window.chrome")
        expect ={'app': {'InstallState': {'DISABLED': 'disabled',
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

    def test_02_go_booking_with_location_id_Millennium_City(self):
        self.driver.go_booking_with_location_id(40)
        expect = "Yoga - Millennium City 5"
        actual = self.driver.find_element_by_xpath('//span[@id="select2-location-container"]').get_attribute('innerText')
        self.assertEqual(expect, actual)

    def test_02_go_booking_with_location_id_Yoga_Langham_Place(self):
        self.driver.go_booking_with_location_id(7)
        expect = "Yoga - Langham Place"
        actual = self.driver.find_element_by_xpath('//span[@id="select2-location-container"]').get_attribute('innerText')
        self.assertEqual(expect, actual)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
