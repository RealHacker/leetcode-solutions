import operator

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # sort and merge
        intervals = sorted(intervals, key=operator.attrgetter("start"))
        i = 0
        while i<len(intervals)-1:
            if intervals[i].end>=intervals[i+1].start:
                intervals[i].end = max(intervals[i].end, intervals[i+1].end)
                del intervals[i+1]
            else:
                i+=1
        return intervals
