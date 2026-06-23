"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        arr = []
        for i in intervals:
            start, end = i.start, i.end
            arr.append([start, end])
        arr.sort()
        time = 0

        for start, end in arr:
            if start < time:
                return False
            time = end
        return True