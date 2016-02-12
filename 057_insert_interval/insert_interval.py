# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        while i<len(intervals) and intervals[i].end<newInterval.start:
            i+=1
        j = i
        while j<len(intervals) and intervals[j].start<=newInterval.end:
            j+=1
        if i<j:
            newInterval.start = min(newInterval.start, intervals[i].start)
            newInterval.end = max(newInterval.end, intervals[j-1].end)
            del intervals[i:j]
        intervals.insert(i, newInterval)
        return intervals
