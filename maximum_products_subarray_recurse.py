import sys
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        self.nums = nums
        self.max = - sys.maxint
        self.maxStartFrom(0)
        return self.max
        
    def maxStartFrom(self, i):
        if i==len(self.nums)-1:
            if self.nums[i]>self.max:
                self.max = self.nums[i]
            if self.nums[i]==0:
                return (0, 0)
            elif self.nums[i]>0:
                return (self.nums[i], None)
            else:
                return (None, self.nums[i])
        else:
            _max, _min = self.maxStartFrom(i+1)
            if self.nums[i]==0:
                return (0, 0)
            elif self.nums[i]>0:
                if _max is None:
                    _max_ = self.nums[i]
                else:
                    _max_ = max(self.nums[i], self.nums[i]*_max)
                _min_ = self.nums[i]*_min if _min is not None else None
            else:
                if _min is None:
                    _max_ = None
                else:
                    _max_ = self.nums[i]*_min
                if _max is None:
                    _min_ = self.nums[i]
                else:
                    _min_ = min(self.nums[i], self.nums[i]*_max)
            if _max_ and _max_>self.max:
                self.max = _max_
            elif _min_ and _min_>self.max:
                self.max = _min_
            return _max_, _min_
            
                
                
                
