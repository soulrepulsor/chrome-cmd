from typing import List
from bs4 import BeautifulSoup
from Object.time_location_obj import TimeLocationObj
from Object.activity_obj import ActivityObj
from Object.current_course_obj import CurrentCourseObj
from Object.session_current_course_obj import SessionCurrentCourseObj
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os

class CurrentCourses():
    _url: str

    def __init__(self, browser):
        # path = os.path.dirname(os.path.abspath(__file__))
        # self._url = os.path.join(
        #     path, 'Testing\EnrolledCourses.html'
        # )
        self._url = 'https://acorn.utoronto.ca/sws/#/courses/'
        self._browser = browser

    def current_courses(self) -> List[SessionCurrentCourseObj]:
        result = []

        # soup = BeautifulSoup(open(self._url), 'html.parser')
        self._browser.get(self._url + str(0))
        wait = WebDriverWait(self._browser, 0.5)
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'enrolment-code')
        ))
        soup = BeautifulSoup(self._browser.page_source, 'html.parser')
        title = soup.find_all(attrs={'class': 'tab-heading'})

        for index in range(0, len(title)):

            data = soup.find_all(name='div', attrs={'class': 'courseEnrolment'})
            courses = []
            for item in data:
                current_course = self._parse_course_info(
                    BeautifulSoup(str(item), 'html.parser'))
                courses.append(current_course)

            result.append(SessionCurrentCourseObj(
                title[index].getText().strip(), courses)
            )
            try:
                self._browser.get(self._url + str(index + 1))
                wait = WebDriverWait(self._browser, 1)
                wait.until(EC.presence_of_element_located(
                    (By.CLASS_NAME, 'enrolment-code')
                ))
                soup = BeautifulSoup(self._browser.page_source, 'html.parser')

            except Exception:
                pass

        self._browser.quit()

        return result

    def _parse_course_info(self, soup: BeautifulSoup) -> CurrentCourseObj:
        data = soup.find(attrs={'class': 'enrolment-code'})
        title_code_term_list = data.getText().strip().split('\n')
        sub_info = title_code_term_list[0].split()
        course_code = sub_info[0].strip()
        term_code = sub_info[1].strip()
        term_text = title_code_term_list[1].strip()
        course_title = title_code_term_list[2].strip()

        result = []

        activity_row_list = soup.find_all(attrs={'class': 'activityRow'})
        for activity_row in activity_row_list:
            activity = self._parse_course_deep_info(
                BeautifulSoup(str(activity_row), 'html.parser'))
            result.append(activity)

        return CurrentCourseObj(course_code, term_code, term_text, course_title,
                                result)

    def _parse_course_deep_info(self, soup: BeautifulSoup) -> ActivityObj:
        activity_title_data = soup.find(attrs={'class': 'activity'})
        activity_title = activity_title_data.getText().strip()
        time_details_list = soup.find_all(attrs={'class': 'timeDetails'})[1:]
        loc_details_list = soup.find_all(attrs={'class': 'locationDetails'})

        result = []

        for i in range(len(time_details_list)):
            time_temp1 = time_details_list[i].getText().strip().split('-')
            time_temp2 = time_temp1[0].split('\n\t\t\t')

            day = time_temp2[0].strip()
            start = time_temp2[1].strip()
            end = time_temp1[1].strip()

            location_temp1 = loc_details_list[i].getText().split(',')
            location_temp2 = location_temp1[0].split(' ')
            building = location_temp2[0].strip()
            room = location_temp2[1].strip()

            result.append(TimeLocationObj(day, start, end, building, room))

        return ActivityObj(activity_title, result)

if __name__ == '__main__':
    test = CurrentCourses()
    course_list = test.current_courses()

    for course in course_list:
        print(course)
