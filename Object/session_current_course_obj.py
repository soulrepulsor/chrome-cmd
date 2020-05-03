from typing import List
from Object.current_course_obj import CurrentCourseObj

class SessionCurrentCourseObj():
    _session: str
    _current_courses: List[CurrentCourseObj]

    def __init__(self, session: str, current_courses: List[CurrentCourseObj]):
        self._session = session
        self._current_courses = current_courses

    def __str__(self):
        result = ''
        for course in self._current_courses:
            result += str(course) + '\n'

        return self._session + '\n' + result
