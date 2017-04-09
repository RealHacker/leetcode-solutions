# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import bisect
class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if not self.numbers:
            self.numbers = [val, val]
        idx = bisect.bisect_left(self.numbers, val)
        mleft, mright = False, False
        if idx%2:
            return
        if idx > 0:
            if self.numbers[idx-1] == val-1:
                mleft = True
            
        if idx < len(self.numbers)-1:
            if self.numbers[idx] == val+1:
                mright = True
            elif self.numbers[idx] == val:
                return
        if not mleft and not mright:
            self.numbers.insert(idx, val)
            self.numbers.insert(idx, val)
        elif not mleft and mright:
            self.numbers[idx] = val
        elif mleft and not mright:
            self.numbers[idx-1] = val
        else:
            del self.numbers[idx-1:idx+1]
            
    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        n = self.numbers
        return [[n[i], n[i+1]] for i in range(0, len(n), 2)]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
