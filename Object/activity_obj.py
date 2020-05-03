from Object.time_location_obj import TimeLocationObj
from typing import List, Tuple

class ActivityObj():
    _activity_title: str
    _time_location_list: List[TimeLocationObj]

    def __init__(self, activity_title: str,
                 time_location_list: List[TimeLocationObj]):
        self._activity_title = activity_title
        self._time_location_list = time_location_list

    def to_str_tabulate(self) -> Tuple[List, List]:
        titles = []
        content = []
        for item in self._time_location_list:
            li = item.to_str_tabulate()
            titles = li[0]
            temp = li[1]
            temp.insert(0, self._activity_title)
            content.append(temp)

        titles.insert(0, 'Activity')
        return (titles, content)
