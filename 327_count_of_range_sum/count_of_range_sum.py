class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums: return 0
        self.nums = nums
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1]+num)
        self.lower = lower
        self.upper = upper
        return self.recurse(0, len(self.sums))
    
    def recurse(self, lo, hi):
        mid = (lo+hi)/2
        if mid == lo:
            return 0
        n1 = self.recurse(lo, mid)
        n2 = self.recurse(mid, hi)
        n3 = 0
        i = j = mid
        for sum in self.sums[lo:mid]:
            while i<hi and self.sums[i]-sum<self.lower: i+=1
            while j<hi and self.sums[j]-sum<=self.upper: j+=1
            n3+= (j-i)
        self.sums[lo:hi] = sorted(self.sums[lo:hi])
        print n1, n2, n3
        return n1+n2+n3