from typing import List
from Object.activity_obj import ActivityObj
from tabulate import tabulate

class CurrentCourseObj():

    _course_code: str
    _term_code: str
    _term_text: str
    _course_title: str
    _activity_obj_list: List[ActivityObj]

    def __init__(self, course_code: str, term_code: str, term_text: str,
                 course_title: str, activity_obj_list: List[ActivityObj]):

        self._course_code = course_code
        self._course_title = course_title
        self._term_code = term_code
        self._term_text = term_text
        self._activity_obj_list = activity_obj_list

    def __str__(self):
        header = '{} {} {} {}'.format(
            self._course_code, self._term_code,
            self._term_text, self._course_title
        )
        titles = []
        content = []

        for item in self._activity_obj_list:
            li = item.to_str_tabulate()
            titles = li[0]
            content.extend(li[1])

        result = header + '\n' + tabulate(content, headers=titles) + '\n'

        return result
