# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import operator
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        pairs = []
        for interval in intervals:
            pairs.append((interval.start, 1))
            pairs.append((interval.end, -1))
        # sort first by time value, and make sure endtime (-1) comes before starttime(1)
        pairs.sort()
        
        
        max_depth = 0
        depth = 0
        for _, pos in pairs:
            if pos>0:
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
        return max_depth
