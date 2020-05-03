from typing import Tuple, List

class TimeLocationObj():
    _day: str
    _start_time: str
    _end_time: str
    _building: str
    _room: str

    def __init__(self, day: str, start_time: str, end_time: str,
                 building: str, room: str):
        self._day = day
        self._start_time = start_time
        self._end_time = end_time
        self._building = building
        self._room = room

    def to_str_tabulate(self) -> Tuple[List, List]:
        titles = ['day', 'start time', 'end time', 'building', 'room']
        content = [
            self._day, self._start_time, self._end_time,
            self._building, self._room
        ]

        return (titles, content)
