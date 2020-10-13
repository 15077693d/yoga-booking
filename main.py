from model.pureDriver import PureDriver
from model.util import *

if __name__ == '__main__':
    try:
        driver = PureDriver()
        driver.go_booking_with_location_id()
        driver.sign_in()
        driver.go_next_week()
        time_list = driver.get_time_list()
        target_date = get_target_date()
        xpaths = list(map(lambda time: time_date_2_xpath(time, target_date), time_list))
        dict_list = driver.get_lesson_dict_list(xpaths)
        driver.click_book(dict_list[0])
        input()
        driver.quit()
    except:
        driver.quit()