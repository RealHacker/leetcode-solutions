class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        start = lower
        ranges = []
        for num in nums:
            if num>start:
                ranges.append((start, num-1))
            start = num+1
        if start<=upper:
            ranges.append((start, upper))
        result = ["%d"%a if a==b else "%d->%d"%(a,b) for a,b in ranges]
        return result
            
