# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import operator
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=operator.attrgetter("start"))
        for i in range(len(intervals)-1):
            if intervals[i].end>intervals[i+1].start:
                return False
        return True
