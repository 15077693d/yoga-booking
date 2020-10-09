from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import os, pathlib
from resources.config import wait_seconds
class PureDriver(Chrome):
    def __init__(self,headless=False):
        executable_path = os.path.join(pathlib.Path(os.path.dirname(__file__)).parent, "resources/chromedriver")
        options = Options()
        if headless:
            options.headless = True
        super().__init__(executable_path=executable_path, options=options)
        self.implicitly_wait(wait_seconds)

    def go_booking_with_location_id(self,location_id):
        url = f"https://pure360.pure-yoga.com/en/HK?location_id={location_id}"
        self.get(url=url)

    def sign_in(self):
