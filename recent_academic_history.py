import os

from tabulate import tabulate

import re
from bs4 import BeautifulSoup

class RecentAcademicHistory:
    _url : str

    # def __init__(self):
    #     path = os.path.dirname(os.path.abspath(__file__))
    #     self._url = os.path.join(
    #         path, 'Testing\Academic History.html'
    #     )

    def __init__(self, browser):
        self._browser = browser
        self._url = 'https://acorn.utoronto.ca/sws/#/history/academic'

    def recent_academic_history(self):
        self._browser.get(self._url)
        # soup = BeautifulSoup(open(self._url), 'html.parser')
        soup = BeautifulSoup(self._browser.page_source, 'html.parser')
        data = soup.find_all(
            attrs={'class': 'section academic-history xs-block-table'}
        )
        result = ''

        for i in range(len(data)):
            string = self._clean_up(str(data[i]))

            result += string

        print(result)

        self._browser.quit()

    def _clean_up(self, data) -> str:
        titles = [
            'Course Code', 'Title', 'Weight', 'Mark', 'Grade', 'Course Average'
        ]

        soup = BeautifulSoup(data, 'html.parser')
        header = soup.find(attrs={'class': 'sessionHeader'})
        gpa_listing = soup.find(attrs={'class': 'gpa-listing'})

        course_list = soup.find_all(attrs={'class': 'courses'})

        parsed_course_list = []
        result = ''

        for course in course_list:
            course_str = course.getText()
            course_str = re.sub('\n+\t{2,}', '\n', course_str)
            course_str = re.sub('\n{2,}', '\n', course_str)
            course_str_list = course_str.split('\n')

            temp = course_str_list[1:-1]
            temp.extend([' '] * (len(titles) - len(temp)))

            parsed_course_list.append(temp)

        result += header.getText().strip() + '\n'

        try:
            gpa_listing_str = gpa_listing.getText().strip()
            gpa_listing_str = re.sub('\n{2,}', ' ', gpa_listing_str)
            result += gpa_listing_str + '\n'
        except:
            pass

        result += tabulate(parsed_course_list, headers=titles) + '\n\n'

        return result


if __name__ == '__main__':
    test = RecentAcademicHistory()
    test.recent_academic_history()
