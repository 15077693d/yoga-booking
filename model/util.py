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
    return (datetime.now() + timedelta(days=2)).strftime("%a %b %d")


def extract_lesson_tutor_name_mins_button(element):
    """
    Get lesson info from element
    :param element:
    :return:
    """
    lesson = element.find_element_by_xpath('.//span[contains(@class,"class-type")]').get_attribute("innerText")
    teacher = element.find_element_by_xpath('.//span[contains(@class,"class-teacher")]').get_attribute("innerText")
    duration = element.find_element_by_xpath('.//span[contains(@class,"duration")]').get_attribute("innerText")
    button = element.find_element_by_xpath('.//button')
    return {
        "lesson": lesson,
        "teacher": teacher,
        "duration": duration,
        "button":button
    }
