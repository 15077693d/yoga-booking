import os
import pathlib
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from model.util import *
from resources.config import wait_seconds, xpath
from resources.logger import Logger


class PureDriver(Chrome):
    def __init__(self, headless=False):
        self.logger = Logger("PureDriver").get_logger()
        executable_path = os.path.join(pathlib.Path(os.path.dirname(__file__)).parent, "resources/chromedriver")
        options = Options()
        if headless:
            options.headless = True
        super().__init__(executable_path=executable_path, options=options)
        self.implicitly_wait(wait_seconds)

    def go_booking_with_location_id(self, location_id:int) -> None:
        """
        go booking site by location id
        :param location_id:
        :return:
        """
        url = f"https://pure360.pure-yoga.com/en/HK?location_id={location_id}"
        try:
            self.logger.info(f"Go to {url}")
            self.get(url=url)
        except Exception as e:
            self.logger.error(e)


    def sign_in(self):
        """
        Sign in the booking system
        :return:
        """
        self.logger.info(f"[Start] sign in...")
        try:
            username = os.environ['username']
            password = os.environ['password']
            time.sleep(1)
            sign_in_element = WebDriverWait(self, wait_seconds).until(
                EC.element_to_be_clickable((By.XPATH, xpath['sign_in_button'])))
            sign_in_element.click()
            time.sleep(1)
            self.find_element_by_xpath(xpath['username_input']).send_keys(username)
            self.find_element_by_xpath(xpath['password_input']).send_keys(password)
            self.find_element_by_xpath(xpath['login_input']).click()
            self.logger.info(f"[End] sign in...")
        except Exception as e:
            self.logger.error(e)


    def get_time_list(self) -> list:
        """
        Get vertical column time to list
        :return:
        """
        self.logger.info(f"[Start] get time list...")
        try:
            time_list_elements = self.find_elements_by_xpath(xpath['time_tr'])
            time_list = list(map(lambda element: element.get_attribute("data-time"),time_list_elements))
            self.logger.info(f"[End] get time list...")
            return time_list
        except Exception as e:
            self.logger.error(e)

    def get_date_list(self) -> list:
        """
        Get horizontal row date to list
        :return: 
        """
        self.logger.info(f"[Start] get date list...")
        try:
            date_list_elements = self.find_elements_by_xpath(xpath["date_tr"])
            date_list = list(map(lambda element: element.get_attribute("data-date"), date_list_elements))
            self.logger.info(f"[End] get date list...")
            return date_list
        except Exception as e:
            self.logger.error(e)

    def go_next_week(self):
        """
        if sat and sun i need to click next week...
        since the date is on next week table
        :return:
        """
        self.logger.info(f"[Start] go next week...")
        try:
            self.find_element_by_xpath(xpath['week_span']).click()
            time.sleep(2)
            self.find_element_by_xpath(xpath['next_week_2li']).click()
            time.sleep(3)
            self.logger.info(f"[End] go next week...")
        except Exception as e:
            self.logger.error(e)

    def get_lesson_dict(self, xpaths):
        """
        Get the target column with class
        :return:
        """
        self.logger.info(f"[Start] go get lesson box...")
        try:
            lesson_elements = list(map(lambda xpath: self.find_element_by_xpath(xpath),xpaths))
            not_empty_lesson_element =list(filter(lambda element: len(element.find_elements_by_xpath("./*"))>0,lesson_elements))
            lesson_dict = list(map(lambda element: extract_lesson_tutor_name_mins_button(element), not_empty_lesson_element))
            self.logger.info(f"[End] go get lesson box...{lesson_dict})")
            return lesson_dict
        except Exception as e:
            self.logger.error(e)

    def click_book(self, lesson_dict):
        """
        Click book lesson
        :param xpath:
        :return:
        """
        self.logger.info(f"[Start] Click Book {lesson_dict}")
        lesson_dict['button'].click()
        self.logger.info(f"[End] Click Book {lesson_dict}")
