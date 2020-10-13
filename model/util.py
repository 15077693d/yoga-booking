import json
import os
from datetime import datetime, timedelta


def time_date_2_xpath(time, date):
    """
    transform time date to xpath
    etc //td[@data-date="Fri Oct 9" and @data-time="07:00"]
    :param time:
    :param date:
    :return:
    """
    return f'//td[@data-date="{date}" and @data-time="{time}"]'


def get_target_date():
    """
    get the second after day etc mon -> wed
    today + 2
    :return:
    """
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources/condition.json")) as f:
        condition = json.load(f)
    return (datetime.now() + timedelta(days=condition['day_delta'])).strftime("%a %b %d")


def extract_lesson_tutor_name_mins_button(element):
    """
    Get lesson info from element
    :param element:
    :return:
    """
    try:
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources/condition.json")) as f:
            condition = json.load(f)
        max_time = datetime.strptime(condition["time"][1], "%H:%S")
        min_time = datetime.strptime(condition["time"][0], "%H:%S")
        lesson = element.find_element_by_xpath('.//span[contains(@class,"class-type")]').get_attribute("innerText")
        teacher = element.find_element_by_xpath('.//span[contains(@class,"class-teacher")]').get_attribute("innerText")
        duration = element.find_element_by_xpath('.//span[contains(@class,"duration")]').get_attribute("innerText")
        button = element.find_element_by_xpath('.//button')
        status = button.get_attribute("innerText") in condition['status']
        date = element.get_attribute("data-date")
        time = datetime.strptime(element.get_attribute("data-time"), "%H:%S")
        if time > max_time or time < min_time or status == False or lesson not in condition['class']:
            return False
        else:
            return {
                "date": date,
                "time": element.get_attribute("data-time"),
                "lesson": lesson,
                "teacher": teacher,
                "duration": duration,
                "button": button,
                "status": status
            }
    except Exception as e:
        print(e)